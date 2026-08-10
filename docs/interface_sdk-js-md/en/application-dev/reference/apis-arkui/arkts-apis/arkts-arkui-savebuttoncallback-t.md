# SaveButtonCallback

```TypeScript
export type SaveButtonCallback 
  = (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError<void>) => void
```

Callback function when the save button is clicked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SaveButtonCallback   = (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError<void>) => void--><!--Device-unnamed-export type SaveButtonCallback   = (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ClickEvent](../arkts-components/arkts-arkui-clickevent-i.md) | Yes | The click event. |
| result | [SaveButtonOnClickResult](../arkts-components/arkts-arkui-savebuttononclickresult-e.md) | Yes | The result of click event. |
| error | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | No | The error code and message of click event. |

