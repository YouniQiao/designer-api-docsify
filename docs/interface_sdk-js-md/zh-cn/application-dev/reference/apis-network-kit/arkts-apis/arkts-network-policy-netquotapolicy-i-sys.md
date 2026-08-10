# NetQuotaPolicy（系统接口）

Net quota policies, including matching network rule usage periods, restrictions, and warnings.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-policy-export interface NetQuotaPolicy--><!--Device-policy-export interface NetQuotaPolicy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## networkMatchRule

```TypeScript
networkMatchRule: NetworkMatchRule
```

The matching rules of network quota policies.

**类型：** [NetworkMatchRule](arkts-network-policy-networkmatchrule-i-sys.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetQuotaPolicy-networkMatchRule: NetworkMatchRule--><!--Device-NetQuotaPolicy-networkMatchRule: NetworkMatchRule-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## quotaPolicy

```TypeScript
quotaPolicy: QuotaPolicy
```

Policies that limit network quota.

**类型：** [QuotaPolicy](arkts-network-policy-quotapolicy-i-sys.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetQuotaPolicy-quotaPolicy: QuotaPolicy--><!--Device-NetQuotaPolicy-quotaPolicy: QuotaPolicy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

