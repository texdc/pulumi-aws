// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `ec2.SecurityGroup` provides details about a specific Security Group.
// 
// This resource can prove useful when a module accepts a Security Group id as
// an input variable and needs to, for example, determine the id of the
// VPC that the security group belongs to.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/security_group.html.markdown.
func LookupSecurityGroup(ctx *pulumi.Context, args *GetSecurityGroupArgs) (*GetSecurityGroupResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["id"] = args.Id
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
		inputs["vpcId"] = args.VpcId
	}
	outputs, err := ctx.Invoke("aws:ec2/getSecurityGroup:getSecurityGroup", inputs)
	if err != nil {
		return nil, err
	}
	return &GetSecurityGroupResult{
		Arn: outputs["arn"],
		Description: outputs["description"],
		Filters: outputs["filters"],
		Id: outputs["id"],
		Name: outputs["name"],
		Tags: outputs["tags"],
		VpcId: outputs["vpcId"],
	}, nil
}

// A collection of arguments for invoking getSecurityGroup.
type GetSecurityGroupArgs struct {
	// Custom filter block as described below.
	Filters interface{}
	// The id of the specific security group to retrieve.
	Id interface{}
	// The name of the field to filter by, as defined by
	// [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html).
	Name interface{}
	// A mapping of tags, each pair of which must exactly match
	// a pair on the desired security group.
	Tags interface{}
	// The id of the VPC that the desired security group belongs to.
	VpcId interface{}
}

// A collection of values returned by getSecurityGroup.
type GetSecurityGroupResult struct {
	// The computed ARN of the security group.
	Arn interface{}
	// The description of the security group.
	Description interface{}
	Filters interface{}
	Id interface{}
	Name interface{}
	Tags interface{}
	VpcId interface{}
}
