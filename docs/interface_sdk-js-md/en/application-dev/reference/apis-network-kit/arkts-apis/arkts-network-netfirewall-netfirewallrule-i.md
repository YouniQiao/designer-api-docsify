# NetFirewallRule

Firewall rules.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-netFirewall-interface NetFirewallRule--><!--Device-netFirewall-interface NetFirewallRule-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## Modules to Import

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
```

## action

```TypeScript
action: FirewallRuleAction
```

Rule action.

**Type:** [FirewallRuleAction](arkts-network-netfirewall-firewallruleaction-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-action: FirewallRuleAction--><!--Device-NetFirewallRule-action: FirewallRuleAction-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## appUid

```TypeScript
appUid?: number
```

Application or service UID.

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-appUid?: number--><!--Device-NetFirewallRule-appUid?: number-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## description

```TypeScript
description?: string
```

Rule description.

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-description?: string--><!--Device-NetFirewallRule-description?: string-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## direction

```TypeScript
direction: NetFirewallRuleDirection
```

Rule direction, inbound or outbound.

**Type:** [NetFirewallRuleDirection](arkts-network-netfirewall-netfirewallruledirection-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-direction: NetFirewallRuleDirection--><!--Device-NetFirewallRule-direction: NetFirewallRuleDirection-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## dns

```TypeScript
dns?: NetFirewallDnsParams
```

DNS: valid when ruleType = RULE_DNS, otherwise it will be ignored.

**Type:** [NetFirewallDnsParams](arkts-network-netfirewall-netfirewalldnsparams-i.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-dns?: NetFirewallDnsParams--><!--Device-NetFirewallRule-dns?: NetFirewallDnsParams-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## domains

```TypeScript
domains?: Array<NetFirewallDomainParams>
```

Domain name list: valid when ruleType = RULE_DOMAIN, otherwise it will be ignored.

**Type:** Array&lt;[NetFirewallDomainParams](arkts-network-netfirewall-netfirewalldomainparams-i.md)&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-domains?: Array<NetFirewallDomainParams>--><!--Device-NetFirewallRule-domains?: Array<NetFirewallDomainParams>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## id

```TypeScript
id?: number
```

Rule id: When a rule is added to the system, the system generates a rule ID.

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-id?: number--><!--Device-NetFirewallRule-id?: number-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## interface

```TypeScript
interface?: string
```

Interface name: valid when type = RULE_IP, otherwise it will be ignored.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NetFirewallRule-interface?: string--><!--Device-NetFirewallRule-interface?: string-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## isEnabled

```TypeScript
isEnabled: boolean
```

Whether the rule is enabled.

**Type:** boolean

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-isEnabled: boolean--><!--Device-NetFirewallRule-isEnabled: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## localIps

```TypeScript
localIps?: Array<NetFirewallIpParams>
```

Local IP address: valid when ruleType = RULE_IP, otherwise it will be ignored.

**Type:** Array&lt;[NetFirewallIpParams](arkts-network-netfirewall-netfirewallipparams-i.md)&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-localIps?: Array<NetFirewallIpParams>--><!--Device-NetFirewallRule-localIps?: Array<NetFirewallIpParams>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## localPorts

```TypeScript
localPorts?: Array<NetFirewallPortParams>
```

Local ports: valid when ruleType = RULE_IP, otherwise it will be ignored.

**Type:** Array&lt;[NetFirewallPortParams](arkts-network-netfirewall-netfirewallportparams-i.md)&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-localPorts?: Array<NetFirewallPortParams>--><!--Device-NetFirewallRule-localPorts?: Array<NetFirewallPortParams>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## name

```TypeScript
name: string
```

Rule name.

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-name: string--><!--Device-NetFirewallRule-name: string-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## protocol

```TypeScript
protocol?: number
```

Protocol, 1: ICMPv4, 6: TCP, 17: UDP, 58: ICMPv6. Valid when ruleType = RULE_IP, otherwise it will be ignored.

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-protocol?: number--><!--Device-NetFirewallRule-protocol?: number-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## remoteIps

```TypeScript
remoteIps?: Array<NetFirewallIpParams>
```

Remote IP address: valid when ruleType = RULE_IP, otherwise it will be ignored.

**Type:** Array&lt;[NetFirewallIpParams](arkts-network-netfirewall-netfirewallipparams-i.md)&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-remoteIps?: Array<NetFirewallIpParams>--><!--Device-NetFirewallRule-remoteIps?: Array<NetFirewallIpParams>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## remotePorts

```TypeScript
remotePorts?: Array<NetFirewallPortParams>
```

Remote ports: valid when ruleType = RULE_IP, otherwise it will be ignored.

**Type:** Array&lt;[NetFirewallPortParams](arkts-network-netfirewall-netfirewallportparams-i.md)&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-remotePorts?: Array<NetFirewallPortParams>--><!--Device-NetFirewallRule-remotePorts?: Array<NetFirewallPortParams>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## type

```TypeScript
type: NetFirewallRuleType
```

Rule type.

**Type:** [NetFirewallRuleType](arkts-network-netfirewall-netfirewallruletype-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-type: NetFirewallRuleType--><!--Device-NetFirewallRule-type: NetFirewallRuleType-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## userId

```TypeScript
userId: number
```

User id.

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-NetFirewallRule-userId: number--><!--Device-NetFirewallRule-userId: number-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

