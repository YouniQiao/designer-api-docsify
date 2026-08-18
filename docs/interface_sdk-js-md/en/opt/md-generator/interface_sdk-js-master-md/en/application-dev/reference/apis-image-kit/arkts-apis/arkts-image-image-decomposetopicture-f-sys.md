# decomposeToPicture (System API)

## Modules to Import

```TypeScript
```

## decomposeToPicture

```TypeScript
function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>
```

Decomposes an HDR Pixelmap object to a Picture object which contains an SDR PixelMap and a gainmap. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-image-function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>--><!--Device-image-function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| options | [HdrDecomposeOptions](arkts-image-image-hdrdecomposeoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600208](../errorcode-image.md#7600208-failed-to-decompose-an-hdr-image) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function DecomposeToPictureTest(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let imageSource: image.ImageSource = image.createImageSource(rawFile);
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.HDR,
  };
  let hdrPixelMap = await imageSource.createPixelMap(decodingOptions);
  // Set the gain map to full size and the pixel format to NV12.
  let options: image.HdrDecomposeOptions = {
    isFullSizeGainmap: true,
    desiredPixelFormat: image.PixelMapFormat.NV12,
  };
  let picture: image.Picture | undefined = await image.decomposeToPicture(hdrPixelMap, options);
  if (picture != undefined) {
    console.info('Decompose to picture with options successfully');
  } else {
    console.error('Decompose to picture with options failed');
  }
}
```
