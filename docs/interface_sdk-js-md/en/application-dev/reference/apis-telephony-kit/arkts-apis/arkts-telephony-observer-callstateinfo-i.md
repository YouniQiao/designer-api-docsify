# CallStateInfo

Indicates call state and number.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-observer-export interface CallStateInfo--><!--Device-observer-export interface CallStateInfo-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## number

```TypeScript
number: string
```

Indicates call number.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-CallStateInfo-number: string--><!--Device-CallStateInfo-number: string-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## state

```TypeScript
state: CallState
```

Indicates call state.

**Type:** [CallState](arkts-telephony-call-callstate-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CallStateInfo-state: CallState--><!--Device-CallStateInfo-state: CallState-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

## teleNumber

```TypeScript
teleNumber: string
```

Indicates call number.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CallStateInfo-teleNumber: string--><!--Device-CallStateInfo-teleNumber: string-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

