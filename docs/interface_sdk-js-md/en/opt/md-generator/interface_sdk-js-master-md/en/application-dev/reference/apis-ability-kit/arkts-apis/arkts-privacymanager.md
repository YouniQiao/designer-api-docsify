# @ohos.privacyManager

This module primarily provides privacy management APIs such as permission usage records, supporting system applications in recording, querying, listening to, and controlling the usage of sensitive permissions. A permission usage record describes when a sensitive permission was used, how it was used, whether it is currently in use, and whether these usage records are allowed to be recorded or queried. This module is mainly used in the following scenarios: - Adding/querying the sensitive permission access records of a specified application. - Subscribing to permission usage status change events, sensing changes in permission usage from unused to foreground use and background use, and linking with business logic. - Controlling the permission access record toggle for the current user. - Querying whether a certain permission is currently being used.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace privacyManager--><!--Device-unnamed-declare namespace privacyManager-End-->

**System capability:** SystemCapability.Security.AccessToken

## Modules to Import

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord-(System-API)) |
| [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord-(System-API)) |
| [checkPermissionInUse](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md#checkPermissionInUse-(System-API)) |
| [getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getPermissionUsedRecord-(System-API)) |
| [getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getPermissionUsedRecord-(System-API)) |
| [getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getPermissionUsedRecordToggleStatus-(System-API)) |
| [getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getPermissionUsedRecordToggleStatus-(System-API)) |
| [getPermissionUsedTypeInfos](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md#getPermissionUsedTypeInfos-(System-API)) |
| [offActiveStateChange](arkts-ability-privacymanager-offactivestatechange-f-sys.md#offActiveStateChange-(System-API)) |
| off_activeStateChange |
| [onActiveStateChange](arkts-ability-privacymanager-onactivestatechange-f-sys.md#onActiveStateChange-(System-API)) |
| on_activeStateChange |
| [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus-(System-API)) |
| [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus-(System-API)) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission-(System-API)) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission-(System-API)) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission-(System-API)) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission-(System-API)) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission-(System-API)) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission-(System-API)) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission-(System-API)) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission-(System-API)) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md) |
| [AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) |
| [BundleUsedRecord](arkts-ability-privacymanager-bundleusedrecord-i-sys.md) |
| [PermissionUsedRecord](arkts-ability-privacymanager-permissionusedrecord-i-sys.md) |
| [PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) |
| [PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md) |
| [PermissionUsedTypeInfo](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md) |
| [PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) |
| [UsedRecordDetail](arkts-ability-privacymanager-usedrecorddetail-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PermissionActiveStatus](arkts-ability-privacymanager-permissionactivestatus-e-sys.md) |
| [PermissionUsageFlag](arkts-ability-privacymanager-permissionusageflag-e-sys.md) |
| [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | Enumerates the means for using a sensitive permission. \| Name \| Value\| Description \| \| ----------------------- \| -- \| ---------------- \| \| NORMAL_TYPE \| 0 \| The sensitive permission is used after authorization through a dialog box or a system settings page. \| \| PICKER_TYPE \| 1 \| Indicates that a sensitive permission is used through a PICKER service, but this method does not grant the permission. \| \| SECURITY_COMPONENT_TYPE \| 2 \| Indicates that a sensitive permission is used through security component authorization. A security component is a system-provided authorization component; after the user taps it, the application can temporarily obtain the corresponding permission. \|
<!--DelEnd-->
