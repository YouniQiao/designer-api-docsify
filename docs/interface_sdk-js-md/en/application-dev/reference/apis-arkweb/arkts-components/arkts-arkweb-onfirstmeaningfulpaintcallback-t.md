# OnFirstMeaningfulPaintCallback

```TypeScript
type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: FirstMeaningfulPaint) => void
```

Callback for measuring the first meaningful paint of the main content on the page. This callback is triggered when the page finishes loading the main content. Compared with OnLargestContentfulPaintCallback, which focuses on the paint time of the largest content element, and OnFirstScreenPaintCallback, which focuses on the rendering completion of the first screen's visible content, this callback focuses more on whether the main content has finished loading, making it suitable for evaluating the loading experience of user-visible content.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| firstMeaningfulPaint | [FirstMeaningfulPaint](arkts-arkweb-firstmeaningfulpaint-i.md) | Yes |
