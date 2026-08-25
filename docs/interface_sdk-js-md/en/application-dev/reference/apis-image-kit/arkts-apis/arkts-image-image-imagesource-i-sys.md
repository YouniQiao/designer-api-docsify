# ImageSource

The **ImageSource** class provides APIs to obtain image information.Before calling any API in ImageSource, you must use [image.createImageSource](arkts-image-image-createimagesource-f.md) to create an ImageSource instance.All APIs in ImageSource cannot be called concurrently.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createWideGamutSdrPixelMap

```TypeScript
createWideGamutSdrPixelMap(): Promise<PixelMap>
```

Decodes to a SDR PixelMap, using a as wide gamut as possible. For a SDR ImageSource, decodes to a SDR PixelMap using its native color space. For a HDR ImageSource with a single-channel gainmap, decodes its base(SDR) image and ingores its gainmap. For a HDR ImageSource with a three-channel gainmap, decodes to a SDR PixelMap using CM_DISPLAY_BT2020_SRGB color space.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700103](../errorcode-image.md#7700103-image-oversized) |
| [7700301](../errorcode-image.md#7700301-decoding-failure) |

## isJpegProgressive

```TypeScript
isJpegProgressive(): Promise<boolean>
```

Checks whether a JPEG image is progressive. This API uses a promise to return the result.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7700101](../errorcode-image.md#7700101-abnormal-image-source) |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |

## modifyImageAllProperties

```TypeScript
modifyImageAllProperties(records: Record<string, string|null>): Promise<void>
```

Modify the value of properties in an image with the specified keys.The HwMnote read-only key is supported.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| records | Record & lt;string, string \ | null & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [7700102](../errorcode-image.md#7700102-unsupported-mime-type) |
| [7700202](../errorcode-image.md#7700202-unsupported-metadata) |
| [7700304](../errorcode-image.md#7700304-failed-to-write-image-information-to-the-file) |
