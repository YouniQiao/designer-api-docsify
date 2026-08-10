# EditableTextOnChangeCallback

```TypeScript
declare type EditableTextOnChangeCallback = (value: string, previewText?: PreviewText, options?: TextChangeOptions) => void
```

输入内容发生变化时，触发该回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type EditableTextOnChangeCallback = (value: string, previewText?: PreviewText, options?: TextChangeOptions) => void--><!--Device-unnamed-declare type EditableTextOnChangeCallback = (value: string, previewText?: PreviewText, options?: TextChangeOptions) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | Text displayed in the text box. |
| previewText | [PreviewText](arkts-arkui-previewtext-i.md) | No | Information about the preview text, including its start position and text content. |
| options | [TextChangeOptions](arkts-arkui-textcommon-textchangeoptions-i.md) | No | Information about the text change, including the selection range, text displayed in the text box, and preview text. |

