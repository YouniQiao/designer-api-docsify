# MmsRetrieveConf（系统接口）

Defines the MMS message retrieval configuration.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsRetrieveConf--><!--Device-sms-export interface MmsRetrieveConf-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## cc

```TypeScript
cc?: Array<MmsAddress>
```

Indicates the carbon copy address for the MMS message retrieval configuration.

**类型：** Array&lt;MmsAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-cc?: Array<MmsAddress>--><!--Device-MmsRetrieveConf-cc?: Array<MmsAddress>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## contentType

```TypeScript
contentType: string
```

Indicates the content type for the MMS message retrieval configuration.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-contentType: string--><!--Device-MmsRetrieveConf-contentType: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## date

```TypeScript
date: long
```

Indicates the date for the MMS message retrieval configuration.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-date: long--><!--Device-MmsRetrieveConf-date: long-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## deliveryReport

```TypeScript
deliveryReport?: int
```

Indicates the status report for the MMS message retrieval configuration.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-deliveryReport?: int--><!--Device-MmsRetrieveConf-deliveryReport?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## from

```TypeScript
from?: MmsAddress
```

Indicates the source address for the MMS message retrieval configuration.

**类型：** [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-from?: MmsAddress--><!--Device-MmsRetrieveConf-from?: MmsAddress-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## messageId

```TypeScript
messageId: string
```

Indicates the message ID for the MMS message retrieval configuration.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-messageId: string--><!--Device-MmsRetrieveConf-messageId: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## priority

```TypeScript
priority?: MmsPriorityType
```

Indicates the priority for the MMS message retrieval configuration.

**类型：** [MmsPriorityType](arkts-telephony-sms-mmsprioritytype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-priority?: MmsPriorityType--><!--Device-MmsRetrieveConf-priority?: MmsPriorityType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## readReport

```TypeScript
readReport?: int
```

Indicates the read report for the MMS message retrieval configuration.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-readReport?: int--><!--Device-MmsRetrieveConf-readReport?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## retrieveStatus

```TypeScript
retrieveStatus?: int
```

Indicates the retrieval status for the MMS message retrieval configuration.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-retrieveStatus?: int--><!--Device-MmsRetrieveConf-retrieveStatus?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## retrieveText

```TypeScript
retrieveText?: string
```

Indicates the retrieval text for the MMS message retrieval configuration.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-retrieveText?: string--><!--Device-MmsRetrieveConf-retrieveText?: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## subject

```TypeScript
subject?: string
```

Indicates the subject for the MMS message retrieval configuration.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-subject?: string--><!--Device-MmsRetrieveConf-subject?: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## to

```TypeScript
to: Array<MmsAddress>
```

Indicates the destination address for the MMS message retrieval configuration.

**类型：** Array&lt;MmsAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-to: Array<MmsAddress>--><!--Device-MmsRetrieveConf-to: Array<MmsAddress>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## transactionId

```TypeScript
transactionId: string
```

Indicates the transaction ID for the MMS message retrieval configuration.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-transactionId: string--><!--Device-MmsRetrieveConf-transactionId: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the MMS message retrieval configuration.

**类型：** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsRetrieveConf-version: MmsVersionType--><!--Device-MmsRetrieveConf-version: MmsVersionType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

