# OnSafeBrowsingCheckResultCallback

```TypeScript
type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void
```

The callback of safe browsing check.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void--><!--Device-unnamed-type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| threatType | [ThreatType](arkts-arkweb-threattype-e.md) | Yes |
