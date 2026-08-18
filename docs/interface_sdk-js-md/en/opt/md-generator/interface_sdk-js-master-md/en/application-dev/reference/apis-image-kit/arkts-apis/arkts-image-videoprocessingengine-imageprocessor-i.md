# ImageProcessor

Provides the ImageProcessor type, including the processing function.

**Since:** 23

<!--Device-videoProcessingEngine-interface ImageProcessor--><!--Device-videoProcessingEngine-interface ImageProcessor-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

## Modules to Import

```TypeScript
```

## enhanceDetail

```TypeScript
enhanceDetail(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): Promise<image.PixelMap>
```

The function generate the destinationImage from sourceImage with necessary scaling operation <br>according to width and height. Different levels of scaling methods are provided to <br>balance performance and image quality. This method uses a promise to return the result.

**Since:** 23

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): Promise<image.PixelMap>--><!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceImage | image.PixelMap | Yes |
| width | number | Yes |
| height | number | Yes |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-invalid-value) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |

**Examples**

```TypeScript
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetail(sourceImage: image.PixelMap, width: number, height: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // Example: The width can be set to 1024, and the height can be set to 1280.
  let enhancedPixelmap: Promise<image.PixelMap> =
    imageProcessor.enhanceDetail(sourceImage, width, height, videoProcessingEngine.QualityLevel.HIGH);
}
```

## enhanceDetail

```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>
```

The function generate the destinationImage from sourceImage with necessary scaling operation <br>according to the zoom ratio. Different levels of scaling methods are provided to <br>balance performance and image quality. This method uses a promise to return the result.

**Since:** 23

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>--><!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceImage | image.PixelMap | Yes |
| scale | number | Yes |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-invalid-value) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |

**Examples**

```TypeScript
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetail(sourceImage: image.PixelMap, scale: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // Example: The scale can be set to 2.0.
  let enhancedPixelmap: Promise<image.PixelMap> =
    imageProcessor.enhanceDetail(sourceImage, scale, videoProcessingEngine.QualityLevel.HIGH);
}
```

## enhanceDetailSync

```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap
```

The function generate the destinationImage from sourceImage with necessary scaling operation <br>according to width and height. Different levels of scaling methods are provided to <br>balance performance and image quality.

**Since:** 23

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap--><!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceImage | image.PixelMap | Yes |
| width | number | Yes |
| height | number | Yes |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-invalid-value) |
| [29200004](../errorcode-videoprocessingengine.md#29200004-processing-failure) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |

**Examples**

```TypeScript
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // Example: The width can be set to 1024, and the height can be set to 1280.
  let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
    sourceImage, width, height, videoProcessingEngine.QualityLevel.HIGH);
}
```

## enhanceDetailSync

```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap
```

The function generate the destinationImage from sourceImage with necessary scaling operation <br>according to the zoom ratio. Different levels of scaling methods are provided to <br>balance performance and image quality.

**Since:** 23

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap--><!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceImage | image.PixelMap | Yes |
| scale | number | Yes |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200009](../errorcode-videoprocessingengine.md#29200009-invalid-value) |
| [29200004](../errorcode-videoprocessingengine.md#29200004-processing-failure) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |

**Examples**

```TypeScript
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetailSync(sourceImage: image.PixelMap, scale: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // Example: The scale can be set to 2.0.
  let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
    sourceImage, scale, videoProcessingEngine.QualityLevel.HIGH);
}
```
