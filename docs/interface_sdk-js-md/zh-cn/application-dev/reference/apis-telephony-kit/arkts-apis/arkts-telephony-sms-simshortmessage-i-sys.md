# SimShortMessage（系统接口）

Defines a SIM message.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface SimShortMessage--><!--Device-sms-export interface SimShortMessage-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## indexOnSim

```TypeScript
indexOnSim: int
```

Indicates the index of SMS messages in the SIM.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimShortMessage-indexOnSim: int--><!--Device-SimShortMessage-indexOnSim: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## shortMessage

```TypeScript
shortMessage: ShortMessage
```

Indicates the SMS message in the SIM.

**类型：** [ShortMessage](arkts-telephony-sms-shortmessage-i.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimShortMessage-shortMessage: ShortMessage--><!--Device-SimShortMessage-shortMessage: ShortMessage-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## simMessageStatus

```TypeScript
simMessageStatus: SimMessageStatus
```

Indicates the storage status of SMS messages in the SIM.

**类型：** [SimMessageStatus](arkts-telephony-sms-simmessagestatus-e-sys.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimShortMessage-simMessageStatus: SimMessageStatus--><!--Device-SimShortMessage-simMessageStatus: SimMessageStatus-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

