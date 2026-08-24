# PixelMap

The **PixelMap** class provides APIs to read or write image data and obtain image information. Before calling any API in PixelMap, you must use [image.createPixelMap](arkts-image-image-createpixelmap-f.md) to create a PixelMap object. Currently, the maximum size of a serialized PixelMap is 128 MB. A larger size will cause a display failure. The size is calculated as follows: Width x Height x [Bytes per pixel](arkts-image-image-pixelmapformat-e.md). Since API version 11, PixelMap supports cross-thread calls through [Worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md). If a PixelMap object is invoked by another thread through [Worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md), all APIs of the PixelMap object cannot be called in the original thread. Otherwise, error 501 is reported, indicating that the server cannot complete the request. Before calling any API in PixelMap, you can use [image.createPixelMap](arkts-image-image-createpixelmap-f.md) to pass pixel data to create a PixelMap object, or use [ImageSource](arkts-multimedia-image.md) to decode an image to a PixelMap object. To develop an atomic service, use [ImageSource](arkts-multimedia-image.md) to create a PixelMap object. Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-image-interface PixelMap--><!--Device-image-interface PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## applyColorSpace

```TypeScript
applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void
```

Performs color space conversion (CSC) on the image pixel color based on a given color space. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void--><!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetColorSpace | colorSpaceManager.ColorSpaceManager | Yes | Target color space. SRGB, DCI_P3, DISPLAY_P3, and ADOBE_RGB_1998 are supported. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [62980104](../errorcode-image.md#62980104-image-initialization-error) | Failed to initialize the internal object. |
| [62980108](../errorcode-image.md#62980108-image-color-conversion-error) | Failed to convert the color space. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |

**Examples**

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function ApplyColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // The colorSpaceManager.ColorSpace object is supported only on 2-in-1 devices/PCs.
  let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
    try {
      pixelMap.applyColorSpace(targetColorSpace, (error: BusinessError) => {
        if (error) {
          console.error(`ApplyColorSpace failed. code is ${error.code}, message is ${error.message}`);
          return;
        } else {
          console.info("Succeeded ApplyColorSpace.");
        }
      });
    } catch (error) {
      console.error(`Failed to apply color space for pixelmap object, error code is ${error}`);
      return;
    }
    console.info('Succeeded in applying color space for pixelmap object.');
  }
}
```

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function ApplyColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // The colorSpaceManager.ColorSpace object is supported only on 2-in-1 devices/PCs.
  let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
      pixelMap.applyColorSpace(targetColorSpace).then(() => {
      console.info('Succeeded in applying color space for pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to apply color space for pixelmap object, error code is ${error}`);
      return;
    });
  }
}
```

## applyColorSpace

```TypeScript
applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>
```

Performs Color Space Converters (CSC) on the image pixel color based on a given color space. This API uses a promise to return the result.

**Since:** 23

<!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>--><!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetColorSpace | colorSpaceManager.ColorSpaceManager | Yes | Target color space. SRGB, DCI_P3, DISPLAY_P3, and ADOBE_RGB_1998 are supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [62980104](../errorcode-image.md#62980104-image-initialization-error) | Failed to initialize the internal object. |
| [62980108](../errorcode-image.md#62980108-image-color-conversion-error) | Failed to convert the color space. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |

**Examples**

See [applyColorSpace](#applycolorspace)

## applyCrop

```TypeScript
applyCrop(region: Region): Promise<void>
```

Crops the PixelMap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyCrop(region: Region): Promise<void>--><!--Device-PixelMap-applyCrop(region: Region): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | The region to crop. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600204](../errorcode-image.md#7600204-invalid-region) | The specified region is invalid or out of range. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. Failed to process pixel data. 2. The system is out of memory. |

## applyCropSync

```TypeScript
applyCropSync(region: Region): void
```

Crops the PixelMap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyCropSync(region: Region): void--><!--Device-PixelMap-applyCropSync(region: Region): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | The region to crop. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600204](../errorcode-image.md#7600204-invalid-region) | The specified region is invalid or out of range. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. Failed to process pixel data. 2. The system is out of memory. |

## applyFlip

```TypeScript
applyFlip(horizontal: boolean, vertical: boolean): Promise<void>
```

Flips the PixelMap in the horizontal and/or vertical directions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyFlip(horizontal: boolean, vertical: boolean): Promise<void>--><!--Device-PixelMap-applyFlip(horizontal: boolean, vertical: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontal | boolean | Yes | Whether to flip horizontally. |
| vertical | boolean | Yes | Whether to flip vertically. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible cause: The system is out of memory. |

## applyFlipSync

```TypeScript
applyFlipSync(horizontal: boolean, vertical: boolean): void
```

Flips the PixelMap in the horizontal and/or vertical directions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyFlipSync(horizontal: boolean, vertical: boolean): void--><!--Device-PixelMap-applyFlipSync(horizontal: boolean, vertical: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontal | boolean | Yes | Whether to flip horizontally. |
| vertical | boolean | Yes | Whether to flip vertically. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible cause: The system is out of memory. |

## applyRotate

```TypeScript
applyRotate(angle: double): Promise<void>
```

Rotates the PixelMap.Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyRotate(angle: double): Promise<void>--><!--Device-PixelMap-applyRotate(angle: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double | Yes | The rotation angle in degrees. Unit: Degree. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

## applyRotateSync

```TypeScript
applyRotateSync(angle: double): void
```

Rotates the PixelMap.Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyRotateSync(angle: double): void--><!--Device-PixelMap-applyRotateSync(angle: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double | Yes | The rotation angle in degrees. Unit: Degree. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

## applyScale

```TypeScript
applyScale(x: double, y: double, level?: AntiAliasingLevel): Promise<void>
```

Scales the PixelMap in the horizontal and/or vertical dimensions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyScale(x: double, y: double, level?: AntiAliasingLevel): Promise<void>--><!--Device-PixelMap-applyScale(x: double, y: double, level?: AntiAliasingLevel): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The scale ratio of width. Unit: Percentage. |
| y | double | Yes | The scale ratio of height. Unit: Percentage. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | The anti-aliasing algorithm to be used. Default value: NONE. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

## applyScaleSync

```TypeScript
applyScaleSync(x: double, y: double, level?: AntiAliasingLevel): void
```

Scales the PixelMap in the horizontal and/or vertical dimensions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyScaleSync(x: double, y: double, level?: AntiAliasingLevel): void--><!--Device-PixelMap-applyScaleSync(x: double, y: double, level?: AntiAliasingLevel): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The scale ratio of width. Unit: Percentage. |
| y | double | Yes | The scale ratio of height. Unit: Percentage. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | The anti-aliasing algorithm to be used. Default value: NONE. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

## applyTranslate

```TypeScript
applyTranslate(x: double, y: double): Promise<void>
```

Repositions the PixelMap in the horizontal and/or vertical directions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyTranslate(x: double, y: double): Promise<void>--><!--Device-PixelMap-applyTranslate(x: double, y: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The distance in pixels to move in the horizontal direction. Unit: px. |
| y | double | Yes | The distance in pixels to move in the vertical direction. Unit: px. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

## applyTranslateSync

```TypeScript
applyTranslateSync(x: double, y: double): void
```

Repositions the PixelMap in the horizontal and/or vertical directions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyTranslateSync(x: double, y: double): void--><!--Device-PixelMap-applyTranslateSync(x: double, y: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The distance in pixels to move in the horizontal direction. Unit: px. |
| y | double | Yes | The distance in pixels to move in the vertical direction. Unit: px. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

## clone

```TypeScript
clone(): Promise<PixelMap>
```

Copies this PixelMap object. This API uses a promise to return the result.

**Since:** 23

<!--Device-PixelMap-clone(): Promise<PixelMap>--><!--Device-PixelMap-clone(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [501](../errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980102](../errorcode-image.md#62980102-memory-allocation-error-for-images) | Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data. |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) | Image YUV And ASTC types are not supported. |
| [62980104](../errorcode-image.md#62980104-image-initialization-error) | Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
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
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // An image containing HeifsMetadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.clone().then((clonePixelMap: image.PixelMap) => {
      console.info('Succeeded clone pixelmap.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to clone pixelmap. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

## cloneSync

```TypeScript
cloneSync(): PixelMap
```

Copies this PixelMap object. This API returns the result synchronously.

**Since:** 23

<!--Device-PixelMap-cloneSync(): PixelMap--><!--Device-PixelMap-cloneSync(): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. If the operation fails, an error is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [501](../errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980102](../errorcode-image.md#62980102-memory-allocation-error-for-images) | Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data. |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) | Image YUV And ASTC types are not supported. |
| [62980104](../errorcode-image.md#62980104-image-initialization-error) | Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap. |
| [62980106](../errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function CloneSync(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    try {
      let clonedPixelMap:image.PixelMap = pixelMap.cloneSync();
    } catch(e) {
      let error = e as BusinessError;
      console.error(`clone pixelmap error. code is ${error.code}, message is ${error.message}`);
    }
  }
}
```

