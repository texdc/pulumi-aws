# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetLoadBalancerResult:
    """
    A collection of values returned by getLoadBalancer.
    """
    def __init__(__self__, access_logs=None, availability_zones=None, connection_draining=None, connection_draining_timeout=None, cross_zone_load_balancing=None, dns_name=None, health_check=None, idle_timeout=None, instances=None, internal=None, listeners=None, name=None, security_groups=None, source_security_group=None, source_security_group_id=None, subnets=None, tags=None, zone_id=None, id=None):
        if access_logs and not isinstance(access_logs, dict):
            raise TypeError("Expected argument 'access_logs' to be a dict")
        __self__.access_logs = access_logs
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        __self__.availability_zones = availability_zones
        if connection_draining and not isinstance(connection_draining, bool):
            raise TypeError("Expected argument 'connection_draining' to be a bool")
        __self__.connection_draining = connection_draining
        if connection_draining_timeout and not isinstance(connection_draining_timeout, float):
            raise TypeError("Expected argument 'connection_draining_timeout' to be a float")
        __self__.connection_draining_timeout = connection_draining_timeout
        if cross_zone_load_balancing and not isinstance(cross_zone_load_balancing, bool):
            raise TypeError("Expected argument 'cross_zone_load_balancing' to be a bool")
        __self__.cross_zone_load_balancing = cross_zone_load_balancing
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        __self__.dns_name = dns_name
        if health_check and not isinstance(health_check, dict):
            raise TypeError("Expected argument 'health_check' to be a dict")
        __self__.health_check = health_check
        if idle_timeout and not isinstance(idle_timeout, float):
            raise TypeError("Expected argument 'idle_timeout' to be a float")
        __self__.idle_timeout = idle_timeout
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        __self__.instances = instances
        if internal and not isinstance(internal, bool):
            raise TypeError("Expected argument 'internal' to be a bool")
        __self__.internal = internal
        if listeners and not isinstance(listeners, list):
            raise TypeError("Expected argument 'listeners' to be a list")
        __self__.listeners = listeners
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if security_groups and not isinstance(security_groups, list):
            raise TypeError("Expected argument 'security_groups' to be a list")
        __self__.security_groups = security_groups
        if source_security_group and not isinstance(source_security_group, str):
            raise TypeError("Expected argument 'source_security_group' to be a str")
        __self__.source_security_group = source_security_group
        if source_security_group_id and not isinstance(source_security_group_id, str):
            raise TypeError("Expected argument 'source_security_group_id' to be a str")
        __self__.source_security_group_id = source_security_group_id
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        __self__.subnets = subnets
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        __self__.zone_id = zone_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            access_logs=self.access_logs,
            availability_zones=self.availability_zones,
            connection_draining=self.connection_draining,
            connection_draining_timeout=self.connection_draining_timeout,
            cross_zone_load_balancing=self.cross_zone_load_balancing,
            dns_name=self.dns_name,
            health_check=self.health_check,
            idle_timeout=self.idle_timeout,
            instances=self.instances,
            internal=self.internal,
            listeners=self.listeners,
            name=self.name,
            security_groups=self.security_groups,
            source_security_group=self.source_security_group,
            source_security_group_id=self.source_security_group_id,
            subnets=self.subnets,
            tags=self.tags,
            zone_id=self.zone_id,
            id=self.id)

def get_load_balancer(name=None,tags=None,opts=None):
    """
    Provides information about a "classic" Elastic Load Balancer (ELB).
    See [LB Data Source](https://www.terraform.io/docs/providers/aws/d/lb.html) if you are looking for "v2"
    Application Load Balancer (ALB) or Network Load Balancer (NLB).
    
    This data source can prove useful when a module accepts an LB as an input
    variable and needs to, for example, determine the security groups associated
    with it, etc.
    
    :param str name: The unique name of the load balancer.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elb.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:elb/getLoadBalancer:getLoadBalancer', __args__, opts=opts).value

    return AwaitableGetLoadBalancerResult(
        access_logs=__ret__.get('accessLogs'),
        availability_zones=__ret__.get('availabilityZones'),
        connection_draining=__ret__.get('connectionDraining'),
        connection_draining_timeout=__ret__.get('connectionDrainingTimeout'),
        cross_zone_load_balancing=__ret__.get('crossZoneLoadBalancing'),
        dns_name=__ret__.get('dnsName'),
        health_check=__ret__.get('healthCheck'),
        idle_timeout=__ret__.get('idleTimeout'),
        instances=__ret__.get('instances'),
        internal=__ret__.get('internal'),
        listeners=__ret__.get('listeners'),
        name=__ret__.get('name'),
        security_groups=__ret__.get('securityGroups'),
        source_security_group=__ret__.get('sourceSecurityGroup'),
        source_security_group_id=__ret__.get('sourceSecurityGroupId'),
        subnets=__ret__.get('subnets'),
        tags=__ret__.get('tags'),
        zone_id=__ret__.get('zoneId'),
        id=__ret__.get('id'))
