# queryAppKeyState (System API)

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'screenLockFileManager';
```

## queryAppKeyState

```TypeScript
function queryAppKeyState(dataType: DataType): KeyStatus
```

Queries the status of a specified type of sensitive data key under the lock screen synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA or ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA

<!--Device-screenLockFileManager-function queryAppKeyState(dataType: DataType): KeyStatus--><!--Device-screenLockFileManager-function queryAppKeyState(dataType: DataType): KeyStatus-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | DataType | Yes | Type of sensitive data that is accessible on the lock screen. |

**Return value:**

| Type | Description |
| --- | --- |
| [KeyStatus](arkts-ability-screenlockfilemanager-keystatus-e.md) | Status of the key for sensitive data under lock screen. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameter is left unspecified. 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | The specified SystemCapability name was not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed, usually returned by VerifyAccessToken. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [29300002](../errorcode-screenLockFileManager.md#29300002-system-service-abnormal) | The system ability works abnormally. |
| [29300001](../errorcode-screenLockFileManager.md#29300001-invalid-parameter) | Invalid DataType. |

## Examples

```TypeScript
// Obtain the state of access permissions for media data on the lock screen.
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    let keyStatus = screenLockFileManager.queryAppKeyState(screenLockFileManager.DataType.MEDIA_DATA);
    if (keyStatus === screenLockFileManager.KeyStatus.KEY_NOT_EXIST) {
        hilog.info(0x0000, 'testTag', 'Key does not exist.');
    } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_RELEASED) {
        hilog.info(0x0000, 'testTag', 'Key has been released.');
    } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_EXIST) {
        hilog.info(0x0000, 'testTag', 'Key exists.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'queryAppKeyState failed: %{public}s', message);
}
```

