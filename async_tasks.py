def hello_cron(event, context):
    import logging

    logging.error("hello cron")
    return True
