# SendMessageOptions

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-unnamed-export interface SendMessageOptions--><!--Device-unnamed-export interface SendMessageOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## complete

```TypeScript
complete?: () => void
```

Called when the execution is completed.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SendMessageOptions-complete?: () => void--><!--Device-SendMessageOptions-complete?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Called when the messages fail to be sent.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SendMessageOptions-fail?: (data: string, code: number) => void--><!--Device-SendMessageOptions-fail?: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 |  |
| code | number | 是 |  |

## success

```TypeScript
success?: () => void
```

Called when the messages are sent successfully.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SendMessageOptions-success?: () => void--><!--Device-SendMessageOptions-success?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## abilityName

```TypeScript
abilityName: string
```

Destination ability name, which is case sensitive.

**类型：** string

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SendMessageOptions-abilityName: string--><!--Device-SendMessageOptions-abilityName: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## bundleName

```TypeScript
bundleName: string
```

Name of the destination bundle where the ability has been located. The name is case sensitive.

**类型：** string

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SendMessageOptions-bundleName: string--><!--Device-SendMessageOptions-bundleName: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## deviceId

```TypeScript
deviceId: string
```

Destination device ID.

**类型：** string

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SendMessageOptions-deviceId: string--><!--Device-SendMessageOptions-deviceId: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## message

```TypeScript
message?: string
```

Messages sent to the destination device.A maximum of 1 KB of data can be transmitted at a time.If more than 1 KB of data needs to be transmitted, split the messages into multiple parts to transmit.

**类型：** string

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SendMessageOptions-message?: string--><!--Device-SendMessageOptions-message?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

