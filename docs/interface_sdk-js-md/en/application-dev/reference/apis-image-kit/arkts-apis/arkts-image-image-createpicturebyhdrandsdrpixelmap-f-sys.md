# createPictureByHdrAndSdrPixelMap (System API)

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPictureByHdrAndSdrPixelMap

```TypeScript
function createPictureByHdrAndSdrPixelMap(hdrPixelMap: PixelMap, sdrPixelMap: PixelMap): Promise<Picture>
```

Creates a Picture object based on an HDR PixelMap and an SDR PixelMap. The system uses the HDR PixelMap and SDR PixelMap to generate a gainmap. The returned Picture object contains the SDR PixelMap and the generated gainmap, both in RGBA8888 format. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| sdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |


## createPictureByHdrAndSdrPixelMap

```TypeScript
function createPictureByHdrAndSdrPixelMap(hdrPixelMap: PixelMap, sdrPixelMap: PixelMap, 
      params: GainmapParams): Promise<Picture>
```

Creates a Picture object by a HDR PixelMap and a SDR PixelMap with specified options. A gainmap will be generated using the HDR and SDR PixelMap, and the returned Picture will contain the SDR PixelMap and the generated gainmap.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| sdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| params | [GainmapParams](arkts-image-image-gainmapparams-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |
