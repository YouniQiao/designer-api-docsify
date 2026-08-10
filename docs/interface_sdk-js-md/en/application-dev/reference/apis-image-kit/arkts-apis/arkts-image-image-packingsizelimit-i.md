# PackingSizeLimit

图片编码的大小限制。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-interface PackingSizeLimit--><!--Device-image-interface PackingSizeLimit-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## level

```TypeScript
level: AntiAliasingLevel
```

缩放时采用的缩放算法。默认值是AntiAliasingLevel.NONE。

**Type:** [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingSizeLimit-level: AntiAliasingLevel--><!--Device-PackingSizeLimit-level: AntiAliasingLevel-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## maxSize

```TypeScript
maxSize: Size
```

最大编码尺寸。

当指定的width或者height大于0时，原图尺寸超过限制将保持原宽高比进行缩放，确保图像尺寸不超过该边界。

默认值为{width: 0, height: 0}，表示不限制编码尺寸。

单位：像素（px）。

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingSizeLimit-maxSize: Size--><!--Device-PackingSizeLimit-maxSize: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

