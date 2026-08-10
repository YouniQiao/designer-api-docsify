# ImageErrorCallback

```TypeScript
type ImageErrorCallback = (error: ImageError) => void
```

图片加载异常时触发此回调。

当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时该事件不触发。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-unnamed-type ImageErrorCallback = (error: ImageError) => void--><!--Device-unnamed-type ImageErrorCallback = (error: ImageError) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | [ImageError](../arkts-apis/arkts-arkui-image-imageerror-i.md) | Yes | 图片加载异常时触发回调的返回对象。 |

