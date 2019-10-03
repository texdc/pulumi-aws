// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides information about a MQ Broker.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const config = new pulumi.Config();
 * const brokerId = config.get("brokerId") || "";
 * const brokerName = config.get("brokerName") || "";
 * 
 * const byId = aws.mq.getBroker({
 *     brokerId: brokerId,
 * });
 * const byName = aws.mq.getBroker({
 *     brokerName: brokerName,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/mq_broker.html.markdown.
 */
export function getBroker(args?: GetBrokerArgs, opts?: pulumi.InvokeOptions): Promise<GetBrokerResult> & GetBrokerResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetBrokerResult> = pulumi.runtime.invoke("aws:mq/getBroker:getBroker", {
        "brokerId": args.brokerId,
        "brokerName": args.brokerName,
        "logs": args.logs,
        "tags": args.tags,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getBroker.
 */
export interface GetBrokerArgs {
    /**
     * The unique id of the mq broker.
     */
    readonly brokerId?: string;
    /**
     * The unique name of the mq broker.
     */
    readonly brokerName?: string;
    readonly logs?: inputs.mq.GetBrokerLogs;
    readonly tags?: {[key: string]: any};
}

/**
 * A collection of values returned by getBroker.
 */
export interface GetBrokerResult {
    readonly arn: string;
    readonly autoMinorVersionUpgrade: boolean;
    readonly brokerId: string;
    readonly brokerName: string;
    readonly configuration: outputs.mq.GetBrokerConfiguration;
    readonly deploymentMode: string;
    readonly encryptionOptions: outputs.mq.GetBrokerEncryptionOption[];
    readonly engineType: string;
    readonly engineVersion: string;
    readonly hostInstanceType: string;
    readonly instances: outputs.mq.GetBrokerInstance[];
    readonly logs?: outputs.mq.GetBrokerLogs;
    readonly maintenanceWindowStartTime: outputs.mq.GetBrokerMaintenanceWindowStartTime;
    readonly publiclyAccessible: boolean;
    readonly securityGroups: string[];
    readonly subnetIds: string[];
    readonly tags: {[key: string]: any};
    readonly users: outputs.mq.GetBrokerUser[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
