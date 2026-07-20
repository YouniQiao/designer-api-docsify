# SetPreviewTextCallback

```TypeScript
export type SetPreviewTextCallback = (text: string, range: Range) => void
```

The callback of 'setPreviewText' event.

**Since:** 17

<!--Device-inputMethod-export type SetPreviewTextCallback = (text: string, range: Range) => void--><!--Device-inputMethod-export type SetPreviewTextCallback = (text: string, range: Range) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text to be previewed.  |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | the range of the text to be replaced by the preview text.  |

