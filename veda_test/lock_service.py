from aws_cdk import (core,
                     aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_)

class LockService(core.Construct):
    def __init__(self, scope: core.Construct, id: str):
        super().__init__(scope, id)

        bucket = s3.Bucket(self, 
            "LockStore", 
            removal_policy=core.RemovalPolicy.DESTROY,
            auto_delete_objects=True)

        handler = lambda_.Function(self, "LockHandler",
                    runtime=lambda_.Runtime.NODEJS_14_X,
                    code=lambda_.Code.from_asset("resources"),
                    handler="locks.main",
                    environment=dict(
                    BUCKET=bucket.bucket_name)
                    )

        bucket.grant_read_write(handler)

        api = apigateway.RestApi(self, "locks-api",
                  rest_api_name="Lock Service",
                  description="This service serves locks.")

        get_locks_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_locks_integration)   # GET /
        
        lock = api.root.add_resource("{id}")

        # Add new lock to bucket with: POST /{id}
        post_lock_integration = apigateway.LambdaIntegration(handler)

        # Get a specific lock from bucket with: GET /{id}
        get_lock_integration = apigateway.LambdaIntegration(handler)

        # Remove a specific lock from the bucket with: DELETE /{id}
        delete_lock_integration = apigateway.LambdaIntegration(handler)

        lock.add_method("POST", post_lock_integration);     # POST /{id}
        lock.add_method("GET", get_lock_integration);       # GET /{id}
        lock.add_method("DELETE", delete_lock_integration); # DELETE /{id}