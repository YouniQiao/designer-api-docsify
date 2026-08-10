# releaseAccess (System API)

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## releaseAccess

```TypeScript
function releaseAccess(dataType: DataType): ReleaseStatus
```

以同步方法释放锁屏下指定类型敏感数据访问权限。释放成功后，敏感数据密钥的引用计数减少，当引用计数归零时，密钥可以在锁屏达到系统配置的时长阈值后被销毁。

调用此接口前，请确保应用已开启锁屏下敏感数据保护功能，并且先调用[acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireaccess)接口成功申请权限后才能使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA or ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA

<!--Device-screenLockFileManager-function releaseAccess(dataType: DataType): ReleaseStatus--><!--Device-screenLockFileManager-function releaseAccess(dataType: DataType): ReleaseStatus-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | [DataType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes | 锁屏下访问的敏感数据类型。dataType需要与acquireAccess接口使用的dataType保持一致。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) | 锁屏下敏感数据访问权限的释放状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameter is left unspecified. 2. Incorrect parameter types. |
| 801 | The specified SystemCapability name was not found. |
| 201 | Permission verification failed, usually returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 29300005 | File access was not acquired. |
| 29300003 | The application is not enabled the data protection under lock screen. |
| 29300002 | The system ability works abnormally. |
| 29300001 | Invalid DataType. |

## Examples

```TypeScript
// Release the permission to access media data on the lock screen.
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    // Release access permission
    let releaseStatus = screenLockFileManager.releaseAccess(screenLockFileManager.DataType.MEDIA_DATA);
    if (releaseStatus === screenLockFileManager.ReleaseStatus.RELEASE_GRANTED) {
        hilog.info(0x0000, 'testTag', 'releaseAccess successfully.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'releaseAccess failed: %{public}s', message);
}
```

