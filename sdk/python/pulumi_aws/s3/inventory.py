# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Inventory(pulumi.CustomResource):
    bucket: pulumi.Output[str]
    """
    The S3 bucket configuration where inventory results are published (documented below).
    """
    destination: pulumi.Output[dict]
    """
    Destination bucket where inventory list files are written (documented below).
    
      * `bucket` (`dict`) - The S3 bucket configuration where inventory results are published (documented below).
    
        * `account_id` (`str`) - The ID of the account that owns the destination bucket. Recommended to be set to prevent problems if the destination bucket ownership changes.
        * `bucketArn` (`str`) - The Amazon S3 bucket ARN of the destination.
        * `encryption` (`dict`) - Contains the type of server-side encryption to use to encrypt the inventory (documented below).
    
          * `sseKms` (`dict`) - Specifies to use server-side encryption with AWS KMS-managed keys to encrypt the inventory file (documented below).
    
            * `key_id` (`str`) - The ARN of the KMS customer master key (CMK) used to encrypt the inventory file.
    
          * `sseS3` (`dict`) - Specifies to use server-side encryption with Amazon S3-managed keys (SSE-S3) to encrypt the inventory file.
    
        * `format` (`str`) - Specifies the output format of the inventory results. Can be `CSV`, [`ORC`](https://orc.apache.org/) or [`Parquet`](https://parquet.apache.org/).
        * `prefix` (`str`) - The prefix that is prepended to all inventory results.
    """
    enabled: pulumi.Output[bool]
    """
    Specifies whether the inventory is enabled or disabled.
    """
    filter: pulumi.Output[dict]
    """
    Object filtering that accepts a prefix (documented below).
    
      * `prefix` (`str`) - The prefix that is prepended to all inventory results.
    """
    included_object_versions: pulumi.Output[str]
    """
    Object filtering that accepts a prefix (documented below). Can be `All` or `Current`.
    """
    name: pulumi.Output[str]
    """
    Unique identifier of the inventory configuration for the bucket.
    """
    optional_fields: pulumi.Output[list]
    """
    Contains the optional fields that are included in the inventory results.
    """
    schedule: pulumi.Output[dict]
    """
    Contains the frequency for generating inventory results (documented below).
    
      * `frequency` (`str`) - Specifies how frequently inventory results are produced. Can be `Daily` or `Weekly`.
    """
    def __init__(__self__, resource_name, opts=None, bucket=None, destination=None, enabled=None, filter=None, included_object_versions=None, name=None, optional_fields=None, schedule=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a S3 bucket [inventory configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html) resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The S3 bucket configuration where inventory results are published (documented below).
        :param pulumi.Input[dict] destination: Destination bucket where inventory list files are written (documented below).
        :param pulumi.Input[bool] enabled: Specifies whether the inventory is enabled or disabled.
        :param pulumi.Input[dict] filter: Object filtering that accepts a prefix (documented below).
        :param pulumi.Input[str] included_object_versions: Object filtering that accepts a prefix (documented below). Can be `All` or `Current`.
        :param pulumi.Input[str] name: Unique identifier of the inventory configuration for the bucket.
        :param pulumi.Input[list] optional_fields: Contains the optional fields that are included in the inventory results.
        :param pulumi.Input[dict] schedule: Contains the frequency for generating inventory results (documented below).
        
        The **destination** object supports the following:
        
          * `bucket` (`pulumi.Input[dict]`) - The S3 bucket configuration where inventory results are published (documented below).
        
            * `account_id` (`pulumi.Input[str]`) - The ID of the account that owns the destination bucket. Recommended to be set to prevent problems if the destination bucket ownership changes.
            * `bucketArn` (`pulumi.Input[str]`) - The Amazon S3 bucket ARN of the destination.
            * `encryption` (`pulumi.Input[dict]`) - Contains the type of server-side encryption to use to encrypt the inventory (documented below).
        
              * `sseKms` (`pulumi.Input[dict]`) - Specifies to use server-side encryption with AWS KMS-managed keys to encrypt the inventory file (documented below).
        
                * `key_id` (`pulumi.Input[str]`) - The ARN of the KMS customer master key (CMK) used to encrypt the inventory file.
        
              * `sseS3` (`pulumi.Input[dict]`) - Specifies to use server-side encryption with Amazon S3-managed keys (SSE-S3) to encrypt the inventory file.
        
            * `format` (`pulumi.Input[str]`) - Specifies the output format of the inventory results. Can be `CSV`, [`ORC`](https://orc.apache.org/) or [`Parquet`](https://parquet.apache.org/).
            * `prefix` (`pulumi.Input[str]`) - The prefix that is prepended to all inventory results.
        
        The **filter** object supports the following:
        
          * `prefix` (`pulumi.Input[str]`) - The prefix that is prepended to all inventory results.
        
        The **schedule** object supports the following:
        
          * `frequency` (`pulumi.Input[str]`) - Specifies how frequently inventory results are produced. Can be `Daily` or `Weekly`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_inventory.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if bucket is None:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            if destination is None:
                raise TypeError("Missing required property 'destination'")
            __props__['destination'] = destination
            __props__['enabled'] = enabled
            __props__['filter'] = filter
            if included_object_versions is None:
                raise TypeError("Missing required property 'included_object_versions'")
            __props__['included_object_versions'] = included_object_versions
            __props__['name'] = name
            __props__['optional_fields'] = optional_fields
            if schedule is None:
                raise TypeError("Missing required property 'schedule'")
            __props__['schedule'] = schedule
        super(Inventory, __self__).__init__(
            'aws:s3/inventory:Inventory',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, bucket=None, destination=None, enabled=None, filter=None, included_object_versions=None, name=None, optional_fields=None, schedule=None):
        """
        Get an existing Inventory resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The S3 bucket configuration where inventory results are published (documented below).
        :param pulumi.Input[dict] destination: Destination bucket where inventory list files are written (documented below).
        :param pulumi.Input[bool] enabled: Specifies whether the inventory is enabled or disabled.
        :param pulumi.Input[dict] filter: Object filtering that accepts a prefix (documented below).
        :param pulumi.Input[str] included_object_versions: Object filtering that accepts a prefix (documented below). Can be `All` or `Current`.
        :param pulumi.Input[str] name: Unique identifier of the inventory configuration for the bucket.
        :param pulumi.Input[list] optional_fields: Contains the optional fields that are included in the inventory results.
        :param pulumi.Input[dict] schedule: Contains the frequency for generating inventory results (documented below).
        
        The **destination** object supports the following:
        
          * `bucket` (`pulumi.Input[dict]`) - The S3 bucket configuration where inventory results are published (documented below).
        
            * `account_id` (`pulumi.Input[str]`) - The ID of the account that owns the destination bucket. Recommended to be set to prevent problems if the destination bucket ownership changes.
            * `bucketArn` (`pulumi.Input[str]`) - The Amazon S3 bucket ARN of the destination.
            * `encryption` (`pulumi.Input[dict]`) - Contains the type of server-side encryption to use to encrypt the inventory (documented below).
        
              * `sseKms` (`pulumi.Input[dict]`) - Specifies to use server-side encryption with AWS KMS-managed keys to encrypt the inventory file (documented below).
        
                * `key_id` (`pulumi.Input[str]`) - The ARN of the KMS customer master key (CMK) used to encrypt the inventory file.
        
              * `sseS3` (`pulumi.Input[dict]`) - Specifies to use server-side encryption with Amazon S3-managed keys (SSE-S3) to encrypt the inventory file.
        
            * `format` (`pulumi.Input[str]`) - Specifies the output format of the inventory results. Can be `CSV`, [`ORC`](https://orc.apache.org/) or [`Parquet`](https://parquet.apache.org/).
            * `prefix` (`pulumi.Input[str]`) - The prefix that is prepended to all inventory results.
        
        The **filter** object supports the following:
        
          * `prefix` (`pulumi.Input[str]`) - The prefix that is prepended to all inventory results.
        
        The **schedule** object supports the following:
        
          * `frequency` (`pulumi.Input[str]`) - Specifies how frequently inventory results are produced. Can be `Daily` or `Weekly`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_inventory.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["bucket"] = bucket
        __props__["destination"] = destination
        __props__["enabled"] = enabled
        __props__["filter"] = filter
        __props__["included_object_versions"] = included_object_versions
        __props__["name"] = name
        __props__["optional_fields"] = optional_fields
        __props__["schedule"] = schedule
        return Inventory(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

