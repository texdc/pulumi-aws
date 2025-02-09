// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2transitgateway

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get information on an EC2 Transit Gateway Route Table.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ec2_transit_gateway_route_table.html.markdown.
func LookupRouteTable(ctx *pulumi.Context, args *GetRouteTableArgs) (*GetRouteTableResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["id"] = args.Id
		inputs["tags"] = args.Tags
	}
	outputs, err := ctx.Invoke("aws:ec2transitgateway/getRouteTable:getRouteTable", inputs)
	if err != nil {
		return nil, err
	}
	return &GetRouteTableResult{
		DefaultAssociationRouteTable: outputs["defaultAssociationRouteTable"],
		DefaultPropagationRouteTable: outputs["defaultPropagationRouteTable"],
		Filters: outputs["filters"],
		Id: outputs["id"],
		Tags: outputs["tags"],
		TransitGatewayId: outputs["transitGatewayId"],
	}, nil
}

// A collection of arguments for invoking getRouteTable.
type GetRouteTableArgs struct {
	// One or more configuration blocks containing name-values filters. Detailed below.
	Filters interface{}
	// Identifier of the EC2 Transit Gateway Route Table.
	Id interface{}
	Tags interface{}
}

// A collection of values returned by getRouteTable.
type GetRouteTableResult struct {
	// Boolean whether this is the default association route table for the EC2 Transit Gateway
	DefaultAssociationRouteTable interface{}
	// Boolean whether this is the default propagation route table for the EC2 Transit Gateway
	DefaultPropagationRouteTable interface{}
	Filters interface{}
	// EC2 Transit Gateway Route Table identifier
	Id interface{}
	// Key-value tags for the EC2 Transit Gateway Route Table
	Tags interface{}
	// EC2 Transit Gateway identifier
	TransitGatewayId interface{}
}
