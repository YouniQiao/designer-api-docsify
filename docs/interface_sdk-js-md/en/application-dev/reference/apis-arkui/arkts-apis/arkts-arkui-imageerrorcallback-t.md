# ImageErrorCallback

```TypeScript
export type ImageErrorCallback = (error: ImageError) => void
```

图片加载异常时触发此回调。

当组件的参数类型为  
[AnimatedDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时该事件不触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ImageErrorCallback = (error: ImageError) => void--><!--Device-unnamed-export type ImageErrorCallback = (error: ImageError) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | [ImageError](arkts-arkui-image-imageerror-i.md) | Yes |  |

