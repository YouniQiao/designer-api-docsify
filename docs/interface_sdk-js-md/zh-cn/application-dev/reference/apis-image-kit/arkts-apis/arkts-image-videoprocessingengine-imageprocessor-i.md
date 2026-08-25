# ImageProcessor

提供ImageProcessor类型，包括图像处理功能。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

## 导入模块

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## enhanceDetail

```TypeScript
enhanceDetail(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): Promise<image.PixelMap>
```

根据指定的宽度和高度对源图像进行必要的缩放处理，生成目标图像。 提供不同质量等级的缩放方式，用于平衡处理性能和图像质量。该方法使用Promise返回处理结果。

**起始版本：** 18

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceImage | image.PixelMap | 是 |
| width | number | 是 |
| height | number | 是 |
| level | [QualityLevel](../../apis-camera-kit/arkts-apis/arkts-camera-camera-qualitylevel-e.md) | 否 |

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

## enhanceDetail

```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>
```

根据指定的缩放比例对源图像进行必要的缩放处理，生成目标图像。 提供不同质量等级的缩放方式，用于平衡处理性能和图像质量。该方法使用Promise返回处理结果。

**起始版本：** 18

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceImage | image.PixelMap | 是 |
| scale | number | 是 |
| level | [QualityLevel](../../apis-camera-kit/arkts-apis/arkts-camera-camera-qualitylevel-e.md) | 否 |

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

## enhanceDetailSync

```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap
```

根据指定的宽度和高度对源图像进行必要的缩放处理，生成目标图像。 提供不同质量等级的缩放方式，用于平衡处理性能和图像质量。

**起始版本：** 18

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceImage | image.PixelMap | 是 |
| width | number | 是 |
| height | number | 是 |
| level | [QualityLevel](../../apis-camera-kit/arkts-apis/arkts-camera-camera-qualitylevel-e.md) | 否 |

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

## enhanceDetailSync

```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap
```

根据指定的缩放比例对源图像进行必要的缩放处理，生成目标图像。 提供不同质量等级的缩放方式，用于平衡处理性能和图像质量。

**起始版本：** 18

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceImage | image.PixelMap | 是 |
| scale | number | 是 |
| level | [QualityLevel](../../apis-camera-kit/arkts-apis/arkts-camera-camera-qualitylevel-e.md) | 否 |

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
