# NetUidPolicyInfo (System API)

Callback function for registering network UID policy changes.

**Since:** 11

<!--Device-policy-export interface NetUidPolicyInfo--><!--Device-policy-export interface NetUidPolicyInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## policy

```TypeScript
policy: NetUidPolicy
```

Uid Specifies the Internet access policy in background mode.

**Type:** NetUidPolicy

**Since:** 11

<!--Device-NetUidPolicyInfo-policy: NetUidPolicy--><!--Device-NetUidPolicyInfo-policy: NetUidPolicy-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## uid

```TypeScript
uid: number
```

The warning threshold of traffic, default: DATA_USAGE_UNKNOWN.

**Type:** number

**Since:** 11

<!--Device-NetUidPolicyInfo-uid: number--><!--Device-NetUidPolicyInfo-uid: number-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

