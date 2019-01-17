# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Route(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the route.
    """
    created_date: pulumi.Output[str]
    """
    The creation date of the route.
    """
    last_updated_date: pulumi.Output[str]
    """
    The last update date of the route.
    """
    mesh_name: pulumi.Output[str]
    """
    The name of the service mesh in which to create the route.
    """
    name: pulumi.Output[str]
    """
    The name to use for the route.
    """
    spec: pulumi.Output[dict]
    """
    The route specification to apply.
    """
    virtual_router_name: pulumi.Output[str]
    def __init__(__self__, __name__, __opts__=None, mesh_name=None, name=None, spec=None, virtual_router_name=None):
        """
        Provides an AWS App Mesh route resource.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the route.
        :param pulumi.Input[str] name: The name to use for the route.
        :param pulumi.Input[dict] spec: The route specification to apply.
        :param pulumi.Input[str] virtual_router_name
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not mesh_name:
            raise TypeError('Missing required property mesh_name')
        __props__['mesh_name'] = mesh_name

        __props__['name'] = name

        if not spec:
            raise TypeError('Missing required property spec')
        __props__['spec'] = spec

        if not virtual_router_name:
            raise TypeError('Missing required property virtual_router_name')
        __props__['virtual_router_name'] = virtual_router_name

        __props__['arn'] = None
        __props__['created_date'] = None
        __props__['last_updated_date'] = None

        super(Route, __self__).__init__(
            'aws:appmesh/route:Route',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

