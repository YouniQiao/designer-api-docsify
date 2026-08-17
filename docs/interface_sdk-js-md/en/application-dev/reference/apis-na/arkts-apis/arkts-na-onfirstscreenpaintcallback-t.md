# OnFirstScreenPaintCallback

```TypeScript
export type OnFirstScreenPaintCallback = (firstScreenPaint: FirstScreenPaint) => void
```

The callback reports the time required for the first screen painting of the current web page.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export type OnFirstScreenPaintCallback = (firstScreenPaint: FirstScreenPaint) => void--><!--Device-unnamed-export type OnFirstScreenPaintCallback = (firstScreenPaint: FirstScreenPaint) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstScreenPaint | [FirstScreenPaint](arkts-na-web-firstscreenpaint-i.md) | Yes | the first screen paint info. |