## convertPixelFormat

```TypeScript
convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>
```

The method is used for the transformation of the image formats. Pixel data will be changed by calling this method.

**Since:** 23

<!--Device-PixelMap-convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>--><!--Device-PixelMap-convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetPixelFormat | PixelMapFormat | Yes | The pixel format for pixelmap conversion. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid input parameter. |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |
| [62980274](../errorcode-image.md#62980274-failed-to-convert-images) | The conversion failed. |
| [62980276](../errorcode-image.md#62980276-unsupported-image-conversion-target-type) | The type to be converted is an unsupported target pixel format. |
| [62980178](../errorcode-image.md#62980178-failure-in-creating-a-pixelmap) | Failed to create the pixelmap. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ConvertPixelFormat(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    // Set the target pixel format to NV12.
    let targetPixelFormat = image.PixelMapFormat.NV12;
    pixelMap.convertPixelFormat(targetPixelFormat).then(() => {
      // The pixelMap is converted to the NV12 format.
      console.info('PixelMapFormat convert Succeeded');
    }).catch((error: BusinessError) => {
      // The pixelMap fails to be converted to the NV12 format.
      console.error(`PixelMapFormat convert Failed. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(): Promise<PixelMap>
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMap](#extractalphapixelmap) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-createAlphaPixelmap(): Promise<PixelMap>--><!--Device-PixelMap-createAlphaPixelmap(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateAlphaPixelmap(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.createAlphaPixelmap().then((alphaPixelMap: image.PixelMap) => {
      console.info('Succeeded in creating alpha pixelmap.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to create alpha pixelmap. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateAlphaPixelmap(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.createAlphaPixelmap((err: BusinessError, alphaPixelMap: image.PixelMap) => {
      if (alphaPixelMap == undefined) {
        console.error(`Failed to obtain new pixel map. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info('Succeeded in obtaining new pixel map.');
      }
    })
  }
}
```

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API returns the result through a callback.Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMap](#extractalphapixelmap) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void--><!--Device-PixelMap-createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object. |

**Examples**

See [createAlphaPixelmap](#createalphapixelmap)

## createAlphaPixelmapSync

```TypeScript
createAlphaPixelmapSync(): PixelMap
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. This API returns the result synchronously. It is invalid for YUV images.Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMapSync](#extractalphapixelmapsync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-createAlphaPixelmapSync(): PixelMap--><!--Device-PixelMap-createAlphaPixelmapSync(): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. If the operation fails, an error is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function CreateAlphaPixelmapSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let pixelmap : image.PixelMap = pixelMap.createAlphaPixelmapSync();
    return pixelmap;
  }
  return undefined;
}
```

## createCroppedAndScaledPixelMap

```TypeScript
createCroppedAndScaledPixelMap(region: Region, x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>
```

Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the width and height, and anti-aliasing level. This API uses a promise to return the result.

**Since:** 23

<!--Device-PixelMap-createCroppedAndScaledPixelMap(region: Region, x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>--><!--Device-PixelMap-createCroppedAndScaledPixelMap(region: Region, x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Area to crop. It must be within the original image's dimension (in pixels). |
| x | double | Yes | Scale factor of the width. It must not be **0**. |
| y | double | Yes | Scale factor of the height. It must not be **0**. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | Anti-aliasing level. Default value: **NONE**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | The PixelMap has been released. |
| [7600204](../errorcode-image.md#7600204-invalid-region) | Invalid region. |
| [7600205](../errorcode-image.md#7600205-unsupported-format) | Unsupported memory format or pixel format. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Memory alloc failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function DemoCreateCroppedAndScaledPixelMap(pixelMap: PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: number = 2.0;
  const scaleY: number = 2.0;
  pixelMap.createCroppedAndScaledPixelMap(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH)
    .then((croppedAndScaled: PixelMap) => {
      console.info('PixelMap crop and scale succeeded.');
    })
    .catch((error: BusinessError) => {
      console.error(`PixelMap crop and scale failed. Error code: ${error.code}, message: ${error.message}`);
    });
}
```

## createCroppedAndScaledPixelMapSync

```TypeScript
createCroppedAndScaledPixelMapSync(region: Region, x: double, y: double, level?: AntiAliasingLevel): PixelMap
```

Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the width and height, and anti-aliasing level. This API returns the result synchronously.

**Since:** 23

<!--Device-PixelMap-createCroppedAndScaledPixelMapSync(region: Region, x: double, y: double, level?: AntiAliasingLevel): PixelMap--><!--Device-PixelMap-createCroppedAndScaledPixelMapSync(region: Region, x: double, y: double, level?: AntiAliasingLevel): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Area to crop. It must be within the original image's dimension (in pixels). |
| x | double | Yes | Scale factor of the width. It must not be **0**. |
| y | double | Yes | Scale factor of the height. It must not be **0**. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | Anti-aliasing level. Default value: **NONE**. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. If the operation fails, an error is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | The PixelMap has been released. |
| [7600204](../errorcode-image.md#7600204-invalid-region) | Invalid region. |
| [7600205](../errorcode-image.md#7600205-unsupported-format) | Unsupported memory format or pixel format. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Memory alloc failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function DemoCreateCroppedAndScaledPixelMapSync(pixelMap: PixelMap) {
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
  } catch (e) {
    const error = e as BusinessError;
    console.error(`PixelMap crop and scale failed. Error code: ${error.code}, message: ${error.message}`);
  }
}
```

## createScaledPixelMap

```TypeScript
createScaledPixelMap(x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>
```

Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. This API uses a promise to return the result.

**Since:** 23

<!--Device-PixelMap-createScaledPixelMap(x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>--><!--Device-PixelMap-createScaledPixelMap(x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Scale factor of the width. |
| y | double | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateScaledPixelMap(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
      pixelMap.createScaledPixelMap(scaleX, scaleY, image.AntiAliasingLevel.LOW).then((scaledPixelMap: image.PixelMap) => {
      console.info('Succeeded in creating scaledPixelMap.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to create scaledPixelMap. Error code is ${error.code}, error message is ${error.message}`);
    })
  }
}
```

## createScaledPixelMapSync

```TypeScript
createScaledPixelMapSync(x: double, y: double, level?: AntiAliasingLevel): PixelMap
```

Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. This API returns the result synchronously.

**Since:** 23

<!--Device-PixelMap-createScaledPixelMapSync(x: double, y: double, level?: AntiAliasingLevel): PixelMap--><!--Device-PixelMap-createScaledPixelMapSync(x: double, y: double, level?: AntiAliasingLevel): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Scale factor of the width. |
| y | double | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. If the operation fails, an error is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function CreateScaledPixelMapSync(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    let scaledPixelMap = pixelMap.createScaledPixelMapSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
  }
}
```

