# NetUidPolicyInfo（系统接口）

Callback function for registering network UID policy changes.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-policy-export interface NetUidPolicyInfo--><!--Device-policy-export interface NetUidPolicyInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## policy

```TypeScript
policy: NetUidPolicy
```

Uid Specifies the Internet access policy in background mode.

**类型：** [NetUidPolicy](arkts-network-policy-netuidpolicy-e-sys.md)

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-NetUidPolicyInfo-policy: NetUidPolicy--><!--Device-NetUidPolicyInfo-policy: NetUidPolicy-End-->

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

<!--Device-NetUidPolicyInfo-uid: number--><!--Device-NetUidPolicyInfo-uid: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

