# getBackupVersion (System API)

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## getBackupVersion

```TypeScript
function getBackupVersion(): string
```

获取备份版本信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function getBackupVersion(): string--><!--Device-backup-function getBackupVersion(): string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回备份版本信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backup } from '@kit.CoreFileKit';

function getBackupVersion() {
  try {
    let result = backup.getBackupVersion();
    console.info('getBackupVersion success, result: ' + result);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getBackupVersion failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

Content example:

```TypeScript
{ "backupVersion" : "16.0" }
```

