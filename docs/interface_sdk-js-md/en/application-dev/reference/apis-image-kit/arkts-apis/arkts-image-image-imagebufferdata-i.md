# ImageBufferData

Describes the image buffer data.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-image-interface ImageBufferData--><!--Device-image-interface ImageBufferData-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## byteBuffer

```TypeScript
readonly byteBuffer: ArrayBuffer
```

Image data buffer.

**Type:** ArrayBuffer

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageBufferData-readonly byteBuffer: ArrayBuffer--><!--Device-ImageBufferData-readonly byteBuffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelStride

```TypeScript
readonly pixelStride: int[]
```

Pixel stride of each component.

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageBufferData-readonly pixelStride: int[]--><!--Device-ImageBufferData-readonly pixelStride: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## rowStride

```TypeScript
readonly rowStride: int[]
```

Row stride of each component.

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageBufferData-readonly rowStride: int[]--><!--Device-ImageBufferData-readonly rowStride: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

