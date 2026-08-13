# getOriginalFileName

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## getOriginalFileName

```TypeScript
function getOriginalFileName(fileName: string): string
```

Obtains the original name of a DLP file. This API returns the result synchronously. Determine the file type based on the original file name extension and select an application to open the file.

**Since:** 10

**Deprecated since:** -1

<!--Device-dlpPermission-function getOriginalFileName(fileName: string): string--><!--Device-dlpPermission-function getOriginalFileName(fileName: string): string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fileName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let originalFileName = dlpPermission.getOriginalFileName('test.txt.dlp'); // Obtain the original file name.
console.info('originalFileName:', originalFileName);
```
