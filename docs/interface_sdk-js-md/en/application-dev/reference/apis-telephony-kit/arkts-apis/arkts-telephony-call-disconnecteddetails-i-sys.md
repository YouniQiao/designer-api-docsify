# DisconnectedDetails (System API)

Indicates the cause of a call disconnection.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-call-export interface DisconnectedDetails--><!--Device-call-export interface DisconnectedDetails-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## message

```TypeScript
message: string
```

Indicates the message for ending the call.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DisconnectedDetails-message: string--><!--Device-DisconnectedDetails-message: string-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## reason

```TypeScript
reason: DisconnectedReason
```

Indicates the reason for ending the call.

**Type:** [DisconnectedReason](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-wifimanager-disconnectedreason-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DisconnectedDetails-reason: DisconnectedReason--><!--Device-DisconnectedDetails-reason: DisconnectedReason-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

