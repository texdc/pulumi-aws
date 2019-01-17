# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GlobalCluster(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    RDS Global Cluster Amazon Resource Name (ARN)
    """
    database_name: pulumi.Output[str]
    """
    Name for an automatically created database on cluster creation.
    """
    deletion_protection: pulumi.Output[bool]
    """
    If the Global Cluster should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.
    """
    engine: pulumi.Output[str]
    """
    Name of the database engine to be used for this DB cluster. Valid values: `aurora`. Defaults to `aurora`.
    """
    engine_version: pulumi.Output[str]
    """
    Engine version of the Aurora global database.
    """
    global_cluster_identifier: pulumi.Output[str]
    global_cluster_resource_id: pulumi.Output[str]
    """
    AWS Region-unique, immutable identifier for the global database cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed
    """
    storage_encrypted: pulumi.Output[bool]
    """
    Specifies whether the DB cluster is encrypted. The default is `false`.
    """
    def __init__(__self__, __name__, __opts__=None, database_name=None, deletion_protection=None, engine=None, engine_version=None, global_cluster_identifier=None, storage_encrypted=None):
        """
        Manages a RDS Global Cluster, which is an Aurora global database spread across multiple regions. The global database contains a single primary cluster with read-write capability, and a read-only secondary cluster that receives data from the primary cluster through high-speed replication performed by the Aurora storage subsystem.
        
        More information about Aurora global databases can be found in the [Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database-creating).
        
        > **NOTE:** RDS only supports the `aurora` engine (MySQL 5.6 compatible) for Global Clusters at this time.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] database_name: Name for an automatically created database on cluster creation.
        :param pulumi.Input[bool] deletion_protection: If the Global Cluster should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.
        :param pulumi.Input[str] engine: Name of the database engine to be used for this DB cluster. Valid values: `aurora`. Defaults to `aurora`.
        :param pulumi.Input[str] engine_version: Engine version of the Aurora global database.
        :param pulumi.Input[str] global_cluster_identifier
        :param pulumi.Input[bool] storage_encrypted: Specifies whether the DB cluster is encrypted. The default is `false`.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['database_name'] = database_name

        __props__['deletion_protection'] = deletion_protection

        __props__['engine'] = engine

        __props__['engine_version'] = engine_version

        if not global_cluster_identifier:
            raise TypeError('Missing required property global_cluster_identifier')
        __props__['global_cluster_identifier'] = global_cluster_identifier

        __props__['storage_encrypted'] = storage_encrypted

        __props__['arn'] = None
        __props__['global_cluster_resource_id'] = None

        super(GlobalCluster, __self__).__init__(
            'aws:rds/globalCluster:GlobalCluster',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

