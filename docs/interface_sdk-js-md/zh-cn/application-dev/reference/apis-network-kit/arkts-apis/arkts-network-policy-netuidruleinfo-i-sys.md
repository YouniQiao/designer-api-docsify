# NetUidRuleInfo（系统接口）

The interface is used to generate network unique identifiers.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-policy-export interface NetUidRuleInfo--><!--Device-policy-export interface NetUidRuleInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## rule

```TypeScript
rule: NetUidRule
```

Rules whether an uid can access to a metered or non-metered network.

**类型：** [NetUidRule](arkts-network-policy-netuidrule-e-sys.md)

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-NetUidRuleInfo-rule: NetUidRule--><!--Device-NetUidRuleInfo-rule: NetUidRule-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## uid

```TypeScript
uid: number
```

The warning threshold of traffic, default: DATA_USAGE_UNKNOWN.

**类型：** number

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-NetUidRuleInfo-uid: number--><!--Device-NetUidRuleInfo-uid: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

