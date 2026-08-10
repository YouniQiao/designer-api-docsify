# ImageSource

ImageSource类，用于获取图片相关信息。

在调用ImageSource的方法前，需要先通过[image.createImageSource](arkts-image-image-createimagesource-f.md#createimagesource)构建一个ImageSource实例。

ImageSource的所有方法均不支持并发调用。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-image-interface ImageSource--><!--Device-image-interface ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createWideGamutSdrPixelMap

```TypeScript
createWideGamutSdrPixelMap(): Promise<PixelMap>
```

创建SDR的PixelMap对象。当图片为带有3通道GainMap的HDR图片时，会将其基础图扩展为BT.2020色域的SDR图。使用Promise异步回调。

> **说明：**
> 
> - 对SDR图片源，按图片自带的色彩空间解码，输出SDR图。
> 
> - 对带有单通道GainMap的HDR图片源，解码其基础图（SDR图），忽略GainMap。
> 
> - 对带有3通道GainMap的HDR图片源，解码其基础图（SDR图），并将输出SDR图的色域扩展为
> [ColorSpace](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-colorspacemanager-colorspace-e.md/arkts-arkgraphics2d-colorspacemanager-colorspace-e.md).DISPLAY_BT2020_SRGB。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageSource-createWideGamutSdrPixelMap(): Promise<PixelMap>--><!--Device-ImageSource-createWideGamutSdrPixelMap(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise对象，返回PixelMap。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7700101 | Bad source. |
| 7700103 | Image too large. |
| 7700102 | Unsupported MIME type. |
| 7700301 | Decoding failed. |

## Examples

```TypeScript
async function CreateWideGamutSdrPixelMap(context: Context) {
  // 'sdr.jpg' is only an example. Replace it with the actual one.
  let filePath: string = context.filesDir + "/sdr.jpg";
  let sdrImageSource = image.createImageSource(filePath);
  let pixelmap = sdrImageSource.createWideGamutSdrPixelMap();
  if (pixelmap != undefined) {
    console.info('Succeeded in creating sdr pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }

  // 'singleChannelGainmapFilePath.jpg' is only an example. Replace it with the actual one.
  let singleChannelGainmapFilePath: string = context.filesDir + "/singleChannelGainmapFilePath.jpg";
  let singleChannelGainmapImageSource = image.createImageSource(singleChannelGainmapFilePath);
  let singleChannelGainmapPixelmap = singleChannelGainmapImageSource.createWideGamutSdrPixelMap();
  if (singleChannelGainmapPixelmap != undefined) {
    console.info('Succeeded in creating sdr pixelMap object by using singleChannelGainmapImageSource.');
  } else {
    console.error('Failed to create pixelMap.');
  }
  // 'threeChannelGainmapFilePath.jpg' is only an example. Replace it with the actual one.
  let threeChannelGainmapFilePath: string = context.filesDir + "/threeChannelGainmapFilePath.jpg";
  let threeChannelGainmapImageSource = image.createImageSource(threeChannelGainmapFilePath);
  let threeChannelGainmapPixelmap = threeChannelGainmapImageSource.createWideGamutSdrPixelMap();
  if (threeChannelGainmapPixelmap != undefined) {
    console.info('Succeeded in creating sdr pixelMap using DISPLAY_BT2020_SRGB.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

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
| 7700101 | Bad source. |
| 7700103 | Image too large. |
| 7700102 | Unsupported MIME type. |
| 7700301 | Decoding failed. |

## isJpegProgressive

```TypeScript
isJpegProgressive(): Promise<boolean>
```

判断Jpeg图片是否是渐进式图片。使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-isJpegProgressive(): Promise<boolean>--><!--Device-ImageSource-isJpegProgressive(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示Jpeg图片是渐进式；返回false表示Jpeg图片不是渐进式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7700101 | Bad source. |
| 7700102 | Unsupported MIME type. |

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

批量修改图片属性。使用Promise异步回调。

Exif属性中除"JPEGInterchangeFormat"/"JPEGInterchangeFormatLength"/"GIFLoopCount"字段外，其他均支持修改。

> **说明：**
> 
> - 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](arkts-image-image-createimagesource-f.md#createimagesource)实例或通过传入的uri创建
> [image.createImageSource](arkts-image-image-createimagesource-f.md#createimagesource)实例。
> 
> - 支持修改JPEG、PNG、HEIF和WEBP文件类型的图片属性，图片需要包含Exif信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageSource-modifyImageAllProperties(records: Record<string, string|null>): Promise<void>--><!--Device-ImageSource-modifyImageAllProperties(records: Record<string, string|null>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| records | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string \| null&gt; | Yes | 包含图片属性名和属性值的键值对集合。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7700102 | Unsupported MIME type. |
| 7700304 | Failed to write image properties to the file. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 7700202 | Unsupported metadata. For example, the property key is not supported, or the property value is invalid. |

## Examples

```TypeScript
async function ModifyImageAllProperties(imageSource: image.ImageSource) {
  try {
    let record: Record<string, string | null> = {
      "HwMnotePhysicalAperture": "13",
    }
    await imageSource.modifyImageAllProperties(record);
  } catch (err) {
    console.error('[modifyImageAllProperties]', `modify image property failed.err: ${err.code}, errorMessage: ${err.message}`);
  }
}
```

