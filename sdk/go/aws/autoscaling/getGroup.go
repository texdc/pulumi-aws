// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package autoscaling

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get information on an existing autoscaling group.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/autoscaling_group.html.markdown.
func LookupGroup(ctx *pulumi.Context, args *GetGroupArgs) (*GetGroupResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("aws:autoscaling/getGroup:getGroup", inputs)
	if err != nil {
		return nil, err
	}
	return &GetGroupResult{
		Arn: outputs["arn"],
		AvailabilityZones: outputs["availabilityZones"],
		DefaultCooldown: outputs["defaultCooldown"],
		DesiredCapacity: outputs["desiredCapacity"],
		HealthCheckGracePeriod: outputs["healthCheckGracePeriod"],
		HealthCheckType: outputs["healthCheckType"],
		LaunchConfiguration: outputs["launchConfiguration"],
		LoadBalancers: outputs["loadBalancers"],
		MaxSize: outputs["maxSize"],
		MinSize: outputs["minSize"],
		Name: outputs["name"],
		NewInstancesProtectedFromScaleIn: outputs["newInstancesProtectedFromScaleIn"],
		PlacementGroup: outputs["placementGroup"],
		ServiceLinkedRoleArn: outputs["serviceLinkedRoleArn"],
		Status: outputs["status"],
		TargetGroupArns: outputs["targetGroupArns"],
		TerminationPolicies: outputs["terminationPolicies"],
		VpcZoneIdentifier: outputs["vpcZoneIdentifier"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getGroup.
type GetGroupArgs struct {
	// Specify the exact name of the desired autoscaling group.
	Name interface{}
}

// A collection of values returned by getGroup.
type GetGroupResult struct {
	// The Amazon Resource Name (ARN) of the Auto Scaling group.
	Arn interface{}
	// One or more Availability Zones for the group.
	AvailabilityZones interface{}
	DefaultCooldown interface{}
	// The desired size of the group.
	DesiredCapacity interface{}
	// The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.
	HealthCheckGracePeriod interface{}
	// The service to use for the health checks. The valid values are EC2 and ELB.
	HealthCheckType interface{}
	// The name of the associated launch configuration.
	LaunchConfiguration interface{}
	// One or more load balancers associated with the group.
	LoadBalancers interface{}
	// The maximum size of the group.
	MaxSize interface{}
	// The minimum size of the group.
	MinSize interface{}
	// The name of the Auto Scaling group.
	Name interface{}
	NewInstancesProtectedFromScaleIn interface{}
	// The name of the placement group into which to launch your instances, if any. For more information, see Placement Groups (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the Amazon Elastic Compute Cloud User Guide.
	PlacementGroup interface{}
	// The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.
	ServiceLinkedRoleArn interface{}
	// The current state of the group when DeleteAutoScalingGroup is in progress.
	Status interface{}
	// The Amazon Resource Names (ARN) of the target groups for your load balancer.
	TargetGroupArns interface{}
	// The termination policies for the group.
	TerminationPolicies interface{}
	// VPC ID for the group.
	VpcZoneIdentifier interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
