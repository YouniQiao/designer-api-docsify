# UpdateSimMessageOptions (System API)

Defines the updating SIM message options.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-sms-export interface UpdateSimMessageOptions--><!--Device-sms-export interface UpdateSimMessageOptions-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## msgIndex

```TypeScript
msgIndex: int
```

Message index.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-UpdateSimMessageOptions-msgIndex: int--><!--Device-UpdateSimMessageOptions-msgIndex: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## newStatus

```TypeScript
newStatus: SimMessageStatus
```

New status.

**Type:** [SimMessageStatus](arkts-telephony-sms-simmessagestatus-e-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-UpdateSimMessageOptions-newStatus: SimMessageStatus--><!--Device-UpdateSimMessageOptions-newStatus: SimMessageStatus-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## pdu

```TypeScript
pdu: string
```

Protocol data unit.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-UpdateSimMessageOptions-pdu: string--><!--Device-UpdateSimMessageOptions-pdu: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## slotId

```TypeScript
slotId: int
```

Card slot ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-UpdateSimMessageOptions-slotId: int--><!--Device-UpdateSimMessageOptions-slotId: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## smsc

```TypeScript
smsc: string
```

Short message service center.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-UpdateSimMessageOptions-smsc: string--><!--Device-UpdateSimMessageOptions-smsc: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

