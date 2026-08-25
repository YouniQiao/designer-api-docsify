# PixelMap

The **PixelMap** class provides APIs to read or write image data and obtain image information. Before calling any API in PixelMap, you must use [image.createPixelMap](arkts-image-image-createpixelmap-f.md) to create a PixelMap object. Currently, the maximum size of a serialized PixelMap is 128 MB. A larger size will cause a display failure. The size is calculated as follows: Width x Height x [Bytes per pixel](arkts-image-image-pixelmapformat-e.md). Since API version 11, PixelMap supports cross-thread calls through [Worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md). If a PixelMap object is invoked by another thread through [Worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md), all APIs of the PixelMap object cannot be called in the original thread. Otherwise, error 501 is reported, indicating that the server cannot complete the request. Before calling any API in PixelMap, you can use [image.createPixelMap](arkts-image-image-createpixelmap-f.md) to pass pixel data to create a PixelMap object, or use [ImageSource](arkts-multimedia-image.md) to decode an image to a PixelMap object. To develop an atomic service, use [ImageSource](arkts-multimedia-image.md) to create a PixelMap object. Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## applyColorSpace

```TypeScript
applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void
```

Performs color space conversion (CSC) on the image pixel color based on a given color space. This API uses an asynchronous callback to return the result.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetColorSpace | colorSpaceManager.ColorSpaceManager | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980108](../errorcode-image.md#62980108-图片颜色转换错误) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

**示例**

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function applyColorSpace(pixelMap: image.PixelMap) {
  const colorSpaceName = colorSpaceManager.ColorSpace.SRGB;
  const targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  pixelMap.applyColorSpace(targetColorSpace, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to apply color space. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in applying color space.');
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function applyColorSpace(pixelMap: image.PixelMap) {
  const colorSpaceName = colorSpaceManager.ColorSpace.SRGB;
  const targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  pixelMap.applyColorSpace(targetColorSpace).then(() => {
    console.info('Succeeded in applying color space.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to apply color space. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function applyColorSpace(pixelMap: image.PixelMap) {
  const colorSpaceName = colorSpaceManager.ColorSpace.SRGB;
  const targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  pixelMap.applyColorSpace(targetColorSpace).then(() => {
    console.info('Succeeded in applying color space.');
  }).catch((err: Error) => {
    console.error(`Failed to apply color space. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## applyColorSpace

```TypeScript
applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>
```

Performs Color Space Converters (CSC) on the image pixel color based on a given color space. This API uses a promise to return the result.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetColorSpace | colorSpaceManager.ColorSpaceManager | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980108](../errorcode-image.md#62980108-图片颜色转换错误) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

**示例**

参见 [applyColorSpace](#applycolorspace)

## applyCrop

```TypeScript
applyCrop(region: Region): Promise<void>
```

Crops the PixelMap.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600204](../errorcode-image.md#7600204-无效的区域) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyCrop(pixelMap: image.PixelMap) {
  const currSize = pixelMap.getImageInfoSync().size;
  const region: image.Region = { // 裁剪区域设为图像中心四分之一的区域。
    x: currSize.width / 4,
    y: currSize.height / 4,
    size: {
      width: currSize.width / 2,
      height: currSize.height / 2
    }
  };

  pixelMap.applyCrop(region)
    .then(() => {
      console.info('Succeeded in cropping the PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function applyCrop(pixelMap: image.PixelMap) {
  const currSize = pixelMap.getImageInfoSync().size;
  const region: image.Region = { // 裁剪区域设为图像中心四分之一的区域。
    x: currSize.width / 4,
    y: currSize.height / 4,
    size: {
      width: currSize.width / 2,
      height: currSize.height / 2
    }
  };

  pixelMap.applyCrop(region)
    .then(() => {
      console.info('Succeeded in cropping the PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## applyCropSync

```TypeScript
applyCropSync(region: Region): void
```

Crops the PixelMap.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600204](../errorcode-image.md#7600204-无效的区域) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyCropSync(pixelMap: image.PixelMap) {
  const currSize = pixelMap.getImageInfoSync().size;
  const region: image.Region = { // 裁剪区域设为图像中心四分之一的区域。
    x: currSize.width / 4,
    y: currSize.height / 4,
    size: {
      width: currSize.width / 2,
      height: currSize.height / 2
    }
  };

  try {
    pixelMap.applyCropSync(region);
    console.info('Succeeded in cropping the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function applyCropSync(pixelMap: image.PixelMap) {
  const currSize = pixelMap.getImageInfoSync().size;
  const region: image.Region = { // 裁剪区域设为图像中心四分之一的区域。
    x: currSize.width / 4,
    y: currSize.height / 4,
    size: {
      width: currSize.width / 2,
      height: currSize.height / 2
    }
  };

  try {
    pixelMap.applyCropSync(region);
    console.info('Succeeded in cropping the PixelMap.');
  } catch (err) {
    console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## applyFlip

```TypeScript
applyFlip(horizontal: boolean, vertical: boolean): Promise<void>
```

Flips the PixelMap in the horizontal and/or vertical directions.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyFlip(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  pixelMap.applyFlip(horizontal, vertical)
    .then(() => {
      console.info('Succeeded in flipping the PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function applyFlip(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  pixelMap.applyFlip(horizontal, vertical)
    .then(() => {
      console.info('Succeeded in flipping the PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## applyFlipSync

```TypeScript
applyFlipSync(horizontal: boolean, vertical: boolean): void
```

Flips the PixelMap in the horizontal and/or vertical directions.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyFlipSync(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  try {
    pixelMap.applyFlipSync(horizontal, vertical);
    console.info('Succeeded in flipping the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function applyFlipSync(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  try {
    pixelMap.applyFlipSync(horizontal, vertical);
    console.info('Succeeded in flipping the PixelMap.');
  } catch (err) {
    console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## applyRotate

ArkTS-Dyn:
```TypeScript
applyRotate(angle: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
applyRotate(angle: double): Promise<void>
```

Rotates the PixelMap.Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyRotate(pixelMap: image.PixelMap) {
  const angle: number = 90.0;
  pixelMap.applyRotate(angle)
    .then(() => {
      console.info('Succeeded in rotating the PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function applyRotate(pixelMap: image.PixelMap) {
  const angle: double = 90.0;
  pixelMap.applyRotate(angle)
    .then(() => {
      console.info('Succeeded in rotating the PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## applyRotateSync

ArkTS-Dyn:
```TypeScript
applyRotateSync(angle: number): void
```

ArkTS-Sta:
```TypeScript
applyRotateSync(angle: double): void
```

Rotates the PixelMap.Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyRotateSync(pixelMap: image.PixelMap) {
  const angle: number = 90.0;
  try {
    pixelMap.applyRotateSync(angle);
    console.info('Succeeded in rotating the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function applyRotateSync(pixelMap: image.PixelMap) {
  const angle: double = 90.0;
  try {
    pixelMap.applyRotateSync(angle);
    console.info('Succeeded in rotating the PixelMap.');
  } catch (err) {
    console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## applyScale

ArkTS-Dyn:
```TypeScript
applyScale(x: number, y: number, level?: AntiAliasingLevel): Promise<void>
```

ArkTS-Sta:
```TypeScript
applyScale(x: double, y: double, level?: AntiAliasingLevel): Promise<void>
```

Scales the PixelMap in the horizontal and/or vertical dimensions.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyScale(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.5;
  pixelMap.applyScale(scaleX, scaleY)
    .then(() => {
      console.info('Succeeded in scaling the PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function applyScale(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.5;
  pixelMap.applyScale(scaleX, scaleY)
    .then(() => {
      console.info('Succeeded in scaling the PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## applyScaleSync

ArkTS-Dyn:
```TypeScript
applyScaleSync(x: number, y: number, level?: AntiAliasingLevel): void
```

ArkTS-Sta:
```TypeScript
applyScaleSync(x: double, y: double, level?: AntiAliasingLevel): void
```

Scales the PixelMap in the horizontal and/or vertical dimensions.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyScaleSync(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.5;
  try {
    pixelMap.applyScaleSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
    console.info('Succeeded in scaling the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function applyScaleSync(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.5;
  try {
    pixelMap.applyScaleSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
    console.info('Succeeded in scaling the PixelMap.');
  } catch (err) {
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## applyTranslate

ArkTS-Dyn:
```TypeScript
applyTranslate(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
applyTranslate(x: double, y: double): Promise<void>
```

Repositions the PixelMap in the horizontal and/or vertical directions.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyTranslate(pixelMap: image.PixelMap) {
  const translateX: number = 50.0;
  const translateY: number = 10.0;
  pixelMap.applyTranslate(translateX, translateY)
    .then(() => {
      console.info('Succeeded in translating the PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function applyTranslate(pixelMap: image.PixelMap) {
  const translateX: double = 50.0;
  const translateY: double = 10.0;
  pixelMap.applyTranslate(translateX, translateY)
    .then(() => {
      console.info('Succeeded in translating the PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## applyTranslateSync

ArkTS-Dyn:
```TypeScript
applyTranslateSync(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
applyTranslateSync(x: double, y: double): void
```

Repositions the PixelMap in the horizontal and/or vertical directions.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function applyTranslateSync(pixelMap: image.PixelMap) {
  const translateX: number = 50.0;
  const translateY: number = 10.0;
  try {
    pixelMap.applyTranslateSync(translateX, translateY);
    console.info('Succeeded in translating the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function applyTranslateSync(pixelMap: image.PixelMap) {
  const translateX: double = 50.0;
  const translateY: double = 10.0;
  try {
    pixelMap.applyTranslateSync(translateX, translateY);
    console.info('Succeeded in translating the PixelMap.');
  } catch (err) {
    console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## clone

```TypeScript
clone(): Promise<PixelMap>
```

Copies this PixelMap object. This API uses a promise to return the result.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |
| [62980102](../errorcode-image.md#62980102-图片分配内存错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    let new_metadata: image.Metadata = await metaData.clone();
    new_metadata.getProperties(["ImageWidth"]).then((data1) => {
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to clone new_metadata, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function CloneFunc(metadata: image.Metadata): void {
  try {
    let newMetadata = await metadata.clone();
    console.info(0x00000, 'CloneFunc', 'clone success!');
  } catch (err) {
    console.error(0x00000, 'CloneFunc', 'CloneFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataClone(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let new_metadata = await metaData.exifMetadata.clone();
    new_metadata.getProperties(["ImageWidth"]).then((data1) => {
      console.info(`Succeeded in cloning metadata and getting properties. Data: ${JSON.stringify(data1)}.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to clone metadata and get properties. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function exifMetadataClone(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    try {
      const exif = metaData?.exifMetadata;
      if (exif) {
        let new_metadata = await exif.clone();
        let data = new_metadata.getProperties(["ImageWidth"]);
        const count = Object.keys(data).length;
        console.info(`Clone new_metadata and get Properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Clone new_metadata failed, error : ${err}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function makerNoteHuaweiClone(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    let new_metadata = await metaData.makerNoteHuaweiMetadata.clone();
    new_metadata.getProperties(["HwMnoteIsXmageSupported"]).then((data1) => {
      console.info(`Succeeded in cloning metadata and getting properties. Data: ${JSON.stringify(data1)}.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to clone metadata and get properties. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function makerNoteHuaweiMetadataClone(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    try {
      const exif = metaData?.makerNoteHuaweiMetadata;
      if (exif) {
        let new_metadata = await exif.clone();
        let data = new_metadata.getProperties(["HwMnoteIsXmageSupported"]);
        const count = Object.keys(data).length;
        console.info(`Clone new_metadata and get Properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Clone new_metadata failed, error : ${err}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataClone(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    let new_metadata = await metaData.heifsMetadata.clone();
    new_metadata.getProperties(["HeifsDelayTime"]).then((data1) => {
      console.info(`Succeeded in cloning metadata and getting properties. Data: ${JSON.stringify(data1)}.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to clone metadata and get properties. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function heifsMetadataClone(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    try {
      const exif = metaData?.heifsMetadata;
      if (exif) {
        let new_metadata = await exif.clone();
        let data = new_metadata.getProperties(["HeifsDelayTime"]);
        const count = Object.keys(data).length;
        console.info(`Clone new_metadata and get Properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Clone new_metadata failed, error : ${err}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function clone(pixelMap: image.PixelMap) {
  pixelMap.clone().then((clonedPixelMap: image.PixelMap) => {
    console.info('Succeeded in cloning the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to clone the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function clone(pixelMap: image.PixelMap) {
  pixelMap.clone().then((clonedPixelMap: image.PixelMap) => {
    console.info('Succeeded in cloning the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to clone the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## cloneSync

```TypeScript
cloneSync(): PixelMap
```

Copies this PixelMap object. This API returns the result synchronously.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |
| [62980102](../errorcode-image.md#62980102-图片分配内存错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function cloneSync(pixelMap: image.PixelMap) {
  try {
    let clonedPixelMap: image.PixelMap = pixelMap.cloneSync();
    console.info('Succeeded in cloning the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to clone the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function cloneSync(pixelMap: image.PixelMap) {
  try {
    let clonedPixelMap: image.PixelMap = pixelMap.cloneSync();
    console.info('Succeeded in cloning the PixelMap.');
  } catch (err) {
    console.error(`Failed to clone the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## convertPixelFormat

```TypeScript
convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>
```

The method is used for the transformation of the image formats. Pixel data will be changed by calling this method.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetPixelFormat | [PixelMapFormat](arkts-image-image-pixelmapformat-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980274](../errorcode-image.md#62980274-图片转换失败) |
| [62980276](../errorcode-image.md#62980276-不支持图片转换目标类型) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function convertPixelFormat(pixelMap: image.PixelMap) {
  // 设置目标像素格式为NV12。
  let targetPixelFormat = image.PixelMapFormat.NV12;
  pixelMap.convertPixelFormat(targetPixelFormat).then(() => {
    console.info('Succeeded in converting pixel format.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to convert pixel format. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function convertPixelFormat(pixelMap: image.PixelMap) {
  // 设置目标像素格式为NV12。
  let targetPixelFormat = image.PixelMapFormat.NV12;
  pixelMap.convertPixelFormat(targetPixelFormat).then(() => {
    console.info('Succeeded in converting pixel format.');
  }).catch((err: Error) => {
    console.error(`Failed to convert pixel format. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(): Promise<PixelMap>
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMap](#extractalphapixelmap) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createAlphaPixelmap(pixelMap: image.PixelMap) {
  pixelMap.createAlphaPixelmap().then((alphaPixelMap: image.PixelMap) => {
    console.info('Succeeded in creating alpha PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function createAlphaPixelmap(pixelMap: image.PixelMap) {
  pixelMap.createAlphaPixelmap().then((alphaPixelMap: image.PixelMap) => {
    console.info('Succeeded in creating alpha PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createAlphaPixelmap(pixelMap: image.PixelMap) {
  pixelMap.createAlphaPixelmap((err: BusinessError, alphaPixelMap: image.PixelMap) => {
    if (err) {
      console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in creating alpha PixelMap.');
  });
}
```

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API returns the result through a callback.Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMap](#extractalphapixelmap) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | 是 |

**示例**

参见 [createAlphaPixelmap](#createalphapixelmap)

## createAlphaPixelmapSync

```TypeScript
createAlphaPixelmapSync(): PixelMap
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. This API returns the result synchronously. It is invalid for YUV images.Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMapSync](#extractalphapixelmapsync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createAlphaPixelmapSync(pixelMap: image.PixelMap) {
  try {
    let alphaPixelMap: image.PixelMap = pixelMap.createAlphaPixelmapSync();
    if (alphaPixelMap == undefined) {
      console.error(`Failed to create alpha PixelMap.`);
      return;
    }
    console.info('Succeeded in creating alpha PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function createAlphaPixelmapSync(pixelMap: image.PixelMap) {
  try {
    let pixelmap: image.PixelMap = pixelMap.createAlphaPixelmapSync();
    console.info('Succeeded in creating alpha PixelMap.');
  } catch (err) {
    console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## createCroppedAndScaledPixelMap

ArkTS-Dyn:
```TypeScript
createCroppedAndScaledPixelMap(region: Region, x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>
```

ArkTS-Sta:
```TypeScript
createCroppedAndScaledPixelMap(region: Region, x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>
```

Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the width and height, and anti-aliasing level. This API uses a promise to return the result.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md) | 是 |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600204](../errorcode-image.md#7600204-无效的区域) |
| [7600205](../errorcode-image.md#7600205-不支持的内存格式或像素格式) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createCroppedAndScaledPixelMap(pixelMap: image.PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: number = 2.0;
  const scaleY: number = 2.0;
  pixelMap.createCroppedAndScaledPixelMap(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH)
    .then((croppedAndScaled: image.PixelMap) => {
      console.info('Succeeded in creating cropped and scaled PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to create cropped and scaled PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function createCroppedAndScaledPixelMap(pixelMap: image.PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: double = 2.0;
  const scaleY: double = 2.0;
  pixelMap.createCroppedAndScaledPixelMap(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH)
    .then((croppedAndScaled: image.PixelMap) => {
      console.info('Succeeded in creating cropped and scaled PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to create cropped and scaled PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## createCroppedAndScaledPixelMapSync

ArkTS-Dyn:
```TypeScript
createCroppedAndScaledPixelMapSync(region: Region, x: number, y: number, level?: AntiAliasingLevel): PixelMap
```

ArkTS-Sta:
```TypeScript
createCroppedAndScaledPixelMapSync(region: Region, x: double, y: double, level?: AntiAliasingLevel): PixelMap
```

Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the width and height, and anti-aliasing level. This API returns the result synchronously.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md) | 是 |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600204](../errorcode-image.md#7600204-无效的区域) |
| [7600205](../errorcode-image.md#7600205-不支持的内存格式或像素格式) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createCroppedAndScaledPixelMapSync(pixelMap: image.PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: number = 2.0;
  const scaleY: number = 2.0;
  try {
    const croppedAndScaled = pixelMap.createCroppedAndScaledPixelMapSync(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH);
    console.info('Succeeded in creating cropped and scaled PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create cropped and scaled PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function createCroppedAndScaledPixelMapSync(pixelMap: image.PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: double = 2.0;
  const scaleY: double = 2.0;
  try {
    const croppedAndScaled = pixelMap.createCroppedAndScaledPixelMapSync(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH);
    console.info('Succeeded in creating cropped and scaled PixelMap.');
  } catch (err) {
    console.error(`Failed to create cropped and scaled PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## createScaledPixelMap

ArkTS-Dyn:
```TypeScript
createScaledPixelMap(x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>
```

ArkTS-Sta:
```TypeScript
createScaledPixelMap(x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>
```

Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. This API uses a promise to return the result.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createScaledPixelMap(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.0;
  pixelMap.createScaledPixelMap(scaleX, scaleY, image.AntiAliasingLevel.LOW).then((scaledPixelMap: image.PixelMap) => {
    console.info('Succeeded in creating scaled PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create scaled PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function createScaledPixelMap(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.0;
  pixelMap.createScaledPixelMap(scaleX, scaleY, image.AntiAliasingLevel.LOW).then((scaledPixelMap: image.PixelMap) => {
    console.info('Succeeded in creating scaled PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to create scaled PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## createScaledPixelMapSync

ArkTS-Dyn:
```TypeScript
createScaledPixelMapSync(x: number, y: number, level?: AntiAliasingLevel): PixelMap
```

ArkTS-Sta:
```TypeScript
createScaledPixelMapSync(x: double, y: double, level?: AntiAliasingLevel): PixelMap
```

Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. This API returns the result synchronously.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createScaledPixelMapSync(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.0;
  try {
    let scaledPixelMap = pixelMap.createScaledPixelMapSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
    console.info('Succeeded in creating scaled PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create scaled PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function createScaledPixelMapSync(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.0;
  try {
    let scaledPixelMap = pixelMap.createScaledPixelMapSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
    console.info('Succeeded in creating scaled PixelMap.');
  } catch (err) {
    console.error(`Failed to create scaled PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## crop

```TypeScript
crop(region: Region, callback: AsyncCallback<void>): void
```

Crops this image based on a given size. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [applyCrop](#applycrop) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function crop(pixelMap: image.PixelMap) {
  const region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  pixelMap.crop(region, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in cropping the PixelMap.");
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function crop(pixelMap: image.PixelMap) {
  const region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  pixelMap.crop(region).then(() => {
    console.info('Succeeded in cropping the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function crop(pixelMap: image.PixelMap) {
  const region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  pixelMap.crop(region).then(() => {
    console.info('Succeeded in cropping the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## crop

```TypeScript
crop(region: Region): Promise<void>
```

Crops a PixelMap based on a given size. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyCrop](#applycrop) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [crop](#crop)

## cropSync

```TypeScript
cropSync(region: Region): void
```

Crops this image based on a given size. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyCropSync](#applycropsync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function cropSync(pixelMap: image.PixelMap) {
  const region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  try {
    pixelMap.cropSync(region);
    console.info('Succeeded in cropping the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function cropSync(pixelMap: image.PixelMap) {
  const region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  try {
    pixelMap.cropSync(region);
    console.info('Succeeded in cropping the PixelMap.');
  } catch (err) {
    console.error(`Failed to crop the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## extractAlphaPixelMap

```TypeScript
extractAlphaPixelMap(): Promise<PixelMap>
```

Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600305](../errorcode-image.md#7600305-创建pixelmap失败) |
| [7600306](../errorcode-image.md#7600306-数据转换失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function extractAlphaPixelMap(pixelMap: image.PixelMap) {
  pixelMap.extractAlphaPixelMap()
    .then((alphaMap: image.PixelMap) => {
      console.info('Succeeded in creating alpha PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function extractAlphaPixelMap(pixelMap: image.PixelMap) {
  pixelMap.extractAlphaPixelMap()
    .then((alphaMap: image.PixelMap) => {
      console.info('Succeeded in creating alpha PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## extractAlphaPixelMapSync

```TypeScript
extractAlphaPixelMapSync(): PixelMap
```

Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600305](../errorcode-image.md#7600305-创建pixelmap失败) |
| [7600306](../errorcode-image.md#7600306-数据转换失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function extractAlphaPixelMapSync(pixelMap: image.PixelMap) {
  try {
    const alphaMap = pixelMap.extractAlphaPixelMapSync();
    console.info('Succeeded in creating alpha PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function extractAlphaPixelMapSync(pixelMap: image.PixelMap) {
  try {
    const alphaMap = pixelMap.extractAlphaPixelMapSync();
    console.info('Succeeded in creating alpha PixelMap.');
  } catch (err) {
    console.error(`Failed to create alpha PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void
```

Flips this image horizontally or vertically, or both. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [applyFlip](#applyflip) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function flip(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  pixelMap.flip(horizontal, vertical, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in flipping the PixelMap.");
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function flip(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  pixelMap.flip(horizontal, vertical).then(() => {
    console.info('Succeeded in flipping the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function flip(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  pixelMap.flip(horizontal, vertical).then(() => {
    console.info('Succeeded in flipping the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean): Promise<void>
```

Flips a PixelMap based on a given angle. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyFlip](#applyflip) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [flip](#flip)

## flipSync

```TypeScript
flipSync(horizontal: boolean, vertical: boolean): void
```

Flips this image horizontally or vertically, or both. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyFlipSync](#applyflipsync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function flipSync(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  try {
    pixelMap.flipSync(horizontal, vertical);
    console.info('Succeeded in flipping the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function flipSync(pixelMap: image.PixelMap) {
  const horizontal: boolean = true;
  const vertical: boolean = false;
  try {
    pixelMap.flipSync(horizontal, vertical);
    console.info('Succeeded in flipping the PixelMap.');
  } catch (err) {
    console.error(`Failed to flip the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## getBytesNumberPerRow

ArkTS-Dyn:
```TypeScript
getBytesNumberPerRow(): number
```

ArkTS-Sta:
```TypeScript
getBytesNumberPerRow(): int
```

Obtains the number of bytes per row of this image. Unit: bytes.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**示例**

ArkTS-Dyn示例：

```TypeScript
function getBytesNumberPerRow(pixelMap: image.PixelMap) {
  let rowBytes: number = pixelMap.getBytesNumberPerRow();
}
```

ArkTS-Sta示例：

```TypeScript
function getBytesNumberPerRow(pixelMap: image.PixelMap) {
  let rowBytes: int = pixelMap.getBytesNumberPerRow();
}
```

## getColorSpace

```TypeScript
getColorSpace(): colorSpaceManager.ColorSpaceManager
```

Obtains the color space of this image.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| colorSpaceManager.ColorSpaceManager |

**错误码：**

| 错误码ID |
| --- |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getColorSpace(pixelMap: image.PixelMap) {
  try {
    const csm = pixelMap.getColorSpace();
    console.info(`Succeeded in getting color space: ${csm.getColorSpaceName()}.`);
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to get color space. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function getColorSpace(pixelMap: image.PixelMap) {
  try {
    const csm = pixelMap.getColorSpace();
    console.info(`Succeeded in getting color space: ${csm.getColorSpaceName()}.`);
  } catch (err) {
    console.error(`Failed to get color space. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## getDensity

ArkTS-Dyn:
```TypeScript
getDensity(): number
```

ArkTS-Sta:
```TypeScript
getDensity(): int
```

Obtains the pixel density of this image. Unit: ppi (pixels/inch)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**示例**

ArkTS-Dyn示例：

```TypeScript
function getDensity(pixelMap: image.PixelMap) {
  let density: number = pixelMap.getDensity();
}
```

ArkTS-Sta示例：

```TypeScript
function getDensity(pixelMap: image.PixelMap) {
  let density: int = pixelMap.getDensity();
}
```

## getImageInfo

```TypeScript
getImageInfo(): Promise<ImageInfo>
```

Obtains the image information of a PixelMap. This API uses a promise to return the result.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

imageSourceApi.getImageInfo(0, (error: BusinessError, imageInfo: image.ImageInfo) => {
  if (error) {
    console.error(`Failed to obtain the image information.code is ${error.code}, message is ${error.message}`);
  } else {
    console.info('Succeeded in obtaining the image information.');
  }
})
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function GetImageInfoFunc(imageSource: image.ImageSource): void {
  try {
    imageSource.getImageInfo(0, (err: BusinessError | null, imageInfo: image.ImageInfo | undefined) => {
      if (err) {
        console.error(0x00000, 'GetImageInfoFunc', 'getImageInfo failed: ' + err);
      } else {
        console.info(0x00000, 'GetImageInfoFunc', 'getImageInfo success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'GetImageInfoFunc', 'GetImageInfoFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo(0, (error: BusinessError, imageInfo: image.ImageInfo) => {
    if (error) {
      console.error(`Failed to obtain the image information.code is ${error.code}, message is ${error.message}`);
    } else {
      console.info('Succeeded in obtaining the image information.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function GetImageInfoFunc(imageSource: image.ImageSource): void {
  try {
    imageSource.getImageInfo((err: BusinessError | null, imageInfo: image.ImageInfo | undefined) => {
      if (err) {
        console.error(0x00000, 'GetImageInfoFunc', 'getImageInfo failed: ' + err);
      } else {
        console.info(0x00000, 'GetImageInfoFunc', 'getImageInfo success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'GetImageInfoFunc', 'GetImageInfoFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo((err: BusinessError, imageInfo: image.ImageInfo) => {
    if (err) {
      console.error(`Failed to obtain the image information.code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('Succeeded in obtaining the image information.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
async function GetImageInfoFunc(imageSource: image.ImageSource): Promise<void> {
  try {
    let imageInfo = await imageSource.getImageInfo(0);
    console.info(0x00000, 'GetImageInfoFunc', 'getImageInfo success!');
  } catch (err) {
    console.error(0x00000, 'GetImageInfoFunc', 'GetImageInfoFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getImageInfo(pixelMap: image.PixelMap) {
  pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
    console.info(`Succeeded in obtaining information of the PixelMap with size ${imageInfo.size} and pixel format ${imageInfo.pixelFormat}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to obtain information of the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function getImageInfo(pixelMap: image.PixelMap) {
  pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
    console.info(`Succeeded in obtaining information of the PixelMap with size ${imageInfo.size} and pixel format ${imageInfo.pixelFormat}.`);
  }).catch((err: Error) => {
    console.error(`Failed to obtain information of the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getImageInfo(pixelMap: image.PixelMap) {
  pixelMap.getImageInfo((err: BusinessError, imageInfo: image.ImageInfo) => {
    if (err) {
      console.error(`Failed to obtain information of the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in obtaining information of the PixelMap with size ${imageInfo.size} and pixel format ${imageInfo.pixelFormat}.`);
  });
}
```

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo>): void
```

Obtains the image information. This API uses an asynchronous callback to return the result.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | 是 |

**示例**

参见 [getImageInfo](#getimageinfo)

## getImageInfoSync

```TypeScript
getImageInfoSync(): ImageInfo
```

Obtains the image information. This API returns the result synchronously.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo(0)
    .then((imageInfo: image.ImageInfo) => {
      console.info('Succeeded in obtaining the image information.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to obtain the image information.code is ${error.code}, message is ${error.message}`);
    })
}
```

ArkTS-Sta示例：

```TypeScript
function GetImageInfoSyncFunc(imageSource: image.ImageSource) {
  try {
    let imageInfo = imageSource.getImageInfoSync(0);
    console.info(0x00000, 'GetImageInfoSyncFunc', 'getImageInfoSync success!');
  } catch (err) {
    console.error(0x00000, 'GetImageInfoSyncFunc', 'GetImageInfoSyncFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getImageInfoSync(pixelMap: image.PixelMap) {
  try {
    let imageInfo: image.ImageInfo = pixelMap.getImageInfoSync();
    console.info(`Succeeded in obtaining information of the PixelMap with size ${imageInfo.size} and pixel format ${imageInfo.pixelFormat}.`);
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to obtain information of the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function getImageInfoSync(pixelMap: image.PixelMap) {
  try {
    let imageInfo: image.ImageInfo = pixelMap.getImageInfoSync();
    console.info(`Succeeded in obtaining information of the PixelMap with size ${imageInfo.size} and pixel format ${imageInfo.pixelFormat}.`);
  } catch (err) {
    console.error(`Failed to obtain information of the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## getMetadata

```TypeScript
getMetadata(key: HdrMetadataKey): HdrMetadataValue
```

Obtains the value of the metadata with a given key in this PixelMap.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [HdrMetadataValue](arkts-image-image-hdrmetadatavalue-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |
| [62980173](../errorcode-image.md#62980173-dma内存空间错误) |
| [62980302](../errorcode-image.md#62980302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
async function GetAuxPictureObjMetadata(auxPictureObj: image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let auxPictureObjMetaData: image.Metadata | null = await auxPictureObj.getMetadata(metadataType);
    if (auxPictureObjMetaData != null) {
      console.info('Succeeded in getting AuxPictureObj Metadata.' );
    } else {
      console.error('Failed to get AuxPictureObj Metadata.');
    }
  } else {
    console.error('Get AuxPictureObj is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function GetMetadataFunc(auxPicture: image.AuxiliaryPicture): void {
  try {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let metadata = auxPicture.getMetadata(metadataType);
    if (metadata != null) {
      console.info(0x00000, 'GetMetadataFunc', 'getMetadata success!');
    }
  } catch (err) {
    console.error(0x00000, 'GetMetadataFunc', 'GetMetadataFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function GetMetadata(img : image.Image) {
  try {
    let staticMetadata = img.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
    console.info(`getMetadata:${staticMetadata}`);
  } catch (err) {
    console.error('Failed to getMetadata.' + err);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetMetadata(img : image.Image) {
  try {
    let staticMetadata = img.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
    if (staticMetadata) {
      console.info(`GetMetadata:${staticMetadata}`);
    }
  } catch (err) {
    console.error('GetMetadata failed' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function GetPictureObjMetadataProperties(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let pictureObjMetaData: image.Metadata = await pictureObj.getMetadata(metadataType);
    if (pictureObjMetaData != null) {
      console.info('Succeeded in getting picture metadata.');
    } else {
      console.error('Failed to get picture metadata.');
    }
  } else {
    console.error(" pictureObj is null");
  }
}
```

ArkTS-Sta示例：

```TypeScript
function GetMetadataFunc(picture: image.Picture): void {
  try {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let metaData = await picture.getMetadata(metadataType);
    console.info(0x00000, 'SetMetadataFunc', 'getMetadata success!');
  } catch (err) {
    console.error(0x00000, 'SetMetadataFunc', 'SetMetadataFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getMetadata(context: Context) {
  // 此处'app.media.startIcon'需要替换为本地HDR图片。
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelMap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelMap != undefined) {
    console.info('Succeeded in creating the PixelMap object.');
    try {
      let staticMetadata = pixelMap.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
      console.info('Succeeded in getting the metadata.');
    } catch (e) {
      const err = e as BusinessError;
      console.error(`Failed to get the metadata. Code: ${err.code}, message: ${err.message}`);
    }
  } else {
    console.error('Failed to create the PixelMap.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function getMetadata(context: Context) {
  // 此处'app.media.startIcon'需要替换为本地HDR图片。
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelMap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelMap != undefined) {
    console.info('Succeeded in creating the PixelMap object.');
    try {
      let staticMetadata = pixelMap.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
      console.info('Succeeded in getting the metadata.');
    } catch (err) {
      console.error(`Failed to get the metadata. Code: ${err.code}, message: ${err.message}`);
    }
  } else {
    console.error('Failed to create the PixelMap.');
  }
}
```

## getPixelBytesNumber

ArkTS-Dyn:
```TypeScript
getPixelBytesNumber(): number
```

ArkTS-Sta:
```TypeScript
getPixelBytesNumber(): int
```

Obtains the total number of bytes of this image. Unit: bytes.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**示例**

ArkTS-Dyn示例：

```TypeScript
function getPixelBytesNumber(pixelMap: image.PixelMap) {
  let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
}
```

ArkTS-Sta示例：

```TypeScript
function getPixelBytesNumber(pixelMap: image.PixelMap) {
  let pixelBytesNumber: int = pixelMap.getPixelBytesNumber();
}
```

## getUniqueId

ArkTS-Dyn:
```TypeScript
getUniqueId(): number
```

ArkTS-Sta:
```TypeScript
getUniqueId(): int
```

Obtains the unique ID of this PixelMap.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getUniqueId(pixelMap: image.PixelMap) {
  try {
    const uniqueId: number = pixelMap.getUniqueId();
    console.info(`Succeeded in getting the unique ID: ${uniqueId}.`);
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to get the unique ID. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function getUniqueId(pixelMap: image.PixelMap) {
  try {
    const uniqueId: int = pixelMap.getUniqueId();
    console.info(`Succeeded in getting the unique ID: ${uniqueId}.`);
  } catch (err) {
    console.error(`Failed to get the unique ID. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## isReleased

```TypeScript
isReleased(): boolean
```

Checks whether this PixelMap object is released. If released, any attempt to access the internal data of this object will fail.

> **NOTE：**&gt;
> Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
> by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
async function isReleased(pixelMap: image.PixelMap) { // 未释放的PixelMap。
  pixelMap.isReleased(); // 返回false。
  await pixelMap.release();
  pixelMap.isReleased(); // 返回true。
}
```

## marshalling

```TypeScript
marshalling(sequence: rpc.MessageSequence): void
```

Marshals this PixelMap object and writes it to a MessageSequence object.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequence | rpc.MessageSequence | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  picture: image.Picture | null = null;
  constructor(conPicture: image.Picture) {
    this.picture = conPicture;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    if(this.picture != null) {
      this.picture.marshalling(messageSequence);
      console.info('Succeeded in marshalling a picture.');
      return true;
    } else {
      console.error('Failed to marshall a picture.');
      return false;
    }
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    this.picture = image.createPictureFromParcel(messageSequence);
    this.picture.getMainPixelmap().getImageInfo().then((imageInfo : image.ImageInfo) => {
      console.info(`Succeeded in unmarshalling a picture and getting main PixelMap information. Height: ${imageInfo.size.height}, width: ${imageInfo.size.width}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to unmarshall a picture. Code: ${error.code}, message: ${error.message}.`);
    });
    return true;
  }
}

async function Marshalling_UnMarshalling(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let parcelable: MySequence = new MySequence(pictureObj);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    // 序列化。
    data.writeParcelable(parcelable);
    let ret: MySequence = new MySequence(pictureObj);
    // 反序列化。
    data.readParcelable(ret);
  } else {
    console.error('Picture object is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
import { resourceManager } from '@kit.LocalizationKit';
import { rpc } from '@kit.IPCKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
if (context != undefined) {
  MarshallingUnMarshallingFunc(context);
}

class MySequence implements rpc.Parcelable {
  picture_: image.Picture;

  constructor(conPicture: image.Picture) {
    this.picture_ = conPicture;
  }

  marshalling(messageSequence: rpc.MessageSequence): boolean {
    this.picture_.marshalling(messageSequence);
    console.info(0x00000, 'MySequence', 'marshalling success!');
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    let picture: image.Picture = image.createPictureFromParcel(messageSequence)
    this.picture_ = picture;
    console.info(0x00000, 'MySequence', 'unmarshalling success!');
    return true;
  }
}

function MarshallingUnMarshallingFunc(context: common.UIAbilityContext): void {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test_image.jpg");
  let opts: image.SourceOptions = { sourceDensity: 98 };
  try {
    let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, opts);
    let pixelMap: image.PixelMap = await imageSource.createPixelMap();
    let picture: image.Picture = image.createPicture(pixelMap);
    if (picture != null || picture != undefined) {
      let parcelable: MySequence = new MySequence(picture);
      let data: rpc.MessageSequence = rpc.MessageSequence.create();
      // 序列化。
      data.writeParcelable(parcelable);

      let ret: MySequence = new MySequence(picture);
      // 反序列化。
      data.readParcelable(ret);
    } else {
      console.error(0x00000, 'MarshallingUnMarshallingFunc', 'picture is null!');
    }
  } catch (err) {
    console.error(0x00000, 'MarshallingUnMarshallingFunc', 'MarshallingUnMarshallingFunc failed: ' + err);
  }
}
```

```TypeScript
// EntryAbility.ets
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixelMap: image.PixelMap;
  constructor(pixelMap: image.PixelMap) {
    this.pixelMap = pixelMap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixelMap.marshalling(messageSequence);
    console.info('Marshalled the PixelMap.');
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height: 4, width: 6 }}).then((pixelParcel: image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: image.PixelMap) => {
        this.pixelMap = pixelMap;
        pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
          console.info(`Unmarshalled information: height = ${imageInfo.size.height}, width = ${imageInfo.size.width}.`);
        });
      });
    });
    return true;
  }
}

async function marshal() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.BGRA_8888,
    size: { height: 4, width: 6 },
    alphaType: image.AlphaType.UNPREMUL
  };
  let pixelMap: image.PixelMap | undefined = await image.createPixelMap(color, opts);
  if (pixelMap != undefined) {
    // 序列化。
    let parcelable: MySequence = new MySequence(pixelMap);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // 反序列化rpc获取到data。
    let seq: MySequence = new MySequence(pixelMap);
    data.readParcelable(seq);
  }
}
```

## opacity

ArkTS-Dyn:
```TypeScript
opacity(rate: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
opacity(rate: double, callback: AsyncCallback<void>): void
```

Sets an opacity rate for this image. This API uses an asynchronous callback to return the result. It is invalid for YUV images.Starting from API 26.0.0, it is recommended to use [setOpacity](#setopacity) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function opacity(pixelMap: image.PixelMap) {
  const rate: number = 0.5;
  pixelMap.opacity(rate, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in setting opacity.");
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function opacity(pixelMap: image.PixelMap) {
  const rate: double = 0.5;
  pixelMap.opacity(rate, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in setting opacity.");
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function opacity(pixelMap: image.PixelMap) {
  const rate: number = 0.5;
  pixelMap.opacity(rate).then(() => {
    console.info('Succeeded in setting opacity.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function opacity(pixelMap: image.PixelMap) {
  const rate: double = 0.5;
  pixelMap.opacity(rate).then(() => {
    console.info('Succeeded in setting opacity.');
  }).catch((err: Error) => {
    console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## opacity

ArkTS-Dyn:
```TypeScript
opacity(rate: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
opacity(rate: double): Promise<void>
```

Sets an opacity rate for this image. It is invalid for YUV images. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [setOpacity](#setopacity) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [opacity](#opacity)

## opacitySync

ArkTS-Dyn:
```TypeScript
opacitySync(rate: number): void
```

ArkTS-Sta:
```TypeScript
opacitySync(rate: double): void
```

Sets an opacity rate for this image. This API returns the result synchronously. It is invalid for YUV images.Starting from API 26.0.0, it is recommended to use [setOpacitySync](#setopacitysync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function opacitySync(pixelMap: image.PixelMap) {
  const rate: number = 0.5;
  try {
    pixelMap.opacitySync(rate);
    console.info('Succeeded in setting opacity.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function opacitySync(pixelMap: image.PixelMap) {
  const rate: double = 0.5;
  try {
    pixelMap.opacitySync(rate);
    console.info('Succeeded in setting opacity.');
  } catch (err) {
    console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## readAllPixelsToBuffer

```TypeScript
readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads all the pixel data from the PixelMap and writes the data to a buffer. The resulting data will be in the same pixel format as the PixelMap.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readAllPixelsToBuffer(pixelMap: image.PixelMap) {
  const readBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());

  pixelMap.readAllPixelsToBuffer(readBuffer)
    .then(() => {
      console.info('Succeeded in reading pixel data from the PixelMap to readBuffer.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function readAllPixelsToBuffer(pixelMap: image.PixelMap) {
  const readBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());

  pixelMap.readAllPixelsToBuffer(readBuffer)
    .then(() => {
      console.info('Succeeded in reading pixel data from the PixelMap to readBuffer.');
    })
    .catch((err: Error) => {
      console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## readAllPixelsToBufferSync

```TypeScript
readAllPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads all the pixel data from the PixelMap and writes the data to a buffer. The resulting data will be in the same pixel format as the PixelMap.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readAllPixelsToBufferSync(pixelMap: image.PixelMap) {
  const readBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());

  try {
    pixelMap.readAllPixelsToBufferSync(readBuffer);
    console.info('Succeeded in reading pixel data from the PixelMap to readBuffer.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function readAllPixelsToBufferSync(pixelMap: image.PixelMap) {
  const readBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());

  try {
    pixelMap.readAllPixelsToBufferSync(readBuffer);
    console.info('Succeeded in reading pixel data from the PixelMap to readBuffer.');
  } catch (err) {
    console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## readPixels

```TypeScript
readPixels(area: PositionArea): Promise<void>
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md).pixels buffer. This API uses a promise to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)Starting from API 26.0.0, it is recommended to use [readPixelsToArea](#readpixelstoarea) instead for better exception handling capabilities.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readPixelsRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  pixelMap.readPixels(area).then(() => {
    console.info('Succeeded in reading the image data in the area from the specified area.');
    console.info('BGRA data: ', new Uint8Array(area.pixels));
  }).catch((err: BusinessError) => {
    console.error(`Failed to read the image data from the specified area. Code: ${err.code}, message: ${err.message}`);
  });
}

function readPixelsYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  pixelMap.readPixels(area).then(() => {
    console.info('Succeeded in reading the image data in the area from the specified area.');
    console.info('YUV data: ', new Uint8Array(area.pixels));
  }).catch((err: BusinessError) => {
    console.error(`Failed to read the image data from the specified area. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function readPixelsRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  pixelMap.readPixels(area).then(() => {
    console.info('Succeeded in reading the image data in the area from the specified area.');
    console.info('BGRA data: ', new Uint8Array(area.pixels));
  }).catch((err: Error) => {
    console.error(`Failed to read the image data from the specified area. Code: ${err.code}, message: ${err.message}`);
  });
}

function readPixelsYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  pixelMap.readPixels(area).then(() => {
    console.info('Succeeded in reading the image data in the area from the specified area.');
    console.info('YUV data: ', new Uint8Array(area.pixels));
  }).catch((err: Error) => {
    console.error(`Failed to read the image data from the specified area. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readPixelsRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  pixelMap.readPixels(area, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to read the image data from the specified area. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in reading the image data from the specified area.');
    console.info('BGRA data: ', new Uint8Array(area.pixels));
  });
}

function readPixelsYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6), // 6为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  pixelMap.readPixels(area, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to read the image data from the specified area. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in reading the image data from the specified area.');
    console.info('YUV data: ', new Uint8Array(area.pixels));
  });
}
```

## readPixels

```TypeScript
readPixels(area: PositionArea, callback: AsyncCallback<void>): void
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md).pixels buffer. This API uses an asynchronous callback to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)Starting from API 26.0.0, it is recommended to use [readPixelsToArea](#readpixelstoarea) instead for better exception handling capabilities.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

参见 [readPixels](#readpixels)

## readPixelsSync

```TypeScript
readPixelsSync(area: PositionArea): void
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md).pixels buffer. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [readPixelsToAreaSync](#readpixelstoareasync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readPixelsSync(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  try {
    pixelMap.readPixelsSync(area);
    console.info('Succeeded in reading the image data from the specified area.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to read the image data from the specified area. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function readPixelsSync(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  try {
    pixelMap.readPixelsSync(area);
    console.info('Succeeded in reading the image data from the specified area.');
  } catch (err) {
    console.error(`Failed to read the image data from the specified area. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## readPixelsToArea

```TypeScript
readPixelsToArea(area: PositionArea): Promise<void>
```

Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readPixelsToAreaRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(24), // 24为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 4。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };

  pixelMap.readPixelsToArea(area)
    .then(() => {
      console.info('Succeeded in reading pixel data from the specified area of the PixelMap to area.pixels.');
      console.info('BGRA data: ', new Uint8Array(area.pixels));
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}

function readPixelsToAreaYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(9), // 9为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 2, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 1（1倍Y分量）。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };

  pixelMap.readPixelsToArea(area)
    .then(() => {
      console.info('Succeeded in reading pixel data from the specified area of the PixelMap to area.pixels.');
      console.info('YUV data: ', new Uint8Array(area.pixels));
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function readPixelsToAreaRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(24), // 24为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 4。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };

  pixelMap.readPixelsToArea(area)
    .then(() => {
      console.info('Succeeded in reading pixel data from the specified area of the PixelMap to area.pixels.');
      console.info('BGRA data: ', new Uint8Array(area.pixels));
    })
    .catch((err: Error) => {
      console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}

function readPixelsToAreaYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(9), // 9为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 2, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 1（1倍Y分量）。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };

  pixelMap.readPixelsToArea(area)
    .then(() => {
      console.info('Succeeded in reading pixel data from the specified area of the PixelMap to area.pixels.');
      console.info('YUV data: ', new Uint8Array(area.pixels));
    })
    .catch((err: Error) => {
      console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## readPixelsToAreaSync

```TypeScript
readPixelsToAreaSync(area: PositionArea): void
```

Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readPixelsToAreaSyncRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(24), // 24为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 4。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };

  try {
    pixelMap.readPixelsToAreaSync(area);
    console.info('Succeeded in reading pixel data from the specified area of the PixelMap to area.pixels.');
    console.info('BGRA data: ', new Uint8Array(area.pixels));
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}

function readPixelsToAreaSyncYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(9), // 9为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 2, // 跨距，即每行像素所占的字节数，在没有行末填充的字节情况下取值为：width * 1（1倍Y分量）。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };

  try {
    pixelMap.readPixelsToAreaSync(area);
    console.info('Succeeded in reading pixel data from the specified area of the PixelMap to area.pixels.');
    console.info('YUV data: ', new Uint8Array(area.pixels));
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function readPixelsToAreaSyncRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(24), // 24为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 4。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };

  try {
    pixelMap.readPixelsToAreaSync(area);
    console.info('Succeeded in reading pixel data from the specified area of the PixelMap to area.pixels.');
    console.info('BGRA data: ', new Uint8Array(area.pixels));
  } catch (err) {
    console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}

function readPixelsToAreaSyncYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(9), // 9为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 2, // 跨距，即每行像素所占的字节数，在没有行末填充的字节情况下取值为：width * 1（1倍Y分量）。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };

  try {
    pixelMap.readPixelsToAreaSync(area);
    console.info('Succeeded in reading pixel data from the specified area of the PixelMap to area.pixels.');
    console.info('YUV data: ', new Uint8Array(area.pixels));
  } catch (err) {
    console.error(`Failed to read pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [readAllPixelsToBuffer](#readallpixelstobuffer) instead for better exception handling capabilities.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // 需要支持hdr的图片。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
  if(auxPictureObj != null) {
    await auxPictureObj.readPixelsToBuffer().then((pixelsBuffer: ArrayBuffer) => {
      console.info('Succeeded in reading pixels to buffer.' );
    }).catch((error: BusinessError) => {
      console.error(`Failed to read pixels to buffer. error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObj is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function ReadPixelsToBufferFunc(auxPicture: image.AuxiliaryPicture): void {
  try {
    let auxBuffer = auxPicture.readPixelsToBuffer();
    console.info(0x00000, 'ReadPixelsToBufferFunc', 'readPixelsToBuffer success!');
  } catch (err) {
    console.error(0x00000, 'ReadPixelsToBufferFunc', 'ReadPixelsToBufferFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readPixelsToBuffer(pixelMap: image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  pixelMap.readPixelsToBuffer(readBuffer).then(() => {
    console.info('Succeeded in reading image pixel data.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to read image pixel data. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function readPixelsToBuffer(pixelMap: image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  pixelMap.readPixelsToBuffer(readBuffer).then(() => {
    console.info('Succeeded in reading image pixel data.');
  }).catch((err: Error) => {
    console.error(`Failed to read image pixel data. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readPixelsToBuffer(pixelMap: image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  pixelMap.readPixelsToBuffer(readBuffer, (err: BusinessError, res: void) => {
    if (err) {
      console.error(`Failed to read image pixel data. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in reading image pixel data.');
  });
}
```

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [readAllPixelsToBuffer](#readallpixelstobuffer) instead for better exception handling capabilities.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

参见 [readPixelsToBuffer](#readpixelstobuffer)

## readPixelsToBufferSync

```TypeScript
readPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [readAllPixelsToBufferSync](#readallpixelstobuffersync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function readPixelsToBufferSync(pixelMap: image.PixelMap) {
  const readBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  try {
    pixelMap.readPixelsToBufferSync(readBuffer);
    console.info('Succeeded in reading image pixel data.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to read image pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function readPixelsToBufferSync(pixelMap: image.PixelMap) {
  const readBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  try {
    pixelMap.readPixelsToBufferSync(readBuffer);
    console.info('Succeeded in reading image pixel data.');
  } catch (err) {
    console.error(`Failed to read image pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will fail. This API uses an asynchronous callback to return the result. Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

> **NOTE：**&gt;
> Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
> by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
async function Release(auxPictureObj: image.AuxiliaryPicture) {
  let funcName = "Release";
  if (auxPictureObj != null) {
    auxPictureObj.release();
    if (auxPictureObj.getType() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
if (context != undefined) {
  let auxPicture: image.AuxiliaryPicture | null = GetAuxiliaryPicture(context)
  if (auxPicture != null) {
    auxPicture.release();
  } else {
    console.error(0x00000, 'GetAuxiliaryPicture', 'auxPicture is null!');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image instance.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@ohos.base';

function ReleaseFunc(img: image.Image): void {
  try {
    img.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    })
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release().then(() => {
    console.info('Succeeded in releasing the image instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image instance.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(img: image.Image): void {
  try {
    await img.release()
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the creator.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing creator.');
    }
  });
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(creator: image.ImageCreator): void {
  try {
    creator.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    })
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release().then(() => {
    console.info('Succeeded in releasing creator.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the creator.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(creator: image.ImageCreator): void {
  try {
    await creator.release();
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release((err: BusinessError)=>{
    if (err) {
      console.error(`Failed to release image packaging.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing image packaging.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(): void {
  try {
    let imagePacker: image.ImagePacker = image.createImagePacker();
    imagePacker.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release().then(() => {
    console.info('Succeeded in releasing image packaging.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release image packaging.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
async function ReleaseFunc(): Promise<void> {
  try {
    let imagePacker: image.ImagePacker = image.createImagePacker();
    await imagePacker.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the receiver.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the receiver.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    receiver.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'ReleaseFunc success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release().then(() => {
    console.info('Succeeded in releasing the receiver.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the receiver.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    await receiver.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image source instance.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(imageSource: image.ImageSource): void {
  try {
    imageSource.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release().then(() => {
    console.info('Succeeded in releasing the image source instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image source instance.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
async function ReleaseFunc(imageSource: image.ImageSource): Promise<void> {
  try {
    await imageSource.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function Release(pictureObj : image.Picture) {
  let funcName = "Release";
  if (pictureObj != null) {
    pictureObj.release();
    if (pictureObj.getMainPixelmap() == null) {
      console.info(funcName, 'Succeeded in releasing a picture.');
    } else {
      console.error(funcName, 'Failed to release a picture.');
    }
  } else {
    console.error('Picture object is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(picture: image.Picture): void {
  try {
    picture.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function release(pixelMap: image.PixelMap) {
  pixelMap.release().then(() => {
    console.info('Succeeded in releasing the PixelMap object.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function release(pixelMap: image.PixelMap) {
  pixelMap.release().then(() => {
    console.info('Succeeded in releasing the PixelMap object.');
  }).catch((err: Error) => {
    console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function release(pixelMap: image.PixelMap) {
  pixelMap.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in releasing the PixelMap object.');
  });
}
```

## release

```TypeScript
release(): Promise<void>
```

Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will fail. This API uses a promise to return the result. Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

> **NOTE：**&gt;
> Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
> by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [release](#release)

## rotate

ArkTS-Dyn:
```TypeScript
rotate(angle: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
rotate(angle: double, callback: AsyncCallback<void>): void
```

Rotates this image based on a given angle. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [applyRotate](#applyrotate) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function rotate(pixelMap: image.PixelMap) {
  const angle: number = 90.0;
  pixelMap.rotate(angle, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in rotating the PixelMap.");
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function rotate(pixelMap: image.PixelMap) {
  const angle: double = 90.0;
  pixelMap.rotate(angle, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in rotating the PixelMap.");
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function rotate(pixelMap: image.PixelMap) {
  const angle: number = 90.0;
  pixelMap.rotate(angle).then(() => {
    console.info('Succeeded in rotating the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function rotate(pixelMap: image.PixelMap) {
  const angle: double = 90.0;
  pixelMap.rotate(angle).then(() => {
    console.info('Succeeded in rotating the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## rotate

ArkTS-Dyn:
```TypeScript
rotate(angle: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
rotate(angle: double): Promise<void>
```

Rotates a PixelMap based on a given angle. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyRotate](#applyrotate) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [rotate](#rotate)

## rotateSync

ArkTS-Dyn:
```TypeScript
rotateSync(angle: number): void
```

ArkTS-Sta:
```TypeScript
rotateSync(angle: double): void
```

Rotates this image based on a given angle. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyRotateSync](#applyrotatesync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function rotateSync(pixelMap: image.PixelMap) {
  const angle: number = 90.0;
  try {
    pixelMap.rotateSync(angle);
    console.info('Succeeded in rotating the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function rotateSync(pixelMap: image.PixelMap) {
  const angle: double = 90.0;
  try {
    pixelMap.rotateSync(angle);
    console.info('Succeeded in rotating the PixelMap.');
  } catch (err) {
    console.error(`Failed to rotate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## scale

ArkTS-Dyn:
```TypeScript
scale(x: number, y: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
scale(x: double, y: double, callback: AsyncCallback<void>): void
```

Scales this image based on the scale factors of the width and height. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [applyScale](#applyscale) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function scale(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.0;
  pixelMap.scale(scaleX, scaleY, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in scaling the PixelMap.");
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function scale(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.0;
  pixelMap.scale(scaleX, scaleY, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in scaling the PixelMap.");
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function scale(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.0;
  pixelMap.scale(scaleX, scaleY).then(() => {
    console.info('Succeeded in scaling the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function scale(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.0;
  pixelMap.scale(scaleX, scaleY).then(() => {
    console.info('Succeeded in scaling the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function scaleSync(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.0;
  pixelMap.scale(scaleX, scaleY, image.AntiAliasingLevel.LOW).then(() => {
    console.info('Succeeded in scaling the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function scaleSync(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.0;
  pixelMap.scale(scaleX, scaleY, image.AntiAliasingLevel.LOW).then(() => {
    console.info('Succeeded in scaling the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## scale

ArkTS-Dyn:
```TypeScript
scale(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
scale(x: double, y: double): Promise<void>
```

Scales this image based on the scale factors of the width and height. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyScale](#applyscale) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [scale](#scale)

## scale

ArkTS-Dyn:
```TypeScript
scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>
```

ArkTS-Sta:
```TypeScript
scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>
```

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyScale](#applyscale) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

参见 [scale](#scale)

## scaleSync

ArkTS-Dyn:
```TypeScript
scaleSync(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
scaleSync(x: double, y: double): void
```

Scales this image based on the scale factors of the width and height. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyScaleSync](#applyscalesync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function scaleSync(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.0;
  try {
    pixelMap.scaleSync(scaleX, scaleY);
    console.info('Succeeded in scaling the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function scaleSync(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.0;
  try {
    pixelMap.scaleSync(scaleX, scaleY);
    console.info('Succeeded in scaling the PixelMap.');
  } catch (err) {
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function scaleSync(pixelMap: image.PixelMap) {
  const scaleX: number = 2.0;
  const scaleY: number = 1.0;
  try {
    pixelMap.scaleSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
    console.info('Succeeded in scaling the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function scaleSync(pixelMap: image.PixelMap) {
  const scaleX: double = 2.0;
  const scaleY: double = 1.0;
  try {
    pixelMap.scaleSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
    console.info('Succeeded in scaling the PixelMap.');
  } catch (err) {
    console.error(`Failed to scale the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## scaleSync

ArkTS-Dyn:
```TypeScript
scaleSync(x: number, y: number, level: AntiAliasingLevel): void
```

ArkTS-Sta:
```TypeScript
scaleSync(x: double, y: double, level: AntiAliasingLevel): void
```

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyScaleSync](#applyscalesync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

参见 [scaleSync](#scalesync)

## setColorSpace

```TypeScript
setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void
```

Set color space of pixel map.This method is only used to set the colorspace property of pixelmap, while all pixel data remains the same after calling this method. If you want to change colorspace for all pixels, use method {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager)} or {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager, AsyncCallback&lt;void&gt;)}.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpaceManager | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function setColorSpace(pixelMap: image.PixelMap) {
  const colorSpaceName = colorSpaceManager.ColorSpace.SRGB;
  const csm: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  try {
    pixelMap.setColorSpace(csm);
    console.info('Succeeded in setting color space.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to set color space. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function setColorSpace(pixelMap: image.PixelMap) {
  const colorSpaceName = colorSpaceManager.ColorSpace.SRGB;
  const csm: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  try {
    pixelMap.setColorSpace(csm);
    console.info('Succeeded in setting color space.');
  } catch (err) {
    console.error(`Failed to set color space. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## setMemoryNameSync

```TypeScript
setMemoryNameSync(name: string): void
```

Sets a memory name for this PixelMap.

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |
| [62980286](../errorcode-image.md#62980286-pixelmap设置内存标识符失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setMemoryNameSync(pixelMap: image.PixelMap) {
  try {
    pixelMap.setMemoryNameSync("PixelMapName Test");
    console.info('Succeeded in setting memory name.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to set memory name. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function setMemoryNameSync(pixelMap: image.PixelMap) {
  try {
    pixelMap.setMemoryNameSync("PixelMapName Test");
    console.info('Succeeded in setting memory name.');
  } catch (err) {
    console.error(`Failed to set memory name. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## setMetadata

```TypeScript
setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>
```

Sets the value for the metadata with a given key in this PixelMap. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md) | 是 |
| value | [HdrMetadataValue](arkts-image-image-hdrmetadatavalue-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |
| [62980173](../errorcode-image.md#62980173-dma内存空间错误) |
| [62980302](../errorcode-image.md#62980302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetAuxPictureObjMetadata(exifContext: Context, auxPictureObj: image.AuxiliaryPicture) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg");// 图片包含exif metadata。
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Succeeded in creating picture.');
  } else {
    console.error('Failed to create picture.');
  }

  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    auxPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Succeeded in setting metadata.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata. error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObjMetaData is null');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';

function SetMetadataFunc(auxPicture: image.AuxiliaryPicture, context: common.UIAbilityContext): void {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr_exif_image.jpg");
  let opts: image.SourceOptions = { sourceDensity: 98 };
  try {
    let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, opts);
    let pixelMap: image.PixelMap = await imageSource.createPixelMap(); // 解码图片获取PixelMap。
    let picture: image.Picture = image.createPicture(pixelMap); // 创建Picture对象以获取元数据。
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let metadata: image.Metadata | null = await picture.getMetadata(metadataType); // 从Picture获取EXIF元数据。
    if (metadata != null) {
       auxPicture.setMetadata(metadataType, metadata); // 将元数据设置到辅助图对象。
       console.info(0x00000, 'SetMetadataFunc', 'setMetadata success!');
    }
  } catch (err) {
    console.error(0x00000, 'SetMetadataFunc', 'SetMetadataFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetPictureObjMetadata(exifContext: Context) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg");// 含有exif metadata的图片。
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Succeeded in creating picture.');
  } else {
    console.error('Failed to create picture.');
  }

  if (exifPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    exifPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Succeeded in setting metadata.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata. error.code: ${error.code} ,error.message: ${error.message}`);
    });
  } else {
    console.error('exifPictureObj is null');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function SetMetadataFunc(picture: image.Picture): void {
  try {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let metaData: image.Metadata = await picture.getMetadata(metadataType);
    await picture.setMetadata(metadataType, metaData);
    console.info(0x00000, 'SetMetadataFunc', 'setMetadata success!');
  } catch (err) {
    console.error(0x00000, 'SetMetadataFunc', 'SetMetadataFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setMetadata(pixelMap: image.PixelMap) { // 入参pixelMap内存类型需为DMA_ALLOC内存类型，其创建方法请参考上方说明。
  let staticMetadata: image.HdrStaticMetadata = {
    displayPrimariesX: [1.1, 1.1, 1.1],
    displayPrimariesY: [1.2, 1.2, 1.2],
    whitePointX: 1.1,
    whitePointY: 1.2,
    maxLuminance: 2.1,
    minLuminance: 1.0,
    maxContentLightLevel: 2.1,
    maxFrameAverageLightLevel: 2.1,
  };
  pixelMap.setMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA, staticMetadata).then(() => {
    console.info('Succeeded in setting the metadata.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the metadata. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function setMetadata(pixelMap: image.PixelMap) { // 入参pixelMap内存类型需为DMA_ALLOC内存类型，其创建方法请参考上方说明。
  let staticMetadata: image.HdrStaticMetadata = {
    displayPrimariesX: [1.1, 1.1, 1.1],
    displayPrimariesY: [1.2, 1.2, 1.2],
    whitePointX: 1.1,
    whitePointY: 1.2,
    maxLuminance: 2.1,
    minLuminance: 1.0,
    maxContentLightLevel: 2.1,
    maxFrameAverageLightLevel: 2.1,
  };
  pixelMap.setMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA, staticMetadata).then(() => {
    console.info('Succeeded in setting the metadata.');
  }).catch((err: Error) => {
    console.error(`Failed to set the metadata. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## setOpacity

ArkTS-Dyn:
```TypeScript
setOpacity(value: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setOpacity(value: double): Promise<void>
```

Sets opacity of the PixelMap. Every pixel will be set to the same opacity value.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600207](../errorcode-image.md#7600207-不支持的数据格式) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setOpacity(pixelMap: image.PixelMap) {
  const opacity: number = 0.5;
  pixelMap.setOpacity(opacity)
    .then(() => {
      console.info('Succeeded in setting opacity.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function setOpacity(pixelMap: image.PixelMap) {
  const opacity: double = 0.5;
  pixelMap.setOpacity(opacity)
    .then(() => {
      console.info('Succeeded in setting opacity.');
    })
    .catch((err: Error) => {
      console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## setOpacitySync

ArkTS-Dyn:
```TypeScript
setOpacitySync(value: number): void
```

ArkTS-Sta:
```TypeScript
setOpacitySync(value: double): void
```

Sets opacity of the PixelMap. Every pixel will be set to the same opacity value.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600207](../errorcode-image.md#7600207-不支持的数据格式) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setOpacitySync(pixelMap: image.PixelMap) {
  const opacity: number = 0.5;
  try {
    pixelMap.setOpacitySync(opacity);
    console.info('Succeeded in setting opacity.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function setOpacitySync(pixelMap: image.PixelMap) {
  const opacity: double = 0.5;
  try {
    pixelMap.setOpacitySync(opacity);
    console.info('Succeeded in setting opacity.');
  } catch (err) {
    console.error(`Failed to set opacity. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## setTransferDetached

```TypeScript
setTransferDetached(detached: boolean): void
```

Sets whether to detach from the original thread when this PixelMap is transmitted across threads. This API applies to the scenario where the PixelMap needs to be released immediately.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [detached](../../apis-arkts/arkts-apis/arkts-arkts-arraybuffer-c.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

```TypeScript
// EntryAbility.ets
import { common } from '@kit.AbilityKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
// 子线程方法。
async function loadPixelMap(rawFileDescriptor: number): Promise<image.PixelMap> {
  // 创建ImageSource。
  const imageSource = image.createImageSource(rawFileDescriptor);
  // 创建PixelMap。
  const pixelMap = imageSource.createPixelMapSync();
  // 释放ImageSource。
  imageSource.release();
  // 使PixelMap在跨线程传输完成后，断开原线程的引用。
  pixelMap.setTransferDetached(true);
  // 返回PixelMap给主线程。
  return pixelMap;
}

@Entry
@Component
struct Demo {
  @State pixelMap: image.PixelMap | undefined = undefined;
  // 主线程方法。
  private loadImageFromThread(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const resourceMgr = context.resourceManager;
    // 此处'example.jpg'仅作示例，请开发者自行替换，否则创建失败会导致后续无法正常执行。
    resourceMgr.getRawFd('example.jpg').then(rawFileDescriptor => {
      taskpool.execute(loadPixelMap, rawFileDescriptor).then(pixelMap => {
        if (pixelMap) {
          this.pixelMap = pixelMap as image.PixelMap;
          console.info('Succeeded in creating the PixelMap.');
          // 主线程释放PixelMap。由于子线程返回PixelMap前已调用setTransferDetached(true)，所以此处能够立即释放PixelMap，不需要等待子线程被销毁。
          this.pixelMap.release();
        } else {
          console.error('Failed to create the PixelMap.');
        }
      });
    });
  }
  build() {
    // ...
  }
}
```

## toSdr

```TypeScript
toSdr(): Promise<void>
```

Convert pixelmap to standard dynamic range.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function toSdr(context: Context) {
  // 此处'app.media.startIcon'需要替换为本地HDR图片。
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating the PixelMap object.');
    pixelmap.toSdr().then(() => {
      let imageInfo = pixelmap.getImageInfoSync();
      console.info("Succeeded in converting to SDR. imageInfo.isHdr: " + imageInfo.isHdr);
    }).catch((err: BusinessError) => {
      console.error(`Failed to convert to SDR. Code: ${err.code}, message: ${err.message}`);
    });
  } else {
    console.error('Failed to create the PixelMap.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
async function toSdr(context: Context) {
  // 此处'app.media.startIcon'需要替换为本地HDR图片。
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating the PixelMap object.');
    pixelmap.toSdr().then(() => {
      let imageInfo = pixelmap.getImageInfoSync();
      console.info("Succeeded in converting to SDR. imageInfo.isHdr: " + imageInfo.isHdr);
    }).catch((err: Error) => {
      console.error(`Failed to convert to SDR. Code: ${err.code}, message: ${err.message}`);
    });
  } else {
    console.error('Failed to create the PixelMap.');
  }
}
```

## translate

ArkTS-Dyn:
```TypeScript
translate(x: number, y: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
translate(x: double, y: double, callback: AsyncCallback<void>): void
```

Translates this image based on given coordinates. This API uses an asynchronous callback to return the result. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.Starting from API 26.0.0, it is recommended to use [applyTranslate](#applytranslate) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function translate(pixelMap: image.PixelMap) {
  const translateX: number = 50.0;
  const translateY: number = 10.0;
  pixelMap.translate(translateX, translateY, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in translating the PixelMap.");
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function translate(pixelMap: image.PixelMap) {
  const translateX: double = 50.0;
  const translateY: double = 10.0;
  pixelMap.translate(translateX, translateY, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in translating the PixelMap.");
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function translate(pixelMap: image.PixelMap) {
  const translateX: number = 50.0;
  const translateY: number = 10.0;
  pixelMap.translate(translateX, translateY).then(() => {
    console.info('Succeeded in translating the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function translate(pixelMap: image.PixelMap) {
  const translateX: double = 50.0;
  const translateY: double = 10.0;
  pixelMap.translate(translateX, translateY).then(() => {
    console.info('Succeeded in translating the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## translate

ArkTS-Dyn:
```TypeScript
translate(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
translate(x: double, y: double): Promise<void>
```

Translates a PixelMap based on given coordinates. This API uses a promise to return the result. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.Starting from API 26.0.0, it is recommended to use [applyTranslate](#applytranslate) instead for better exception handling capabilities.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [translate](#translate)

## translateSync

ArkTS-Dyn:
```TypeScript
translateSync(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
translateSync(x: double, y: double): void
```

Translates this image based on given coordinates. This API returns the result synchronously. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.Starting from API 26.0.0, it is recommended to use [applyTranslateSync](#applytranslatesync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function translateSync(pixelMap: image.PixelMap) {
  const translateX: number = 50.0;
  const translateY: number = 10.0;
  try {
    pixelMap.translateSync(translateX, translateY);
    console.info('Succeeded in translating the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function translateSync(pixelMap: image.PixelMap) {
  const translateX: double = 50.0;
  const translateY: double = 10.0;
  try {
    pixelMap.translateSync(translateX, translateY);
    console.info('Succeeded in translating the PixelMap.');
  } catch (err) {
    console.error(`Failed to translate the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## unmarshalling

```TypeScript
unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>
```

Unmarshals a MessageSequence object to obtain a PixelMap object. To create a PixelMap object in synchronous mode, use [createPixelMapFromParcel](arkts-image-image-createpixelmapfromparcel-f.md).

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequence | rpc.MessageSequence | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |

**示例**

```TypeScript
// EntryAbility.ets
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixelMap: image.PixelMap;
  constructor(pixelMap: image.PixelMap) {
    this.pixelMap = pixelMap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixelMap.marshalling(messageSequence);
    console.info('Marshalled the PixelMap.');
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height: 4, width: 6 }}).then((pixelParcel: image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: image.PixelMap) => {
        this.pixelMap = pixelMap;
        pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
          console.info(`Unmarshalled information: height = ${imageInfo.size.height}, width = ${imageInfo.size.width}.`);
        });
      });
    });
    return true;
  }
}

async function unmarshal() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.BGRA_8888,
    size: { height: 4, width: 6 },
    alphaType: image.AlphaType.UNPREMUL
  };
  let pixelMap: image.PixelMap | undefined = await image.createPixelMap(color, opts);
  if (pixelMap != undefined) {
    // 序列化。
    let parcelable: MySequence = new MySequence(pixelMap);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // 反序列化rpc获取到data。
    let seq: MySequence = new MySequence(pixelMap);
    data.readParcelable(seq);
  }
}
```

## writeAllPixelsFromBuffer

```TypeScript
writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>
```

Reads the pixel data from a buffer and writes the data to the PixelMap. The source data must be in the same pixel format as the PixelMap.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writeAllPixelsFromBuffer(pixelMap: image.PixelMap) {
  const writeBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  const bufferArr = new Uint8Array(writeBuffer);
  for (let i = 0; i < bufferArr.length; i += 4) {
    // 假设pixelMap的像素格式为RGBA_8888，则下列数组索引依次为：R通道、G通道、B通道、A通道。
    bufferArr[i] = 0xFF;
    bufferArr[i + 1] = 0x00;
    bufferArr[i + 2] = 0x00;
    bufferArr[i + 3] = 0xFF;
  }

  pixelMap.writeAllPixelsFromBuffer(writeBuffer)
    .then(() => {
      console.info('Succeeded in writing pixel data from writeBuffer to the PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function writeAllPixelsFromBuffer(pixelMap: image.PixelMap) {
  const writeBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  const bufferArr = new Uint8Array(writeBuffer);
  for (let i = 0; i < bufferArr.length; i += 4) {
    // 假设pixelMap的像素格式为RGBA_8888，则下列数组索引依次为：R通道、G通道、B通道、A通道。
    bufferArr[i] = 0xFF;
    bufferArr[i + 1] = 0x00;
    bufferArr[i + 2] = 0x00;
    bufferArr[i + 3] = 0xFF;
  }

  pixelMap.writeAllPixelsFromBuffer(writeBuffer)
    .then(() => {
      console.info('Succeeded in writing pixel data from writeBuffer to the PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## writeAllPixelsFromBufferSync

```TypeScript
writeAllPixelsFromBufferSync(src: ArrayBuffer): void
```

Reads the pixel data from a buffer and writes the data to the PixelMap. The source data must be in the same pixel format as the PixelMap.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writeAllPixelsFromBufferSync(pixelMap: image.PixelMap) {
  const writeBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  const bufferArr = new Uint8Array(writeBuffer);
  for (let i = 0; i < bufferArr.length; i += 4) {
    // 假设pixelMap的像素格式为RGBA_8888，则下列数组索引依次为：R通道、G通道、B通道、A通道。
    bufferArr[i] = 0xFF;
    bufferArr[i + 1] = 0x00;
    bufferArr[i + 2] = 0x00;
    bufferArr[i + 3] = 0xFF;
  }

  try {
    pixelMap.writeAllPixelsFromBufferSync(writeBuffer);
    console.info('Succeeded in writing pixel data from writeBuffer to the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function writeAllPixelsFromBufferSync(pixelMap: image.PixelMap) {
  const writeBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  const bufferArr = new Uint8Array(writeBuffer);
  for (let i = 0; i < bufferArr.length; i += 4) {
    // 假设pixelMap的像素格式为RGBA_8888，则下列数组索引依次为：R通道、G通道、B通道、A通道。
    bufferArr[i] = 0xFF;
    bufferArr[i + 1] = 0x00;
    bufferArr[i + 2] = 0x00;
    bufferArr[i + 3] = 0xFF;
  }

  try {
    pixelMap.writeAllPixelsFromBufferSync(writeBuffer);
    console.info('Succeeded in writing pixel data from writeBuffer to the PixelMap.');
  } catch (err) {
    console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer): Promise<void>
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBuffer](#writeallpixelsfrombuffer) instead for better exception handling capabilities.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writeBufferToPixels(pixelMap: image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writeBufferToPixels(color).then(() => {
    console.info('Succeeded in writing data from the buffer to the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to write data from the buffer to the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function writeBufferToPixels(pixelMap: image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writeBufferToPixels(color).then(() => {
    console.info('Succeeded in writing data from the buffer to the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to write data from the buffer to the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writeBufferToPixels(pixelMap: image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writeBufferToPixels(color, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to write data from the buffer to the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in writing data from the buffer to the PixelMap.');
  });
}
```

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBuffer](#writeallpixelsfrombuffer) instead for better exception handling capabilities.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

参见 [writeBufferToPixels](#writebuffertopixels)

## writeBufferToPixelsSync

```TypeScript
writeBufferToPixelsSync(src: ArrayBuffer): void
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBufferSync](#writeallpixelsfrombuffersync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writeBufferToPixelsSync(pixelMap: image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  try {
    pixelMap.writeBufferToPixelsSync(color);
    console.info('Succeeded in writing data from the buffer to the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to write data from the buffer to the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function writeBufferToPixelsSync(pixelMap: image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  try {
    pixelMap.writeBufferToPixelsSync(color);
    console.info('Succeeded in writing data from the buffer to the PixelMap.');
  } catch (err) {
    console.error(`Failed to write data from the buffer to the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## writePixels

```TypeScript
writePixels(area: PositionArea): Promise<void>
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md).pixels in this PixelMap object. This API uses a promise to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)Starting from API 26.0.0, it is recommended to use [writePixelsFromArea](#writepixelsfromarea) instead for better exception handling capabilities.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writePixelsRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writePixels(area).then(() => {
    console.info('Succeeded in writing pixels into the specified area.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to write pixels into the specified area. Code: ${err.code}, message: ${err.message}`);
  });
}

function writePixelsYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6), // 6为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 8, // PixelMap为YUV格式时，writePixels函数不使用该变量。
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writePixels(area).then(() => {
    console.info('Succeeded in writing pixels into the specified area.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to write pixels into the specified area. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function writePixelsRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writePixels(area).then(() => {
    console.info('Succeeded in writing pixels into the specified area.');
  }).catch((err: Error) => {
    console.error(`Failed to write pixels into the specified area. Code: ${err.code}, message: ${err.message}`);
  });
}

function writePixelsYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6), // 6为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 8, // PixelMap为YUV格式时，writePixels函数不使用该变量。
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writePixels(area).then(() => {
    console.info('Succeeded in writing pixels into the specified area.');
  }).catch((error: Error) => {
    console.error(`Failed to write pixels into the specified area. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writePixelsRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writePixels(area, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to write pixels into the specified area. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in writing pixels into the specified area.');
  });
}

function writePixelsYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6), // 6为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 8, // PixelMap为YUV格式时，writePixels函数不使用该变量。
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  pixelMap.writePixels(area, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to write pixels into the specified area. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in writing pixels into the specified area.');
  });
}
```

## writePixels

```TypeScript
writePixels(area: PositionArea, callback: AsyncCallback<void>): void
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md).pixels in this PixelMap object. This API uses an asynchronous callback to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)Starting from API 26.0.0, it is recommended to use [writePixelsFromArea](#writepixelsfromarea) instead for better exception handling capabilities.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

参见 [writePixels](#writepixels)

## writePixelsFromArea

```TypeScript
writePixelsFromArea(area: PositionArea): Promise<void>
```

Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writePixelsFromAreaRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(24), // 24为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 4。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };
  const bufferArr = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i += 4) {
    // 数据源的格式必须是BGRA_8888，下列数组索引依次为：B通道、G通道、R通道、A通道。
    bufferArr[i] = 0xFF;
    bufferArr[i + 1] = 0x00;
    bufferArr[i + 2] = 0x00;
    bufferArr[i + 3] = 0xFF;
  }

  pixelMap.writePixelsFromArea(area)
    .then(() => {
      console.info('Succeeded in writing pixel data from area.pixels to the specified area of the PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}

function writePixelsFromAreaYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(9), // 9为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 2, // PixelMap为YUV格式时，writePixelsFromArea函数不使用该变量。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };
  const bufferArr = new Uint8Array(area.pixels);
  const ySize = area.region.size.width * area.region.size.height;
  for (let i = 0; i < ySize; i++) { // Y平面。
    bufferArr[i] = 0xFF;
  }
  for (let i = ySize; i < bufferArr.length; i++) { // UV交错平面。
    bufferArr[i] = 0x80;
  }

  pixelMap.writePixelsFromArea(area)
    .then(() => {
      console.info('Succeeded in writing pixel data from area.pixels to the specified area of the PixelMap.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
function writePixelsFromAreaRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(24), // 24为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 4。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };
  const bufferArr = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i += 4) {
    // 数据源的格式必须是BGRA_8888，下列数组索引依次为：B通道、G通道、R通道、A通道。
    bufferArr[i] = 0xFF;
    bufferArr[i + 1] = 0x00;
    bufferArr[i + 2] = 0x00;
    bufferArr[i + 3] = 0xFF;
  }

  pixelMap.writePixelsFromArea(area)
    .then(() => {
      console.info('Succeeded in writing pixel data from area.pixels to the specified area of the PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}

function writePixelsFromAreaYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(9), // 9为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 2, // PixelMap为YUV格式时，writePixelsFromArea函数不使用该变量。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };
  const bufferArr = new Uint8Array(area.pixels);
  const ySize = area.region.size.width * area.region.size.height;
  for (let i = 0; i < ySize; i++) { // Y平面。
    bufferArr[i] = 0xFF;
  }
  for (let i = ySize; i < bufferArr.length; i++) { // UV交错平面。
    bufferArr[i] = 0x80;
  }

  pixelMap.writePixelsFromArea(area)
    .then(() => {
      console.info('Succeeded in writing pixel data from area.pixels to the specified area of the PixelMap.');
    })
    .catch((err: Error) => {
      console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
    });
}
```

## writePixelsFromAreaSync

```TypeScript
writePixelsFromAreaSync(area: PositionArea): void
```

Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writePixelsFromAreaSyncRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(24), // 24为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 4。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };
  const bufferArr = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i += 4) {
    // 数据源的格式必须是BGRA_8888，下列数组索引依次为：B通道、G通道、R通道、A通道。
    bufferArr[i] = 0xFF;
    bufferArr[i + 1] = 0x00;
    bufferArr[i + 2] = 0x00;
    bufferArr[i + 3] = 0xFF;
  }

  try {
    pixelMap.writePixelsFromAreaSync(area);
    console.info('Succeeded in writing pixel data from area.pixels to the specified area of the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}

function writePixelsFromAreaSyncYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(9), // 9为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 2, // PixelMap为YUV格式时，writePixelsFromAreaSync函数不使用该变量。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };
  const bufferArr = new Uint8Array(area.pixels);
  const ySize = area.region.size.width * area.region.size.height;
  for (let i = 0; i < ySize; i++) { // Y平面。
    bufferArr[i] = 0xFF;
  }
  for (let i = ySize; i < bufferArr.length; i++) { // UV交错平面。
    bufferArr[i] = 0x80;
  }

  try {
    pixelMap.writePixelsFromAreaSync(area);
    console.info('Succeeded in writing pixel data from area.pixels to the specified area of the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function writePixelsFromAreaSyncRGBA(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(24), // 24为需要创建的像素缓冲区大小，取值为：width * height * 4。
    offset: 0,
    stride: 8, // 跨距，即每行像素所占的字节数，在没有行末填充字节的情况下取值为：width * 4。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };
  const bufferArr = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i += 4) {
    // 数据源的格式必须是BGRA_8888，下列数组索引依次为：B通道、G通道、R通道、A通道。
    bufferArr[i] = 0xFF;
    bufferArr[i + 1] = 0x00;
    bufferArr[i + 2] = 0x00;
    bufferArr[i + 3] = 0xFF;
  }

  try {
    pixelMap.writePixelsFromAreaSync(area);
    console.info('Succeeded in writing pixel data from area.pixels to the specified area of the PixelMap.');
  } catch (err) {
    console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}

function writePixelsFromAreaSyncYUV(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(9), // 9为需要创建的像素缓冲区大小，取值为：width * height * 1.5。
    offset: 0,
    stride: 2, // PixelMap为YUV格式时，writePixelsFromAreaSync函数不使用该变量。
    region: {
      size: { width: 2, height: 3 },
      x: 0,
      y: 0
    }
  };
  const bufferArr = new Uint8Array(area.pixels);
  const ySize = area.region.size.width * area.region.size.height;
  for (let i = 0; i < ySize; i++) { // Y平面。
    bufferArr[i] = 0xFF;
  }
  for (let i = ySize; i < bufferArr.length; i++) { // UV交错平面。
    bufferArr[i] = 0x80;
  }

  try {
    pixelMap.writePixelsFromAreaSync(area);
    console.info('Succeeded in writing pixel data from area.pixels to the specified area of the PixelMap.');
  } catch (err) {
    console.error(`Failed to write pixel data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## writePixelsSync

```TypeScript
writePixelsSync(area: PositionArea): void
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md).pixels in this PixelMap object. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [writePixelsFromAreaSync](#writepixelsfromareasync) instead for better exception handling capabilities.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function writePixelsSync(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  try {
    pixelMap.writePixelsSync(area);
    console.info('Succeeded in writing pixels into the specified area.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to write pixels into the specified area. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function writePixelsSync(pixelMap: image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  try {
    pixelMap.writePixelsSync(area);
    console.info('Succeeded in writing pixels into the specified area.');
  } catch (err) {
    console.error(`Failed to write pixels into the specified area. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## isEditable

```TypeScript
readonly isEditable: boolean
```

Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides better image rendering and transmission performance.<br> This API can be used in atomic services since API version 11.<br> This API can be used in ArkTS widgets since API version 12.

**类型：** boolean

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

## isStrideAlignment

```TypeScript
readonly isStrideAlignment: boolean
```

Whether the row data of the image is memory aligned. The value **true** means that the row data is memory-aligned, and there may be blank bytes padded at the end of each row to meet alignment requirements. The value **false** means that the row data is not memory-aligned, and rows are packed contiguously with no padding bytes at the end.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.Core
