# DisconnectedDetails (System API)

Indicates the cause of a call disconnection.

**Since:** 9

<!--Device-call-export interface DisconnectedDetails--><!--Device-call-export interface DisconnectedDetails-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## message

```TypeScript
message: string
```

Indicates the message for ending the call.

**Type:** string

**Since:** 9

<!--Device-DisconnectedDetails-message: string--><!--Device-DisconnectedDetails-message: string-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

## reason

```TypeScript
reason: DisconnectedReason
```

Indicates the reason for ending the call.

**Type:** DisconnectedReason

**Since:** 9

<!--Device-DisconnectedDetails-reason: DisconnectedReason--><!--Device-DisconnectedDetails-reason: DisconnectedReason-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

