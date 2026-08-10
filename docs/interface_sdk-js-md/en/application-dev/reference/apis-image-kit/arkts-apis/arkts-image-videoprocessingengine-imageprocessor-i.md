# ImageProcessor

Provides the ImageProcessor type, including the processing function.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-videoProcessingEngine-interface ImageProcessor--><!--Device-videoProcessingEngine-interface ImageProcessor-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

## Modules to Import

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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): Promise<image.PixelMap>--><!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceImage | image.PixelMap | Yes | The source pixelmap. |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The zoom value of width. |
| height | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The zoom value of height. |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | No | The quality level. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise instance used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function enhanceDetail can not work correctly due to &lt;br&gt;limited device capabilities. |
| 29200009 | Input value is invalid. This error is returned for &lt;br&gt;all of the following error conditions: &lt;br&gt;1 - Invalid input or output image buffer - The image buffer width(height) &lt;br&gt;is too large or colorspace is incorrect. &lt;br&gt;2 - Invalid parameter - The parameter does not contain valid information, &lt;br&gt;such as detail enhancer level is incorrect. |
| 29200007 | Out of memory. |

## Examples

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

ArkTS-Dyn:
```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>
```

ArkTS-Sta:
```TypeScript
enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>
```

The function generate the destinationImage from sourceImage with necessary scaling operation&lt;br&gt;according to the zoom ratio. Different levels of scaling methods are provided to&lt;br&gt;balance performance and image quality. This method uses a promise to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>--><!--Device-ImageProcessor-enhanceDetail(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceImage | image.PixelMap | Yes | The source pixelmap. |
| scale | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The zoom ratio. |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | No | The quality level. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise instance used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function enhanceDetail can not work correctly due to &lt;br&gt;limited device capabilities. |
| 29200009 | Input value is invalid. This error is returned for &lt;br&gt;all of the following error conditions: &lt;br&gt;1 - Invalid input or output image buffer - The image buffer width(height) &lt;br&gt;is too large or colorspace is incorrect. &lt;br&gt;2 - Invalid parameter - The parameter does not contain valid information, &lt;br&gt;such as detail enhancer level is incorrect. |
| 29200007 | Out of memory. |

## Examples

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

ArkTS-Dyn:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap
```

ArkTS-Sta:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap
```

The function generate the destinationImage from sourceImage with necessary scaling operation&lt;br&gt;according to width and height. Different levels of scaling methods are provided to&lt;br&gt;balance performance and image quality.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap--><!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, width: int, height: int, level?: QualityLevel): image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceImage | image.PixelMap | Yes | The source pixelmap. |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The zoom value of width. |
| height | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The zoom value of height. |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | No | The quality level. |

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | Returns the destination pixelmap instance . &lt;br&gt;if the operation is successful; Otherwise, return undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function enhanceDetailSync can not work correctly due &lt;br&gt;to limited device capabilities. |
| 29200009 | Input value is invalid. This error is returned for &lt;br&gt;all of the following error conditions: &lt;br&gt;1 - Invalid input or output image buffer - The image buffer width(height) &lt;br&gt;is too large or colorspace is incorrect. &lt;br&gt;2 - Invalid parameter - The parameter does not contain valid information, &lt;br&gt;such as detail enhancer level is incorrect. |
| 29200004 | Failed to process image buffer. For example, the processing times out. |
| 29200007 | Out of memory. |

## Examples

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

ArkTS-Dyn:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap
```

ArkTS-Sta:
```TypeScript
enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap
```

The function generate the destinationImage from sourceImage with necessary scaling operation&lt;br&gt;according to the zoom ratio. Different levels of scaling methods are provided to&lt;br&gt;balance performance and image quality.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap--><!--Device-ImageProcessor-enhanceDetailSync(sourceImage: image.PixelMap, scale: double, level?: QualityLevel): image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceImage | image.PixelMap | Yes | The source pixelmap. |
| scale | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The zoom ratio. |
| level | [QualityLevel](arkts-image-videoprocessingengine-qualitylevel-e.md) | No | The quality level. |

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | Returns the destination pixelmap instance &lt;br&gt;if the operation is successful; Otherwise, return undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function enhanceDetailSync can not work correctly due &lt;br&gt;to limited device capabilities. |
| 29200009 | Input value is invalid. This error is returned for &lt;br&gt;all of the following error conditions: &lt;br&gt;1 - Invalid input or output image buffer - The image buffer width(height) &lt;br&gt;is too large or colorspace is incorrect. &lt;br&gt;2 - Invalid parameter - The parameter does not contain valid information, &lt;br&gt;such as detail enhancer level is incorrect. |
| 29200004 | Failed to process image buffer. For example, the processing times out. |
| 29200007 | Out of memory. |

## Examples

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

