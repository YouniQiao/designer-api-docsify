# updateSendRate (System API)

## updateSendRate

```TypeScript
function updateSendRate(bundleName: string, sendRate: int): boolean
```

Update send file fd rate.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function updateSendRate(bundleName: string, sendRate: int): boolean--><!--Device-backup-function updateSendRate(bundleName: string, sendRate: int): boolean-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | set update to bundleName app. |
| sendRate | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | set send file fd rate. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return update result, true is success, false is fail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed, usually the result returned by VerifyAccessToken. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backup } from '@kit.CoreFileKit';

function updateSendRate() {
  try {
    let bundleName = "com.example.myApp";
    let sendRate = 300;
    let result = backup.updateSendRate(bundleName, sendRate);
    if (result) {
      console.info('updateSendRate success');
    } else {
      console.info('updateSendRate fail');
    }
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`updateSendRate failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

