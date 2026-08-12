# @ohos.privacyManager(Privacy Management)

###### Core Enum Types
 - **[PermissionUsageFlag](arkts-ability-privacymanager-permissionusageflag-e-sys.md#PermissionUsageFlag):** Enum for querying permission usage records,
 used to specify querying summary data or detailed data.
 - **[PermissionActiveStatus](arkts-ability-privacymanager-permissionactivestatus-e-sys.md#PermissionActiveStatus):** Enum for permission usage status change
 types, used to indicate unused, foreground use, or background use status.
 - **[PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md#PermissionUsedType):** Enum for sensitive permission usage types, used
 to indicate the use of sensitive permissions through normal authorization, Picker, or security components.
 ###### Core Interface Types
 - **[PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md#PermissionUsedRequest):** Permission usage record query request
 object, used to specify the query application, permission, time range, and query method.
 - **[PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md#PermissionUsedResponse):** Permission usage record query response
 object, used to return the query time range and a collection of application-level records.
 - **[BundleUsedRecord](arkts-ability-privacymanager-bundleusedrecord-i-sys.md#BundleUsedRecord):** Application or device-level permission usage record
 object, used to return the permission access records of a specific application or remote device.
 - **[PermissionUsedRecord](arkts-ability-privacymanager-permissionusedrecord-i-sys.md#PermissionUsedRecord):** Access record object for a single
 permission, used to return the number of accesses, number of denials, last access time, and detailed records.
 - **[UsedRecordDetail](arkts-ability-privacymanager-usedrecorddetail-i-sys.md#UsedRecordDetail):** Single access record detail object, used to return
 information such as access status, timestamp, access duration, and usage type.
 - **[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md#ActiveChangeResponse):** Permission usage status change event
 object, to return details of permission active status changes.
 - **[PermissionUsedTypeInfo](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md#PermissionUsedTypeInfo):** Permission usage type information
 object, used to return the usage type when an application accesses a sensitive permission.
 - **[AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md#AddPermissionUsedRecordOptions):** Optional parameter
 object for adding a permission usage record, used to specify the sensitive permission usage type and extension
 identity.
 - **[PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md#PermissionUsingOptions):** Optional parameter object for
 permission usage, used to specify the extension identity.
 ###### Core Function Types
 - **[addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord):** Adds a permission usage record.
 - **[getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getPermissionUsedRecord):** Queries permission usage records.
 - **[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus):** Sets the
 permission usage record toggle status.
 - **[getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getPermissionUsedRecordToggleStatus):** Queries the
 permission usage record toggle status.
 - **[startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission):** Marks the start of using a sensitive
 permission.
 - **[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission):** Marks the stop of using a sensitive
 permission.
 - **[checkPermissionInUse](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md#checkPermissionInUse):** Checks whether a specified permission is
 currently being used.
 - **[on](privacyManager.on):** Subscribes to permission usage status change events.
 - **[off](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authinstance-i.md#off):** Unsubscribes from permission usage status change events.
 - **[getPermissionUsedTypeInfos](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md#getPermissionUsedTypeInfos):** Queries sensitive permission
 access type information.
 ###### Core Class
 - **privacyManager:** Provides the core class for privacy management.
 ![image_privacyManager](../../../reference/apis-ability-kit/figures/privacyManager.png)


**Since:** 9

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
| [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord) |
| [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord-1) |
| [checkPermissionInUse](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md#checkpermissioninuse) |
| [getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getpermissionusedrecord) |
| [getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getpermissionusedrecord-1) |
| [getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getpermissionusedrecordtogglestatus) |
| [getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getpermissionusedrecordtogglestatus-1) |
| [getPermissionUsedTypeInfos](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md#getpermissionusedtypeinfos) |
| [off](arkts-ability-privacymanager-off-f-sys.md#off) |
| [on](arkts-ability-privacymanager-on-f-sys.md#on) |
| [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus) |
| [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus-1) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-1) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-2) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-3) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission-1) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission-2) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission-3) |
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
| [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | Enumerates the means for using a sensitive permission.  \| Name \| Value\| Description \|  \| ----------------------- \| -- \| ---------------- \|  \| NORMAL_TYPE \| 0 \| The sensitive permission is used after authorization through a dialog box or a system settings page. \|  \| PICKER_TYPE \| 1 \| Indicates that a sensitive permission is used through a PICKER service, but this method does not grant the permission. \|  \| SECURITY_COMPONENT_TYPE \| 2 \| Indicates that a sensitive permission is used through security component authorization. A security component is a system-provided authorization component; after the user taps it, the application can temporarily obtain the corresponding permission. \|
<!--DelEnd-->
