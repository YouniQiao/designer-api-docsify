# @ohos.ability.screenLockFileManager(Sensitive Data Access Management Under Lock Screen)

This module provides the capability to protect app sensitive data under the lock screen, supporting requesting and releasing access permissions for sensitive data under the lock screen, as well as querying the status of sensitive data keys. When the reference count of a sensitive data key reaches zero and the screen has been locked for a duration reaching the system-configured lock duration threshold, the key is destroyed, and operations on that data become impossible. These keys can be restored only after the screen is unlocked. By calling the [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md) API of this module, you can prevent the key from being destroyed after the screen has been locked for a duration reaching the system-configured lock duration threshold.

> **NOTE：**&gt;
> - To enable the sensitive data protection function under the lock screen for an app, you need to configure the
> ohos.permission.PROTECT_SCREEN_LOCK_DATA permission in
> [requestPermissions](../../../security/AccessToken/declare-permissions.md#declaring-permissions-in-the-configuration-file).

**Since:** 12

**System capability:** SystemCapability.Security.ScreenLockFileManager

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireAccess(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-acquireaccess-f.md) |
| [queryAppKeyState(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-queryappkeystate-f.md) |
| [releaseAccess(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-releaseaccess-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireAccess(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-acquireaccess-f-sys.md) |
| [queryAppKeyState(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-queryappkeystate-f-sys.md) |
| [releaseAccess(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-releaseaccess-f-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccessStatus(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-accessstatus-e.md) |
| [DataType(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-datatype-e.md) |
| [KeyStatus(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-keystatus-e.md) |
| [ReleaseStatus(Sensitive Data Access Management Under Lock Screen)](arkts-ability-screenlockfilemanager-releasestatus-e.md) |
