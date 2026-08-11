# getDLPSuffix

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## getDLPSuffix

```TypeScript
function getDLPSuffix(): string
```

Obtains the DLP file name extension. After the API is called successfully, the DLP file name extension (for example, .dlp) is returned. This API returns the result synchronously.

This API is used to obtain the standard extension of the DLP file, which can be used to construct the DLP file name or the determination of the file type.

**Since:** 10

<!--Device-dlpPermission-function getDLPSuffix(): string--><!--Device-dlpPermission-function getDLPSuffix(): string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let dlpSuffix = dlpPermission.getDLPSuffix(); // Obtain the DLP file name extension.
console.info('dlpSuffix:', dlpSuffix);
```
