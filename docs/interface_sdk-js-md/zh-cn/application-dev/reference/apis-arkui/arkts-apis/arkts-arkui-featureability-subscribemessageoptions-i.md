# SubscribeMessageOptions

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-unnamed-export interface SubscribeMessageOptions--><!--Device-unnamed-export interface SubscribeMessageOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Called when the messages fail to be sent.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SubscribeMessageOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeMessageOptions-fail?: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 |  |
| code | number | 是 |  |

## success

```TypeScript
success?: (data: SubscribeMessageResponse) => void
```

Called when the messages are sent successfully.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-SubscribeMessageOptions-success?: (data: SubscribeMessageResponse) => void--><!--Device-SubscribeMessageOptions-success?: (data: SubscribeMessageResponse) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [SubscribeMessageResponse](arkts-arkui-featureability-subscribemessageresponse-i.md) | 是 |  |

