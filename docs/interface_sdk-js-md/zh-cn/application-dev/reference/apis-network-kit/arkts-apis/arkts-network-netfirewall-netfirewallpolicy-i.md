# NetFirewallPolicy

Firewall policy.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-netFirewall-interface NetFirewallPolicy--><!--Device-netFirewall-interface NetFirewallPolicy-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## inAction

```TypeScript
inAction: FirewallRuleAction
```

Inbound connections are allowed or denied by default.

**类型：** [FirewallRuleAction](arkts-network-netfirewall-firewallruleaction-e.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallPolicy-inAction: FirewallRuleAction--><!--Device-NetFirewallPolicy-inAction: FirewallRuleAction-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## isOpen

```TypeScript
isOpen: boolean
```

Whether the firewall is open.

**类型：** boolean

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallPolicy-isOpen: boolean--><!--Device-NetFirewallPolicy-isOpen: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## outAction

```TypeScript
outAction: FirewallRuleAction
```

Outbound connections are allowed or denied by default.

**类型：** [FirewallRuleAction](arkts-network-netfirewall-firewallruleaction-e.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallPolicy-outAction: FirewallRuleAction--><!--Device-NetFirewallPolicy-outAction: FirewallRuleAction-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

