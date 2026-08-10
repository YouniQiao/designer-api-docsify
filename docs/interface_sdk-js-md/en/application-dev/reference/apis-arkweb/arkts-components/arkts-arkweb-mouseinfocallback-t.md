# MouseInfoCallback

```TypeScript
type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void
```

当鼠标/触摸板点击到同层标签时触发该回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void--><!--Device-unnamed-type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [NativeEmbedMouseInfo](../arkts-apis/arkts-arkweb-web-nativeembedmouseinfo-i.md) | Yes | 提供鼠标/触摸板在同层标签上点击或长按的详细信息。 |

