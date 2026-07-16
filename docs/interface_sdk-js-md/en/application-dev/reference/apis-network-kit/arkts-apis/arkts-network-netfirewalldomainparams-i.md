# NetFirewallDomainParams

Firewall domain name parameters.

**Since:** 15

<!--Device-netFirewall-interface NetFirewallDomainParams--><!--Device-netFirewall-interface NetFirewallDomainParams-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## Modules to Import

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
```

## domain

```TypeScript
domain: string
```

Domain: when isWildcard is false, the complete domain that needs to be determined;When isWildcard is true, fuzzy domain only support domains like *.openharmony.cn; *.com.

**Type:** string

**Since:** 15

<!--Device-NetFirewallDomainParams-domain: string--><!--Device-NetFirewallDomainParams-domain: string-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## isWildcard

```TypeScript
isWildcard: boolean
```

Is there a universal configuration rule.

**Type:** boolean

**Since:** 15

<!--Device-NetFirewallDomainParams-isWildcard: boolean--><!--Device-NetFirewallDomainParams-isWildcard: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

