# ImageRotateOrientation

期望的图像内容显示方向。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-unnamed-declare enum ImageRotateOrientation--><!--Device-unnamed-declare enum ImageRotateOrientation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 0
```

读取图片携带的EXIF元数据作为显示方向，支持旋转和镜像。

[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)和[DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md)类型的图片不包含头信息，调用该接口时图片显示效果不变化。

![imageRotateOrientation_0](../../../reference/apis-arkui/arkui-ts/figures/imageRotateOrientation_0.png)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-AUTO = 0--><!--Device-ImageRotateOrientation-AUTO = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## UP

```TypeScript
UP = 1
```

默认按照当前图片的像素数据进行显示，不做任何处理。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-UP = 1--><!--Device-ImageRotateOrientation-UP = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT

```TypeScript
RIGHT = 2
```

将当前图片顺时针旋转90度后显示。

![imageRotateOrientation_2](../../../reference/apis-arkui/arkui-ts/figures/imageRotateOrientation_2.png)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-RIGHT = 2--><!--Device-ImageRotateOrientation-RIGHT = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DOWN

```TypeScript
DOWN = 3
```

将当前图片顺时针旋转180度后显示。

![imageRotateOrientation_3](../../../reference/apis-arkui/arkui-ts/figures/imageRotateOrientation_3.png)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-DOWN = 3--><!--Device-ImageRotateOrientation-DOWN = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LEFT

```TypeScript
LEFT = 4
```

将当前图片顺时针旋转270度后显示。

![imageRotateOrientation_4](../../../reference/apis-arkui/arkui-ts/figures/imageRotateOrientation_4.png)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-LEFT = 4--><!--Device-ImageRotateOrientation-LEFT = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## UP_MIRRORED

```TypeScript
UP_MIRRORED = 5
```

将当前图片水平翻转后显示。

![imageRotateOrientation_5](../../../reference/apis-arkui/arkui-ts/figures/imageRotateOrientation_5.png)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-UP_MIRRORED = 5--><!--Device-ImageRotateOrientation-UP_MIRRORED = 5-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT_MIRRORED

```TypeScript
RIGHT_MIRRORED = 6
```

将当前图片水平翻转再顺时针旋转90度后显示。

![imageRotateOrientation_6](../../../reference/apis-arkui/arkui-ts/figures/imageRotateOrientation_6.png)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-RIGHT_MIRRORED = 6--><!--Device-ImageRotateOrientation-RIGHT_MIRRORED = 6-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DOWN_MIRRORED

```TypeScript
DOWN_MIRRORED = 7
```

将当前图片垂直翻转后显示。

![imageRotateOrientation_7](../../../reference/apis-arkui/arkui-ts/figures/imageRotateOrientation_7.png)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-DOWN_MIRRORED = 7--><!--Device-ImageRotateOrientation-DOWN_MIRRORED = 7-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LEFT_MIRRORED

```TypeScript
LEFT_MIRRORED = 8
```

将当前图片水平翻转再顺时针旋转270度后显示。

![imageRotateOrientation_8](../../../reference/apis-arkui/arkui-ts/figures/imageRotateOrientation_8.png)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-LEFT_MIRRORED = 8--><!--Device-ImageRotateOrientation-LEFT_MIRRORED = 8-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

