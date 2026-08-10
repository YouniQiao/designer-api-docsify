# UpdateSimMessageOptions（系统接口）

Defines the updating SIM message options.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface UpdateSimMessageOptions--><!--Device-sms-export interface UpdateSimMessageOptions-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## msgIndex

```TypeScript
msgIndex: int
```

Indicates the message index for the updating SIM message options.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-UpdateSimMessageOptions-msgIndex: int--><!--Device-UpdateSimMessageOptions-msgIndex: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## newStatus

```TypeScript
newStatus: SimMessageStatus
```

Indicates the new status for the updating SIM message options.

**类型：** [SimMessageStatus](arkts-telephony-sms-simmessagestatus-e-sys.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-UpdateSimMessageOptions-newStatus: SimMessageStatus--><!--Device-UpdateSimMessageOptions-newStatus: SimMessageStatus-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## pdu

```TypeScript
pdu: string
```

Indicates the protocol data unit for the updating SIM message options.

**类型：** string

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-UpdateSimMessageOptions-pdu: string--><!--Device-UpdateSimMessageOptions-pdu: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## slotId

```TypeScript
slotId: int
```

Indicates the card slot ID for the updating SIM message options.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-UpdateSimMessageOptions-slotId: int--><!--Device-UpdateSimMessageOptions-slotId: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## smsc

```TypeScript
smsc: string
```

Indicates the short message service center for the updating SIM message options.

**类型：** string

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-UpdateSimMessageOptions-smsc: string--><!--Device-UpdateSimMessageOptions-smsc: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

