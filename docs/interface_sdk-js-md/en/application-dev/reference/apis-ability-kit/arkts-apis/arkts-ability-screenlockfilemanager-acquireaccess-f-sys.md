# acquireAccess (System API)

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## acquireAccess

```TypeScript
function acquireAccess(dataType: DataType): AccessStatus
```

Requests the permission to access a specified type of sensitive data under the lock screen synchronously. After the request is successful, the reference count of the sensitive data key increases, preventing the key from being destroyed after the screen has been locked for the system-configured duration threshold. This method must be used in pair with [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md).Before calling this API, ensure that the app has enabled the sensitive data protection under lock screen feature and that the key state queried through the [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md) API is KEY_EXIST.

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA or ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA

**System capability:** SystemCapability.Security.ScreenLockFileManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataType | [DataType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AccessStatus](arkts-ability-screenlockfilemanager-accessstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29300001](../errorcode-screenLockFileManager.md#29300001-invalid-parameter) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-system-service-abnormal) |
| [29300003](../errorcode-screenLockFileManager.md#29300003-sensitive-data-access-management-under-lock-screen-is-not-enabled) |
| [29300004](../errorcode-screenLockFileManager.md#29300004-permission-to-access-sensitive-data-on-the-lock-screen-has-been-revoked) |
