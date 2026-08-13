# releaseAccess (System API)

## Modules to Import

```TypeScript
import { screenLockFileManager } from '@kit.AbilityKit';
```

## releaseAccess

```TypeScript
function releaseAccess(dataType: DataType): ReleaseStatus
```

Releases the permission to access a specified type of sensitive data under the lock screen synchronously. After the release is successful, the reference count of the sensitive data key decreases. When the reference count reaches zero, the key can be destroyed after the screen has been locked for the system-configured duration threshold. Before calling this API, ensure that the app has enabled the sensitive data protection under lock screen feature and that the permission has been successfully requested by calling the [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireAccess) API first.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA or ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA

<!--Device-screenLockFileManager-function releaseAccess(dataType: DataType): ReleaseStatus--><!--Device-screenLockFileManager-function releaseAccess(dataType: DataType): ReleaseStatus-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataType | [DataType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [29300005](../errorcode-screenLockFileManager.md#29300005-permission-to-access-sensitive-data-on-the-lock-screen-is-not-requested) |
| [29300003](../errorcode-screenLockFileManager.md#29300003-sensitive-data-access-management-under-lock-screen-is-not-enabled) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-system-service-abnormal) |
| [29300001](../errorcode-screenLockFileManager.md#29300001-invalid-parameter) |

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
