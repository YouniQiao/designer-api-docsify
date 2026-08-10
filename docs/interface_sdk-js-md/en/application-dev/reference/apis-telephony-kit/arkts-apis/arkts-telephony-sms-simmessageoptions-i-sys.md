# SimMessageOptions (System API)

Defines the SIM message options.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-sms-export interface SimMessageOptions--><!--Device-sms-export interface SimMessageOptions-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## pdu

```TypeScript
pdu: string
```

Indicates the protocol data unit for the SIM message options.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SimMessageOptions-pdu: string--><!--Device-SimMessageOptions-pdu: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## slotId

```TypeScript
slotId: int
```

Indicates the card slot ID for the SIM message options.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SimMessageOptions-slotId: int--><!--Device-SimMessageOptions-slotId: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## smsc

```TypeScript
smsc: string
```

Indicates the short message service center for the SIM message options.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SimMessageOptions-smsc: string--><!--Device-SimMessageOptions-smsc: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## status

```TypeScript
status: SimMessageStatus
```

Indicates the status for the SIM message options.

**Type:** [SimMessageStatus](arkts-telephony-sms-simmessagestatus-e-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SimMessageOptions-status: SimMessageStatus--><!--Device-SimMessageOptions-status: SimMessageStatus-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

