# OnViewportFitChangedCallback

```TypeScript
type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void
```

网页meta中viewport-fit配置项更改时触发的回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void--><!--Device-unnamed-type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| viewportFit | [ViewportFit](../arkts-apis/arkts-arkweb-web-viewportfit-e.md) | Yes | 网页meta中viewport-fit配置的视口类型。 |

