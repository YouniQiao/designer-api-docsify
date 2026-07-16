# QuotaPolicy (System API)

Policies that limit network quota.

**Since:** 10

<!--Device-policy-export interface QuotaPolicy--><!--Device-policy-export interface QuotaPolicy-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## lastLimitRemind

```TypeScript
lastLimitRemind?: number
```

The time of the last limit reminder. For notifying only, default: REMIND_NEVER.

**Type:** number

**Since:** 10

<!--Device-QuotaPolicy-lastLimitRemind?: number--><!--Device-QuotaPolicy-lastLimitRemind?: number-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## lastWarningRemind

```TypeScript
lastWarningRemind?: number
```

The time of the last warning reminder. For notifying only, default: REMIND_NEVER.

**Type:** number

**Since:** 10

<!--Device-QuotaPolicy-lastWarningRemind?: number--><!--Device-QuotaPolicy-lastWarningRemind?: number-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## limitAction

```TypeScript
limitAction: LimitAction
```

The action while the used bytes reach the limit, see {@link LimitAction}.

**Type:** LimitAction

**Since:** 10

<!--Device-QuotaPolicy-limitAction: LimitAction--><!--Device-QuotaPolicy-limitAction: LimitAction-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## limitBytes

```TypeScript
limitBytes: number
```

The limit threshold of traffic, default: DATA_USAGE_UNKNOWN.

**Type:** number

**Since:** 10

<!--Device-QuotaPolicy-limitBytes: number--><!--Device-QuotaPolicy-limitBytes: number-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## metered

```TypeScript
metered: boolean
```

Is metered network or not.

**Type:** boolean

**Since:** 10

<!--Device-QuotaPolicy-metered: boolean--><!--Device-QuotaPolicy-metered: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## periodDuration

```TypeScript
periodDuration: string
```

The period and the start time for quota policy, default: "M1" (Monthly cycle).

**Type:** string

**Since:** 10

<!--Device-QuotaPolicy-periodDuration: string--><!--Device-QuotaPolicy-periodDuration: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## warningBytes

```TypeScript
warningBytes: number
```

The warning threshold of traffic, default: DATA_USAGE_UNKNOWN.

**Type:** number

**Since:** 10

<!--Device-QuotaPolicy-warningBytes: number--><!--Device-QuotaPolicy-warningBytes: number-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

