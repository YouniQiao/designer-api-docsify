# ImageProcessor

Provides the ImageProcessor type, including the processing function.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-videoProcessingEngine-interface ImageProcessor--><!--Device-videoProcessingEngine-interface ImageProcessor-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

## 导入模块

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## enhanceDetail

ArkTS-Dyn:
```TypeScript
enhanceDetail(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): Promise<image.PixelMap>
```

ArkTS-Sta:
```TypeScript
enhanceDetail(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): Promise<image.PixelMap>
```

The function generate the destinationImage from sourceImage with necessary scaling operation&lt;br&gt;according to width and height. Different levels of scaling methods are provided to&lt;br&gt;balance performance and image quality. This method uses a promise to return the result.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): Promise<image.PixelMap>--><!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceImage | image.PixelMap | 是 | The source pixelmap. |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The zoom value of width. |
| height | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The zoom value of height. |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | 否 | The quality level. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise instance used to return the PixelMap object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function enhanceDetail can not work correctly due to &lt;br&gt;limited device capabilities. |
| 29200009 | Input value is invalid. This error is returned for &lt;br&gt;all of the following error conditions: &lt;br&gt;1 - Invalid input or output image buffer - The image buffer width(height) &lt;br&gt;is too large or colorspace is incorrect. &lt;br&gt;2 - Invalid parameter - The parameter does not contain valid information, &lt;br&gt;such as detail enhancer level is incorrect. |
| 29200007 | Out of memory. |

## 示例

```TypeScript
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetail(sourceImage: image.PixelMap, width: number, height: number) {
  await videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // 示例：width可配置为1024，height可配置为1280。
  let enhancedPixelMap: Promise<image.PixelMap> =
    imageProcessor.enhanceDetail(sourceImage, width, height, videoProcessingEngine.QualityLevel.HIGH);
}
```

## enhanceDetail

ArkTS-Dyn:
```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>
```

ArkTS-Sta:
```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>
```

The function generate the destinationImage from sourceImage with necessary scaling operation&lt;br&gt;according to the zoom ratio. Different levels of scaling methods are provided to&lt;br&gt;balance performance and image quality. This method uses a promise to return the result.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>--><!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceImage | image.PixelMap | 是 | The source pixelmap. |
| scale | ArkTS-Dyn: number  <br>ArkTS-Sta：double | 是 | The zoom ratio. |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | 否 | The quality level. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise instance used to return the PixelMap object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function enhanceDetail can not work correctly due to &lt;br&gt;limited device capabilities. |
| 29200009 | Input value is invalid. This error is returned for &lt;br&gt;all of the following error conditions: &lt;br&gt;1 - Invalid input or output image buffer - The image buffer width(height) &lt;br&gt;is too large or colorspace is incorrect. &lt;br&gt;2 - Invalid parameter - The parameter does not contain valid information, &lt;br&gt;such as detail enhancer level is incorrect. |
| 29200007 | Out of memory. |

## 示例

```TypeScript
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetail(sourceImage: image.PixelMap, scale: number) {
  await videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // 示例：scale可配置为2.0。
  let enhancedPixelMap: Promise<image.PixelMap> =
    imageProcessor.enhanceDetail(sourceImage, scale, videoProcessingEngine.QualityLevel.HIGH);
}
```

## enhanceDetailSync

ArkTS-Dyn:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap
```

ArkTS-Sta:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap
```

The function generate the destinationImage from sourceImage with necessary scaling operation&lt;br&gt;according to width and height. Different levels of scaling methods are provided to&lt;br&gt;balance performance and image quality.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap--><!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceImage | image.PixelMap | 是 | The source pixelmap. |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The zoom value of width. |
| height | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The zoom value of height. |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | 否 | The quality level. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | Returns the destination pixelmap instance . &lt;br&gt;if the operation is successful; Otherwise, return undefined. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function enhanceDetailSync can not work correctly due &lt;br&gt;to limited device capabilities. |
| 29200009 | Input value is invalid. This error is returned for &lt;br&gt;all of the following error conditions: &lt;br&gt;1 - Invalid input or output image buffer - The image buffer width(height) &lt;br&gt;is too large or colorspace is incorrect. &lt;br&gt;2 - Invalid parameter - The parameter does not contain valid information, &lt;br&gt;such as detail enhancer level is incorrect. |
| 29200004 | Failed to process image buffer. For example, the processing times out. |
| 29200007 | Out of memory. |

## 示例

```TypeScript
import { image, videoProcessingEngine } from '@kit.ImageKit';

sync function enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // 示例：width可配置为1024，height可配置为1280。
  let enhancedPixelMap: image.PixelMap = imageProcessor.enhanceDetailSync(
    sourceImage, width, height, videoProcessingEngine.QualityLevel.HIGH);
}
```

## enhanceDetailSync

ArkTS-Dyn:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap
```

ArkTS-Sta:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap
```

The function generate the destinationImage from sourceImage with necessary scaling operation&lt;br&gt;according to the zoom ratio. Different levels of scaling methods are provided to&lt;br&gt;balance performance and image quality.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap--><!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceImage | image.PixelMap | 是 | The source pixelmap. |
| scale | ArkTS-Dyn: number  <br>ArkTS-Sta：double | 是 | The zoom ratio. |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | 否 | The quality level. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | Returns the destination pixelmap instance &lt;br&gt;if the operation is successful; Otherwise, return undefined. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function enhanceDetailSync can not work correctly due &lt;br&gt;to limited device capabilities. |
| 29200009 | Input value is invalid. This error is returned for &lt;br&gt;all of the following error conditions: &lt;br&gt;1 - Invalid input or output image buffer - The image buffer width(height) &lt;br&gt;is too large or colorspace is incorrect. &lt;br&gt;2 - Invalid parameter - The parameter does not contain valid information, &lt;br&gt;such as detail enhancer level is incorrect. |
| 29200004 | Failed to process image buffer. For example, the processing times out. |
| 29200007 | Out of memory. |

## 示例

```TypeScript
import { image, videoProcessingEngine } from '@kit.ImageKit';

sync function enhanceDetailSync(sourceImage: image.PixelMap, scale: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // 示例：scale可配置为2.0。
  let enhancedPixelMap: image.PixelMap = imageProcessor.enhanceDetailSync(
    sourceImage, scale, videoProcessingEngine.QualityLevel.HIGH);
}
```

