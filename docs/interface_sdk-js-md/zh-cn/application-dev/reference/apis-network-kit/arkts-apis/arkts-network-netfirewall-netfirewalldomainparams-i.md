# NetFirewallDomainParams

Firewall domain name parameters.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-netFirewall-interface NetFirewallDomainParams--><!--Device-netFirewall-interface NetFirewallDomainParams-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## domain

```TypeScript
domain: string
```

Domain: when isWildcard is false, the complete domain that needs to be determined;When isWildcard is true, fuzzy domain only support domains like *.openharmony.cn; *.com.

**类型：** string

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallDomainParams-domain: string--><!--Device-NetFirewallDomainParams-domain: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## isWildcard

```TypeScript
isWildcard: boolean
```

Is there a universal configuration rule.

**类型：** boolean

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallDomainParams-isWildcard: boolean--><!--Device-NetFirewallDomainParams-isWildcard: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

