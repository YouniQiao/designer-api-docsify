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
| enterKey | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the enter key type of soft keyboard.  |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Provides the method of keeping RichEditor editable state when submitted.  |

