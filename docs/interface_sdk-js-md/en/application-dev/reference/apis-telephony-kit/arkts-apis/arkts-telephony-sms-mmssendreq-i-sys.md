# MmsSendReq (System API)

Defines an MMS message sending request.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sms-export interface MmsSendReq--><!--Device-sms-export interface MmsSendReq-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## bcc

```TypeScript
bcc?: Array<MmsAddress>
```

Blind carbon copy.

**Type:** Array&lt;[MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-bcc?: Array<MmsAddress>--><!--Device-MmsSendReq-bcc?: Array<MmsAddress>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## cc

```TypeScript
cc?: Array<MmsAddress>
```

Carbon copy.

**Type:** Array&lt;[MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-cc?: Array<MmsAddress>--><!--Device-MmsSendReq-cc?: Array<MmsAddress>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## contentType

```TypeScript
contentType: string
```

Content type.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-contentType: string--><!--Device-MmsSendReq-contentType: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## date

```TypeScript
date?: long
```

Date.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-date?: long--><!--Device-MmsSendReq-date?: long-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## deliveryReport

```TypeScript
deliveryReport?: int
```

Delivery report.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-deliveryReport?: int--><!--Device-MmsSendReq-deliveryReport?: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## expiry

```TypeScript
expiry?: int
```

Expiration.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-expiry?: int--><!--Device-MmsSendReq-expiry?: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## from

```TypeScript
from: MmsAddress
```

MMS message source.

**Type:** [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-from: MmsAddress--><!--Device-MmsSendReq-from: MmsAddress-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## messageClass

```TypeScript
messageClass?: int
```

Message class.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-messageClass?: int--><!--Device-MmsSendReq-messageClass?: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## priority

```TypeScript
priority?: MmsPriorityType
```

Priority.

**Type:** [MmsPriorityType](arkts-telephony-sms-mmsprioritytype-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-priority?: MmsPriorityType--><!--Device-MmsSendReq-priority?: MmsPriorityType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## readReport

```TypeScript
readReport?: int
```

Read report.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-readReport?: int--><!--Device-MmsSendReq-readReport?: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## senderVisibility

```TypeScript
senderVisibility?: int
```

Sender visibility.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-senderVisibility?: int--><!--Device-MmsSendReq-senderVisibility?: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## subject

```TypeScript
subject?: string
```

Subject.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-subject?: string--><!--Device-MmsSendReq-subject?: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## to

```TypeScript
to?: Array<MmsAddress>
```

Destination address.

**Type:** Array&lt;[MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-to?: Array<MmsAddress>--><!--Device-MmsSendReq-to?: Array<MmsAddress>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## transactionId

```TypeScript
transactionId: string
```

Transaction ID.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-transactionId: string--><!--Device-MmsSendReq-transactionId: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## version

```TypeScript
version: MmsVersionType
```

Version.

**Type:** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MmsSendReq-version: MmsVersionType--><!--Device-MmsSendReq-version: MmsVersionType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

