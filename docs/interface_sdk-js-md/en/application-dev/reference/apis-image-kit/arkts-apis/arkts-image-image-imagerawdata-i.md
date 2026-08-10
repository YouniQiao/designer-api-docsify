# ImageRawData

图像的RAW数据。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-image-interface ImageRawData--><!--Device-image-interface ImageRawData-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## bitsPerPixel

```TypeScript
bitsPerPixel: int
```

每个像素在缓冲区数据中实际占用的位数。单位：比特（bit）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageRawData-bitsPerPixel: int--><!--Device-ImageRawData-bitsPerPixel: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## buffer

```TypeScript
buffer: ArrayBuffer
```

图像缓冲区。

**Type:** ArrayBuffer

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageRawData-buffer: ArrayBuffer--><!--Device-ImageRawData-buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

