# ISendShortMessageCallback

Provides the callback for the SMS message sending result.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface ISendShortMessageCallback--><!--Device-sms-export interface ISendShortMessageCallback-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## isLastPart

```TypeScript
isLastPart: boolean
```

Specifies whether this is the last part of a multi-part SMS message.

**类型：** boolean

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ISendShortMessageCallback-isLastPart: boolean--><!--Device-ISendShortMessageCallback-isLastPart: boolean-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## result

```TypeScript
result: SendSmsResult
```

Indicates the SMS message sending result.

**类型：** [SendSmsResult](arkts-telephony-sms-sendsmsresult-e.md)

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ISendShortMessageCallback-result: SendSmsResult--><!--Device-ISendShortMessageCallback-result: SendSmsResult-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## url

```TypeScript
url: string
```

Indicates the URI to store the sent SMS message.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-ISendShortMessageCallback-url: string--><!--Device-ISendShortMessageCallback-url: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

