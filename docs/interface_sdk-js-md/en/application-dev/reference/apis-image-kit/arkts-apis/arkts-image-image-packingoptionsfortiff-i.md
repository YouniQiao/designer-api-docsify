# PackingOptionsForTiff

描述TIFF图像编码参数的选项。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-interface PackingOptionsForTiff--><!--Device-image-interface PackingOptionsForTiff-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## compression

```TypeScript
compression?: int
```

该值应为整数，目前仅支持取3、4、5，分别对应压缩算法类型：3（CCITT G3）、4（CCITT G4）、5（LZW）。

- 对于二值图像：必须为3（G3）或4（G4），自动使用4（G4）。  
- 对于Y8/RGB_888格式：自动使用LZW（5），不支持指定其他压缩算法。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOptionsForTiff-compression?: int--><!--Device-PackingOptionsForTiff-compression?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## orientation

```TypeScript
orientation?: Orientation
```

图像方向。默认值为TOP_LEFT。

**Type:** [Orientation](../../apis-arkui/arkts-apis/arkts-arkui-window-orientation-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOptionsForTiff-orientation?: Orientation--><!--Device-PackingOptionsForTiff-orientation?: Orientation-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## resolutionUnit

```TypeScript
resolutionUnit?: int
```

分辨率单位：1（无单位）、2（英寸）、3（厘米）。目前仅支持1、2、3。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOptionsForTiff-resolutionUnit?: int--><!--Device-PackingOptionsForTiff-resolutionUnit?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## xResolution

```TypeScript
xResolution?: double
```

水平分辨率。该值必须大于0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOptionsForTiff-xResolution?: double--><!--Device-PackingOptionsForTiff-xResolution?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## yResolution

```TypeScript
yResolution?: double
```

垂直分辨率。该值必须大于0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOptionsForTiff-yResolution?: double--><!--Device-PackingOptionsForTiff-yResolution?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

