import json
import sys

from process.management.commands.base.worker import BaseWorker


class Command(BaseWorker):

    worker_name = "checker"

    consume_keys = ["loader"]

    def __init__(self):
        super().__init__(self.worker_name)

    def process(self, channel, method, properties, body):
        try:
            # parse input message
            input_message = json.loads(body.decode('utf8'))

            self.debug("Received message {}".format(input_message))

            # send message for a next phase
            message = {"dataset_id": 1}
            self.publish(json.dumps(message))

            # confirm message processing
            channel.basic_ack(delivery_tag=method.delivery_tag)
        except Exception:
            self.exception(
                "Something went wrong when processing {}".format(body))
            sys.exit()
