# ISendShortMessageCallback

Provides the callback for the SMS message sending result.

**Since:** 6

<!--Device-sms-export interface ISendShortMessageCallback--><!--Device-sms-export interface ISendShortMessageCallback-End-->

**System capability:** SystemCapability.Telephony.SmsMms

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## isLastPart

```TypeScript
isLastPart: boolean
```

Specifies whether this is the last part of a multi-part SMS message.

**Type:** boolean

**Since:** 6

<!--Device-ISendShortMessageCallback-isLastPart: boolean--><!--Device-ISendShortMessageCallback-isLastPart: boolean-End-->

**System capability:** SystemCapability.Telephony.SmsMms

## result

```TypeScript
result: SendSmsResult
```

Indicates the SMS message sending result.

**Type:** SendSmsResult

**Since:** 6

<!--Device-ISendShortMessageCallback-result: SendSmsResult--><!--Device-ISendShortMessageCallback-result: SendSmsResult-End-->

**System capability:** SystemCapability.Telephony.SmsMms

## url

```TypeScript
url: string
```

Indicates the URI to store the sent SMS message.

**Type:** string

**Since:** 6

<!--Device-ISendShortMessageCallback-url: string--><!--Device-ISendShortMessageCallback-url: string-End-->

**System capability:** SystemCapability.Telephony.SmsMms

