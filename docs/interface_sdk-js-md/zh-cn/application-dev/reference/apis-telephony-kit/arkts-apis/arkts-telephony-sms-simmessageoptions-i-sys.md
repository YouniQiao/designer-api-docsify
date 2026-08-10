# SimMessageOptions（系统接口）

Defines the SIM message options.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface SimMessageOptions--><!--Device-sms-export interface SimMessageOptions-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## pdu

```TypeScript
pdu: string
```

Indicates the protocol data unit for the SIM message options.

**类型：** string

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimMessageOptions-pdu: string--><!--Device-SimMessageOptions-pdu: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## slotId

```TypeScript
slotId: int
```

Indicates the card slot ID for the SIM message options.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimMessageOptions-slotId: int--><!--Device-SimMessageOptions-slotId: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## smsc

```TypeScript
smsc: string
```

Indicates the short message service center for the SIM message options.

**类型：** string

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimMessageOptions-smsc: string--><!--Device-SimMessageOptions-smsc: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## status

```TypeScript
status: SimMessageStatus
```

Indicates the status for the SIM message options.

**类型：** [SimMessageStatus](arkts-telephony-sms-simmessagestatus-e-sys.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimMessageOptions-status: SimMessageStatus--><!--Device-SimMessageOptions-status: SimMessageStatus-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

