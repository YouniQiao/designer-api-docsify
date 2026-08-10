# OnNativeEmbedVisibilityChangeCallback

```TypeScript
type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) => void
```

当同层标签可见性变化时触发该回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) => void--><!--Device-unnamed-type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nativeEmbedVisibilityInfo | [NativeEmbedVisibilityInfo](../arkts-apis/arkts-arkweb-web-nativeembedvisibilityinfo-i.md) | Yes | 提供同层标签的可见性信息。 |

