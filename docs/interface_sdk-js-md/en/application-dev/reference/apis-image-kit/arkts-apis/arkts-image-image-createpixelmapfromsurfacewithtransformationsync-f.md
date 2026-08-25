# createPixelMapFromSurfaceWithTransformationSync

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMapFromSurfaceWithTransformationSync

```TypeScript
function createPixelMapFromSurfaceWithTransformationSync(surfaceId: string, transformEnabled: boolean): PixelMap
```

Creates a PixelMap object based on the ID of a Surface with transformation.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| surfaceId | string | Yes |
| transformEnabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7600104](../errorcode-image.md#7600104-failed-to-obtain-image-data) |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |
| [7600305](../errorcode-image.md#7600305-failed-to-create-the-pixelmap) |
