# NetUidRuleInfo (System API)

The interface is used to generate network unique identifiers.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-policy-export interface NetUidRuleInfo--><!--Device-policy-export interface NetUidRuleInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { policy } from 'policy';
```

## rule

```TypeScript
rule: NetUidRule
```

Rules whether an uid can access to a metered or non-metered network.

**Type:** [NetUidRule](arkts-network-policy-netuidrule-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-NetUidRuleInfo-rule: NetUidRule--><!--Device-NetUidRuleInfo-rule: NetUidRule-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## uid

```TypeScript
uid: number
```

The warning threshold of traffic, default: DATA_USAGE_UNKNOWN.

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-NetUidRuleInfo-uid: number--><!--Device-NetUidRuleInfo-uid: number-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

