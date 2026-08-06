# ButtonElement

The \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ component includes capsule, circle, text, arc, and download buttons.

**Inheritance/Implementation:** ButtonElement extends [Element](viewmodel-element-i.md)

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

<!--Device-unnamed-export interface ButtonElement extends Element--><!--Device-unnamed-export interface ButtonElement extends Element-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setProgress

```TypeScript
setProgress(param: { progress: number }): void
```

Progress bar of the download button.The value ranges from 0 to 100. The progress bar is displayed if the value is greater than 0.If the value is greater than or equal to 100, the progress bar is not displayed.NOTE The text displayed on the progress bar is changed based on the value.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ButtonElement-setProgress(param: { progress: number }): void--><!--Device-ButtonElement-setProgress(param: { progress: number }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | { progress: number } | Yes |  |

