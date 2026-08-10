# MmsAttachment（系统接口）

Defines the attachment of an MMS message.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface MmsAttachment--><!--Device-sms-export interface MmsAttachment-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## charset

```TypeScript
charset?: MmsCharSets
```

Indicates the character set for the attachment.

**类型：** [MmsCharSets](arkts-telephony-sms-mmscharsets-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-charset?: MmsCharSets--><!--Device-MmsAttachment-charset?: MmsCharSets-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## contentDisposition

```TypeScript
contentDisposition: DispositionType
```

Indicates the content disposition for the attachment.

**类型：** [DispositionType](arkts-telephony-sms-dispositiontype-e-sys.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-contentDisposition: DispositionType--><!--Device-MmsAttachment-contentDisposition: DispositionType-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## contentId

```TypeScript
contentId: string
```

Indicates the content ID for the attachment.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-contentId: string--><!--Device-MmsAttachment-contentId: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## contentLocation

```TypeScript
contentLocation: string
```

Indicates the content location.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-contentLocation: string--><!--Device-MmsAttachment-contentLocation: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## contentTransferEncoding

```TypeScript
contentTransferEncoding: string
```

Indicates the encoding for content transfer.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-contentTransferEncoding: string--><!--Device-MmsAttachment-contentTransferEncoding: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## contentType

```TypeScript
contentType: string
```

Indicates the content type for the attachment.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-contentType: string--><!--Device-MmsAttachment-contentType: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## fileName

```TypeScript
fileName?: string
```

Indicates the file name for the attachment.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-fileName?: string--><!--Device-MmsAttachment-fileName?: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## inBuff

```TypeScript
inBuff?: Array<int>
```

Indicates whether the message is in the buffer.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-inBuff?: Array<int>--><!--Device-MmsAttachment-inBuff?: Array<int>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## isSmil

```TypeScript
isSmil: boolean
```

Indicates whether the synchronized multimedia integration language is used.

**类型：** boolean

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-isSmil: boolean--><!--Device-MmsAttachment-isSmil: boolean-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

## path

```TypeScript
path?: string
```

Indicates the path for the attachment.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-MmsAttachment-path?: string--><!--Device-MmsAttachment-path?: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

