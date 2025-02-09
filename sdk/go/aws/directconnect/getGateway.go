// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package directconnect

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Retrieve information about a Direct Connect Gateway.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/dx_gateway.html.markdown.
func LookupGateway(ctx *pulumi.Context, args *GetGatewayArgs) (*GetGatewayResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("aws:directconnect/getGateway:getGateway", inputs)
	if err != nil {
		return nil, err
	}
	return &GetGatewayResult{
		AmazonSideAsn: outputs["amazonSideAsn"],
		Name: outputs["name"],
		OwnerAccountId: outputs["ownerAccountId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getGateway.
type GetGatewayArgs struct {
	// The name of the gateway to retrieve.
	Name interface{}
}

// A collection of values returned by getGateway.
type GetGatewayResult struct {
	// The ASN on the Amazon side of the connection.
	AmazonSideAsn interface{}
	Name interface{}
	// AWS Account ID of the gateway.
	OwnerAccountId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
