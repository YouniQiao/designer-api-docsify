# MmsRetrieveConf (System API)

Defines the MMS message retrieval configuration.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sms-export interface MmsRetrieveConf--><!--Device-sms-export interface MmsRetrieveConf-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## cc

```TypeScript
cc?: Array<MmsAddress>
```

Indicates the carbon copy address for the MMS message retrieval configuration.

**Type:** Array&lt;[MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-cc?: Array<MmsAddress>--><!--Device-MmsRetrieveConf-cc?: Array<MmsAddress>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## contentType

```TypeScript
contentType: string
```

Indicates the content type for the MMS message retrieval configuration.

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-contentType: string--><!--Device-MmsRetrieveConf-contentType: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## date

```TypeScript
date: long
```

Indicates the date for the MMS message retrieval configuration.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-date: long--><!--Device-MmsRetrieveConf-date: long-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## deliveryReport

```TypeScript
deliveryReport?: int
```

Indicates the status report for the MMS message retrieval configuration.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-deliveryReport?: int--><!--Device-MmsRetrieveConf-deliveryReport?: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## from

```TypeScript
from?: MmsAddress
```

Indicates the source address for the MMS message retrieval configuration.

**Type:** [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-from?: MmsAddress--><!--Device-MmsRetrieveConf-from?: MmsAddress-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## messageId

```TypeScript
messageId: string
```

Indicates the message ID for the MMS message retrieval configuration.

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-messageId: string--><!--Device-MmsRetrieveConf-messageId: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## priority

```TypeScript
priority?: MmsPriorityType
```

Indicates the priority for the MMS message retrieval configuration.

**Type:** [MmsPriorityType](arkts-telephony-sms-mmsprioritytype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-priority?: MmsPriorityType--><!--Device-MmsRetrieveConf-priority?: MmsPriorityType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## readReport

```TypeScript
readReport?: int
```

Indicates the read report for the MMS message retrieval configuration.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-readReport?: int--><!--Device-MmsRetrieveConf-readReport?: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## retrieveStatus

```TypeScript
retrieveStatus?: int
```

Indicates the retrieval status for the MMS message retrieval configuration.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-retrieveStatus?: int--><!--Device-MmsRetrieveConf-retrieveStatus?: int-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## retrieveText

```TypeScript
retrieveText?: string
```

Indicates the retrieval text for the MMS message retrieval configuration.

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-retrieveText?: string--><!--Device-MmsRetrieveConf-retrieveText?: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## subject

```TypeScript
subject?: string
```

Indicates the subject for the MMS message retrieval configuration.

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-subject?: string--><!--Device-MmsRetrieveConf-subject?: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## to

```TypeScript
to: Array<MmsAddress>
```

Indicates the destination address for the MMS message retrieval configuration.

**Type:** Array&lt;[MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-to: Array<MmsAddress>--><!--Device-MmsRetrieveConf-to: Array<MmsAddress>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## transactionId

```TypeScript
transactionId: string
```

Indicates the transaction ID for the MMS message retrieval configuration.

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-transactionId: string--><!--Device-MmsRetrieveConf-transactionId: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the MMS message retrieval configuration.

**Type:** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MmsRetrieveConf-version: MmsVersionType--><!--Device-MmsRetrieveConf-version: MmsVersionType-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

