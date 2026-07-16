# NetFirewallPolicy

Firewall policy.

**Since:** 15

<!--Device-netFirewall-interface NetFirewallPolicy--><!--Device-netFirewall-interface NetFirewallPolicy-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## Modules to Import

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
```

## inAction

```TypeScript
inAction: FirewallRuleAction
```

Inbound connections are allowed or denied by default.

**Type:** FirewallRuleAction

**Since:** 15

<!--Device-NetFirewallPolicy-inAction: FirewallRuleAction--><!--Device-NetFirewallPolicy-inAction: FirewallRuleAction-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## isOpen

```TypeScript
isOpen: boolean
```

Whether the firewall is open.

**Type:** boolean

**Since:** 15

<!--Device-NetFirewallPolicy-isOpen: boolean--><!--Device-NetFirewallPolicy-isOpen: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## outAction

```TypeScript
outAction: FirewallRuleAction
```

Outbound connections are allowed or denied by default.

**Type:** FirewallRuleAction

**Since:** 15

<!--Device-NetFirewallPolicy-outAction: FirewallRuleAction--><!--Device-NetFirewallPolicy-outAction: FirewallRuleAction-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

