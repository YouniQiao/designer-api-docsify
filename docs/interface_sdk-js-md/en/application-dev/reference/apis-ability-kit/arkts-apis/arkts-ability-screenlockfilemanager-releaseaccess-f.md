# releaseAccess

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## releaseAccess

```TypeScript
function releaseAccess(): ReleaseStatus
```

Releases the access permission for the caller app's sensitive data under the lock screen in synchronous mode. After the release is successful, the reference count of the sensitive data key decreases. When the count reaches zero, the key can be destroyed after the screen has been locked for a duration reaching the system-configured lock duration threshold.Before calling this API, ensure that the app has enabled the sensitive data protection function under the lock screen, and that the [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md) API has been called to request the permission successfully first.

**Since:** 12

**System capability:** SystemCapability.Security.ScreenLockFileManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-system-service-abnormal) |
| [29300003](../errorcode-screenLockFileManager.md#29300003-sensitive-data-access-management-under-lock-screen-is-not-enabled) |
| [29300005](../errorcode-screenLockFileManager.md#29300005-permission-to-access-sensitive-data-on-the-lock-screen-is-not-requested) |
