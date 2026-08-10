# BinaryBufferInfo

描述二值图像缓冲区内的信息及数据。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-interface BinaryBufferInfo--><!--Device-image-interface BinaryBufferInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## bytesPerRow

```TypeScript
bytesPerRow?: int
```

每行字节数。若未指定，将按(width + 7) / 8计算。该值应为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BinaryBufferInfo-bytesPerRow?: int--><!--Device-BinaryBufferInfo-bytesPerRow?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## data

```TypeScript
data: ArrayBuffer
```

图像数据缓冲区，包含二值图像数据。

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BinaryBufferInfo-data: ArrayBuffer--><!--Device-BinaryBufferInfo-data: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## size

```TypeScript
size: Size
```

图像尺寸，包含宽度和高度。

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BinaryBufferInfo-size: Size--><!--Device-BinaryBufferInfo-size: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

