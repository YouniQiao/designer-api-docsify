# PixelMap

The **PixelMap** class provides APIs to read or write image data and obtain image information. Before calling any API in PixelMap, you must use  
[image.createPixelMap](arkts-image-image-createpixelmap-f.md#createPixelMap-1)to create a PixelMap object. Currently, the maximum size of a serialized PixelMap is 128 MB. A larger size will cause a display failure. The size is calculated as follows: Width x Height x  
[Bytes per pixel](arkts-image-image-pixelmapformat-e.md#PixelMapFormat).Since API version 11, PixelMap supports cross-thread calls through [Worker](@ohos.worker). If a PixelMap object is invoked by another thread through [Worker](@ohos.worker), all APIs of the PixelMap object cannot be called in the original thread. Otherwise, error 501 is reported, indicating that the server cannot complete the request.Before calling any API in PixelMap, you can use  
[image.createPixelMap](arkts-image-image-createpixelmap-f.md#createPixelMap-1)to pass pixel data to create a PixelMap object, or use [ImageSource](arkts-multimedia-image.md#image) to decode an image to a PixelMap object.To develop an atomic service, use [ImageSource](arkts-multimedia-image.md#image) to create a PixelMap object.Images occupy a large amount of memory. When you finish using a PixelMap instance, call  
[release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void--><!--Device-PixelMap-applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetColorSpace | colorSpaceManager.ColorSpaceManager | Yes | Target color space. SRGB, DCI_P3, DISPLAY_P3, and ADOBE_RGB_1998 are supported. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [62980115](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980104-image-initialization-error) | Failed to initialize the internal object. |
| [62980108](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980108-image-color-conversion-error) | Failed to convert the color space. |

## applyColorSpace

```TypeScript
applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>
```

Performs Color Space Converters (CSC) on the image pixel color based on a given color space. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [62980115](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980104-image-initialization-error) | Failed to initialize the internal object. |
| [62980108](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980108-image-color-conversion-error) | Failed to convert the color space. |

## applyCrop

```TypeScript
applyCrop(region: Region): Promise<void>
```

Crops the PixelMap.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. Failed to process pixel data. 2. The system is out of memory. |
| [7600204](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600204-invalid-region) | The specified region is invalid or out of range. |

## applyCropSync

```TypeScript
applyCropSync(region: Region): void
```

Crops the PixelMap.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. Failed to process pixel data. 2. The system is out of memory. |
| [7600204](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600204-invalid-region) | The specified region is invalid or out of range. |

## applyFlip

```TypeScript
applyFlip(horizontal: boolean, vertical: boolean): Promise<void>
```

Flips the PixelMap in the horizontal and/or vertical directions.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible cause: The system is out of memory. |

## applyFlipSync

```TypeScript
applyFlipSync(horizontal: boolean, vertical: boolean): void
```

Flips the PixelMap in the horizontal and/or vertical directions.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible cause: The system is out of memory. |

## applyRotate

ArkTS-Dyn:
```TypeScript
applyRotate(angle: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
applyRotate(angle: double): Promise<void>
```

Rotates the PixelMap.

Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyRotate(angle: double): Promise<void>--><!--Device-PixelMap-applyRotate(angle: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The rotation angle in degrees. Unit: Degree. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

## applyRotateSync

ArkTS-Dyn:
```TypeScript
applyRotateSync(angle: number): void
```

ArkTS-Sta:
```TypeScript
applyRotateSync(angle: double): void
```

Rotates the PixelMap.

Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyRotateSync(angle: double): void--><!--Device-PixelMap-applyRotateSync(angle: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The rotation angle in degrees. Unit: Degree. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyScale(x: double, y: double, level?: AntiAliasingLevel): Promise<void>--><!--Device-PixelMap-applyScale(x: double, y: double, level?: AntiAliasingLevel): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The scale ratio of width. Unit: Percentage. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The scale ratio of height. Unit: Percentage. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | The anti-aliasing algorithm to be used. Default value: NONE. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyScaleSync(x: double, y: double, level?: AntiAliasingLevel): void--><!--Device-PixelMap-applyScaleSync(x: double, y: double, level?: AntiAliasingLevel): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The scale ratio of width. Unit: Percentage. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The scale ratio of height. Unit: Percentage. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | The anti-aliasing algorithm to be used. Default value: NONE. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyTranslate(x: double, y: double): Promise<void>--><!--Device-PixelMap-applyTranslate(x: double, y: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The distance in pixels to move in the horizontal direction. Unit: px. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The distance in pixels to move in the vertical direction. Unit: px. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-applyTranslateSync(x: double, y: double): void--><!--Device-PixelMap-applyTranslateSync(x: double, y: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The distance in pixels to move in the horizontal direction. Unit: px. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The distance in pixels to move in the vertical direction. Unit: px. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |

## clone

```TypeScript
clone(): Promise<PixelMap>
```

Copies this PixelMap object. This API uses a promise to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PixelMap-clone(): Promise<PixelMap>--><!--Device-PixelMap-clone(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980103-unsupported-image-type) | Image YUV And ASTC types are not supported. |
| [62980102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980102-memory-allocation-error-for-images) | Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data. |
| [62980104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980104-image-initialization-error) | Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap. |
| [62980106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |

## cloneSync

```TypeScript
cloneSync(): PixelMap
```

Copies this PixelMap object. This API returns the result synchronously.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PixelMap-cloneSync(): PixelMap--><!--Device-PixelMap-cloneSync(): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. If the operation fails, an error is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980103-unsupported-image-type) | Image YUV And ASTC types are not supported. |
| [62980102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980102-memory-allocation-error-for-images) | Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data. |
| [62980104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980104-image-initialization-error) | Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap. |
| [62980106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980106-too-large-image-data) | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |

## convertPixelFormat

```TypeScript
convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>
```

The method is used for the transformation of the image formats. Pixel data will be changed by calling this method.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

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
| [62980115](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980115-invalid-image-parameter) | Invalid input parameter. |
| [62980274](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980274-failed-to-convert-images) | The conversion failed. |
| [62980178](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980178-failure-in-creating-a-pixelmap) | Failed to create the pixelmap. |
| [62980276](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980276-unsupported-image-conversion-target-type) | The type to be converted is an unsupported target pixel format. |
| [62980111](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(): Promise<PixelMap>
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMap](#extractAlphaPixelMap) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-createAlphaPixelmap(): Promise<PixelMap>--><!--Device-PixelMap-createAlphaPixelmap(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API returns the result through a callback.

Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMap](#extractAlphaPixelMap) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void--><!--Device-PixelMap-createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;PixelMap&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object. |

## createAlphaPixelmapSync

```TypeScript
createAlphaPixelmapSync(): PixelMap
```

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. This API returns the result synchronously. It is invalid for YUV images.

Starting from API 26.0.0, it is recommended to use [extractAlphaPixelMapSync](#extractAlphaPixelMapSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-createAlphaPixelmapSync(): PixelMap--><!--Device-PixelMap-createAlphaPixelmapSync(): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. If the operation fails, an error is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

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

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-PixelMap-createCroppedAndScaledPixelMap(region: Region, x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>--><!--Device-PixelMap-createCroppedAndScaledPixelMap(region: Region, x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Area to crop. It must be within the original image's dimension (in pixels). |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. It must not be **0**. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. It must not be **0**. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | Anti-aliasing level. Default value: **NONE**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | The PixelMap has been released. |
| [7600205](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600205-unsupported-format) | Unsupported memory format or pixel format. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Memory alloc failed. |
| [7600204](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600204-invalid-region) | Invalid region. |

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

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-PixelMap-createCroppedAndScaledPixelMapSync(region: Region, x: double, y: double, level?: AntiAliasingLevel): PixelMap--><!--Device-PixelMap-createCroppedAndScaledPixelMapSync(region: Region, x: double, y: double, level?: AntiAliasingLevel): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Area to crop. It must be within the original image's dimension (in pixels). |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. It must not be **0**. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. It must not be **0**. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | Anti-aliasing level. Default value: **NONE**. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. If the operation fails, an error is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | The PixelMap has been released. |
| [7600205](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600205-unsupported-format) | Unsupported memory format or pixel format. |
| [7600301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600301-memory-allocation-failure) | Memory alloc failed. |
| [7600204](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600204-invalid-region) | Invalid region. |

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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PixelMap-createScaledPixelMap(x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>--><!--Device-PixelMap-createScaledPixelMap(x: double, y: double, level?: AntiAliasingLevel): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PixelMap-createScaledPixelMapSync(x: double, y: double, level?: AntiAliasingLevel): PixelMap--><!--Device-PixelMap-createScaledPixelMapSync(x: double, y: double, level?: AntiAliasingLevel): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | No | Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. If the operation fails, an error is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## crop

```TypeScript
crop(region: Region, callback: AsyncCallback<void>): void
```

Crops this image based on a given size. This API uses an asynchronous callback to return the result.

Starting from API 26.0.0, it is recommended to use [applyCrop](#applyCrop) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-crop(region: Region, callback: AsyncCallback<void>): void--><!--Device-PixelMap-crop(region: Region, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Size of the image after cropping. The value cannot exceed the width or height of the image. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## crop

```TypeScript
crop(region: Region): Promise<void>
```

Crops a PixelMap based on a given size. This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [applyCrop](#applyCrop) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

## cropSync

```TypeScript
cropSync(region: Region): void
```

Crops this image based on a given size. This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [applyCropSync](#applyCropSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-cropSync(region: Region): void--><!--Device-PixelMap-cropSync(region: Region): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Size of the image after cropping. The value cannot exceed the width or height of the image. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## extractAlphaPixelMap

```TypeScript
extractAlphaPixelMap(): Promise<PixelMap>
```

Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600306](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600306-data-conversion-failed) | Failed to convert the data. Possible causes: 1. Failed to perform pixel format conversion. 2. The system is out of memory. |
| [7600305](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600305-failed-to-create-the-pixelmap) | Failed to create the PixelMap. Possible cause: Current PixelMap data is corrupted. |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The current PixelMap has been passed across threads. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The current PixelMap has been released. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |

## extractAlphaPixelMapSync

```TypeScript
extractAlphaPixelMapSync(): PixelMap
```

Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600306](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600306-data-conversion-failed) | Failed to convert the data. Possible causes: 1. Failed to perform pixel format conversion. 2. The system is out of memory. |
| [7600305](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600305-failed-to-create-the-pixelmap) | Failed to create the PixelMap. Possible cause: Current PixelMap data is corrupted. |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The current PixelMap has been passed across threads. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The current PixelMap has been released. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void
```

Flips this image horizontally or vertically, or both. This API uses an asynchronous callback to return the result.

Starting from API 26.0.0, it is recommended to use [applyFlip](#applyFlip) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void--><!--Device-PixelMap-flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontal | boolean | Yes | Whether to flip the image horizontally. **true** to flip the image horizontally, **false** otherwise. |
| vertical | boolean | Yes | Whether to flip the image vertically. **true** to flip the image vertically, **false** otherwise. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean): Promise<void>
```

Flips a PixelMap based on a given angle. This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [applyFlip](#applyFlip) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

## flipSync

```TypeScript
flipSync(horizontal: boolean, vertical: boolean): void
```

Flips this image horizontally or vertically, or both. This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [applyFlipSync](#applyFlipSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

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
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

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

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getBytesNumberPerRow(): int--><!--Device-PixelMap-getBytesNumberPerRow(): int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Number of bytes per row. |

## getColorSpace

```TypeScript
getColorSpace(): colorSpaceManager.ColorSpaceManager
```

Obtains the color space of this image.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PixelMap-getColorSpace(): colorSpaceManager.ColorSpaceManager--><!--Device-PixelMap-getColorSpace(): colorSpaceManager.ColorSpaceManager-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| colorSpaceManager.ColorSpaceManager | Color space obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980115](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |
| [62980101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980101-incorrect-input-image-data) | The image data is abnormal. |
| [62980103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980103-unsupported-image-type) | The image data is not supported. |

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getDensity(): int--><!--Device-PixelMap-getDensity(): int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Pixel density, in ppi. |

## getImageInfo

```TypeScript
getImageInfo(): Promise<ImageInfo>
```

Obtains the image information of a PixelMap. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getImageInfo(): Promise<ImageInfo>--><!--Device-PixelMap-getImageInfo(): Promise<ImageInfo>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Promise used to return the image information. |

## getImageInfo

```TypeScript
getImageInfo(callback: AsyncCallback<ImageInfo>): void
```

Obtains the image information. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getImageInfo(callback: AsyncCallback<ImageInfo>): void--><!--Device-PixelMap-getImageInfo(callback: AsyncCallback<ImageInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful , **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error object. |

## getImageInfoSync

```TypeScript
getImageInfoSync(): ImageInfo
```

Obtains the image information. This API returns the result synchronously.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getImageInfoSync(): ImageInfo--><!--Device-PixelMap-getImageInfoSync(): ImageInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) | Image information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## getMetadata

```TypeScript
getMetadata(key: HdrMetadataKey): HdrMetadataValue
```

Obtains the value of the metadata with a given key in this PixelMap.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

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
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980173](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980173-dma-memory-space-error) | The DMA memory does not exist. |
| [62980302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980302-memory-copy-failed) | Memory copy failed. Possibly caused by invalid metadata value. |

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

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-getPixelBytesNumber(): int--><!--Device-PixelMap-getPixelBytesNumber(): int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Total number of bytes. |

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

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-PixelMap-getUniqueId(): int--><!--Device-PixelMap-getUniqueId(): int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Unique ID. The value is a positive integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | The PixelMap has been released. |

## isReleased

```TypeScript
isReleased(): boolean
```

Checks whether this PixelMap object is released. If released, any attempt to access the internal data of this object will fail.

> **NOTE：**
> 
> Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
> by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-PixelMap-isReleased(): boolean--><!--Device-PixelMap-isReleased(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the PixelMap object is released. **true** if released; **false** otherwise. |

## marshalling

```TypeScript
marshalling(sequence: rpc.MessageSequence): void
```

Marshals this PixelMap object and writes it to a MessageSequence object.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PixelMap-marshalling(sequence: rpc.MessageSequence): void--><!--Device-PixelMap-marshalling(sequence: rpc.MessageSequence): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sequence | rpc.MessageSequence | Yes | MessageSequence object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980097](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980097-pixelmap-serialization-failed) | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |
| [62980115](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |

## opacity

ArkTS-Dyn:
```TypeScript
opacity(rate: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
opacity(rate: double, callback: AsyncCallback<void>): void
```

Sets an opacity rate for this image. This API uses an asynchronous callback to return the result. It is invalid for YUV images.

Starting from API 26.0.0, it is recommended to use [setOpacity](#setOpacity) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-opacity(rate: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-opacity(rate: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Opacity rate. The value range is (0,1]. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## opacity

ArkTS-Dyn:
```TypeScript
opacity(rate: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
opacity(rate: double): Promise<void>
```

Sets an opacity rate for this image. It is invalid for YUV images. This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [setOpacity](#setOpacity) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-opacity(rate: double): Promise<void>--><!--Device-PixelMap-opacity(rate: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Opacity rate. The value range is (0,1]. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## opacitySync

ArkTS-Dyn:
```TypeScript
opacitySync(rate: number): void
```

ArkTS-Sta:
```TypeScript
opacitySync(rate: double): void
```

Sets an opacity rate for this image. This API returns the result synchronously. It is invalid for YUV images.

Starting from API 26.0.0, it is recommended to use [setOpacitySync](#setOpacitySync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-opacitySync(rate: double): void--><!--Device-PixelMap-opacitySync(rate: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Opacity rate. The value range is (0,1]. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## readAllPixelsToBuffer

```TypeScript
readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads all the pixel data from the PixelMap and writes the data to a buffer.The resulting data will be in the same pixel format as the PixelMap.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the buffer is too small. |
| [7600302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## readAllPixelsToBufferSync

```TypeScript
readAllPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads all the pixel data from the PixelMap and writes the data to a buffer.The resulting data will be in the same pixel format as the PixelMap.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the buffer is too small. |
| [7600302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## readPixels

```TypeScript
readPixels(area: PositionArea): Promise<void>
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region of this PixelMap object in the BGRA_8888 format and writes the data to the  
[PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels buffer. This API uses a promise to return the result.You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component)RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)

Starting from API 26.0.0, it is recommended to use [readPixelsToArea](#readPixelsToArea) instead for better exception handling capabilities.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

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

## readPixels

```TypeScript
readPixels(area: PositionArea, callback: AsyncCallback<void>): void
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region of this PixelMap object in the BGRA_8888 format and writes the data to the  
[PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels buffer. This API uses an asynchronous callback to return the result.You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component)RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)

Starting from API 26.0.0, it is recommended to use [readPixelsToArea](#readPixelsToArea) instead for better exception handling capabilities.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readPixels(area: PositionArea, callback: AsyncCallback<void>): void--><!--Device-PixelMap-readPixels(area: PositionArea, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area from which the pixels will be read. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## readPixelsSync

```TypeScript
readPixelsSync(area: PositionArea): void
```

Reads the pixels in the area specified by [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region of this PixelMap object in the BGRA_8888 format and writes the data to the  
[PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels buffer. This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [readPixelsToAreaSync](#readPixelsToAreaSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-readPixelsSync(area: PositionArea): void--><!--Device-PixelMap-readPixelsSync(area: PositionArea): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area from which the pixels will be read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## readPixelsToArea

```TypeScript
readPixelsToArea(area: PositionArea): Promise<void>
```

Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range. |
| [7600302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## readPixelsToAreaSync

```TypeScript
readPixelsToAreaSync(area: PositionArea): void
```

Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range. |
| [7600302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer.This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [readAllPixelsToBuffer](#readAllPixelsToBuffer) instead for better exception handling capabilities.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer): Promise<void>--><!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getPixelBytesNumber). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer.This API uses an asynchronous callback to return the result.

Starting from API 26.0.0, it is recommended to use [readAllPixelsToBuffer](#readAllPixelsToBuffer) instead for better exception handling capabilities.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void--><!--Device-PixelMap-readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getPixelBytesNumber). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## readPixelsToBufferSync

```TypeScript
readPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer.This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [readAllPixelsToBufferSync](#readAllPixelsToBufferSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readPixelsToBufferSync(dst: ArrayBuffer): void--><!--Device-PixelMap-readPixelsToBufferSync(dst: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getPixelBytesNumber). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will fail. This API uses an asynchronous callback to return the result.Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

> **NOTE：**
> 
> Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
> by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-release(callback: AsyncCallback<void>): void--><!--Device-PixelMap-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## release

```TypeScript
release(): Promise<void>
```

Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will fail. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

> **NOTE：**
> 
> Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
> by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-release(): Promise<void>--><!--Device-PixelMap-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## rotate

ArkTS-Dyn:
```TypeScript
rotate(angle: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
rotate(angle: double, callback: AsyncCallback<void>): void
```

Rotates this image based on a given angle. This API uses an asynchronous callback to return the result.

Starting from API 26.0.0, it is recommended to use [applyRotate](#applyRotate) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-rotate(angle: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-rotate(angle: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Angle to rotate. Unit: degrees. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## rotate

ArkTS-Dyn:
```TypeScript
rotate(angle: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
rotate(angle: double): Promise<void>
```

Rotates a PixelMap based on a given angle. This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [applyRotate](#applyRotate) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-rotate(angle: double): Promise<void>--><!--Device-PixelMap-rotate(angle: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Angle to rotate. Unit: degrees. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## rotateSync

ArkTS-Dyn:
```TypeScript
rotateSync(angle: number): void
```

ArkTS-Sta:
```TypeScript
rotateSync(angle: double): void
```

Rotates this image based on a given angle. This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [applyRotateSync](#applyRotateSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-rotateSync(angle: double): void--><!--Device-PixelMap-rotateSync(angle: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Angle to rotate. Unit: degrees. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## scale

ArkTS-Dyn:
```TypeScript
scale(x: number, y: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
scale(x: double, y: double, callback: AsyncCallback<void>): void
```

Scales this image based on the scale factors of the width and height. This API uses an asynchronous callback to return the result.

Starting from API 26.0.0, it is recommended to use [applyScale](#applyScale) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-scale(x: double, y: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-scale(x: double, y: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## scale

ArkTS-Dyn:
```TypeScript
scale(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
scale(x: double, y: double): Promise<void>
```

Scales this image based on the scale factors of the width and height. This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [applyScale](#applyScale) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-scale(x: double, y: double): Promise<void>--><!--Device-PixelMap-scale(x: double, y: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## scale

ArkTS-Dyn:
```TypeScript
scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>
```

ArkTS-Sta:
```TypeScript
scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>
```

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [applyScale](#applyScale) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>--><!--Device-PixelMap-scale(x: double, y: double, level: AntiAliasingLevel): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | Yes | Anti-aliasing level. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## scaleSync

ArkTS-Dyn:
```TypeScript
scaleSync(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
scaleSync(x: double, y: double): void
```

Scales this image based on the scale factors of the width and height. This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [applyScaleSync](#applyScaleSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-scaleSync(x: double, y: double): void--><!--Device-PixelMap-scaleSync(x: double, y: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## scaleSync

ArkTS-Dyn:
```TypeScript
scaleSync(x: number, y: number, level: AntiAliasingLevel): void
```

ArkTS-Sta:
```TypeScript
scaleSync(x: double, y: double, level: AntiAliasingLevel): void
```

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [applyScaleSync](#applyScaleSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-scaleSync(x: double, y: double, level: AntiAliasingLevel): void--><!--Device-PixelMap-scaleSync(x: double, y: double, level: AntiAliasingLevel): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the width. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) | Yes | Anti-aliasing level. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void
```

Set color space of pixel map.

This method is only used to set the colorspace property of pixelmap, while all pixel data remains the same after calling this method.If you want to change colorspace for all pixels, use method {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager)} or{@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager, AsyncCallback&lt;void&gt;)}.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PixelMap-setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void--><!--Device-PixelMap-setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpaceManager | Yes | The color space for pixel map. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980115](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980115-invalid-image-parameter) | If the image parameter invalid. |
| [62980111](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980111-incomplete-image-source-data) | The image source data is incomplete. |

## setMemoryNameSync

```TypeScript
setMemoryNameSync(name: string): void
```

Sets a memory name for this PixelMap.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-PixelMap-setMemoryNameSync(name: string): void--><!--Device-PixelMap-setMemoryNameSync(name: string): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Memory name, which can be set only for a PixelMap with the DMA or ASHMEM memory format. The name length for DMA memory settings should be within the range of 1 to 255 bytes. For ASHMEM memory settings, the name length should be within the range of 1 to 244 bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.The length of the input parameter is too long. 2.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980286](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980286-failed-to-set-a-memory-identifier-for-a-pixelmap) | Memory format not supported. |

## setMetadata

```TypeScript
setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>
```

Sets the value for the metadata with a given key in this PixelMap. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

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
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource unavailable. |
| [62980173](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980173-dma-memory-space-error) | The DMA memory does not exist. |
| [62980302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980302-memory-copy-failed) | Memory copy failed. Possibly caused by invalid metadata value. |

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-setOpacity(value: double): Promise<void>--><!--Device-PixelMap-setOpacity(value: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The target opacity value to be set. Unit: Percentage, Value range: (0,1]. The valid range is (0.0, 1.0] where 1.0 is fully opaque and becoming transparent as it approaches 0.0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise that resolves when the operation completes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600207](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600207-unsupported-data-format) | Unsupported data format. Possible cause: Alpha type is not supported. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: The specified value is out of range. |

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-PixelMap-setOpacitySync(value: double): void--><!--Device-PixelMap-setOpacitySync(value: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The target opacity value to be set. Unit: Percentage, Value range: (0,1]. The valid range is (0.0, 1.0] where 1.0 is fully opaque and becoming transparent as it approaches 0.0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600207](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600207-unsupported-data-format) | Unsupported data format. Possible cause: Alpha type is not supported. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: The specified value is out of range. |

## setTransferDetached

```TypeScript
setTransferDetached(detached: boolean): void
```

Sets whether to detach from the original thread when this PixelMap is transmitted across threads. This API applies to the scenario where the PixelMap needs to be released immediately.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PixelMap-setTransferDetached(detached: boolean): void--><!--Device-PixelMap-setTransferDetached(detached: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| detached | boolean | Yes | Whether to detach from the original thread. **true** to detach, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## toSdr

```TypeScript
toSdr(): Promise<void>
```

Convert pixelmap to standard dynamic range.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PixelMap-toSdr(): Promise<void>--><!--Device-PixelMap-toSdr(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [62980137](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980137-invalid-image-operation) | Invalid image operation. |

## translate

ArkTS-Dyn:
```TypeScript
translate(x: number, y: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
translate(x: double, y: double, callback: AsyncCallback<void>): void
```

Translates this image based on given coordinates. This API uses an asynchronous callback to return the result.The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.

Starting from API 26.0.0, it is recommended to use [applyTranslate](#applyTranslate) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-translate(x: double, y: double, callback: AsyncCallback<void>): void--><!--Device-PixelMap-translate(x: double, y: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | X coordinate to translate, in px. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Y coordinate to translate, in px. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## translate

ArkTS-Dyn:
```TypeScript
translate(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
translate(x: double, y: double): Promise<void>
```

Translates a PixelMap based on given coordinates. This API uses a promise to return the result.The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.

Starting from API 26.0.0, it is recommended to use [applyTranslate](#applyTranslate) instead for better exception handling capabilities.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-translate(x: double, y: double): Promise<void>--><!--Device-PixelMap-translate(x: double, y: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | X coordinate to translate, in px. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Y coordinate to translate, in px. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## translateSync

ArkTS-Dyn:
```TypeScript
translateSync(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
translateSync(x: double, y: double): void
```

Translates this image based on given coordinates. This API returns the result synchronously.The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.

Starting from API 26.0.0, it is recommended to use [applyTranslateSync](#applyTranslateSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-translateSync(x: double, y: double): void--><!--Device-PixelMap-translateSync(x: double, y: double): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | X coordinate to translate, in px. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Y coordinate to translate, in px. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## unmarshalling

```TypeScript
unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>
```

Unmarshals a MessageSequence object to obtain a PixelMap object. To create a PixelMap object in synchronous mode,use [createPixelMapFromParcel](arkts-image-image-createpixelmapfromparcel-f.md#createPixelMapFromParcel).

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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
| [62980097](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980097-pixelmap-serialization-failed) | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |
| [62980096](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980096-operation-failed) | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| [62980115](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980115-invalid-image-parameter) | Invalid image parameter. |

## writeAllPixelsFromBuffer

```TypeScript
writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>
```

Reads the pixel data from a buffer and writes the data to the PixelMap.The source data must be in the same pixel format as the PixelMap.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is not editable or is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the buffer is too small. |
| [7600302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## writeAllPixelsFromBufferSync

```TypeScript
writeAllPixelsFromBufferSync(src: ArrayBuffer): void
```

Reads the pixel data from a buffer and writes the data to the PixelMap.The source data must be in the same pixel format as the PixelMap.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is not editable or is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the buffer is too small. |
| [7600302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer): Promise<void>
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object.This API uses a promise to return the result.

Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBuffer](#writeAllPixelsFromBuffer) instead for better exception handling capabilities.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer): Promise<void>--><!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getPixelBytesNumber). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object.This API uses an asynchronous callback to return the result.

Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBuffer](#writeAllPixelsFromBuffer) instead for better exception handling capabilities.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void--><!--Device-PixelMap-writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getPixelBytesNumber). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the pixels in the buffer are successfully written to the PixelMap, **err** is **undefined**; otherwise, **err** is an error object. |

## writeBufferToPixelsSync

```TypeScript
writeBufferToPixelsSync(src: ArrayBuffer): void
```

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object.This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [writeAllPixelsFromBufferSync](#writeAllPixelsFromBufferSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMap-writeBufferToPixelsSync(src: ArrayBuffer): void--><!--Device-PixelMap-writeBufferToPixelsSync(src: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getPixelBytesNumber). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## writePixels

```TypeScript
writePixels(area: PositionArea): Promise<void>
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region buffer in the BGRA_8888 format and writes the data to the area specified by  
[PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels in this PixelMap object. This API uses a promise to return the result.You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component)RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)

Starting from API 26.0.0, it is recommended to use [writePixelsFromArea](#writePixelsFromArea) instead for better exception handling capabilities.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

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

## writePixels

```TypeScript
writePixels(area: PositionArea, callback: AsyncCallback<void>): void
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region buffer in the BGRA_8888 format and writes the data to the area specified by  
[PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels in this PixelMap object. This API uses an asynchronous callback to return the result.You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U component + 0.25 * V component)RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G component + 1 * B component + 1 * A component)

Starting from API 26.0.0, it is recommended to use [writePixelsFromArea](#writePixelsFromArea) instead for better exception handling capabilities.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-writePixels(area: PositionArea, callback: AsyncCallback<void>): void--><!--Device-PixelMap-writePixels(area: PositionArea, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area to which the pixels will be written. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## writePixelsFromArea

```TypeScript
writePixelsFromArea(area: PositionArea): Promise<void>
```

Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is not editable or is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range. |
| [7600302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## writePixelsFromAreaSync

```TypeScript
writePixelsFromAreaSync(area: PositionArea): void
```

Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [7600106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600106-pixelmap-has-been-passed-to-another-thread) | The PixelMap has been passed to another thread. |
| [7600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600105-pixelmap-object-has-been-released) | The PixelMap has been released. |
| [7600201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600201-unsupported-operation) | Unsupported operation because the PixelMap is not editable or is locked. |
| [7600104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600104-failed-to-obtain-image-data) | Failed to get image data. Possible cause: Internal data is corrupted. Please check the logs for detailed information. |
| [7600206](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range. |
| [7600302](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7600302-memory-copy-failure) | Failed to copy the memory. |

## writePixelsSync

```TypeScript
writePixelsSync(area: PositionArea): void
```

Reads the pixels in the [PositionArea](arkts-image-image-positionarea-i.md#PositionArea).region buffer in the BGRA_8888 format and writes the data to the area specified by  
[PositionArea](arkts-image-image-positionarea-i.md#PositionArea).pixels in this PixelMap object. This API returns the result synchronously.

Starting from API 26.0.0, it is recommended to use [writePixelsFromAreaSync](#writePixelsFromAreaSync) instead for better exception handling capabilities.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-writePixelsSync(area: PositionArea): void--><!--Device-PixelMap-writePixelsSync(area: PositionArea): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [PositionArea](arkts-image-image-positionarea-i.md) | Yes | Area to which the pixels will be written. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [501](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#501-api-call-failed) | Resource Unavailable. |

## isEditable

```TypeScript
readonly isEditable: boolean
```

Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides better image rendering and transmission performance.&lt;br&gt;This API can be used in atomic services since API version 11.&lt;br&gt;This API can be used in ArkTS widgets since API version 12.

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PixelMap-readonly isEditable: boolean--><!--Device-PixelMap-readonly isEditable: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## isStrideAlignment

```TypeScript
readonly isStrideAlignment: boolean
```

Whether the row data of the image is memory aligned. The value **true** means that the row data is memory-aligned, and there may be blank bytes padded at the end of each row to meet alignment requirements. The value **false**means that the row data is not memory-aligned, and rows are packed contiguously with no padding bytes at the end.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PixelMap-readonly isStrideAlignment: boolean--><!--Device-PixelMap-readonly isStrideAlignment: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

