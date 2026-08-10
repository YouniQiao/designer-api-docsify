# updateSendRate (System API)

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## updateSendRate

```TypeScript
function updateSendRate(bundleName: string, sendRate: int): boolean
```

更新备份应用发送文件描述符的速率。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function updateSendRate(bundleName: string, sendRate: int): boolean--><!--Device-backup-function updateSendRate(bundleName: string, sendRate: int): boolean-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 需要控制文件描述符发送速率的应用名称。 |
| sendRate | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符发送速率，单位为个/秒，取值范围为0至800。 |

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

