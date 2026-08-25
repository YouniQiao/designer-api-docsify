# acquireAccess

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## acquireAccess

```TypeScript
function acquireAccess(): AccessStatus
```

Requests the access permission for the caller app's sensitive data under the lock screen in synchronous mode. After the request is successful, the reference count of the sensitive data key increases, preventing the key from being destroyed after the screen has been locked for a duration reaching the system-configured lock duration threshold. This method must be used in pair with [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md).Before calling this API, ensure that the app has enabled the sensitive data protection function under the lock screen, and that the key status queried through the [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md) API is KEY_EXIST.

**Since:** 12

**System capability:** SystemCapability.Security.ScreenLockFileManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AccessStatus](arkts-ability-screenlockfilemanager-accessstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-system-service-abnormal) |
| [29300003](../errorcode-screenLockFileManager.md#29300003-sensitive-data-access-management-under-lock-screen-is-not-enabled) |
| [29300004](../errorcode-screenLockFileManager.md#29300004-permission-to-access-sensitive-data-on-the-lock-screen-has-been-revoked) |
