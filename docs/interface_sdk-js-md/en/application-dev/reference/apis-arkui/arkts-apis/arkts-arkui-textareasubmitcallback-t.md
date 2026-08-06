# TextAreaSubmitCallback

```TypeScript
export type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void
```

Declare the event listener callback of the enter key.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void--><!--Device-unnamed-export type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enterKeyType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The enter key type of soft keyboard. If the type is EnterKeyType.NEW\_LINE, onSubmit is not triggered.  |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Provides the method of keeping textArea editable state when submitted.  |

