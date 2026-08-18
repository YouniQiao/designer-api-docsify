# OnLargestContentfulPaintCallback

```TypeScript
type OnLargestContentfulPaintCallback = (largestContentfulPaint: LargestContentfulPaint) => void
```

Callback triggered when the largest content area is painted on the web page. Used to obtain performance measurement information for the largest content paint. Applicable to scenarios such as monitoring web page loading performance and optimizing page rendering speed. Compared with OnFirstMeaningfulPaintCallback, which focuses on the completion of main content loading, and OnFirstScreenPaintCallback, which focuses on the rendering completion of the first screen's visible content, this callback focuses on the paint time of the largest content element, making it suitable for evaluating page rendering completeness and performance bottlenecks.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type OnLargestContentfulPaintCallback = (largestContentfulPaint: LargestContentfulPaint) => void--><!--Device-unnamed-type OnLargestContentfulPaintCallback = (largestContentfulPaint: LargestContentfulPaint) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| largestContentfulPaint | [LargestContentfulPaint](arkts-arkweb-largestcontentfulpaint-i.md) | Yes |
