// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package wafregional

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `wafregional.IpSet` Retrieves a WAF Regional IP Set Resource Id.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/wafregional_ipset.html.markdown.
func LookupIpset(ctx *pulumi.Context, args *GetIpsetArgs) (*GetIpsetResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("aws:wafregional/getIpset:getIpset", inputs)
	if err != nil {
		return nil, err
	}
	return &GetIpsetResult{
		Name: outputs["name"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getIpset.
type GetIpsetArgs struct {
	// The name of the WAF Regional IP set.
	Name interface{}
}

// A collection of values returned by getIpset.
type GetIpsetResult struct {
	Name interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
