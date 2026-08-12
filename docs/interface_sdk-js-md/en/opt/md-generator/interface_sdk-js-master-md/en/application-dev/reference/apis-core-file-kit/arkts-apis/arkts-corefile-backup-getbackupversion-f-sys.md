# getBackupVersion (System API)

## Modules to Import

```TypeScript
import { backup } from '@kit.CoreFileKit';
```

## getBackupVersion

```TypeScript
function getBackupVersion(): string
```

Obtain the backupVersion.

**Since:** 18

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function getBackupVersion(): string--><!--Device-backup-function getBackupVersion(): string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
