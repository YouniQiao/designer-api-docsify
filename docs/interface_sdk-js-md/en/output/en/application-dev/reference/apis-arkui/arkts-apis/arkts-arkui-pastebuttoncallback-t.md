# PasteButtonCallback

```TypeScript
export type PasteButtonCallback 
  = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void
```

Callback function when the paste button is clicked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type PasteButtonCallback   = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void--><!--Device-unnamed-export type PasteButtonCallback   = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The click event.  |
| result | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The result of click event.  |
| error | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | The error code and message of click event.  |

