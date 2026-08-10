# MmsNotificationInd（系统接口）

Defines an MMS notification indication.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsNotificationInd--><!--Device-sms-export interface MmsNotificationInd-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## contentClass

```TypeScript
contentClass?: int
```

Indicates the content class for the MMS notification indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-contentClass?: int--><!--Device-MmsNotificationInd-contentClass?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## contentLocation

```TypeScript
contentLocation: string
```

Indicates the content location for the MMS notification indication.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-contentLocation: string--><!--Device-MmsNotificationInd-contentLocation: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## deliveryReport

```TypeScript
deliveryReport?: int
```

Indicates the status report for the MMS notification indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-deliveryReport?: int--><!--Device-MmsNotificationInd-deliveryReport?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## expiry

```TypeScript
expiry: int
```

Indicates the expiration for the MMS notification indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-expiry: int--><!--Device-MmsNotificationInd-expiry: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## from

```TypeScript
from?: MmsAddress
```

Indicates the source address for the MMS notification indication.

**类型：** [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-from?: MmsAddress--><!--Device-MmsNotificationInd-from?: MmsAddress-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## messageClass

```TypeScript
messageClass: int
```

Indicates the message class for the MMS notification indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-messageClass: int--><!--Device-MmsNotificationInd-messageClass: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## messageSize

```TypeScript
messageSize: long
```

Indicates the message size for the MMS notification indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-messageSize: long--><!--Device-MmsNotificationInd-messageSize: long-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## subject

```TypeScript
subject?: string
```

Indicates the subject for the MMS notification indication.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-subject?: string--><!--Device-MmsNotificationInd-subject?: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## transactionId

```TypeScript
transactionId: string
```

Indicates the transaction ID for the MMS notification indication.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-transactionId: string--><!--Device-MmsNotificationInd-transactionId: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the MMS notification indication.

**类型：** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsNotificationInd-version: MmsVersionType--><!--Device-MmsNotificationInd-version: MmsVersionType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

