# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Instance(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the Lightsail instance (matches `id`).
    """
    availability_zone: pulumi.Output[str]
    """
    The Availability Zone in which to create your
    instance (see list below)
    """
    blueprint_id: pulumi.Output[str]
    """
    The ID for a virtual private server image
    (see list below)
    """
    bundle_id: pulumi.Output[str]
    """
    The bundle of specification information (see list below)
    """
    cpu_count: pulumi.Output[float]
    created_at: pulumi.Output[str]
    """
    The timestamp when the instance was created.
    * `availability_zone`
    * `blueprint_id`
    * `bundle_id`
    * `key_pair_name`
    * `user_data`
    """
    ipv6_address: pulumi.Output[str]
    is_static_ip: pulumi.Output[bool]
    key_pair_name: pulumi.Output[str]
    """
    The name of your key pair. Created in the
    Lightsail console (cannot use `ec2.KeyPair` at this time)
    """
    name: pulumi.Output[str]
    """
    The name of the Lightsail Instance
    """
    private_ip_address: pulumi.Output[str]
    public_ip_address: pulumi.Output[str]
    ram_size: pulumi.Output[float]
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    user_data: pulumi.Output[str]
    """
    launch script to configure server with additional user data
    """
    username: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, availability_zone=None, blueprint_id=None, bundle_id=None, key_pair_name=None, name=None, tags=None, user_data=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Lightsail Instance. Amazon Lightsail is a service to provide easy virtual private servers
        with custom software already setup. See [What is Amazon Lightsail?](https://lightsail.aws.amazon.com/ls/docs/getting-started/article/what-is-amazon-lightsail)
        for more information.
        
        > **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details
        
        ## Availability Zones
        
        Lightsail currently supports the following Availability Zones (e.g. `us-east-1a`):
        
        - `ap-northeast-1{a,c,d}`
        - `ap-northeast-2{a,c}`
        - `ap-south-1{a,b}`
        - `ap-southeast-1{a,b,c}`
        - `ap-southeast-2{a,b,c}`
        - `ca-central-1{a,b}`
        - `eu-central-1{a,b,c}`
        - `eu-west-1{a,b,c}`
        - `eu-west-2{a,b,c}`
        - `eu-west-3{a,b,c}`
        - `us-east-1{a,b,c,d,e,f}`
        - `us-east-2{a,b,c}`
        - `us-west-2{a,b,c}`
        
        ## Blueprints
        
        Lightsail currently supports the following Blueprint IDs:
        
        ### OS Only
        
        - `amazon_linux_2018_03_0_2`
        - `centos_7_1901_01`
        - `debian_8_7`
        - `debian_9_5`
        - `freebsd_11_1`
        - `opensuse_42_2`
        - `ubuntu_16_04_2`
        - `ubuntu_18_04`
        
        ### Apps and OS
        
        - `drupal_8_5_6`
        - `gitlab_11_1_4_1`
        - `joomla_3_8_11`
        - `lamp_5_6_37_2`
        - `lamp_7_1_20_1`
        - `magento_2_2_5`
        - `mean_4_0_1`
        - `nginx_1_14_0_1`
        - `nodejs_10_8_0`
        - `plesk_ubuntu_17_8_11_1`
        - `redmine_3_4_6`
        - `wordpress_4_9_8`
        - `wordpress_multisite_4_9_8`
        
        ## Bundles
        
        Lightsail currently supports the following Bundle IDs (e.g. an instance in `ap-northeast-1` would use `small_2_0`):
        
        ### Prefix
        
        A Bundle ID starts with one of the below size prefixes:
        
        - `nano_`
        - `micro_`
        - `small_`
        - `medium_`
        - `large_`
        - `xlarge_`
        - `2xlarge_`
        
        ### Suffix
        
        A Bundle ID ends with one of the following suffixes depending on Availability Zone:
        
        - ap-northeast-1: `2_0`
        - ap-northeast-2: `2_0`
        - ap-south-1: `2_1`
        - ap-southeast-1: `2_0`
        - ap-southeast-2: `2_2`
        - ca-central-1: `2_0`
        - eu-central-1: `2_0`
        - eu-west-1: `2_0`
        - eu-west-2: `2_0`
        - eu-west-3: `2_0`
        - us-east-1: `2_0`
        - us-east-2: `2_0`
        - us-west-2: `2_0`
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The Availability Zone in which to create your
               instance (see list below)
        :param pulumi.Input[str] blueprint_id: The ID for a virtual private server image
               (see list below)
        :param pulumi.Input[str] bundle_id: The bundle of specification information (see list below)
        :param pulumi.Input[str] key_pair_name: The name of your key pair. Created in the
               Lightsail console (cannot use `ec2.KeyPair` at this time)
        :param pulumi.Input[str] name: The name of the Lightsail Instance
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] user_data: launch script to configure server with additional user data

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_instance.html.markdown.
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

            if availability_zone is None:
                raise TypeError("Missing required property 'availability_zone'")
            __props__['availability_zone'] = availability_zone
            if blueprint_id is None:
                raise TypeError("Missing required property 'blueprint_id'")
            __props__['blueprint_id'] = blueprint_id
            if bundle_id is None:
                raise TypeError("Missing required property 'bundle_id'")
            __props__['bundle_id'] = bundle_id
            __props__['key_pair_name'] = key_pair_name
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['user_data'] = user_data
            __props__['arn'] = None
            __props__['cpu_count'] = None
            __props__['created_at'] = None
            __props__['ipv6_address'] = None
            __props__['is_static_ip'] = None
            __props__['private_ip_address'] = None
            __props__['public_ip_address'] = None
            __props__['ram_size'] = None
            __props__['username'] = None
        super(Instance, __self__).__init__(
            'aws:lightsail/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, availability_zone=None, blueprint_id=None, bundle_id=None, cpu_count=None, created_at=None, ipv6_address=None, is_static_ip=None, key_pair_name=None, name=None, private_ip_address=None, public_ip_address=None, ram_size=None, tags=None, user_data=None, username=None):
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the Lightsail instance (matches `id`).
        :param pulumi.Input[str] availability_zone: The Availability Zone in which to create your
               instance (see list below)
        :param pulumi.Input[str] blueprint_id: The ID for a virtual private server image
               (see list below)
        :param pulumi.Input[str] bundle_id: The bundle of specification information (see list below)
        :param pulumi.Input[str] created_at: The timestamp when the instance was created.
               * `availability_zone`
               * `blueprint_id`
               * `bundle_id`
               * `key_pair_name`
               * `user_data`
        :param pulumi.Input[str] key_pair_name: The name of your key pair. Created in the
               Lightsail console (cannot use `ec2.KeyPair` at this time)
        :param pulumi.Input[str] name: The name of the Lightsail Instance
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] user_data: launch script to configure server with additional user data

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_instance.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["arn"] = arn
        __props__["availability_zone"] = availability_zone
        __props__["blueprint_id"] = blueprint_id
        __props__["bundle_id"] = bundle_id
        __props__["cpu_count"] = cpu_count
        __props__["created_at"] = created_at
        __props__["ipv6_address"] = ipv6_address
        __props__["is_static_ip"] = is_static_ip
        __props__["key_pair_name"] = key_pair_name
        __props__["name"] = name
        __props__["private_ip_address"] = private_ip_address
        __props__["public_ip_address"] = public_ip_address
        __props__["ram_size"] = ram_size
        __props__["tags"] = tags
        __props__["user_data"] = user_data
        __props__["username"] = username
        return Instance(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

