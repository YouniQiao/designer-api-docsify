# ImageCompleteCallback

```TypeScript
type ImageCompleteCallback = (result: ImageLoadResult) => void
```

图片加载成功和解码成功时均触发的回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type ImageCompleteCallback = (result: ImageLoadResult) => void--><!--Device-unnamed-type ImageCompleteCallback = (result: ImageLoadResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [ImageLoadResult](../arkts-apis/arkts-arkui-imagespan-imageloadresult-i.md) | Yes | 图片数据加载成功和解码成功触发回调时返回的对象。 |

