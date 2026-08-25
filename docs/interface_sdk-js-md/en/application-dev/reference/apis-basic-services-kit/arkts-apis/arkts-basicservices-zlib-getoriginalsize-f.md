# getOriginalSize

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## getOriginalSize

```TypeScript
function getOriginalSize(compressedFile: string): Promise<number>
```

Obtains the original size of a compressed file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| compressedFile | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [900001](../../apis-ability-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900003](../../apis-ability-kit/errorcode-zlib.md#900003-source-file-in-incorrect-format-or-damaged) |
