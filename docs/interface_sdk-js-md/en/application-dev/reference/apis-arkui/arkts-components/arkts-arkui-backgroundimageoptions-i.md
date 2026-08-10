# BackgroundImageOptions

定义背景图选项。

> **说明：**
> 
> 背景图片的同步加载可能会带来潜在性能问题，详情可见[Image](../../../reference/apis-arkui/arkui-ts/ts-basic-components-image.md#image-1)中说明。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface BackgroundImageOptions--><!--Device-unnamed-interface BackgroundImageOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## repeat

```TypeScript
repeat?: ImageRepeat
```

设置背景图片的重复样式。默认值为ImageRepeat.NoRepeat。

**Type:** [ImageRepeat](../arkts-apis/arkts-arkui-imagerepeat-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-BackgroundImageOptions-repeat?: ImageRepeat--><!--Device-BackgroundImageOptions-repeat?: ImageRepeat-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## syncLoad

```TypeScript
syncLoad?: boolean
```

是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。

默认值：false

false：异步加载图片。

true：同步加载图片。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-BackgroundImageOptions-syncLoad?: boolean--><!--Device-BackgroundImageOptions-syncLoad?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

