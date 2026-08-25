# ImageProcessor

Provides the ImageProcessor type, including the processing function.

**Since:** 18

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

## Modules to Import

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## enhanceDetail

```TypeScript
enhanceDetail(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): Promise<image.PixelMap>
```

The function generate the destinationImage from sourceImage with necessary scaling operation according to width and height. Different levels of scaling methods are provided to balance performance and image quality. This method uses a promise to return the result.

**Since:** 18

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceImage | image.PixelMap | Yes |
| width | number | Yes |
| height | number | Yes |
| level | [QualityLevel](../../apis-camera-kit/arkts-apis/arkts-camera-camera-qualitylevel-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-invalid-value) |

## enhanceDetail

```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>
```

The function generate the destinationImage from sourceImage with necessary scaling operation according to the zoom ratio. Different levels of scaling methods are provided to balance performance and image quality. This method uses a promise to return the result.

**Since:** 18

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceImage | image.PixelMap | Yes |
| scale | number | Yes |
| level | [QualityLevel](../../apis-camera-kit/arkts-apis/arkts-camera-camera-qualitylevel-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-invalid-value) |

## enhanceDetailSync

```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap
```

The function generate the destinationImage from sourceImage with necessary scaling operation according to width and height. Different levels of scaling methods are provided to balance performance and image quality.

**Since:** 18

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceImage | image.PixelMap | Yes |
| width | number | Yes |
| height | number | Yes |
| level | [QualityLevel](../../apis-camera-kit/arkts-apis/arkts-camera-camera-qualitylevel-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200004](../errorcode-videoprocessingengine.md#29200004-processing-failure) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-invalid-value) |

## enhanceDetailSync

```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap
```

The function generate the destinationImage from sourceImage with necessary scaling operation according to the zoom ratio. Different levels of scaling methods are provided to balance performance and image quality.

**Since:** 18

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceImage | image.PixelMap | Yes |
| scale | number | Yes |
| level | [QualityLevel](../../apis-camera-kit/arkts-apis/arkts-camera-camera-qualitylevel-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200004](../errorcode-videoprocessingengine.md#29200004-processing-failure) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-invalid-value) |
