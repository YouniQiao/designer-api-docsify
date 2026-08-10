# ImageBufferData

保存图像缓冲区数据的指针、不同颜色分量的行间距与像素间距信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-image-interface ImageBufferData--><!--Device-image-interface ImageBufferData-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## byteBuffer

```TypeScript
readonly byteBuffer: ArrayBuffer
```

图像缓冲区。

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

颜色分量的像素间距。单位：字节（Byte）。

对于编码后的图片如JPEG，该属性无意义。

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

颜色分量的行跨距。单位：字节（Byte）。

对于编码后的图片如JPEG，该属性无意义。

读取相机预览流数据时，需要按rowStride进行读取，使用详情请参考  
[相机预览花屏解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-deal-stride-solution)。

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageBufferData-readonly rowStride: int[]--><!--Device-ImageBufferData-readonly rowStride: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

