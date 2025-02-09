# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Group(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of group
    """
    aws_account_id: pulumi.Output[str]
    """
    The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    """
    description: pulumi.Output[str]
    """
    A description for the group.
    """
    group_name: pulumi.Output[str]
    """
    A name for the group.
    """
    namespace: pulumi.Output[str]
    """
    The namespace. Currently, you should set this to `default`.
    """
    def __init__(__self__, resource_name, opts=None, aws_account_id=None, description=None, group_name=None, namespace=None, __props__=None, __name__=None, __opts__=None):
        """
        Resource for managing Quick Sight Group
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param pulumi.Input[str] description: A description for the group.
        :param pulumi.Input[str] group_name: A name for the group.
        :param pulumi.Input[str] namespace: The namespace. Currently, you should set this to `default`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/quicksight_group.html.markdown.
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

            __props__['aws_account_id'] = aws_account_id
            __props__['description'] = description
            if group_name is None:
                raise TypeError("Missing required property 'group_name'")
            __props__['group_name'] = group_name
            __props__['namespace'] = namespace
            __props__['arn'] = None
        super(Group, __self__).__init__(
            'aws:quicksight/group:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, aws_account_id=None, description=None, group_name=None, namespace=None):
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of group
        :param pulumi.Input[str] aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param pulumi.Input[str] description: A description for the group.
        :param pulumi.Input[str] group_name: A name for the group.
        :param pulumi.Input[str] namespace: The namespace. Currently, you should set this to `default`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/quicksight_group.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["arn"] = arn
        __props__["aws_account_id"] = aws_account_id
        __props__["description"] = description
        __props__["group_name"] = group_name
        __props__["namespace"] = namespace
        return Group(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

