# Filter

图像效果类，用于通过链式调用将指定效果添加到效果链表中，适用于图片滤镜处理、视觉效果增强、图像美化等场景。在调用Filter的方法前，需要先通过[createEffect](arkts-arkgraphics2d-effectkit-createeffect-f.md#createeffect)创建一个Filter实例。在添加效果后，需调用[getEffectPixelMap](arkts-arkgraphics2d-effectkit-filter-i.md#geteffectpixelmap)获取处理后的图像。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-effectKit-interface Filter--><!--Device-effectKit-interface Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## blur

ArkTS-Dyn:
```TypeScript
blur(radius: number): Filter
```

ArkTS-Sta:
```TypeScript
blur(radius: double): Filter
```

将模糊效果添加到效果链表中，返回链表的实例。着色器平铺模式使用DECAL，如需指定平铺模式，可使用[blur](arkts-arkgraphics2d-effectkit-filter-i.md#blur)接口。常用于实现背景虚化效果、隐私信息遮挡、毛玻璃背景效果、弹窗背景模糊等场景。

> **说明：**
> 
> 该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](../../../ui/arkts-blur-effect.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Filter-blur(radius: double): Filter--><!--Device-Filter-blur(radius: double): Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 模糊半径，单位为px，取值范围为[0, +∞)。模糊半径值越大，模糊效果越明显。传入负数时无效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function imageBlur(imageData: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise(async (resolve) => {
    // Create an image source.
    let imageSource = image.createImageSource(imageData);
    await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      // Set the blur radius.
      let radius = 5;
      // Create a Filter instance.
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add a blur effect to the image.
        headFilter.blur(radius);
        // Process the image based on the added effect identifiers and return the processed image data.
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        });
      }
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try {
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (err) {
      return undefined;
    }
  }

  async aboutToAppear(): Promise<void> {
    this.imageBuffer = await this.getFileBuffer();
    if (this.imageBuffer == undefined) {
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await imageBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

## blur

ArkTS-Dyn:
```TypeScript
blur(radius: number, tileMode: TileMode): Filter
```

ArkTS-Sta:
```TypeScript
blur(radius: double, tileMode: TileMode): Filter
```

将模糊效果添加到效果链表中，返回链表的实例。支持选择着色器效果平铺模式，常用于实现背景虚化效果、隐私信息遮挡、毛玻璃背景效果、弹窗背景模糊等场景。

> **说明：**
> 
> 该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](../../../ui/arkts-blur-effect.md)。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-Filter-blur(radius: double, tileMode: TileMode): Filter--><!--Device-Filter-blur(radius: double, tileMode: TileMode): Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 模糊半径，单位为px，取值范围为[0, +∞)。模糊半径值越大，模糊效果越明显。传入负数时无效果。 |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。影响图像边缘的模糊效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function imageBlur(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise(async (resolve) => {
    // Create the image source.
    let imageSource = image.createImageSource(Image);
    await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      // Set the blur radius.
      let radius = 30;
      // Create a Filter instance.
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add a blur effect to the image and set the tile mode.
        headFilter.blur(radius, effectKit.TileMode.DECAL);
        // Process the image based on the added effect identifier and return the processed image data.
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        });
      }
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try {
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (err) {
      return undefined;
    }
  }

  async aboutToAppear(): Promise<void> {
    this.imageBuffer = await this.getFileBuffer();
    if (this.imageBuffer == undefined) {
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await imageBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

## brightness

ArkTS-Dyn:
```TypeScript
brightness(bright: number): Filter
```

ArkTS-Sta:
```TypeScript
brightness(bright: double): Filter
```

将高亮效果添加到效果链表中，返回链表的实例。该方法通过调整图像亮度实现高亮效果，常用于暗图增亮处理、图片预览亮度增强、夜间模式图片适配等场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Filter-brightness(bright: double): Filter--><!--Device-Filter-brightness(bright: double): Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bright | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 高亮程度，取值范围为[0, 1]，取值为0时图像保持不变，取值为1时图像亮度提升到最大值。超出范围时自动修正为0。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function imageBrightness(imageData: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise(async (resolve) => {
    // Create the image source.
    let imageSource = image.createImageSource(imageData);
    await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      // Set the brightness value.
      let bright = 0.5;
      // Create a Filter instance.
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add a highlight effect to the image.
        headFilter.brightness(bright);
        // Process the image based on the added effect identifier and return the processed image data.
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        });
      }
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try {
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (err) {
      return undefined;
    }
  }

  async aboutToAppear(): Promise<void> {
    this.imageBuffer = await this.getFileBuffer();
    if (this.imageBuffer == undefined) {
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await imageBrightness(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

## getEffectPixelMap

```TypeScript
getEffectPixelMap(): Promise<image.PixelMap>
```

获取已添加链表效果的源图像的image.PixelMap，默认使用CPU渲染，使用Promise异步回调。如需指定渲染模式，可使用[getEffectPixelMap](arkts-arkgraphics2d-effectkit-filter-i.md#geteffectpixelmap)接口。常用于图片处理后需要保存或显示结果的场景。

> **说明：**
> 
> 该方法默认使用CPU渲染，着色器平铺模式仅支持DECAL，其他模式（CLAMP、REPEAT、MIRROR）暂不支持。
如需使用GPU渲染或了解渲染模式对TileMode的影响，请参见[TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md)和  
[getEffectPixelMap](arkts-arkgraphics2d-effectkit-filter-i.md#geteffectpixelmap)。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Filter-getEffectPixelMap(): Promise<image.PixelMap>--><!--Device-Filter-getEffectPixelMap(): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | Promise对象。返回已添加链表效果的源图像的image.PixelMap。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
// Create a PixelMap instance.
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  // Create a Filter instance.
  let headFilter = effectKit.createEffect(pixelMap);
  if (headFilter != null) {
    // Add a grayscale effect and obtain the processed PixelMap.
    headFilter.grayscale().getEffectPixelMap().then(data => {
      console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
    });
  }
});
```

## getEffectPixelMap

```TypeScript
getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>
```

获取已添加链表效果的源图像的image.PixelMap，支持指定渲染模式（CPU渲染或者GPU渲染），使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-Filter-getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>--><!--Device-Filter-getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| useCpuRender | boolean | Yes | 指定渲染模式。true表示使用CPU渲染，false表示使用GPU渲染。 使用GPU渲染时，着色器效果平铺模式[TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md)的支持范围与CPU渲染不同，详见TileMode说明。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | Promise对象。返回已添加链表效果的源图像的image.PixelMap。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for the image effect.
const colorBuffer = new ArrayBuffer(96);
// Set the image initialization options.
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
// Create a PixelMap instance.
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  // Create a Filter instance, add a grayscale effect, and obtain the processed PixelMap.
  effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap(false).then(data => {
    console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
  });
});
```

## getPixelMap

```TypeScript
getPixelMap(): image.PixelMap
```

获取已添加链表效果的源图像的image.PixelMap。常用于图片处理后需要保存或显示结果的场景。

> **说明：**
> 
> 从API version 9开始支持，从API version 11开始废弃，建议使用[getEffectPixelMap](arkts-arkgraphics2d-effectkit-filter-i.md#geteffectpixelmap)替代。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [effectKit.Filter#getEffectPixelMap](arkts-arkgraphics2d-effectkit-filter-i.md#geteffectpixelmap)

<!--Device-Filter-getPixelMap(): image.PixelMap--><!--Device-Filter-getPixelMap(): image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | 已添加效果的源图像的image.PixelMap。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

const colorBuffer = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  let pixel = effectKit.createEffect(pixelMap).grayscale().getPixelMap();
  console.info('getPixelBytesNumber = ', pixel.getPixelBytesNumber());
});
```

## grayscale

```TypeScript
grayscale(): Filter
```

将灰度效果添加到效果链表中，返回链表的实例。该方法将彩色图像转换为灰度图像，通过加权计算RGB值得到灰度值。常用于黑白风格照片生成、图片预处理去色、灰度图标制作等场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Filter-grayscale(): Filter--><!--Device-Filter-grayscale(): Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function imageGrayscale(imageData: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise(async (resolve) => {
    // Create the image source.
    let imageSource = image.createImageSource(imageData);
    await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      // Create a Filter instance.
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add a grayscale effect to the image.
        headFilter.grayscale();
        // Process the image based on the added effect identifier and return the processed image data.
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        });
      }
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try {
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (err) {
      return undefined;
    }
  }

  async aboutToAppear(): Promise<void> {
    this.imageBuffer = await this.getFileBuffer();
    if (this.imageBuffer == undefined) {
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await imageGrayscale(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

## invert

```TypeScript
invert(): Filter
```

将反转效果添加到效果链表中，返回链表的实例。该方法将图像的RGB颜色值进行反转，常用于实现底片效果、图片艺术处理、夜间模式适配等场景。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Filter-invert(): Filter--><!--Device-Filter-invert(): Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function imageInvert(imageData: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise(async (resolve) => {
    // Create the image source.
    let imageSource = image.createImageSource(imageData);
    await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      // Create a Filter instance.
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add an inversion effect to the image.
        headFilter.invert();
        // Process the image based on the added effect identifiers and return the processed image data.
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        });
      }
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try {
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (err) {
      return undefined;
    }
  }

  async aboutToAppear(): Promise<void> {
    this.imageBuffer = await this.getFileBuffer();
    if (this.imageBuffer == undefined) {
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await imageInvert(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

## setColorMatrix

ArkTS-Dyn:
```TypeScript
setColorMatrix(colorMatrix: Array<number>): Filter
```

ArkTS-Sta:
```TypeScript
setColorMatrix(colorMatrix: Array<double>): Filter
```

通过自定义颜色矩阵对图像进行颜色变换处理，将效果添加到效果链表中，返回链表的实例。常用于实现预设滤镜不支持的自定义颜色效果，如复古色调、冷暖色调调整等场景。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Filter-setColorMatrix(colorMatrix: Array<double>): Filter--><!--Device-Filter-setColorMatrix(colorMatrix: Array<double>): Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorMatrix | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | Yes | 自定义颜色矩阵。用于创建效果滤镜的4x5大小的矩阵，数组长度必须为20， 前4列对应R、G、B、A通道的变换系数，第5列为常量偏移值。建议元素取值为[-1, 1]，超出此范围可能导致颜色值溢出或产生非预期效果。数组长度不为20时返回null。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 输入参数错误。 |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function imageColorFilter(imageData: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise(async (resolve) => {
    // Create the image source.
    let imageSource = image.createImageSource(imageData);
    await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      // Define the color matrix.
      let colorMatrix: Array<number> = [
        0.2126, 0.7152, 0.0722, 0, 0,
        0.2126, 0.7152, 0.0722, 0, 0,
        0.2126, 0.7152, 0.0722, 0, 0,
        0, 0, 0, 1, 0
      ];
      // Create a Filter instance.
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Apply a custom color matrix effect to the image.
        headFilter.setColorMatrix(colorMatrix);
        // Process the image based on the added effect identifier and return the processed image data.
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        });
      }
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try {
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (err) {
      return undefined;
    }
  }

  async aboutToAppear(): Promise<void> {
    this.imageBuffer = await this.getFileBuffer();
    if (this.imageBuffer == undefined) {
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await imageColorFilter(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

