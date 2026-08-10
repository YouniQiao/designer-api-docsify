# Component

描述图像颜色分量。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-image-interface Component--><!--Device-image-interface Component-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## byteBuffer

```TypeScript
readonly byteBuffer: ArrayBuffer
```

组件缓冲区。

**Type:** ArrayBuffer

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Component-readonly byteBuffer: ArrayBuffer--><!--Device-Component-readonly byteBuffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## componentType

```TypeScript
readonly componentType: ComponentType
```

组件类型。

**Type:** [ComponentType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-update-componenttype-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Component-readonly componentType: ComponentType--><!--Device-Component-readonly componentType: ComponentType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelStride

```TypeScript
readonly pixelStride: int
```

像素间距。单位：字节（Byte）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Component-readonly pixelStride: int--><!--Device-Component-readonly pixelStride: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## rowStride

```TypeScript
readonly rowStride: int
```

行距。单位：字节（Byte）。读取相机预览流数据时，需要按stride进行读取，使用详情请参考  
[相机预览花屏解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-deal-stride-solution)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Component-readonly rowStride: int--><!--Device-Component-readonly rowStride: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

