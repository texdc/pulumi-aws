# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Rule(pulumi.CustomResource):
    metric_name: pulumi.Output[str]
    """
    The name or description for the Amazon CloudWatch metric of this rule.
    """
    name: pulumi.Output[str]
    """
    The name or description of the rule.
    """
    predicates: pulumi.Output[list]
    """
    The objects to include in a rule (documented below).
    
      * `dataId` (`str`)
      * `negated` (`bool`)
      * `type` (`str`)
    """
    def __init__(__self__, resource_name, opts=None, metric_name=None, name=None, predicates=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an WAF Regional Rule Resource for use with Application Load Balancer.
        
        ## Nested Fields
        
        ### `predicate`
        
        See the [WAF Documentation](https://docs.aws.amazon.com/waf/latest/APIReference/API_Predicate.html) for more information.
        
        #### Arguments
        
        * `type` - (Required) The type of predicate in a rule. Valid values: `ByteMatch`, `GeoMatch`, `IPMatch`, `RegexMatch`, `SizeConstraint`, `SqlInjectionMatch`, or `XssMatch`
        * `data_id` - (Required) The unique identifier of a predicate, such as the ID of a `ByteMatchSet` or `IPSet`.
        * `negated` - (Required) Whether to use the settings or the negated settings that you specified in the objects.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule.
        :param pulumi.Input[str] name: The name or description of the rule.
        :param pulumi.Input[list] predicates: The objects to include in a rule (documented below).
        
        The **predicates** object supports the following:
        
          * `dataId` (`pulumi.Input[str]`)
          * `negated` (`pulumi.Input[bool]`)
          * `type` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_rule.html.markdown.
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

            if metric_name is None:
                raise TypeError("Missing required property 'metric_name'")
            __props__['metric_name'] = metric_name
            __props__['name'] = name
            __props__['predicates'] = predicates
        super(Rule, __self__).__init__(
            'aws:wafregional/rule:Rule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, metric_name=None, name=None, predicates=None):
        """
        Get an existing Rule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule.
        :param pulumi.Input[str] name: The name or description of the rule.
        :param pulumi.Input[list] predicates: The objects to include in a rule (documented below).
        
        The **predicates** object supports the following:
        
          * `dataId` (`pulumi.Input[str]`)
          * `negated` (`pulumi.Input[bool]`)
          * `type` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_rule.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["metric_name"] = metric_name
        __props__["name"] = name
        __props__["predicates"] = predicates
        return Rule(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

