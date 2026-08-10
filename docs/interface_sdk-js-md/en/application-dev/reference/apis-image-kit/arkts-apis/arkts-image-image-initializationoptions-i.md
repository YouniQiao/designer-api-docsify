# InitializationOptions

PixelMap的初始化选项。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-image-interface InitializationOptions--><!--Device-image-interface InitializationOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## alphaType

```TypeScript
alphaType?: AlphaType
```

透明度。默认值为IMAGE_ALPHA_TYPE_PREMUL。

**Type:** [AlphaType](arkts-image-image-alphatype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-alphaType?: AlphaType--><!--Device-InitializationOptions-alphaType?: AlphaType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## editable

```TypeScript
editable?: boolean
```

图像像素是否可被编辑。true表示可被编辑，false表示不可被编辑。设为false时，可提升图像的渲染和传输性能，但是图像不可被二次编辑。例如，writePixels操作将失败。默认值为false。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-editable?: boolean--><!--Device-InitializationOptions-editable?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelFormat

```TypeScript
pixelFormat?: PixelMapFormat
```

生成的PixelMap的像素格式。默认值为RGBA_8888。

**Type:** [PixelMapFormat](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-pixelFormat?: PixelMapFormat--><!--Device-InitializationOptions-pixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## scaleMode

```TypeScript
scaleMode?: ScaleMode
```

缩放模式。默认值为FIT_TARGET_SIZE。

**Type:** [ScaleMode](arkts-image-image-scalemode-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-scaleMode?: ScaleMode--><!--Device-InitializationOptions-scaleMode?: ScaleMode-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## size

```TypeScript
size: Size
```

创建的图片尺寸，宽高值必须为正整数。

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-size: Size--><!--Device-InitializationOptions-size: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## srcPixelFormat

```TypeScript
srcPixelFormat?: PixelMapFormat
```

传入的缓冲区数据的像素格式。默认值为BGRA_8888。

**Type:** [PixelMapFormat](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-InitializationOptions-srcPixelFormat?: PixelMapFormat--><!--Device-InitializationOptions-srcPixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

