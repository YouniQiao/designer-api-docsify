# getBackupInfo (System API)

## Modules to Import

```TypeScript
import { backup } from '@kit.CoreFileKit';
```

## getBackupInfo

```TypeScript
function getBackupInfo(bundleToBackup: string): string
```

Get Backup information from bundle.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function getBackupInfo(bundleToBackup: string): string--><!--Device-backup-function getBackupInfo(bundleToBackup: string): string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleToBackup | string | Yes | Bundle to backup. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the backup application's info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed, usually the result returned by VerifyAccessToken. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, backup } from '@kit.CoreFileKit';

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

