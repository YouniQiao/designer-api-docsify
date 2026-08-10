# updateTimer (System API)

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## updateTimer

```TypeScript
function updateTimer(bundleName: string, timeout: int): boolean
```

设置应用备份或恢复的时长。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function updateTimer(bundleName: string, timeout: int): boolean--><!--Device-backup-function updateTimer(bundleName: string, timeout: int): boolean-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 需要设置备份或恢复时长的应用名称。 |
| timeout | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 备份或恢复的限制时长，单位为毫秒，取值范围为0至14400000。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 设置结果，true表示成功，false表示失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

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

