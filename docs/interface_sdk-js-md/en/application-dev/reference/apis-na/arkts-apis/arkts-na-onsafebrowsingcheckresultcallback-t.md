# OnSafeBrowsingCheckResultCallback

```TypeScript
export type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void
```

The callback of safe browsing check.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void--><!--Device-unnamed-export type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| threatType | [ThreatType](arkts-na-web-threattype-e.md) | Yes | callback information of onSafeBrowsingCheckResult. |

