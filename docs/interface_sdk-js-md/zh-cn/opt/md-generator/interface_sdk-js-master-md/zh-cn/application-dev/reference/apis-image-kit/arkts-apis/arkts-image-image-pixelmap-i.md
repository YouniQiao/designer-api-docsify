# PixelMap

The **PixelMap** class provides APIs to read or write image data and obtain image information. Before calling any API in PixelMap, you must use [image.createPixelMap](arkts-image-image-createpixelmap-f.md#createPixelMap) to create a PixelMap object. Currently, the maximum size of a serialized PixelMap is 128 MB. A larger size will cause a display failure. The size is calculated as follows: Width x Height x [Bytes per pixel](arkts-image-image-pixelmapformat-e.md#PixelMapFormat). Since API version 11, PixelMap supports cross-thread calls through [Worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md#worker). If a PixelMap object is invoked by another thread through [Worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md#worker), all APIs of the PixelMap object cannot be called in the original thread. Otherwise, error 501 is reported, indicating that the server cannot complete the request. Before calling any API in PixelMap, you can use [image.createPixelMap](arkts-image-image-createpixelmap-f.md#createPixelMap) to pass pixel data to create a PixelMap object, or use [ImageSource](arkts-multimedia-image.md#@ohos.multimedia.image) to decode an image to a PixelMap object. To develop an atomic service, use [ImageSource](arkts-multimedia-image.md#@ohos.multimedia.image) to create a PixelMap object. Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**起始版本：** 23

**废弃版本：** -1

<!--Device-image-interface PixelMap--><!--Device-image-interface PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## applyColorSpace

```TypeScript
applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void
```

Performs color space conversion (CSC) on the image pixel color based on a given color space. This API uses an asynchronous callback to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void--><!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetColorSpace | colorSpaceManager.ColorSpaceManager | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980108](../errorcode-image.md#62980108-图片颜色转换错误) |

## applyColorSpace

```TypeScript
applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>
```

Performs Color Space Converters (CSC) on the image pixel color based on a given color space. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>--><!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>-End-->

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
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980108](../errorcode-image.md#62980108-图片颜色转换错误) |

## applyCrop

```TypeScript
applyCrop(region: Region): Promise<void>
```

Crops the PixelMap.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyCrop(region: Region): Promise<void>--><!--Device-PixelMap-applyCrop(region: Region): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](arkts-image-image-region-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |
| [7600204](../errorcode-image.md#7600204-无效的区域) |

## applyCropSync

```TypeScript
applyCropSync(region: Region): void
```

Crops the PixelMap.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyCropSync(region: Region): void--><!--Device-PixelMap-applyCropSync(region: Region): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](arkts-image-image-region-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |
| [7600204](../errorcode-image.md#7600204-无效的区域) |

## applyFlip

```TypeScript
applyFlip(horizontal: boolean, vertical: boolean): Promise<void>
```

Flips the PixelMap in the horizontal and/or vertical directions.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyFlip(horizontal: boolean, vertical: boolean): Promise<void>--><!--Device-PixelMap-applyFlip(horizontal: boolean, vertical: boolean): Promise<void>-End-->

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
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## applyFlipSync

```TypeScript
applyFlipSync(horizontal: boolean, vertical: boolean): void
```

Flips the PixelMap in the horizontal and/or vertical directions.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyFlipSync(horizontal: boolean, vertical: boolean): void--><!--Device-PixelMap-applyFlipSync(horizontal: boolean, vertical: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## applyRotate

```TypeScript
applyRotate(angle: number): Promise<void>
```

Rotates the PixelMap. Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyRotate(angle: double): Promise<void>--><!--Device-PixelMap-applyRotate(angle: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## applyRotateSync

```TypeScript
applyRotateSync(angle: number): void
```

Rotates the PixelMap. Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyRotateSync(angle: double): void--><!--Device-PixelMap-applyRotateSync(angle: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## applyScale

```TypeScript
applyScale(x: number, y: number, level?: AntiAliasingLevel): Promise<void>
```

Scales the PixelMap in the horizontal and/or vertical dimensions.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyScale(x: double, y: double, level?: AntiAliasingLevel): Promise<void>--><!--Device-PixelMap-applyScale(x: double, y: double, level?: AntiAliasingLevel): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## applyScaleSync

```TypeScript
applyScaleSync(x: number, y: number, level?: AntiAliasingLevel): void
```

Scales the PixelMap in the horizontal and/or vertical dimensions.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyScaleSync(x: double, y: double, level?: AntiAliasingLevel): void--><!--Device-PixelMap-applyScaleSync(x: double, y: double, level?: AntiAliasingLevel): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## applyTranslate

```TypeScript
applyTranslate(x: number, y: number): Promise<void>
```

Repositions the PixelMap in the horizontal and/or vertical directions.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyTranslate(x: double, y: double): Promise<void>--><!--Device-PixelMap-applyTranslate(x: double, y: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## applyTranslateSync

```TypeScript
applyTranslateSync(x: number, y: number): void
```

Repositions the PixelMap in the horizontal and/or vertical directions.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-applyTranslateSync(x: double, y: double): void--><!--Device-PixelMap-applyTranslateSync(x: double, y: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |

## clone

```TypeScript
clone(): Promise<PixelMap>
```

Copies this PixelMap object. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-clone(): Promise<PixelMap>--><!--Device-PixelMap-clone(): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980102](../errorcode-image.md#62980102-图片分配内存错误) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |

## cloneSync

```TypeScript
cloneSync(): PixelMap
```

Copies this PixelMap object. This API returns the result synchronously.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-cloneSync(): PixelMap--><!--Device-PixelMap-cloneSync(): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980102](../errorcode-image.md#62980102-图片分配内存错误) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |

## convertPixelFormat

```TypeScript
convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>
```

The method is used for the transformation of the image formats. Pixel data will be changed by calling this method.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>--><!--Device-PixelMap-convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>-End-->

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
| [62980274](../errorcode-image.md#62980274-图片转换失败) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |
| [62980276](../errorcode-image.md#62980276-不支持图片转换目标类型) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(): Promise<PixelMap>
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMap](#extractAlphaPixelMap) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-createAlphaPixelmap(): Promise<PixelMap>--><!--Device-PixelMap-createAlphaPixelmap(): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API returns the result through a callback. Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMap](#extractAlphaPixelMap) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void--><!--Device-PixelMap-createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | 是 |

## createAlphaPixelmapSync

```TypeScript
createAlphaPixelmapSync(): PixelMap
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. This API returns the result synchronously. It is invalid for YUV images. Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMapSync](#extractAlphaPixelMapSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-createAlphaPixelmapSync(): PixelMap--><!--Device-PixelMap-createAlphaPixelmapSync(): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## createCroppedAndScaledPixelMap

```TypeScript
createCroppedAndScaledPixelMap(region: Region, x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>
```

Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the width and height, and anti-aliasing level. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-createCroppedAndScaledPixelMap(region: Region, x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>--><!--Device-PixelMap-createCroppedAndScaledPixelMap(region: Region, x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](arkts-image-image-region-i.md) | 是 |
| x | number | 是 |
| y | number | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600205](../errorcode-image.md#7600205-不支持的内存格式或像素格式) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |
| [7600204](../errorcode-image.md#7600204-无效的区域) |

## createCroppedAndScaledPixelMapSync

```TypeScript
createCroppedAndScaledPixelMapSync(region: Region, x: number, y: number, level?: AntiAliasingLevel): PixelMap
```

Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the width and height, and anti-aliasing level. This API returns the result synchronously.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-createCroppedAndScaledPixelMapSync(region: Region, x: double, y: double, level?: AntiAliasingLevel): PixelMap--><!--Device-PixelMap-createCroppedAndScaledPixelMapSync(region: Region, x: double, y: double, level?: AntiAliasingLevel): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](arkts-image-image-region-i.md) | 是 |
| x | number | 是 |
| y | number | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600205](../errorcode-image.md#7600205-不支持的内存格式或像素格式) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |
| [7600204](../errorcode-image.md#7600204-无效的区域) |

## createScaledPixelMap

```TypeScript
createScaledPixelMap(x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>
```

Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-createScaledPixelMap(x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>--><!--Device-PixelMap-createScaledPixelMap(x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
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

## createScaledPixelMapSync

```TypeScript
createScaledPixelMapSync(x: number, y: number, level?: AntiAliasingLevel): PixelMap
```

Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. This API returns the result synchronously.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-createScaledPixelMapSync(x: double, y: double, level?: AntiAliasingLevel): PixelMap--><!--Device-PixelMap-createScaledPixelMapSync(x: double, y: double, level?: AntiAliasingLevel): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## crop

```TypeScript
crop(region: Region, callback: AsyncCallback<void>): void
```

Crops this image based on a given size. This API uses an asynchronous callback to return the result. Starting from API 26.0.0, it is recommended to use [applyCrop](#applyCrop) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-crop(region: Region, callback: AsyncCallback<void>): void--><!--Device-PixelMap-crop(region: Region, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](arkts-image-image-region-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## crop

```TypeScript
crop(region: Region): Promise<void>
```

Crops a PixelMap based on a given size. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [applyCrop](#applyCrop) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-crop(region: Region): Promise<void>--><!--Device-PixelMap-crop(region: Region): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](arkts-image-image-region-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## cropSync

```TypeScript
cropSync(region: Region): void
```

Crops this image based on a given size. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [applyCropSync](#applyCropSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-cropSync(region: Region): void--><!--Device-PixelMap-cropSync(region: Region): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](arkts-image-image-region-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## extractAlphaPixelMap

```TypeScript
extractAlphaPixelMap(): Promise<PixelMap>
```

Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-extractAlphaPixelMap(): Promise<PixelMap>--><!--Device-PixelMap-extractAlphaPixelMap(): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600306](../errorcode-image.md#7600306-数据转换失败) |
| [7600305](../errorcode-image.md#7600305-创建pixelmap失败) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |

## extractAlphaPixelMapSync

```TypeScript
extractAlphaPixelMapSync(): PixelMap
```

Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-extractAlphaPixelMapSync(): PixelMap--><!--Device-PixelMap-extractAlphaPixelMapSync(): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [7600306](../errorcode-image.md#7600306-数据转换失败) |
| [7600305](../errorcode-image.md#7600305-创建pixelmap失败) |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void
```

Flips this image horizontally or vertically, or both. This API uses an asynchronous callback to return the result. Starting from API 26.0.0, it is recommended to use [applyFlip](#applyFlip) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void--><!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean): Promise<void>
```

Flips a PixelMap based on a given angle. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [applyFlip](#applyFlip) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean): Promise<void>--><!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean): Promise<void>-End-->

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

## flipSync

```TypeScript
flipSync(horizontal: boolean, vertical: boolean): void
```

Flips this image horizontally or vertically, or both. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [applyFlipSync](#applyFlipSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-flipSync(horizontal: boolean, vertical: boolean): void--><!--Device-PixelMap-flipSync(horizontal: boolean, vertical: boolean): void-End-->

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

## getBytesNumberPerRow

```TypeScript
getBytesNumberPerRow(): number
```

Obtains the number of bytes per row of this image. Unit: bytes.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-getBytesNumberPerRow(): int--><!--Device-PixelMap-getBytesNumberPerRow(): int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| number |

## getColorSpace

```TypeScript
getColorSpace(): colorSpaceManager.ColorSpaceManager
```

Obtains the color space of this image.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-getColorSpace(): colorSpaceManager.ColorSpaceManager--><!--Device-PixelMap-getColorSpace(): colorSpaceManager.ColorSpaceManager-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| colorSpaceManager.ColorSpaceManager |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |

## getDensity

```TypeScript
getDensity(): number
```

Obtains the pixel density of this image. Unit: ppi (pixels/inch)

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-getDensity(): int--><!--Device-PixelMap-getDensity(): int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| number |

## getImageInfo

```TypeScript
getImageInfo(): Promise<ImageInfo>
```

Obtains the image information of a PixelMap. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-getImageInfo(): Promise<ImageInfo>--><!--Device-PixelMap-getImageInfo(): Promise<ImageInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; |

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo>): void
```

Obtains the image information. This API uses an asynchronous callback to return the result.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-getImageInfo(callback: AsyncCallback<ImageInfo>): void--><!--Device-PixelMap-getImageInfo(callback: AsyncCallback<ImageInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | 是 |

## getImageInfoSync

```TypeScript
getImageInfoSync(): ImageInfo
```

Obtains the image information. This API returns the result synchronously.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-getImageInfoSync(): ImageInfo--><!--Device-PixelMap-getImageInfoSync(): ImageInfo-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |

## getMetadata

```TypeScript
getMetadata(key: HdrMetadataKey): HdrMetadataValue
```

Obtains the value of the metadata with a given key in this PixelMap.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-getMetadata(key: HdrMetadataKey): HdrMetadataValue--><!--Device-PixelMap-getMetadata(key: HdrMetadataKey): HdrMetadataValue-End-->

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

## getPixelBytesNumber

```TypeScript
getPixelBytesNumber(): number
```

Obtains the total number of bytes of this image. Unit: bytes.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-getPixelBytesNumber(): int--><!--Device-PixelMap-getPixelBytesNumber(): int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| number |

## getUniqueId

```TypeScript
getUniqueId(): number
```

Obtains the unique ID of this PixelMap.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-getUniqueId(): int--><!--Device-PixelMap-getUniqueId(): int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |

## isReleased

```TypeScript
isReleased(): boolean
```

Checks whether this PixelMap object is released. If released, any attempt to access the internal data of this object will fail. > **NOTE：**> > Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied > by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-isReleased(): boolean--><!--Device-PixelMap-isReleased(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## marshalling

```TypeScript
marshalling(sequence: rpc.MessageSequence): void
```

Marshals this PixelMap object and writes it to a MessageSequence object.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-marshalling(sequence: rpc.MessageSequence): void--><!--Device-PixelMap-marshalling(sequence: rpc.MessageSequence): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequence | rpc.MessageSequence | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

## opacity

```TypeScript
opacity(rate: number, callback: AsyncCallback<void>): void
```

Sets an opacity rate for this image. This API uses an asynchronous callback to return the result. It is invalid for YUV images. Starting from API 26.0.0, it is recommended to use [setOpacity](#setOpacity) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-opacity(rate: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-opacity(rate: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## opacity

```TypeScript
opacity(rate: number): Promise<void>
```

Sets an opacity rate for this image. It is invalid for YUV images. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [setOpacity](#setOpacity) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-opacity(rate: double): Promise<void>--><!--Device-PixelMap-opacity(rate: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## opacitySync

```TypeScript
opacitySync(rate: number): void
```

Sets an opacity rate for this image. This API returns the result synchronously. It is invalid for YUV images. Starting from API 26.0.0, it is recommended to use [setOpacitySync](#setOpacitySync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-opacitySync(rate: double): void--><!--Device-PixelMap-opacitySync(rate: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## readAllPixelsToBuffer

```TypeScript
readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads all the pixel data from the PixelMap and writes the data to a buffer. The resulting data will be in the same pixel format as the PixelMap.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>--><!--Device-PixelMap-readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>-End-->

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
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

## readAllPixelsToBufferSync

```TypeScript
readAllPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads all the pixel data from the PixelMap and writes the data to a buffer. The resulting data will be in the same pixel format as the PixelMap.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readAllPixelsToBufferSync(dst: ArrayBuffer): void--><!--Device-PixelMap-readAllPixelsToBufferSync(dst: ArrayBuffer): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

## readPixels

```TypeScript
readPixels(area: PositionArea): Promise<void>
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels buffer. This API uses a promise to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component) Starting from API 26.0.0, it is recommended to use [readPixelsToArea](#readPixelsToArea) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readPixels(area: PositionArea): Promise<void>--><!--Device-PixelMap-readPixels(area: PositionArea): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## readPixels

```TypeScript
readPixels(area: PositionArea, callback: AsyncCallback<void>): void
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels buffer. This API uses an asynchronous callback to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component) Starting from API 26.0.0, it is recommended to use [readPixelsToArea](#readPixelsToArea) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readPixels(area: PositionArea, callback: AsyncCallback<void>): void--><!--Device-PixelMap-readPixels(area: PositionArea, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## readPixelsSync

```TypeScript
readPixelsSync(area: PositionArea): void
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels buffer. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [readPixelsToAreaSync](#readPixelsToAreaSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-readPixelsSync(area: PositionArea): void--><!--Device-PixelMap-readPixelsSync(area: PositionArea): void-End-->

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

## readPixelsToArea

```TypeScript
readPixelsToArea(area: PositionArea): Promise<void>
```

Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readPixelsToArea(area: PositionArea): Promise<void>--><!--Device-PixelMap-readPixelsToArea(area: PositionArea): Promise<void>-End-->

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
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

## readPixelsToAreaSync

```TypeScript
readPixelsToAreaSync(area: PositionArea): void
```

Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readPixelsToAreaSync(area: PositionArea): void--><!--Device-PixelMap-readPixelsToAreaSync(area: PositionArea): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [readAllPixelsToBuffer](#readAllPixelsToBuffer) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer): Promise<void>--><!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API uses an asynchronous callback to return the result. Starting from API 26.0.0, it is recommended to use [readAllPixelsToBuffer](#readAllPixelsToBuffer) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void--><!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## readPixelsToBufferSync

```TypeScript
readPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [readAllPixelsToBufferSync](#readAllPixelsToBufferSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readPixelsToBufferSync(dst: ArrayBuffer): void--><!--Device-PixelMap-readPixelsToBufferSync(dst: ArrayBuffer): void-End-->

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

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will fail. This API uses an asynchronous callback to return the result. Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed. > **NOTE：**> > Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied > by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-release(callback: AsyncCallback<void>): void--><!--Device-PixelMap-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will fail. This API uses a promise to return the result. Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed. > **NOTE：**> > Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied > by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-release(): Promise<void>--><!--Device-PixelMap-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## rotate

```TypeScript
rotate(angle: number, callback: AsyncCallback<void>): void
```

Rotates this image based on a given angle. This API uses an asynchronous callback to return the result. Starting from API 26.0.0, it is recommended to use [applyRotate](#applyRotate) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-rotate(angle: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-rotate(angle: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## rotate

```TypeScript
rotate(angle: number): Promise<void>
```

Rotates a PixelMap based on a given angle. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [applyRotate](#applyRotate) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-rotate(angle: double): Promise<void>--><!--Device-PixelMap-rotate(angle: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## rotateSync

```TypeScript
rotateSync(angle: number): void
```

Rotates this image based on a given angle. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [applyRotateSync](#applyRotateSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-rotateSync(angle: double): void--><!--Device-PixelMap-rotateSync(angle: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## scale

```TypeScript
scale(x: number, y: number, callback: AsyncCallback<void>): void
```

Scales this image based on the scale factors of the width and height. This API uses an asynchronous callback to return the result. Starting from API 26.0.0, it is recommended to use [applyScale](#applyScale) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-scale(x: double, y: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-scale(x: double, y: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## scale

```TypeScript
scale(x: number, y: number): Promise<void>
```

Scales this image based on the scale factors of the width and height. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [applyScale](#applyScale) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-scale(x: double, y: double): Promise<void>--><!--Device-PixelMap-scale(x: double, y: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## scale

```TypeScript
scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>
```

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [applyScale](#applyScale) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>--><!--Device-PixelMap-scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
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

## scaleSync

```TypeScript
scaleSync(x: number, y: number): void
```

Scales this image based on the scale factors of the width and height. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [applyScaleSync](#applyScaleSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-scaleSync(x: double, y: double): void--><!--Device-PixelMap-scaleSync(x: double, y: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## scaleSync

```TypeScript
scaleSync(x: number, y: number, level: AntiAliasingLevel): void
```

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [applyScaleSync](#applyScaleSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-scaleSync(x: double, y: double, level: AntiAliasingLevel): void--><!--Device-PixelMap-scaleSync(x: double, y: double, level: AntiAliasingLevel): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void
```

Set color space of pixel map. This method is only used to set the colorspace property of pixelmap, while all pixel data remains the same after calling this method. If you want to change colorspace for all pixels, use method {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager)} or {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager, AsyncCallback&lt;void&gt;)}.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void--><!--Device-PixelMap-setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpaceManager | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |

## setMemoryNameSync

```TypeScript
setMemoryNameSync(name: string): void
```

Sets a memory name for this PixelMap.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-setMemoryNameSync(name: string): void--><!--Device-PixelMap-setMemoryNameSync(name: string): void-End-->

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

## setMetadata

```TypeScript
setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>
```

Sets the value for the metadata with a given key in this PixelMap. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>--><!--Device-PixelMap-setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>-End-->

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

## setOpacity

```TypeScript
setOpacity(value: number): Promise<void>
```

Sets opacity of the PixelMap. Every pixel will be set to the same opacity value.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-setOpacity(value: double): Promise<void>--><!--Device-PixelMap-setOpacity(value: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600207](../errorcode-image.md#7600207-不支持的数据格式) |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## setOpacitySync

```TypeScript
setOpacitySync(value: number): void
```

Sets opacity of the PixelMap. Every pixel will be set to the same opacity value.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-setOpacitySync(value: double): void--><!--Device-PixelMap-setOpacitySync(value: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600207](../errorcode-image.md#7600207-不支持的数据格式) |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## setTransferDetached

```TypeScript
setTransferDetached(detached: boolean): void
```

Sets whether to detach from the original thread when this PixelMap is transmitted across threads. This API applies to the scenario where the PixelMap needs to be released immediately.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-setTransferDetached(detached: boolean): void--><!--Device-PixelMap-setTransferDetached(detached: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| detached | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |

## toSdr

```TypeScript
toSdr(): Promise<void>
```

Convert pixelmap to standard dynamic range.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-toSdr(): Promise<void>--><!--Device-PixelMap-toSdr(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980137](../errorcode-image.md#62980137-图片操作无效) |

## translate

```TypeScript
translate(x: number, y: number, callback: AsyncCallback<void>): void
```

Translates this image based on given coordinates. This API uses an asynchronous callback to return the result. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen. Starting from API 26.0.0, it is recommended to use [applyTranslate](#applyTranslate) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-translate(x: double, y: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-translate(x: double, y: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## translate

```TypeScript
translate(x: number, y: number): Promise<void>
```

Translates a PixelMap based on given coordinates. This API uses a promise to return the result. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen. Starting from API 26.0.0, it is recommended to use [applyTranslate](#applyTranslate) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-translate(x: double, y: double): Promise<void>--><!--Device-PixelMap-translate(x: double, y: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## translateSync

```TypeScript
translateSync(x: number, y: number): void
```

Translates this image based on given coordinates. This API returns the result synchronously. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen. Starting from API 26.0.0, it is recommended to use [applyTranslateSync](#applyTranslateSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-translateSync(x: double, y: double): void--><!--Device-PixelMap-translateSync(x: double, y: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## unmarshalling

```TypeScript
unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>
```

Unmarshals a MessageSequence object to obtain a PixelMap object. To create a PixelMap object in synchronous mode, use [createPixelMapFromParcel](arkts-image-image-createpixelmapfromparcel-f.md#createPixelMapFromParcel).

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>--><!--Device-PixelMap-unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>-End-->

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
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

## writeAllPixelsFromBuffer

```TypeScript
writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>
```

Reads the pixel data from a buffer and writes the data to the PixelMap. The source data must be in the same pixel format as the PixelMap.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>--><!--Device-PixelMap-writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>-End-->

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
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

## writeAllPixelsFromBufferSync

```TypeScript
writeAllPixelsFromBufferSync(src: ArrayBuffer): void
```

Reads the pixel data from a buffer and writes the data to the PixelMap. The source data must be in the same pixel format as the PixelMap.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writeAllPixelsFromBufferSync(src: ArrayBuffer): void--><!--Device-PixelMap-writeAllPixelsFromBufferSync(src: ArrayBuffer): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer): Promise<void>
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API uses a promise to return the result. Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBuffer](#writeAllPixelsFromBuffer) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer): Promise<void>--><!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API uses an asynchronous callback to return the result. Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBuffer](#writeAllPixelsFromBuffer) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void--><!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## writeBufferToPixelsSync

```TypeScript
writeBufferToPixelsSync(src: ArrayBuffer): void
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBufferSync](#writeAllPixelsFromBufferSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PixelMap-writeBufferToPixelsSync(src: ArrayBuffer): void--><!--Device-PixelMap-writeBufferToPixelsSync(src: ArrayBuffer): void-End-->

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

## writePixels

```TypeScript
writePixels(area: PositionArea): Promise<void>
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels in this PixelMap object. This API uses a promise to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component) Starting from API 26.0.0, it is recommended to use [writePixelsFromArea](#writePixelsFromArea) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writePixels(area: PositionArea): Promise<void>--><!--Device-PixelMap-writePixels(area: PositionArea): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## writePixels

```TypeScript
writePixels(area: PositionArea, callback: AsyncCallback<void>): void
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels in this PixelMap object. This API uses an asynchronous callback to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component) Starting from API 26.0.0, it is recommended to use [writePixelsFromArea](#writePixelsFromArea) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writePixels(area: PositionArea, callback: AsyncCallback<void>): void--><!--Device-PixelMap-writePixels(area: PositionArea, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## writePixelsFromArea

```TypeScript
writePixelsFromArea(area: PositionArea): Promise<void>
```

Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writePixelsFromArea(area: PositionArea): Promise<void>--><!--Device-PixelMap-writePixelsFromArea(area: PositionArea): Promise<void>-End-->

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
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

## writePixelsFromAreaSync

```TypeScript
writePixelsFromAreaSync(area: PositionArea): void
```

Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writePixelsFromAreaSync(area: PositionArea): void--><!--Device-PixelMap-writePixelsFromAreaSync(area: PositionArea): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7600106](../errorcode-image.md#7600106-pixelmap已被传递至另一个线程) |
| [7600105](../errorcode-image.md#7600105-pixelmap已被释放) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) |

## writePixelsSync

```TypeScript
writePixelsSync(area: PositionArea): void
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels in this PixelMap object. This API returns the result synchronously. Starting from API 26.0.0, it is recommended to use [writePixelsFromAreaSync](#writePixelsFromAreaSync) instead for better exception handling capabilities.

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-writePixelsSync(area: PositionArea): void--><!--Device-PixelMap-writePixelsSync(area: PositionArea): void-End-->

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

## isEditable

```TypeScript
readonly isEditable: boolean
```

Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides better image rendering and transmission performance.&lt;br&gt; This API can be used in atomic services since API version 11.&lt;br&gt; This API can be used in ArkTS widgets since API version 12.

**类型：** boolean

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PixelMap-readonly isEditable: boolean--><!--Device-PixelMap-readonly isEditable: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## isStrideAlignment

```TypeScript
readonly isStrideAlignment: boolean
```

Whether the row data of the image is memory aligned. The value **true** means that the row data is memory-aligned , and there may be blank bytes padded at the end of each row to meet alignment requirements. The value **false** means that the row data is not memory-aligned, and rows are packed contiguously with no padding bytes at the end.

**类型：** boolean

**起始版本：** 23

**废弃版本：** -1

<!--Device-PixelMap-readonly isStrideAlignment: boolean--><!--Device-PixelMap-readonly isStrideAlignment: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core
