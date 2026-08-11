# getBackupInfo (System API)

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## getBackupInfo

```TypeScript
function getBackupInfo(bundleToBackup: string): string
```

Get Backup information from bundle.

**Since:** 12

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function getBackupInfo(bundleToBackup: string): string--><!--Device-backup-function getBackupInfo(bundleToBackup: string): string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleToBackup | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backup } from '@kit.CoreFileKit';

function getBackupInfo() {
  try {
    let backupApp = "com.example.hiworld";
    let result = backup.getBackupInfo(backupApp);
    console.info('getBackupInfo success, result: ' + result);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getBackupInfo failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```
