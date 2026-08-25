# HashStream

The **HashStream** class is a utility for creating a message digest of data. You can use [createHash](../../../reference/apis-core-file-kit/js-apis-file-hash.md#hashcreatehash12) to create a **HashStream** instance.

**Inheritance/Implementation:** HashStream extends [stream.Transform](../../apis-arkts/arkts-apis/arkts-arkts-stream-transform-c.md)

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { hash } from 'kits/@kit.CoreFileKit';
```

## digest

```TypeScript
digest(): string
```

Generates a message digest.

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900042 |

## update

```TypeScript
update(data: ArrayBuffer): void
```

Updates the data for generating a message digest. This API can be called multiple times.

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900042 |
