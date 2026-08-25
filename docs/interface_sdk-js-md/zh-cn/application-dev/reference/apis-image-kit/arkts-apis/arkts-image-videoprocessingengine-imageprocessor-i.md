# ImageProcessor

提供ImageProcessor类型，包括图像处理功能。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

## 导入模块

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';
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

根据指定的宽度和高度对源图像进行必要的缩放处理，生成目标图像。 <br>提供不同质量等级的缩放方式，用于平衡处理性能和图像质量。该方法使用Promise返回处理结果。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceImage | image.PixelMap | 是 |
| width | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| height | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-内存不足) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-值无效) |

**示例**

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

## enhanceDetail

ArkTS-Dyn:
```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>
```

ArkTS-Sta:
```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>
```

根据指定的缩放比例对源图像进行必要的缩放处理，生成目标图像。 <br>提供不同质量等级的缩放方式，用于平衡处理性能和图像质量。该方法使用Promise返回处理结果。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceImage | image.PixelMap | 是 |
| scale | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-内存不足) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-值无效) |

**示例**

参见 [enhanceDetail](#enhancedetail)

## enhanceDetailSync

ArkTS-Dyn:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap
```

ArkTS-Sta:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap
```

根据指定的宽度和高度对源图像进行必要的缩放处理，生成目标图像。 <br>提供不同质量等级的缩放方式，用于平衡处理性能和图像质量。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceImage | image.PixelMap | 是 |
| width | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| height | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29200004](../errorcode-videoprocessingengine.md#29200004-处理失败) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-内存不足) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-值无效) |

**示例**

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

## enhanceDetailSync

ArkTS-Dyn:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap
```

ArkTS-Sta:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap
```

根据指定的缩放比例对源图像进行必要的缩放处理，生成目标图像。 <br>提供不同质量等级的缩放方式，用于平衡处理性能和图像质量。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceImage | image.PixelMap | 是 |
| scale | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29200004](../errorcode-videoprocessingengine.md#29200004-处理失败) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-内存不足) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-值无效) |

**示例**

参见 [enhanceDetailSync](#enhancedetailsync)
