# decomposeToPicture (System API)

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## decomposeToPicture

```TypeScript
function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>
```

将HDR PixelMap分解为包含SDR PixelMap和增益图（gainmap）的Picture对象。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-image-function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>--><!--Device-image-function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes | HDR PixelMap，像素格式需为RGBA_F16、RGBA_1010102、YCBCR_P010或YCRCB_P010。 |
| options | [HdrDecomposeOptions](arkts-image-image-hdrdecomposeoptions-i-sys.md) | No | HDR分解配置选项，包含增益图尺寸和像素格式设置。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Picture \| undefined&gt; | Promise对象。返回包含SDR PixelMap和增益图的Picture对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7600208 | HDR image decomposition failed. Possible causes: 1. Decomposition processing is not supported. 2. Processing error occurs. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 7600201 | Unsupported operation. hdrPixelMap's PixelMapFormat is not RGBA_F16\RGBA_1010102\YCBCR_P010\YCRCB_P010. |
| 7600206 | Invalid parameter. Possible cause: hdrPixelMap is empty. |
| 7600301 | Alloc memory failed. |

## Examples

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

