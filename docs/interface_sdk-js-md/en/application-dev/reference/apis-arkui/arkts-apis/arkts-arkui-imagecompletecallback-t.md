# ImageCompleteCallback

```TypeScript
export type ImageCompleteCallback = (result: ImageLoadResult) => void
```

图片加载成功和解码成功时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ImageCompleteCallback = (result: ImageLoadResult) => void--><!--Device-unnamed-export type ImageCompleteCallback = (result: ImageLoadResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [ImageLoadResult](arkts-arkui-imagespan-imageloadresult-i.md) | Yes | 图片数据加载成功和解码成功触发回调时返回的对象。 |

