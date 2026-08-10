# releaseAccess

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## releaseAccess

```TypeScript
function releaseAccess(): ReleaseStatus
```

以同步方法释放调用方应用锁屏下敏感数据访问权限。释放成功后，敏感数据密钥的引用计数减少，当计数归零时，密钥可以在屏幕被锁定达到系统配置的时长阈值后被销毁。

调用此接口前，请确保应用已开启锁屏下敏感数据保护功能，并且先调用[acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireaccess)接口成功申请权限后才能使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-screenLockFileManager-function releaseAccess(): ReleaseStatus--><!--Device-screenLockFileManager-function releaseAccess(): ReleaseStatus-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

**Return value:**

| Type | Description |
| --- | --- |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) | 锁屏下敏感数据访问权限的释放状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | The specified SystemCapability name was not found. |
| 29300005 | File access was not acquired. |
| 29300003 | The application is not enabled the data protection under lock screen. |
| 29300002 | The system ability works abnormally. |

## Examples

```TypeScript
// Release the permission to access sensitive data on the lock screen.
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    // Release access permission
    let releaseStatus = screenLockFileManager.releaseAccess();
    if (releaseStatus === screenLockFileManager.ReleaseStatus.RELEASE_GRANTED) {
        hilog.info(0x0000, 'testTag', 'releaseAccess successfully.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'releaseAccess failed: %{public}s', message);
}
```

