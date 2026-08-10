# OnLargestContentfulPaintCallback

```TypeScript
type OnLargestContentfulPaintCallback = (largestContentfulPaint: LargestContentfulPaint) => void
```

网页绘制页面最大内容度量信息的回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type OnLargestContentfulPaintCallback = (largestContentfulPaint: LargestContentfulPaint) => void--><!--Device-unnamed-type OnLargestContentfulPaintCallback = (largestContentfulPaint: LargestContentfulPaint) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| largestContentfulPaint | [LargestContentfulPaint](../arkts-apis/arkts-arkweb-web-largestcontentfulpaint-i.md) | Yes | 网页绘制页面最大内容度量的详细信息。 |

