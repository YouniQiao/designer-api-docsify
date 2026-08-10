# ImageOnCompleteCallback

```TypeScript
export type ImageOnCompleteCallback = (loadEvent?: ImageCompleteEvent) => void
```

图片数据加载成功和解码成功时触发该回调。

当组件的参数类型为  
[AnimatedDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时该事件不触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ImageOnCompleteCallback = (loadEvent?: ImageCompleteEvent) => void--><!--Device-unnamed-export type ImageOnCompleteCallback = (loadEvent?: ImageCompleteEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loadEvent | [ImageCompleteEvent](arkts-arkui-image-imagecompleteevent-i.md) | No |  |

