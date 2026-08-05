# SetPreviewTextCallback

```TypeScript
export type SetPreviewTextCallback = (text: string, range: Range) => void
```

The callback of 'setPreviewText' event.

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

<!--Device-inputMethod-export type SetPreviewTextCallback = (text: string, range: Range) => void--><!--Device-inputMethod-export type SetPreviewTextCallback = (text: string, range: Range) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text to be previewed.  |
| range | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the range of the text to be replaced by the preview text.  |

