# SubmitCallback

```TypeScript
export type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void
```

软键盘按下回车键时的回调事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void--><!--Device-unnamed-export type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enterKey | [EnterKeyType](../arkts-components/arkts-arkui-enterkeytype-e.md) | Yes | 软键盘输入法回车键类型。具体类型见EnterKeyType枚举说明。 |
| event | [SubmitEvent](../arkts-components/arkts-arkui-submitevent-i.md) | Yes | 当提交的时候，提供保持组件编辑状态的方法。EnterKeyType指定为NEW_LINE时，默认保持编辑态。 |