## crop

```TypeScript
crop(region: Region, callback: AsyncCallback<void>): void
```

Crops this image based on a given size. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [applyCrop](#applycrop) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-crop(region: Region, callback: AsyncCallback<void>): void--><!--Device-PixelMap-crop(region: Region, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Size of the image after cropping. The value cannot exceed the width or height of the image. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Crop(pixelMap:image.PixelMap) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.crop(region, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in cropping pixelmap.");
      }
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Crop(pixelMap:image.PixelMap) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.crop(region).then(() => {
      console.info('Succeeded in cropping pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}`);

    });
  }
}
```

## crop

```TypeScript
crop(region: Region): Promise<void>
```

Crops a PixelMap based on a given size. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyCrop](#applycrop) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-crop(region: Region): Promise<void>--><!--Device-PixelMap-crop(region: Region): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Size of the image after cropping. The value cannot exceed the width or height of the image. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [crop](#crop)

## cropSync

```TypeScript
cropSync(region: Region): void
```

Crops this image based on a given size. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyCropSync](#applycropsync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-cropSync(region: Region): void--><!--Device-PixelMap-cropSync(region: Region): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Size of the image after cropping. The value cannot exceed the width or height of the image. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function CropSync(pixelMap:image.PixelMap) {
  let region : image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.cropSync(region);
  }
}
```

## extractAlphaPixelMap

