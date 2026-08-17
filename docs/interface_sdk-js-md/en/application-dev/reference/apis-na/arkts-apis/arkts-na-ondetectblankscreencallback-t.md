# OnDetectBlankScreenCallback

```TypeScript
export type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void
```

The callback when web engine detects current page is blank or nearly blank.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void--><!--Device-unnamed-export type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [BlankScreenDetectionEventInfo](arkts-na-web-blankscreendetectioneventinfo-i.md) | Yes | the detection event info. |

