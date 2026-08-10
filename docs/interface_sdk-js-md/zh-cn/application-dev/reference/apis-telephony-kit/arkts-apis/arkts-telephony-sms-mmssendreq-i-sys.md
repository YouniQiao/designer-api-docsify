# MmsSendReq（系统接口）

Defines an MMS message sending request.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsSendReq--><!--Device-sms-export interface MmsSendReq-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## bcc

```TypeScript
bcc?: Array<MmsAddress>
```

Indicates the blind carbon copy address for the MMS message sending request.

**类型：** Array&lt;MmsAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-bcc?: Array<MmsAddress>--><!--Device-MmsSendReq-bcc?: Array<MmsAddress>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## cc

```TypeScript
cc?: Array<MmsAddress>
```

Indicates the carbon copy address for the MMS message sending request.

**类型：** Array&lt;MmsAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-cc?: Array<MmsAddress>--><!--Device-MmsSendReq-cc?: Array<MmsAddress>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## contentType

```TypeScript
contentType: string
```

Indicates the content type for the MMS message sending request.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-contentType: string--><!--Device-MmsSendReq-contentType: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## date

```TypeScript
date?: long
```

Indicates the date for the MMS message sending request.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-date?: long--><!--Device-MmsSendReq-date?: long-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## deliveryReport

```TypeScript
deliveryReport?: int
```

Indicates the delivery report for the MMS message sending request.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-deliveryReport?: int--><!--Device-MmsSendReq-deliveryReport?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## expiry

```TypeScript
expiry?: int
```

Indicates the expiration for the MMS message sending request.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-expiry?: int--><!--Device-MmsSendReq-expiry?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## from

```TypeScript
from: MmsAddress
```

Indicates the source address for the MMS message sending request.

**类型：** [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-from: MmsAddress--><!--Device-MmsSendReq-from: MmsAddress-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## messageClass

```TypeScript
messageClass?: int
```

Indicates the message class for the MMS message sending request.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-messageClass?: int--><!--Device-MmsSendReq-messageClass?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## priority

```TypeScript
priority?: MmsPriorityType
```

Indicates the priority for the MMS message sending request.

**类型：** [MmsPriorityType](arkts-telephony-sms-mmsprioritytype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-priority?: MmsPriorityType--><!--Device-MmsSendReq-priority?: MmsPriorityType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## readReport

```TypeScript
readReport?: int
```

Indicates the read report for the MMS message sending request.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-readReport?: int--><!--Device-MmsSendReq-readReport?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## senderVisibility

```TypeScript
senderVisibility?: int
```

Indicates the sender visibility for the MMS message sending request.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-senderVisibility?: int--><!--Device-MmsSendReq-senderVisibility?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## subject

```TypeScript
subject?: string
```

Indicates the subject for the MMS message sending request.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-subject?: string--><!--Device-MmsSendReq-subject?: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## to

```TypeScript
to?: Array<MmsAddress>
```

Indicates the destination address for the MMS message sending request.

**类型：** Array&lt;MmsAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-to?: Array<MmsAddress>--><!--Device-MmsSendReq-to?: Array<MmsAddress>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## transactionId

```TypeScript
transactionId: string
```

Indicates the transaction ID for the MMS message sending request.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-transactionId: string--><!--Device-MmsSendReq-transactionId: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the MMS message sending request.

**类型：** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsSendReq-version: MmsVersionType--><!--Device-MmsSendReq-version: MmsVersionType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

