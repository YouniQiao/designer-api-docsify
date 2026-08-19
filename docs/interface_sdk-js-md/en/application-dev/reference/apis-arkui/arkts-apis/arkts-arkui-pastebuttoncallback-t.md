# PasteButtonCallback

```TypeScript
export type PasteButtonCallback 
  = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void
```

Callback function when the paste button is clicked.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type PasteButtonCallback   = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void--><!--Device-unnamed-export type PasteButtonCallback   = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ClickEvent](../arkts-components/arkts-arkui-clickevent-i.md) | Yes | The click event. |
| result | [PasteButtonOnClickResult](arkts-arkui-pastebutton-pastebuttononclickresult-e.md) | Yes | The result of click event. |
| error | [BusinessError](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | No | The error code and message of click event. |

