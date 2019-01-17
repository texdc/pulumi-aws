# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Portfolio(pulumi.CustomResource):
    arn: pulumi.Output[str]
    created_time: pulumi.Output[str]
    description: pulumi.Output[str]
    """
    Description of the portfolio
    """
    name: pulumi.Output[str]
    """
    The name of the portfolio.
    """
    provider_name: pulumi.Output[str]
    """
    Name of the person or organization who owns the portfolio.
    """
    tags: pulumi.Output[dict]
    """
    Tags to apply to the connection.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, name=None, provider_name=None, tags=None):
        """
        Provides a resource to create a Service Catalog Portfolio.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] description: Description of the portfolio
        :param pulumi.Input[str] name: The name of the portfolio.
        :param pulumi.Input[str] provider_name: Name of the person or organization who owns the portfolio.
        :param pulumi.Input[dict] tags: Tags to apply to the connection.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['description'] = description

        __props__['name'] = name

        __props__['provider_name'] = provider_name

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['created_time'] = None

        super(Portfolio, __self__).__init__(
            'aws:servicecatalog/portfolio:Portfolio',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