```TypeScript
extractAlphaPixelMap(): Promise<PixelMap>
```

Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-extractAlphaPixelMap(): Promise<PixelMap>--><!--Device-PixelMap-extractAlphaPixelMap(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | A Promise of the new ALPHA_U8 format PixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The current PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The current PixelMap has been passed across threads. |
| [7600305](../errorcode-image.md#7600305-failed-to-create-the-pixelmap) | Failed to create the PixelMap. Possible cause: Current PixelMap data is corrupted. |
| [7600306](../errorcode-image.md#7600306-data-conversion-failed) | Failed to convert the data. Possible causes: 1. Failed to perform pixel format conversion. 2. The system is out of memory. |

## extractAlphaPixelMapSync

```TypeScript
extractAlphaPixelMapSync(): PixelMap
```

Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-extractAlphaPixelMapSync(): PixelMap--><!--Device-PixelMap-extractAlphaPixelMapSync(): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | A new ALPHA_U8 format PixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The current PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The current PixelMap has been passed across threads. |
| [7600305](../errorcode-image.md#7600305-failed-to-create-the-pixelmap) | Failed to create the PixelMap. Possible cause: Current PixelMap data is corrupted. |
| [7600306](../errorcode-image.md#7600306-data-conversion-failed) | Failed to convert the data. Possible causes: 1. Failed to perform pixel format conversion. 2. The system is out of memory. |

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void
```

Flips this image horizontally or vertically, or both. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [applyFlip](#applyflip) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void--><!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontal | boolean | Yes | Whether to flip the image horizontally. **true** to flip the image horizontally, **false** otherwise. |
| vertical | boolean | Yes | Whether to flip the image vertically. **true** to flip the image vertically, **false** otherwise. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Flip(pixelMap:image.PixelMap) {
  let horizontal: boolean = true;
  let vertical: boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flip(horizontal, vertical, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in flipping pixelmap.");
      }
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Flip(pixelMap:image.PixelMap) {
  let horizontal: boolean = true;
  let vertical: boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flip(horizontal, vertical).then(() => {
      console.info('Succeeded in flipping pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean): Promise<void>
```

Flips a PixelMap based on a given angle. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyFlip](#applyflip) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean): Promise<void>--><!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontal | boolean | Yes | Whether to flip the image horizontally. **true** to flip the image horizontally, **false** otherwise. |
| vertical | boolean | Yes | Whether to flip the image vertically. **true** to flip the image vertically, **false** otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [flip](#flip)

## flipSync

```TypeScript
flipSync(horizontal: boolean, vertical: boolean): void
```

Flips this image horizontally or vertically, or both. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyFlipSync](#applyflipsync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-flipSync(horizontal: boolean, vertical: boolean): void--><!--Device-PixelMap-flipSync(horizontal: boolean, vertical: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontal | boolean | Yes | Whether to flip the image horizontally. **true** to flip the image horizontally, **false** otherwise. |
| vertical | boolean | Yes | Whether to flip the image vertically. **true** to flip the image vertically, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function FlipSync(pixelMap:image.PixelMap) {
  let horizontal : boolean = true;
  let vertical : boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flipSync(horizontal, vertical);
  }
}
```

## getBytesNumberPerRow

```TypeScript
getBytesNumberPerRow(): int
```

Obtains the number of bytes per row of this image. Unit: bytes.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getBytesNumberPerRow(): int--><!--Device-PixelMap-getBytesNumberPerRow(): int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Number of bytes per row. |

**Examples**

```TypeScript
function GetBytesNumberPerRow(pixelMap: image.PixelMap) {
  let rowCount: number = pixelMap.getBytesNumberPerRow();
}
```

## getColorSpace

```TypeScript
getColorSpace(): colorSpaceManager.ColorSpaceManager
```

Obtains the color space of this image.

**Since:** 23

<!--Device-PixelMap-getColorSpace(): colorSpaceManager.ColorSpaceManager--><!--Device-PixelMap-getColorSpace(): colorSpaceManager.ColorSpaceManager-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| colorSpaceManager.ColorSpaceManager | Color space obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980101](../errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) | The image data is not supported. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function GetColorSpace(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let csm = pixelMap.getColorSpace();
  }
}
```

## getDensity

```TypeScript
getDensity(): int
```

Obtains the pixel density of this image. Unit: ppi (pixels/inch)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getDensity(): int--><!--Device-PixelMap-getDensity(): int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Pixel density, in ppi. |

**Examples**

```TypeScript
function GetDensity(pixelMap: image.PixelMap) {
  let getDensity: number = pixelMap.getDensity();
}
```

## getImageInfo

```TypeScript
getImageInfo(): Promise<ImageInfo>
```

Obtains the image information of a PixelMap. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getImageInfo(): Promise<ImageInfo>--><!--Device-PixelMap-getImageInfo(): Promise<ImageInfo>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Promise used to return the image information. |

**Examples**

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
      if (imageInfo != undefined) {
        console.info(`Succeeded in obtaining the image pixel map information ${imageInfo.size.height}`);
      }
    }).catch((error: BusinessError) => {
      console.error(`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function GetImageInfoSync(pixelMap : image.PixelMap){
  if (pixelMap != undefined) {
    pixelMap.getImageInfo((error: BusinessError, imageInfo: image.ImageInfo) => {
      if (error) {
        console.error(`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}`);
        return;
      } else {
        console.info(`Succeeded in obtaining the image pixel map information ${imageInfo.size.height}`);
      }
    })
  }
}
```

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo>): void
```

Obtains the image information. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getImageInfo(callback: AsyncCallback<ImageInfo>): void--><!--Device-PixelMap-getImageInfo(callback: AsyncCallback<ImageInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error object. |

**Examples**

See [getImageInfo](#getimageinfo)

## getImageInfoSync

```TypeScript
getImageInfoSync(): ImageInfo
```

Obtains the image information. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-PixelMap-getImageInfoSync(): ImageInfo--><!--Device-PixelMap-getImageInfoSync(): ImageInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) | Image information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function GetImageInfoSync(context : Context) {
  // "test.jpg" is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let imageInfo = imageSource.getImageInfoSync(0);
  if (imageInfo == undefined) {
    console.error('Failed to obtain the image information.');
  } else {
    console.info('Succeeded in obtaining the image information.');
    console.info('imageInfo.size.height:' + imageInfo.size.height);
    console.info('imageInfo.size.width:' + imageInfo.size.width);
  }
}
```

```TypeScript
function GetImageInfoSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let imageInfo : image.ImageInfo = pixelMap.getImageInfoSync();
    return imageInfo;
  }
  return undefined;
}
```

## getMetadata

```TypeScript
getMetadata(key: HdrMetadataKey): HdrMetadataValue
```

Obtains the value of the metadata with a given key in this PixelMap.

**Since:** 23

<!--Device-PixelMap-getMetadata(key: HdrMetadataKey): HdrMetadataValue--><!--Device-PixelMap-getMetadata(key: HdrMetadataKey): HdrMetadataValue-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md) | Yes | Key of the HDR metadata. |

**Return value:**

| Type | Description |
| --- | --- |
| [HdrMetadataValue](arkts-image-image-hdrmetadatavalue-t.md) | Value of the metadata with the given key. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980173](../errorcode-image.md#62980173-dma-memory-space-error) | The DMA memory does not exist. |
| [62980302](../errorcode-image.md#62980302-memory-copy-failed) | Memory copy failed. Possibly caused by invalid metadata value. |

**Examples**

```TypeScript
async function GetAuxPictureObjMetadata(auxPictureObj: image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let auxPictureObjMetaData: image.Metadata | null = await auxPictureObj.getMetadata(metadataType);
    if (auxPictureObjMetaData != null) {
      console.info('Get AuxPictureObj Metadata success' );
    } else {
      console.error('Get AuxPictureObj Metadata failed');
    }
  } else {
    console.error('Get AuxPictureObj is null.');
  }
}
```

```TypeScript
async function GetMetadata(img : image.Image) {
  try {
    let staticMetadata = img.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
    console.info(`getMetadata:${staticMetadata}`);
  } catch (err) {
    console.error('getMetadata failed' + err);
  }
}
```

```TypeScript
async function GetPictureObjMetadataProperties(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let pictureObjMetaData: image.Metadata = await pictureObj.getMetadata(metadataType);
    if (pictureObjMetaData != null) {
      console.info('get picture metadata success');
    } else {
      console.error('get picture metadata is failed');
    }
  } else {
    console.error(" pictureObj is null");
  }
}
```

```TypeScript
async function GetMetadata(context: Context) {
  // Replace app.media.startIcon with a local HDR image.
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
    try {
      let staticMetadata = pixelmap.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
      console.info(`getMetadata:${staticMetadata}`);
    } catch (e) {
      console.error('pixelmap create failed' + e);
    }
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

## getPixelBytesNumber

```TypeScript
getPixelBytesNumber(): int
```

Obtains the total number of bytes of this image. Unit: bytes.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getPixelBytesNumber(): int--><!--Device-PixelMap-getPixelBytesNumber(): int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Total number of bytes. |

**Examples**

```TypeScript
function GetPixelBytesNumber(pixelMap: image.PixelMap) {
  let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
}
```

## getUniqueId

```TypeScript
getUniqueId(): int
```

Obtains the unique ID of this PixelMap.

**Since:** 23

<!--Device-PixelMap-getUniqueId(): int--><!--Device-PixelMap-getUniqueId(): int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Unique ID. The value is a positive integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | The PixelMap has been released. |

**Examples**

```TypeScript
function DemoGetUniqueId(pixelMap: PixelMap) {
  const uniqueId: number = pixelMap.getUniqueId();
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

**Since:** 23

<!--Device-PixelMap-isReleased(): boolean--><!--Device-PixelMap-isReleased(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the PixelMap object is released. **true** if released; **false** otherwise. |

**Examples**

```TypeScript
async function DemoIsReleased(pixelMap: PixelMap) { // Unreleased PixelMap.
  pixelMap.isReleased(); // Return false.
  await pixelMap.release();
  pixelMap.isReleased(); // Return true.
}
```

## marshalling

```TypeScript
marshalling(sequence: rpc.MessageSequence): void
```

Marshals this PixelMap object and writes it to a MessageSequence object.

**Since:** 23

<!--Device-PixelMap-marshalling(sequence: rpc.MessageSequence): void--><!--Device-PixelMap-marshalling(sequence: rpc.MessageSequence): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sequence | rpc.MessageSequence | Yes | MessageSequence object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980097](../errorcode-image.md#62980097-pixelmap-serialization-failed) | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**Examples**

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
      console.info('Marshalling success !');
      return true;
    } else {
      console.error('Marshalling failed !');
      return false;
    }
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    this.picture = image.createPictureFromParcel(messageSequence);
    this.picture.getMainPixelmap().getImageInfo().then((imageInfo : image.ImageInfo) => {
      console.info(`Unmarshalling to get mainPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
    }).catch((error: BusinessError) => {
      console.error(`Unmarshalling failed error.code: ${error.code} ,error.message: ${error.message}`);
    });
    return true;
  }
}

async function Marshalling_UnMarshalling(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let parcelable: MySequence = new MySequence(pictureObj);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    // Implement serialization.
    data.writeParcelable(parcelable);
    let ret: MySequence = new MySequence(pictureObj);
    // Implement deserialization.
    data.readParcelable(ret);
  } else {
    console.error('PictureObj is null');
  }
}
```

```TypeScript
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel_map: image.PixelMap;
  constructor(conPixelMap : image.PixelMap) {
    this.pixel_map = conPixelMap;
  }
  marshalling(messageSequence : rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel: image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: image.PixelMap) => {
        this.pixel_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
          console.info(`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}`);
        })
      })
    });
    return true;
  }
}
async function Marshalling() {
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
  }
  let pixelMap: image.PixelMap | undefined = undefined;
  await image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
    pixelMap = srcPixelMap;
  })
  if (pixelMap != undefined) {
    // Implement serialization.
    let parcelable: MySequence = new MySequence(pixelMap);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // Implement deserialization to obtain data through the RPC.
    let ret: MySequence = new MySequence(pixelMap);
    data.readParcelable(ret);
  }
}
```

## opacity

```TypeScript
opacity(rate: double, callback: AsyncCallback<void>): void
```

Sets an opacity rate for this image. This API uses an asynchronous callback to return the result. It is invalid for YUV images.Starting from API 26.0.0, it is recommended to use [setOpacity](#setopacity) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-opacity(rate: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-opacity(rate: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | double | Yes | Opacity rate. The value range is (0,1]. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Opacity(pixelMap:image.PixelMap) {
  let rate: number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacity(rate, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to set opacity. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in setting opacity.");
      }
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Opacity(pixelMap:image.PixelMap) {
  let rate: number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacity(rate).then(() => {
      console.info('Succeeded in setting opacity.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to set opacity. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

## opacity

```TypeScript
opacity(rate: double): Promise<void>
```

Sets an opacity rate for this image. It is invalid for YUV images. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [setOpacity](#setopacity) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-opacity(rate: double): Promise<void>--><!--Device-PixelMap-opacity(rate: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | double | Yes | Opacity rate. The value range is (0,1]. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [opacity](#opacity)

## opacitySync

```TypeScript
opacitySync(rate: double): void
```

Sets an opacity rate for this image. This API returns the result synchronously. It is invalid for YUV images.Starting from API 26.0.0, it is recommended to use [setOpacitySync](#setopacitysync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-opacitySync(rate: double): void--><!--Device-PixelMap-opacitySync(rate: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | double | Yes | Opacity rate. The value range is (0,1]. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function OpacitySync(pixelMap:image.PixelMap) {
  let rate : number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacitySync(rate);
  }
}
```

## readAllPixelsToBuffer

```TypeScript
readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads all the pixel data from the PixelMap and writes the data to a buffer. The resulting data will be in the same pixel format as the PixelMap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>--><!--Device-PixelMap-readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | ArrayBuffer | Yes | The buffer to receive the pixel data from the PixelMap. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the buffer is too small. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## readAllPixelsToBufferSync

```TypeScript
readAllPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads all the pixel data from the PixelMap and writes the data to a buffer. The resulting data will be in the same pixel format as the PixelMap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-readAllPixelsToBufferSync(dst: ArrayBuffer): void--><!--Device-PixelMap-readAllPixelsToBufferSync(dst: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | ArrayBuffer | Yes | The buffer to receive the pixel data from the PixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the buffer is too small. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## readPixels

```TypeScript
readPixels(area: PositionArea): Promise<void>
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md).pixels buffer. This API uses a promise to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)Starting from API 26.0.0, it is recommended to use [readPixelsToArea](#readpixelstoarea) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readPixels(area: PositionArea): Promise<void>--><!--Device-PixelMap-readPixels(area: PositionArea): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area from which the pixels will be read. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsRGBA(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8 is the size of the PixelMap buffer to create. The value is calculated as follows: height * width * 4.
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area).then(() => {
      console.info('Succeeded in reading the image data in the area.'); // Called if the condition is met.
      console.info('RGBA data is ', new Uint8Array(area.pixels));
    }).catch((error: BusinessError) => {
      console.error("Failed to read the image data in the area. code is ", error);// Called if the condition is not met.
    })
  }
}

async function ReadPixelsYUV(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6 is the size of the PixelMap buffer to create. The value is calculated as follows: height * width * 1.5.
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area).then(() => {
      console.info('Succeeded in reading the image data in the area.'); // Called if the condition is met.
      console.info('YUV data is ', new Uint8Array(area.pixels));
    }).catch((error: BusinessError) => {
      console.error("Failed to read the image data in the area. code is ", error);// Called if the condition is not met.
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsRGBA(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8 is the size of the PixelMap buffer to create. The value is calculated as follows: height * width * 4.
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area, (error: BusinessError) => {
      if (error) {
        console.error("Failed to read pixelmap from the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in reading pixelmap from the specified area.');
        console.info('RGBA data is ', new Uint8Array(area.pixels));
      }
    })
  }
}

async function ReadPixelsYUV(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6 is the size of the PixelMap buffer to create. The value is calculated as follows: height * width * 1.5.
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area, (error: BusinessError) => {
      if (error) {
        console.error("Failed to read pixelmap from the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in reading pixelmap from the specified area.');
        console.info('YUV data is ', new Uint8Array(area.pixels));
      }
    })
  }
}
```

## readPixels

```TypeScript
readPixels(area: PositionArea, callback: AsyncCallback<void>): void
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md).pixels buffer. This API uses an asynchronous callback to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)Starting from API 26.0.0, it is recommended to use [readPixelsToArea](#readpixelstoarea) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readPixels(area: PositionArea, callback: AsyncCallback<void>): void--><!--Device-PixelMap-readPixels(area: PositionArea, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area from which the pixels will be read. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

See [readPixels](#readpixels)

## readPixelsSync

```TypeScript
readPixelsSync(area: PositionArea): void
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md).region of this PixelMap object in the BGRA_8888 format and writes the data to the [PositionArea](arkts-image-image-positionarea-i.md).pixels buffer. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [readPixelsToAreaSync](#readpixelstoareasync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-readPixelsSync(area: PositionArea): void--><!--Device-PixelMap-readPixelsSync(area: PositionArea): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area from which the pixels will be read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function ReadPixelsSync(pixelMap : image.PixelMap) {
  const area : image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixelsSync(area);
  }
}
```

## readPixelsToArea

```TypeScript
readPixelsToArea(area: PositionArea): Promise<void>
```

Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-readPixelsToArea(area: PositionArea): Promise<void>--><!--Device-PixelMap-readPixelsToArea(area: PositionArea): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area of the PixelMap to read the data. Data will be read from the PixelMap and copied into PositionArea.pixels. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## readPixelsToAreaSync

```TypeScript
readPixelsToAreaSync(area: PositionArea): void
```

Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-readPixelsToAreaSync(area: PositionArea): void--><!--Device-PixelMap-readPixelsToAreaSync(area: PositionArea): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area of the PixelMap to read the data. Data will be read from the PixelMap and copied into PositionArea.pixels. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [readAllPixelsToBuffer](#readallpixelstobuffer) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer): Promise<void>--><!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // An HDR-compatible image is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
  if(auxPictureObj != null) {
    await auxPictureObj.readPixelsToBuffer().then((pixelsBuffer: ArrayBuffer) => {
      console.info('Read pixels to buffer success.' );
    }).catch((error: BusinessError) => {
      console.error(`Read pixels to buffer failed error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObj is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBuffer(readBuffer).then(() => {
      console.info('Succeeded in reading image pixel data.'); // Called if the condition is met.
    }).catch((error: BusinessError) => {
      console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`); // Called if no condition is met.
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBuffer(readBuffer, (error: BusinessError, res: void) => {
      if(error) {
        console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`); // Called if no condition is met.
        return;
      } else {
        console.info('Succeeded in reading image pixel data.'); // Called if the condition is met.
      }
    })
  }
}
```

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [readAllPixelsToBuffer](#readallpixelstobuffer) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void--><!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

See [readPixelsToBuffer](#readpixelstobuffer)

## readPixelsToBufferSync

```TypeScript
readPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [readAllPixelsToBufferSync](#readallpixelstobuffersync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-PixelMap-readPixelsToBufferSync(dst: ArrayBuffer): void--><!--Device-PixelMap-readPixelsToBufferSync(dst: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function ReadPixelsToBufferSync(pixelMap : image.PixelMap) {
  const bufferSize = pixelMap.getPixelBytesNumber();
  const readBuffer = new ArrayBuffer(bufferSize);
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBufferSync(readBuffer);
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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-release(callback: AsyncCallback<void>): void--><!--Device-PixelMap-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

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
}
```

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

```TypeScript
async function Release(pictureObj : image.Picture) {
  let funcName = "Release";
  if (pictureObj != null) {
    pictureObj.release();
    if (pictureObj.getMainPixelmap() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    await pixelMap.release().then(() => {
      console.info('Succeeded in releasing pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to release pixelmap object. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.release((err: BusinessError) => {
      if (err) {
        console.error(`Failed to release pixelmap object. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info('Succeeded in releasing pixelmap object.');
      }
    })
  }
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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-release(): Promise<void>--><!--Device-PixelMap-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [release](#release)

## rotate

```TypeScript
rotate(angle: double, callback: AsyncCallback<void>): void
```

Rotates this image based on a given angle. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [applyRotate](#applyrotate) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-rotate(angle: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-rotate(angle: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double | Yes | Angle to rotate. Unit: degrees. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Rotate(pixelMap:image.PixelMap) {
  let angle: number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotate(angle, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in rotating pixelmap.");
      }
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Rotate(pixelMap:image.PixelMap) {
  let angle: number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotate(angle).then(() => {
      console.info('Succeeded in rotating pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

## rotate

```TypeScript
rotate(angle: double): Promise<void>
```

Rotates a PixelMap based on a given angle. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyRotate](#applyrotate) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-rotate(angle: double): Promise<void>--><!--Device-PixelMap-rotate(angle: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double | Yes | Angle to rotate. Unit: degrees. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [rotate](#rotate)

## rotateSync

```TypeScript
rotateSync(angle: double): void
```

Rotates this image based on a given angle. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyRotateSync](#applyrotatesync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-rotateSync(angle: double): void--><!--Device-PixelMap-rotateSync(angle: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double | Yes | Angle to rotate. Unit: degrees. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function RotateSync(pixelMap: image.PixelMap) {
  let angle : number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotateSync(angle);
  }
}
```

## scale

```TypeScript
scale(x: double, y: double, callback: AsyncCallback<void>): void
```

Scales this image based on the scale factors of the width and height. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [applyScale](#applyscale) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-scale(x: double, y: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-scale(x: double, y: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Scale factor of the width. |
| y | double | Yes | Scale factor of the height. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Scale(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in scaling pixelmap.");
      }
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Scale(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY).then(() => {
      console.info('Succeeded in scaling pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ScaleSync(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY, image.AntiAliasingLevel.LOW).then(() => {
      console.info('Succeeded in scaling pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

## scale

```TypeScript
scale(x: double, y: double): Promise<void>
```

Scales this image based on the scale factors of the width and height. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyScale](#applyscale) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-scale(x: double, y: double): Promise<void>--><!--Device-PixelMap-scale(x: double, y: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Scale factor of the width. |
| y | double | Yes | Scale factor of the height. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [scale](#scale)

## scale

```TypeScript
scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>
```

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [applyScale](#applyscale) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-PixelMap-scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>--><!--Device-PixelMap-scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Scale factor of the width. |
| y | double | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | Yes | Anti-aliasing level. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

See [scale](#scale)

## scaleSync

```TypeScript
scaleSync(x: double, y: double): void
```

Scales this image based on the scale factors of the width and height. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyScaleSync](#applyscalesync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-scaleSync(x: double, y: double): void--><!--Device-PixelMap-scaleSync(x: double, y: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Scale factor of the width. |
| y | double | Yes | Scale factor of the height. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function ScaleSync(pixelMap: image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scaleSync(scaleX, scaleY);
  }
}
```

```TypeScript
function ScaleSync(pixelMap: image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scaleSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
  }
}
```

## scaleSync

```TypeScript
scaleSync(x: double, y: double, level: AntiAliasingLevel): void
```

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [applyScaleSync](#applyscalesync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-scaleSync(x: double, y: double, level: AntiAliasingLevel): void--><!--Device-PixelMap-scaleSync(x: double, y: double, level: AntiAliasingLevel): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Scale factor of the width. |
| y | double | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | Yes | Anti-aliasing level. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

See [scaleSync](#scalesync)

## setColorSpace

```TypeScript
setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void
```

Set color space of pixel map.This method is only used to set the colorspace property of pixelmap, while all pixel data remains the same after calling this method. If you want to change colorspace for all pixels, use method {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager)} or {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager, AsyncCallback&lt;void&gt;)}.

**Since:** 23

<!--Device-PixelMap-setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void--><!--Device-PixelMap-setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpaceManager | Yes | The color space for pixel map. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980111](../errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | If the image parameter invalid. |

**Examples**

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function SetColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // The colorSpaceManager.ColorSpace object is supported only on 2-in-1 devices/PCs.
  let csm: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
    pixelMap.setColorSpace(csm);
  }
}
```

## setMemoryNameSync

```TypeScript
setMemoryNameSync(name: string): void
```

Sets a memory name for this PixelMap.

**Since:** 23

<!--Device-PixelMap-setMemoryNameSync(name: string): void--><!--Device-PixelMap-setMemoryNameSync(name: string): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Memory name, which can be set only for a PixelMap with the DMA or ASHMEM memory format. The name length for DMA memory settings should be within the range of 1 to 255 bytes. For ASHMEM memory settings, the name length should be within the range of 1 to 244 bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.The length of the input parameter is too long. 2.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980286](../errorcode-image.md#62980286-failed-to-set-a-memory-identifier-for-a-pixelmap) | Memory format not supported. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function SetMemoryNameSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    try {
      pixelMap.setMemoryNameSync("PixelMapName Test");
    } catch(e) {
      let error = e as BusinessError;
      console.error(`setMemoryNameSync error. code is ${error.code}, message is ${error.message}`);
    }
  }
}
```

## setMetadata

```TypeScript
setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>
```

Sets the value for the metadata with a given key in this PixelMap. This API uses a promise to return the result.

**Since:** 23

<!--Device-PixelMap-setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>--><!--Device-PixelMap-setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md) | Yes | Key of the HDR metadata. |
| value | [HdrMetadataValue](arkts-image-image-hdrmetadatavalue-t.md) | Yes | Value of the metadata. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980173](../errorcode-image.md#62980173-dma-memory-space-error) | The DMA memory does not exist. |
| [62980302](../errorcode-image.md#62980302-memory-copy-failed) | Memory copy failed. Possibly caused by invalid metadata value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetAuxPictureObjMetadata(exifContext: Context, auxPictureObj: image.AuxiliaryPicture) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    auxPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Set metadata success');
    }).catch((error: BusinessError) => {
      console.error(`Set metadata failed.error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObjMetaData is null');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetPictureObjMetadata(exifContext: Context) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (exifPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    exifPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Set metadata success');
    }).catch((error: BusinessError) => {
      console.error('Failed to set metadata. error.code: ' +JSON.stringify(error.code) + ' ,error.message:' + JSON.stringify(error.message));
    });
  } else {
    console.error('exifPictureOb is null');
  }
}
```

For details about how to create a PixelMap with DMA_ALLOC memory, see [Default Memory Allocation Mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#default-memory-allocation-method).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import {image} from '@kit.ImageKit';

function SetMetadata(pixelMap: image.PixelMap) { // The input parameter pixelMap must be of the DMA_ALLOC memory type. For details about how to create a PixelMap with DMA_ALLOC memory, see the preceding link.
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
    console.info('Succeeded in setting pixelMap metadata.');
  }).catch((error: BusinessError) => {
    console.error("Failed to set the metadata.code ", error);
  })
}
```

## setOpacity

```TypeScript
setOpacity(value: double): Promise<void>
```

Sets opacity of the PixelMap. Every pixel will be set to the same opacity value.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-setOpacity(value: double): Promise<void>--><!--Device-PixelMap-setOpacity(value: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The target opacity value to be set. Unit: Percentage, Value range: (0,1]. The valid range is (0.0, 1.0] where 1.0 is fully opaque and becoming transparent as it approaches 0.0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: The specified value is out of range. |
| [7600207](../errorcode-image.md#7600207-unsupported-data-format) | Unsupported data format. Possible cause: Alpha type is not supported. |

## setOpacitySync

```TypeScript
setOpacitySync(value: double): void
```

Sets opacity of the PixelMap. Every pixel will be set to the same opacity value.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-setOpacitySync(value: double): void--><!--Device-PixelMap-setOpacitySync(value: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The target opacity value to be set. Unit: Percentage, Value range: (0,1]. The valid range is (0.0, 1.0] where 1.0 is fully opaque and becoming transparent as it approaches 0.0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: The specified value is out of range. |
| [7600207](../errorcode-image.md#7600207-unsupported-data-format) | Unsupported data format. Possible cause: Alpha type is not supported. |

## setTransferDetached

```TypeScript
setTransferDetached(detached: boolean): void
```

Sets whether to detach from the original thread when this PixelMap is transmitted across threads. This API applies to the scenario where the PixelMap needs to be released immediately.

**Since:** 23

<!--Device-PixelMap-setTransferDetached(detached: boolean): void--><!--Device-PixelMap-setTransferDetached(detached: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| detached | boolean | Yes | Whether to detach from the original thread. **true** to detach, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
import { common } from '@kit.AbilityKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
// Child thread method.
async function loadPixelMap(rawFileDescriptor: number): Promise<PixelMap> {
  // Create an ImageSource instance.
  const imageSource = image.createImageSource(rawFileDescriptor);
  // Create a pixelMap.
  const pixelMap = imageSource.createPixelMapSync();
  // Release the ImageSource instance.
  imageSource.release();
  // Disconnect the reference of the original thread after the cross-thread transfer of the pixelMap is complete.
  pixelMap.setTransferDetached(true);
  // Return the pixelMap to the main thread.
  return pixelMap;
}

@Entry
@Component
struct Demo {
  @State pixelMap: PixelMap | undefined = undefined;
  // Main thread method.
  private loadImageFromThread(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const resourceMgr = context.resourceManager;
    // 'example.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
    resourceMgr.getRawFd('example.jpg').then(rawFileDescriptor => {
      taskpool.execute(loadPixelMap, rawFileDescriptor).then(pixelMap => {
        if (pixelMap) {
          this.pixelMap = pixelMap as PixelMap;
          console.info('Succeeded in creating pixelMap.');
          // The main thread releases the pixelMap. Because setTransferDetached has been called when the child thread returns pixelMap, the pixelMap can be released immediately.
          this.pixelMap.release();
        } else {
          console.error('Failed to create pixelMap.');
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

**Since:** 23

<!--Device-PixelMap-toSdr(): Promise<void>--><!--Device-PixelMap-toSdr(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980137](../errorcode-image.md#62980137-invalid-image-operation) | Invalid image operation. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ToSdr(context: Context) {
  // Replace app.media.startIcon with a local HDR image.
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
    pixelmap.toSdr().then(() => {
      let imageInfo = pixelmap.getImageInfoSync();
      console.info("after toSdr ,imageInfo isHdr:" + imageInfo.isHdr);
    }).catch((err: BusinessError) => {
      console.error(`Failed to set sdr. code is ${err.code}, message is ${err.message}`);
    });
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

## translate

```TypeScript
translate(x: double, y: double, callback: AsyncCallback<void>): void
```

Translates this image based on given coordinates. This API uses an asynchronous callback to return the result. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.Starting from API 26.0.0, it is recommended to use [applyTranslate](#applytranslate) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-translate(x: double, y: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-translate(x: double, y: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X coordinate to translate, in px. |
| y | double | Yes | Y coordinate to translate, in px. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Translate(pixelMap:image.PixelMap) {
  let translateX: number = 50.0;
  let translateY: number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translate(translateX, translateY, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in translating pixelmap.");
      }
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Translate(pixelMap:image.PixelMap) {
  let translateX: number = 50.0;
  let translateY: number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translate(translateX, translateY).then(() => {
      console.info('Succeeded in translating pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

## translate

```TypeScript
translate(x: double, y: double): Promise<void>
```

Translates a PixelMap based on given coordinates. This API uses a promise to return the result. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.Starting from API 26.0.0, it is recommended to use [applyTranslate](#applytranslate) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-translate(x: double, y: double): Promise<void>--><!--Device-PixelMap-translate(x: double, y: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X coordinate to translate, in px. |
| y | double | Yes | Y coordinate to translate, in px. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [translate](#translate)

## translateSync

```TypeScript
translateSync(x: double, y: double): void
```

Translates this image based on given coordinates. This API returns the result synchronously. The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.Starting from API 26.0.0, it is recommended to use [applyTranslateSync](#applytranslatesync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-translateSync(x: double, y: double): void--><!--Device-PixelMap-translateSync(x: double, y: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X coordinate to translate, in px. |
| y | double | Yes | Y coordinate to translate, in px. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function TranslateSync(pixelMap:image.PixelMap) {
  let translateX : number = 50.0;
  let translateY : number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translateSync(translateX, translateY);
  }
}
```

## unmarshalling

```TypeScript
unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>
```

Unmarshals a MessageSequence object to obtain a PixelMap object. To create a PixelMap object in synchronous mode, use [createPixelMapFromParcel](arkts-image-image-createpixelmapfromparcel-f.md).

**Since:** 23

<!--Device-PixelMap-unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>--><!--Device-PixelMap-unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sequence | rpc.MessageSequence | Yes | MessageSequence object that stores the PixelMap information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980097](../errorcode-image.md#62980097-pixelmap-serialization-failed) | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |
| [62980096](../errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |

**Examples**

```TypeScript
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel_map: image.PixelMap;
  constructor(conPixelMap: image.PixelMap) {
    this.pixel_map = conPixelMap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel : image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap : image.PixelMap) => {
        this.pixel_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo : image.ImageInfo) => {
          console.info(`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}`);
        })
      })
    });
    return true;
  }
}
async function Unmarshalling() {
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
  }
  let pixelMap: image.PixelMap | undefined = undefined;
  await image.createPixelMap(color, opts).then((srcPixelMap : image.PixelMap) => {
    pixelMap = srcPixelMap;
  })
  if (pixelMap != undefined) {
    // Implement serialization.
    let parcelable: MySequence = new MySequence(pixelMap);
    let data : rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // Implement deserialization to obtain data through the RPC.
    let ret : MySequence = new MySequence(pixelMap);
    data.readParcelable(ret);
  }
}
```

## writeAllPixelsFromBuffer

```TypeScript
writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>
```

Reads the pixel data from a buffer and writes the data to the PixelMap. The source data must be in the same pixel format as the PixelMap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>--><!--Device-PixelMap-writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ArrayBuffer | Yes | The buffer that contains pixel data to be written to the PixelMap. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is not editable or is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the buffer is too small. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## writeAllPixelsFromBufferSync

```TypeScript
writeAllPixelsFromBufferSync(src: ArrayBuffer): void
```

Reads the pixel data from a buffer and writes the data to the PixelMap. The source data must be in the same pixel format as the PixelMap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-writeAllPixelsFromBufferSync(src: ArrayBuffer): void--><!--Device-PixelMap-writeAllPixelsFromBufferSync(src: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ArrayBuffer | Yes | The buffer that contains pixel data to be written to the PixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is not editable or is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the buffer is too small. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer): Promise<void>
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API uses a promise to return the result.Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBuffer](#writeallpixelsfrombuffer) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer): Promise<void>--><!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function WriteBufferToPixels(pixelMap:image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixels(color).then(() => {
      console.info("Succeeded in writing data from a buffer to a PixelMap.");
    }).catch((error: BusinessError) => {
      console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function WriteBufferToPixels(pixelMap:image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixels(color, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
        return;
      } else {
        console.info("Succeeded in writing data from a buffer to a PixelMap.");
      }
    })
  }
}
```

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API uses an asynchronous callback to return the result.Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBuffer](#writeallpixelsfrombuffer) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void--><!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the pixels in the buffer are successfully written to the PixelMap, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

See [writeBufferToPixels](#writebuffertopixels)

## writeBufferToPixelsSync

```TypeScript
writeBufferToPixelsSync(src: ArrayBuffer): void
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBufferSync](#writeallpixelsfrombuffersync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PixelMap-writeBufferToPixelsSync(src: ArrayBuffer): void--><!--Device-PixelMap-writeBufferToPixelsSync(src: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function WriteBufferToPixelsSync(pixelMap:image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  let bufferArr : Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixelsSync(color);
  }
}
```

## writePixels

```TypeScript
writePixels(area: PositionArea): Promise<void>
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md).pixels in this PixelMap object. This API uses a promise to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)Starting from API 26.0.0, it is recommended to use [writePixelsFromArea](#writepixelsfromarea) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-writePixels(area: PositionArea): Promise<void>--><!--Device-PixelMap-writePixels(area: PositionArea): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area to which the pixels will be written. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function WritePixelsRGBA(pixelMap:image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8 is the size of the PixelMap buffer to create. The value is calculated as follows: height * width * 4.
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area).then(() => {
      console.info('Succeeded in writing pixelmap into the specified area.');
    }).catch((error: BusinessError) => {
      console.error("Failed to write pixelmap into the specified area. code is ", error);
    })
  }
}

async function WritePixelsYUV(pixelMap:image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6 is the size of the PixelMap buffer to create. The value is calculated as follows: height * width * 1.5.
    offset: 0,
    stride: 8, // This variable is not used by writePixels when the PixelMap is in YUV format.
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area).then(() => {
      console.info('Succeeded in writing pixelmap into the specified area.');
    }).catch((error: BusinessError) => {
      console.error("Failed to write pixelmap into the specified area. code is ", error);
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function WritePixelsRGBA(pixelMap:image.PixelMap) {
  const area: image.PositionArea = { pixels: new ArrayBuffer(8), // 8 is the size of the PixelMap buffer to create. The value is calculated as follows: height * width * 4.
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area, (error : BusinessError) => {
      if (error) {
        console.error("Failed to write pixelmap into the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in writing pixelmap into the specified area.');
      }
    })
  }
}

async function WritePixelsYUV(pixelMap:image.PixelMap) {
  const area: image.PositionArea = { pixels: new ArrayBuffer(6), // 6 is the size of the PixelMap buffer to create. The value is calculated as follows: height * width * 1.5.
    offset: 0,
    stride: 8, // This variable is not used by writePixels when the PixelMap is in YUV format.
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area, (error : BusinessError) => {
      if (error) {
        console.error("Failed to write pixelmap into the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in writing pixelmap into the specified area.');
      }
    })
  }
}
```

## writePixels

```TypeScript
writePixels(area: PositionArea, callback: AsyncCallback<void>): void
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md).pixels in this PixelMap object. This API uses an asynchronous callback to return the result. You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**. YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component) RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)Starting from API 26.0.0, it is recommended to use [writePixelsFromArea](#writepixelsfromarea) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-writePixels(area: PositionArea, callback: AsyncCallback<void>): void--><!--Device-PixelMap-writePixels(area: PositionArea, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area to which the pixels will be written. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

See [writePixels](#writepixels)

## writePixelsFromArea

```TypeScript
writePixelsFromArea(area: PositionArea): Promise<void>
```

Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-writePixelsFromArea(area: PositionArea): Promise<void>--><!--Device-PixelMap-writePixelsFromArea(area: PositionArea): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area of the PixelMap to write the data. Data will be copied from PositionArea.pixels to the PixelMap. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is not editable or is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## writePixelsFromAreaSync

```TypeScript
writePixelsFromAreaSync(area: PositionArea): void
```

Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-writePixelsFromAreaSync(area: PositionArea): void--><!--Device-PixelMap-writePixelsFromAreaSync(area: PositionArea): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area of the PixelMap to write the data. Data will be copied from PositionArea.pixels to the PixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600105](../errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600106](../errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is not editable or is locked. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## writePixelsSync

```TypeScript
writePixelsSync(area: PositionArea): void
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md).region buffer in the BGRA_8888 format and writes the data to the area specified by [PositionArea](arkts-image-image-positionarea-i.md).pixels in this PixelMap object. This API returns the result synchronously.Starting from API 26.0.0, it is recommended to use [writePixelsFromAreaSync](#writepixelsfromareasync) instead for better exception handling capabilities.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-PixelMap-writePixelsSync(area: PositionArea): void--><!--Device-PixelMap-writePixelsSync(area: PositionArea): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area to which the pixels will be written. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

**Examples**

```TypeScript
function WritePixelsSync(pixelMap:image.PixelMap) {
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
  if (pixelMap != undefined) {
    pixelMap.writePixelsSync(area);
  }
}
```

## isEditable

```TypeScript
readonly isEditable: boolean
```

Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides better image rendering and transmission performance.<br> This API can be used in atomic services since API version 11.<br> This API can be used in ArkTS widgets since API version 12.

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readonly isEditable: boolean--><!--Device-PixelMap-readonly isEditable: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## isStrideAlignment

```TypeScript
readonly isStrideAlignment: boolean
```

Whether the row data of the image is memory aligned. The value **true** means that the row data is memory-aligned, and there may be blank bytes padded at the end of each row to meet alignment requirements. The value **false** means that the row data is not memory-aligned, and rows are packed contiguously with no padding bytes at the end.

**Type:** boolean

**Since:** 23

<!--Device-PixelMap-readonly isStrideAlignment: boolean--><!--Device-PixelMap-readonly isStrideAlignment: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

