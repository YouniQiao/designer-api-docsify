# SubmitCallback

```TypeScript
export type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void
```

callback of the listened enter key event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void--><!--Device-unnamed-export type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enterKey | [EnterKeyType](arkts-arkui-textinput-enterkeytype-e.md) | Yes | the enter key type of soft keyboard. |
| event | [SubmitEvent](arkts-arkui-textinput-submitevent-i.md) | Yes | Provides the method of keeping RichEditor editable state when submitted. |

