# compressFiles

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## compressFiles

```TypeScript
function compressFiles(inFiles: Array<string>, outFile: string, options: Options): Promise<void>
```

Compresses multiple specified files. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inFiles | Array & lt;string & gt; | Yes |
| outFile | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [900001](../../apis-ability-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900002](../../apis-ability-kit/errorcode-zlib.md#900002-invalid-destination-file) |
