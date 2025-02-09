# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class RegexMatchSet(pulumi.CustomResource):
    name: pulumi.Output[str]
    """
    The name or description of the Regex Match Set.
    """
    regex_match_tuples: pulumi.Output[list]
    """
    The regular expression pattern that you want AWS WAF to search for in web requests,
    the location in requests that you want AWS WAF to search, and other settings. See below.
    
      * `fieldToMatch` (`dict`) - The part of a web request that you want to search, such as a specified header or a query string.
    
        * `data` (`str`) - When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
          If `type` is any other value, omit this field.
        * `type` (`str`) - The part of the web request that you want AWS WAF to search for a specified string.
          e.g. `HEADER`, `METHOD` or `BODY`.
          See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
          for all supported values.
    
      * `regexPatternSetId` (`str`) - The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
      * `textTransformation` (`str`) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
        e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
        See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
        for all supported values.
    """
    def __init__(__self__, resource_name, opts=None, name=None, regex_match_tuples=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a WAF Regex Match Set Resource
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name or description of the Regex Match Set.
        :param pulumi.Input[list] regex_match_tuples: The regular expression pattern that you want AWS WAF to search for in web requests,
               the location in requests that you want AWS WAF to search, and other settings. See below.
        
        The **regex_match_tuples** object supports the following:
        
          * `fieldToMatch` (`pulumi.Input[dict]`) - The part of a web request that you want to search, such as a specified header or a query string.
        
            * `data` (`pulumi.Input[str]`) - When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
              If `type` is any other value, omit this field.
            * `type` (`pulumi.Input[str]`) - The part of the web request that you want AWS WAF to search for a specified string.
              e.g. `HEADER`, `METHOD` or `BODY`.
              See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
              for all supported values.
        
          * `regexPatternSetId` (`pulumi.Input[str]`) - The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
          * `textTransformation` (`pulumi.Input[str]`) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
            e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
            See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
            for all supported values.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_match_set.html.markdown.
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

            __props__['name'] = name
            __props__['regex_match_tuples'] = regex_match_tuples
        super(RegexMatchSet, __self__).__init__(
            'aws:waf/regexMatchSet:RegexMatchSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, name=None, regex_match_tuples=None):
        """
        Get an existing RegexMatchSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name or description of the Regex Match Set.
        :param pulumi.Input[list] regex_match_tuples: The regular expression pattern that you want AWS WAF to search for in web requests,
               the location in requests that you want AWS WAF to search, and other settings. See below.
        
        The **regex_match_tuples** object supports the following:
        
          * `fieldToMatch` (`pulumi.Input[dict]`) - The part of a web request that you want to search, such as a specified header or a query string.
        
            * `data` (`pulumi.Input[str]`) - When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
              If `type` is any other value, omit this field.
            * `type` (`pulumi.Input[str]`) - The part of the web request that you want AWS WAF to search for a specified string.
              e.g. `HEADER`, `METHOD` or `BODY`.
              See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
              for all supported values.
        
          * `regexPatternSetId` (`pulumi.Input[str]`) - The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
          * `textTransformation` (`pulumi.Input[str]`) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
            e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
            See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
            for all supported values.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_match_set.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["name"] = name
        __props__["regex_match_tuples"] = regex_match_tuples
        return RegexMatchSet(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

