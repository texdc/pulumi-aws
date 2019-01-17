// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Get information on an EC2 Transit Gateway.
 * 
 * ## Example Usage
 * 
 * ### By Filter
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_ec2_transit_gateway_example = pulumi.output(aws.ec2transitgateway.getTransitGateway({
 *     filters: [{
 *         name: "amazon-side-asn",
 *         values: ["64512"],
 *     }],
 * }));
 * ```
 * ### By Identifier
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_ec2_transit_gateway_example = pulumi.output(aws.ec2transitgateway.getTransitGateway({
 *     id: "tgw-12345678",
 * }));
 * ```
 */
export function getTransitGateway(args?: GetTransitGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetTransitGatewayResult> {
    args = args || {};
    return pulumi.runtime.invoke("aws:ec2transitgateway/getTransitGateway:getTransitGateway", {
        "filters": args.filters,
        "id": args.id,
        "tags": args.tags,
    }, opts);
}

/**
 * A collection of arguments for invoking getTransitGateway.
 */
export interface GetTransitGatewayArgs {
    /**
     * One or more configuration blocks containing name-values filters. Detailed below.
     */
    readonly filters?: { name: string, values: string[] }[];
    /**
     * Identifier of the EC2 Transit Gateway.
     */
    readonly id?: string;
    readonly tags?: {[key: string]: any};
}

/**
 * A collection of values returned by getTransitGateway.
 */
export interface GetTransitGatewayResult {
    /**
     * Private Autonomous System Number (ASN) for the Amazon side of a BGP session
     */
    readonly amazonSideAsn: number;
    /**
     * EC2 Transit Gateway Amazon Resource Name (ARN)
     */
    readonly arn: string;
    /**
     * Identifier of the default association route table
     */
    readonly associationDefaultRouteTableId: string;
    /**
     * Whether resource attachment requests are automatically accepted.
     */
    readonly autoAcceptSharedAttachments: string;
    /**
     * Whether resource attachments are automatically associated with the default association route table.
     */
    readonly defaultRouteTableAssociation: string;
    /**
     * Whether resource attachments automatically propagate routes to the default propagation route table.
     */
    readonly defaultRouteTablePropagation: string;
    /**
     * Description of the EC2 Transit Gateway
     */
    readonly description: string;
    /**
     * Whether DNS support is enabled.
     */
    readonly dnsSupport: string;
    /**
     * Identifier of the AWS account that owns the EC2 Transit Gateway
     */
    readonly ownerId: string;
    /**
     * Identifier of the default propagation route table.
     */
    readonly propagationDefaultRouteTableId: string;
    /**
     * Key-value tags for the EC2 Transit Gateway
     */
    readonly tags: {[key: string]: any};
    /**
     * Whether VPN Equal Cost Multipath Protocol support is enabled.
     */
    readonly vpnEcmpSupport: string;
}
