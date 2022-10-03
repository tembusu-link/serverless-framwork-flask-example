import serverless_sdk

sdk = serverless_sdk.SDK(
    org_id="tembusu",
    application_name="serverless-framework-test",
    app_uid="YQPfXtDfHkwwStNDhb",
    org_uid="d53a6863-9635-4ff4-b9d8-47134b82f375",
    deployment_uid="3f37e5c6-96d7-4b2b-8e51-fd14c11af4d2",
    service_name="serverless-framework-test",
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name="dev",
    plugin_version="6.2.2",
    disable_frameworks_instrumentation=False,
    serverless_platform_stage="prod",
)
handler_wrapper_kwargs = {
    "function_name": "serverless-framework-test-dev-cronJob",
    "timeout": 300,
}
try:
    user_handler = serverless_sdk.get_user_handler("async_tasks.hello_cron")
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error

    def error_handler(event, context):
        raise e

    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
