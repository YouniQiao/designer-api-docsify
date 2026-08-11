# updateTimer (System API)

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## updateTimer

```TypeScript
function updateTimer(bundleName: string, timeout: number): boolean
```

Update backup or restore timeout.

**Since:** 12

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function updateTimer(bundleName: string, timeout: int): boolean--><!--Device-backup-function updateTimer(bundleName: string, timeout: int): boolean-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| timeout | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

function updateTimer() {
  try {
    let timeout = 30000;
    let bundleName = "com.example.hiworld";
    let result = backup.updateTimer(bundleName, timeout);
    if (result) {
      console.info('updateTimer success');
    } else {
      console.info('updateTimer fail');
    }
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`updateTimer failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```
