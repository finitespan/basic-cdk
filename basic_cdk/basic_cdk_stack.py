from aws_cdk import (
    App,
    RemovalPolicy,
    Stack,
    aws_s3 as s3
)
from constructs import Construct


class BasicCdkStack(Stack):

    def __init__(self, scope: App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = s3.Bucket(self, "TestBucket",
                           versioned=True,
                           removal_policy=RemovalPolicy.DESTROY,
                           auto_delete_objects=True)
