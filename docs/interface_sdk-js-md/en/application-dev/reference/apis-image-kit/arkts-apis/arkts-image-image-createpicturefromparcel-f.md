# createPictureFromParcel

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPictureFromParcel

```TypeScript
function createPictureFromParcel(sequence: rpc.MessageSequence): Picture
```

Creates a Picture object from a MessageSequence object.Images occupy a large amount of memory. When you finish using a Picture instance, call [release](arkts-image-image-picture-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 13

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sequence | rpc.MessageSequence | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Picture](arkts-image-image-picture-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980097](../errorcode-image.md#62980097-pixelmap-serialization-failed) |
