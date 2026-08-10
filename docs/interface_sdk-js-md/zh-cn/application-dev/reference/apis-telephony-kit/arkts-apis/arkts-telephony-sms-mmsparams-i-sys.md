# MmsParams（系统接口）

Defines the MMS message param.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsParams--><!--Device-sms-export interface MmsParams-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## data

```TypeScript
data: string
```

Indicates the MMS pdu url used for sending the MMS message.

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-MmsParams-data: string--><!--Device-MmsParams-data: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## mmsConfig

```TypeScript
mmsConfig?: MmsConfig
```

Indicates the MMS UA and MMS UaProf used for sending the MMS message.

**类型：** [MmsConfig](arkts-telephony-sms-mmsconfig-i-sys.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-MmsParams-mmsConfig?: MmsConfig--><!--Device-MmsParams-mmsConfig?: MmsConfig-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## mmsc

```TypeScript
mmsc: string
```

Indicates the MMSC used for sending the MMS message.

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-MmsParams-mmsc: string--><!--Device-MmsParams-mmsc: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## slotId

```TypeScript
slotId: int
```

Indicates the ID of the SIM card slot used for sending the MMS message.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-MmsParams-slotId: int--><!--Device-MmsParams-slotId: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

