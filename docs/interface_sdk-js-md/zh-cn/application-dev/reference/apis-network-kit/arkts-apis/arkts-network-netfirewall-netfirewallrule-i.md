# NetFirewallRule

Firewall rules.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-netFirewall-interface NetFirewallRule--><!--Device-netFirewall-interface NetFirewallRule-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## action

```TypeScript
action: FirewallRuleAction
```

Rule action.

**类型：** [FirewallRuleAction](arkts-network-netfirewall-firewallruleaction-e.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-action: FirewallRuleAction--><!--Device-NetFirewallRule-action: FirewallRuleAction-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## appUid

```TypeScript
appUid?: number
```

Application or service UID.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-appUid?: number--><!--Device-NetFirewallRule-appUid?: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## description

```TypeScript
description?: string
```

Rule description.

**类型：** string

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-description?: string--><!--Device-NetFirewallRule-description?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## direction

```TypeScript
direction: NetFirewallRuleDirection
```

Rule direction, inbound or outbound.

**类型：** [NetFirewallRuleDirection](arkts-network-netfirewall-netfirewallruledirection-e.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-direction: NetFirewallRuleDirection--><!--Device-NetFirewallRule-direction: NetFirewallRuleDirection-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## dns

```TypeScript
dns?: NetFirewallDnsParams
```

DNS: valid when ruleType = RULE_DNS, otherwise it will be ignored.

**类型：** [NetFirewallDnsParams](arkts-network-netfirewall-netfirewalldnsparams-i.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-dns?: NetFirewallDnsParams--><!--Device-NetFirewallRule-dns?: NetFirewallDnsParams-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## domains

```TypeScript
domains?: Array<NetFirewallDomainParams>
```

Domain name list: valid when ruleType = RULE_DOMAIN, otherwise it will be ignored.

**类型：** Array&lt;NetFirewallDomainParams&gt;

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-domains?: Array<NetFirewallDomainParams>--><!--Device-NetFirewallRule-domains?: Array<NetFirewallDomainParams>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## id

```TypeScript
id?: number
```

Rule id: When a rule is added to the system, the system generates a rule ID.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-id?: number--><!--Device-NetFirewallRule-id?: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## interface

```TypeScript
interface?: string
```

Interface name: valid when type = RULE_IP, otherwise it will be ignored.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NetFirewallRule-interface?: string--><!--Device-NetFirewallRule-interface?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## isEnabled

```TypeScript
isEnabled: boolean
```

Whether the rule is enabled.

**类型：** boolean

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-isEnabled: boolean--><!--Device-NetFirewallRule-isEnabled: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## localIps

```TypeScript
localIps?: Array<NetFirewallIpParams>
```

Local IP address: valid when ruleType = RULE_IP, otherwise it will be ignored.

**类型：** Array&lt;NetFirewallIpParams&gt;

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-localIps?: Array<NetFirewallIpParams>--><!--Device-NetFirewallRule-localIps?: Array<NetFirewallIpParams>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## localPorts

```TypeScript
localPorts?: Array<NetFirewallPortParams>
```

Local ports: valid when ruleType = RULE_IP, otherwise it will be ignored.

**类型：** Array&lt;NetFirewallPortParams&gt;

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-localPorts?: Array<NetFirewallPortParams>--><!--Device-NetFirewallRule-localPorts?: Array<NetFirewallPortParams>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## name

```TypeScript
name: string
```

Rule name.

**类型：** string

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-name: string--><!--Device-NetFirewallRule-name: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## protocol

```TypeScript
protocol?: number
```

Protocol, 1: ICMPv4, 6: TCP, 17: UDP, 58: ICMPv6. Valid when ruleType = RULE_IP, otherwise it will be ignored.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-protocol?: number--><!--Device-NetFirewallRule-protocol?: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## remoteIps

```TypeScript
remoteIps?: Array<NetFirewallIpParams>
```

Remote IP address: valid when ruleType = RULE_IP, otherwise it will be ignored.

**类型：** Array&lt;NetFirewallIpParams&gt;

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-remoteIps?: Array<NetFirewallIpParams>--><!--Device-NetFirewallRule-remoteIps?: Array<NetFirewallIpParams>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## remotePorts

```TypeScript
remotePorts?: Array<NetFirewallPortParams>
```

Remote ports: valid when ruleType = RULE_IP, otherwise it will be ignored.

**类型：** Array&lt;NetFirewallPortParams&gt;

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-remotePorts?: Array<NetFirewallPortParams>--><!--Device-NetFirewallRule-remotePorts?: Array<NetFirewallPortParams>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## type

```TypeScript
type: NetFirewallRuleType
```

Rule type.

**类型：** [NetFirewallRuleType](arkts-network-netfirewall-netfirewallruletype-e.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-type: NetFirewallRuleType--><!--Device-NetFirewallRule-type: NetFirewallRuleType-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## userId

```TypeScript
userId: number
```

User id.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallRule-userId: number--><!--Device-NetFirewallRule-userId: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

