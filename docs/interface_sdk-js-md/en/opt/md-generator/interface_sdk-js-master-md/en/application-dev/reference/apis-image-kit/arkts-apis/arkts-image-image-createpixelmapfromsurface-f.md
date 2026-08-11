# createPixelMapFromSurface

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMapFromSurface

```TypeScript
function createPixelMapFromSurface(surfaceId: string, region: Region): Promise<PixelMap>
```

Creates a PixelMap object from surface id.

**Since:** 11

<!--Device-image-function createPixelMapFromSurface(surfaceId: string, region: Region): Promise<PixelMap>--><!--Device-image-function createPixelMapFromSurface(surfaceId: string, region: Region): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| surfaceId | string | Yes |
| region | [Region](arkts-image-image-region-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PixelMap&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980178](../errorcode-image.md#62980178-failure-in-creating-a-pixelmap) |
| [62980105](../errorcode-image.md#62980105-failure-in-obtaining-image-data) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapFromSurface(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  image.createPixelMapFromSurface(surfaceId, region).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating the PixelMap from Surface.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create the PixelMap from Surface. Code: ${err.code}, message: ${err.message}`);
  });
}
```


## createPixelMapFromSurface

```TypeScript
function createPixelMapFromSurface(surfaceId: string): Promise<PixelMap>
```

Creates a PixelMap object from surface id.

**Since:** 15

<!--Device-image-function createPixelMapFromSurface(surfaceId: string): Promise<PixelMap>--><!--Device-image-function createPixelMapFromSurface(surfaceId: string): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| surfaceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PixelMap&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [62980178](../errorcode-image.md#62980178-failure-in-creating-a-pixelmap) |
| [62980105](../errorcode-image.md#62980105-failure-in-obtaining-image-data) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapFromSurface(surfaceId: string) {
  image.createPixelMapFromSurface(surfaceId).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating the PixelMap from Surface.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create the PixelMap from Surface. Code: ${err.code}, message: ${err.message}`);
  });
}
```
