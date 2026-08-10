# OnNativeEmbedObjectParamChangeCallback

```TypeScript
type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void
```

增加、修改或删除同层渲染object标签内嵌param元素时触发此回调。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-unnamed-type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void--><!--Device-unnamed-type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [NativeEmbedParamDataInfo](../arkts-apis/arkts-arkweb-web-nativeembedparamdatainfo-i.md) | Yes | object标签内嵌param元素的详细变化信息。 |

