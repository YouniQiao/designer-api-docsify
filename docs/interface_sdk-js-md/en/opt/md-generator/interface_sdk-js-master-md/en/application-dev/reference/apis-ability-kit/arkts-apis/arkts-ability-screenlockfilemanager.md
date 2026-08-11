# @ohos.ability.screenLockFileManager(Sensitive Data Access Management Under Lock Screen)

This module provides the capability to protect app sensitive data under the lock screen, supporting requesting and releasing access permissions for sensitive data under the lock screen, as well as querying the status of sensitive data keys. When the reference count of a sensitive data key reaches zero and the screen has been locked for a duration reaching the system-configured lock duration threshold, the key is destroyed, and operations on that data become impossible. These keys can be restored only after the screen is unlocked. By calling the   
[acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireaccess) API of this module, you can prevent the key from being destroyed after the screen has been locked for a duration reaching the system-configured lock duration threshold.

> **NOTE：**
> 
> - To enable the sensitive data protection function under the lock screen for an app, you need to configure the
> ohos.permission.PROTECT_SCREEN_LOCK_DATA permission in
> [requestPermissions](../../../security/AccessToken/declare-permissions.md#declaring-permissions-in-the-configuration-file).

**Since:** 12

<!--Device-unnamed-declare namespace screenLockFileManager--><!--Device-unnamed-declare namespace screenLockFileManager-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireaccess) |
| [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md#queryappkeystate) |
| [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md#releaseaccess) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f-sys.md#acquireaccess-1) |
| [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f-sys.md#queryappkeystate-1) |
| [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f-sys.md#releaseaccess-1) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccessStatus](arkts-ability-screenlockfilemanager-accessstatus-e.md) |
| [DataType](arkts-ability-screenlockfilemanager-datatype-e.md) |
| [KeyStatus](arkts-ability-screenlockfilemanager-keystatus-e.md) |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) |
