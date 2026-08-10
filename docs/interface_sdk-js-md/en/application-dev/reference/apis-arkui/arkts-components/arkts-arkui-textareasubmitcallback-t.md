# TextAreaSubmitCallback

```TypeScript
declare type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void
```

软键盘按下回车键时的回调事件。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-unnamed-declare type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void--><!--Device-unnamed-declare type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enterKeyType | [EnterKeyType](../arkts-apis/arkts-arkui-textinput-enterkeytype-e.md) | Yes | 软键盘输入法回车键类型。 <br>类型为EnterKeyType.NEW_LINE时不触发onSubmit。 |
| event | [SubmitEvent](arkts-arkui-submitevent-i.md) | No | 提交事件。用于获取提交事件的详细信息。不传入此参数时，无法获取提交事件的详细信息。 |

