# createImageCreator

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageCreator

```TypeScript
function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator
```

Creates an ImageCreator instance by specifying the image width, height, format, and capacity. Images occupy a large amount of memory. When you finish using an ImageCreator instance, call [release](arkts-image-image-imagecreator-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [createImageCreator](#createimagecreator)(size: Size, format: ImageFormat, capacity: int)

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |
| format | number | Yes |
| capacity | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageCreator](arkts-image-image-imagecreator-i.md) |


## createImageCreator

```TypeScript
function createImageCreator(size: Size, format: ImageFormat, capacity: number): ImageCreator
```

Creates an ImageCreator instance by specifying the image size, format, and capacity. Images occupy a large amount of memory. When you finish using an ImageCreator instance, call [release](arkts-image-image-imagecreator-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | Size | Yes |
| format | [ImageFormat](arkts-image-image-imageformat-e.md) | Yes |
| capacity | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageCreator](arkts-image-image-imagecreator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
