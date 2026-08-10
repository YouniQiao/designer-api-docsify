# MmsReadOrigInd（系统接口）

Defines the original MMS message reading indication.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsReadOrigInd--><!--Device-sms-export interface MmsReadOrigInd-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## date

```TypeScript
date: long
```

Indicates the date for the original MMS message reading indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadOrigInd-date: long--><!--Device-MmsReadOrigInd-date: long-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## from

```TypeScript
from: MmsAddress
```

Indicates the source address for the original MMS message reading indication.

**类型：** [MmsAddress](arkts-telephony-sms-mmsaddress-i-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadOrigInd-from: MmsAddress--><!--Device-MmsReadOrigInd-from: MmsAddress-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## messageId

```TypeScript
messageId: string
```

Indicates the message ID for the original MMS message reading indication.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadOrigInd-messageId: string--><!--Device-MmsReadOrigInd-messageId: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## readStatus

```TypeScript
readStatus: int
```

Indicates the read status for the original MMS message reading indication.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadOrigInd-readStatus: int--><!--Device-MmsReadOrigInd-readStatus: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## to

```TypeScript
to: Array<MmsAddress>
```

Indicates the destination address for the original MMS message reading indication.

**类型：** Array&lt;MmsAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadOrigInd-to: Array<MmsAddress>--><!--Device-MmsReadOrigInd-to: Array<MmsAddress>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## version

```TypeScript
version: MmsVersionType
```

Indicates the version for the original MMS message reading indication.

**类型：** [MmsVersionType](arkts-telephony-sms-mmsversiontype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsReadOrigInd-version: MmsVersionType--><!--Device-MmsReadOrigInd-version: MmsVersionType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

