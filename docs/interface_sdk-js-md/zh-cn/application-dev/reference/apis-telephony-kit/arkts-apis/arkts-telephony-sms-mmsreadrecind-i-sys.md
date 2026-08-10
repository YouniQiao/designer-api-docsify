# MmsReadRecInd（系统接口）

Defines the MMS message reading indication.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsReadRecInd--><!--Device-sms-export interface MmsReadRecInd-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## date

```TypeScript
date?: long
```

Indicates the date for the MMS message reading indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadRecInd-date?: long--><!--Device-MmsReadRecInd-date?: long-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## from

```TypeScript
from: MmsAddress
```

Indicates the source address for the MMS message reading indication.

**类型：** [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadRecInd-from: MmsAddress--><!--Device-MmsReadRecInd-from: MmsAddress-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## messageId

```TypeScript
messageId: string
```

Indicates the message ID for the MMS message reading indication.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadRecInd-messageId: string--><!--Device-MmsReadRecInd-messageId: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## readStatus

```TypeScript
readStatus: int
```

Indicates the read status for the MMS message reading indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadRecInd-readStatus: int--><!--Device-MmsReadRecInd-readStatus: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## to

```TypeScript
to: Array<MmsAddress>
```

Indicates the destination address for the MMS message reading indication.

**类型：** Array&lt;MmsAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadRecInd-to: Array<MmsAddress>--><!--Device-MmsReadRecInd-to: Array<MmsAddress>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the MMS message reading indication.

**类型：** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadRecInd-version: MmsVersionType--><!--Device-MmsReadRecInd-version: MmsVersionType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

