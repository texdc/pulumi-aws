# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class AssessmentTarget(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The target assessment ARN.
    """
    name: pulumi.Output[str]
    """
    The name of the assessment target.
    * `resource_group_arn` (Required )- The resource group ARN stating tags for instance matching.
    """
    resource_group_arn: pulumi.Output[str]
    def __init__(__self__, __name__, __opts__=None, name=None, resource_group_arn=None):
        """
        Provides a Inspector assessment target
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] name: The name of the assessment target.
               * `resource_group_arn` (Required )- The resource group ARN stating tags for instance matching.
        :param pulumi.Input[str] resource_group_arn
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['name'] = name

        if not resource_group_arn:
            raise TypeError('Missing required property resource_group_arn')
        __props__['resource_group_arn'] = resource_group_arn

        __props__['arn'] = None

        super(AssessmentTarget, __self__).__init__(
            'aws:inspector/assessmentTarget:AssessmentTarget',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

