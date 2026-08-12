# ImageSource

The **ImageSource** class provides APIs to obtain image information.

Before calling any API in ImageSource, you must use   
[image.createImageSource](arkts-image-image-createimagesource-f.md#createImageSource-1) to create an ImageSource instance.

All APIs in ImageSource cannot be called concurrently.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call   
[release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-image-interface ImageSource--><!--Device-image-interface ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## createWideGamutSdrPixelMap

```TypeScript
createWideGamutSdrPixelMap(): Promise<PixelMap>
```

Decodes to a SDR PixelMap, using a as wide gamut as possible.For a SDR ImageSource, decodes to a SDR PixelMap using its native color space.For a HDR ImageSource with a single-channel gainmap, decodes its base(SDR) image and ingores its gainmap.For a HDR ImageSource with a three-channel gainmap, decodes to a SDR PixelMap using CM_DISPLAY_BT2020_SRGB color space.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageSource-createWideGamutSdrPixelMap(): Promise<PixelMap>--><!--Device-ImageSource-createWideGamutSdrPixelMap(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Decoded PixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700101-abnormal-image-source) | Bad source. |
| [7700103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700103-image-oversized) | Image too large. |
| [7700102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700301-decoding-failure) | Decoding failed. |

## createWideGamutSdrPixelMap

```TypeScript
createWideGamutSdrPixelMap(): Promise<PixelMap | undefined>
```

Decodes to a SDR PixelMap, using a as wide gamut as possible.For a SDR ImageSource, decodes to a SDR PixelMap using its native color space.For a HDR ImageSource with a single-channel gainmap, decodes its base(SDR) image and ingores its gainmap.For a HDR ImageSource with a three-channel gainmap, decodes to a SDR PixelMap using CM_DISPLAY_BT2020_SRGB color space.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ImageSource-createWideGamutSdrPixelMap(): Promise<PixelMap | undefined>--><!--Device-ImageSource-createWideGamutSdrPixelMap(): Promise<PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap \| undefined&gt; | Decoded PixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700101-abnormal-image-source) | Bad source. |
| [7700103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700103-image-oversized) | Image too large. |
| [7700102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700301-decoding-failure) | Decoding failed. |

## isJpegProgressive

```TypeScript
isJpegProgressive(): Promise<boolean>
```

Checks whether a JPEG image is progressive. This API uses a promise to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-isJpegProgressive(): Promise<boolean>--><!--Device-ImageSource-isJpegProgressive(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise object. The value **true** indicates that the JPEG image is progressive, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700101-abnormal-image-source) | Bad source. |
| [7700102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function IsJpegProgressive(imageSource : image.ImageSource) {
  imageSource.isJpegProgressive()
    .then((isProgressive: boolean) => {
      console.info("isJpegProgressive: " + isProgressive);
    }).catch((error: BusinessError) => {
      console.error(`Failed to obtain the jpeg image isprogressive error.code is ${error.code}, message is ${error.message}`);
    })
}
```

## modifyImageAllProperties

```TypeScript
modifyImageAllProperties(records: Record<string, string|null>): Promise<void>
```

Modify the value of properties in an image with the specified keys.The HwMnote read-only key is supported.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-modifyImageAllProperties(records: Record<string, string|null>): Promise<void>--><!--Device-ImageSource-modifyImageAllProperties(records: Record<string, string|null>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| records | Record&lt;string, string \| null&gt; | Yes | Property Records whose values are to be modified, when the value is set to null the tag will be removed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700102-unsupported-mime-type) | Unsupported MIME type. |
| [7700304](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700304-failed-to-write-image-information-to-the-file) | Failed to write image properties to the file. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |
| [7700202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-image.md#7700202-unsupported-metadata) | Unsupported metadata. For example, the property key is not supported, or the property value is invalid. |

