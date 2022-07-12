import json
import os
import sys

import django

sys.path.append('..')
from typing import Any

import pika
import datetime
import modules.support_functions as sup_f

os.environ.setdefault('DJANGO_SETTINGS_MODULE','dc_sonar_web.settings')
django.setup()
from django.conf import settings
from user_cabinet.models import Domain

filename = os.path.basename(__file__).split('.')[0]
logger = sup_f.init_custome_logger(
    os.path.join(settings.LOGS_DIR, f'{filename}.log'),
    os.path.join(settings.LOGS_DIR, f'{filename}_error.log'),
    logging_level=settings.LOGS_LEVEL,
)


def rmq_callback(ch: Any, method: Any, properties: Any, body: Any) -> None:
    domain = None
    try:
        logger.info('Working on a msg')
        msg = json.loads(body.decode('utf-8'))
        logger.info(f'msg: {msg}')
        domain = Domain.objects.get(pk=msg['domain_pk'])
        if msg['status'] == 'PERFORMING':
            domain.dump_status = Domain.ProcessStatus.PERFORMING
        elif msg['status'] == 'ERROR':
            domain.dump_status = Domain.ProcessStatus.ERROR
            domain.dump_err_desc = msg['error_desc']
        elif msg['status'] == 'FINISHED':
            domain.dump_status = Domain.ProcessStatus.FINISHED
        else:
            domain.dump_status = Domain.ProcessStatus.ERROR
            domain.dump_err_desc = f"Unknown msg['status']: {msg['status']}"
        domain.dump_status_update = datetime.datetime.now().astimezone()
        domain.save()

    except Exception as e:
        logger.error('Error', exc_info=sys.exc_info())
        if domain:
            domain.dump_status = Domain.ProcessStatus.ERROR
            domain.dump_err_desc = str(e)
            domain.dump_status_update = datetime.datetime.now().astimezone()
            domain.save()
    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':

    rmq_conn = None
    try:
        rmq_conn = pika.BlockingConnection(pika.ConnectionParameters(**settings.RMQ_SETTINGS))
        channel = rmq_conn.channel()

        channel.queue_declare(queue='info_dumping_ntlm', durable=True)
        channel.basic_consume(queue='info_dumping_ntlm', on_message_callback=rmq_callback)
        channel.start_consuming()
    except Exception as e:
        logger.error('Error', exc_info=sys.exc_info())
    finally:
        if rmq_conn is not None:
            rmq_conn.close()
