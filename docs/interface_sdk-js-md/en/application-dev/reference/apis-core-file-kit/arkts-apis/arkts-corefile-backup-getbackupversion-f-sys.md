# getBackupVersion (System API)

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## getBackupVersion

```TypeScript
function getBackupVersion(): string
```

Obtain the backupVersion.

**Since:** 18

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
