# @ohos.privacyManager(Privacy Management)

###### Core Enum Types
 - **[PermissionUsageFlag](arkts-ability-privacymanager-permissionusageflag-e-sys.md):** Enum for querying permission usage records,
 used to specify querying summary data or detailed data.
 - **[PermissionActiveStatus](arkts-ability-privacymanager-permissionactivestatus-e-sys.md):** Enum for permission usage status change
 types, used to indicate unused, foreground use, or background use status.
 - **[PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md):** Enum for sensitive permission usage types, used
 to indicate the use of sensitive permissions through normal authorization, Picker, or security components.
 ###### Core Interface Types
 - **[PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md):** Permission usage record query request
 object, used to specify the query application, permission, time range, and query method.
 - **[PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md):** Permission usage record query response
 object, used to return the query time range and a collection of application-level records.
 - **[BundleUsedRecord](arkts-ability-privacymanager-bundleusedrecord-i-sys.md):** Application or device-level permission usage record
 object, used to return the permission access records of a specific application or remote device.
 - **[PermissionUsedRecord](arkts-ability-privacymanager-permissionusedrecord-i-sys.md):** Access record object for a single
 permission, used to return the number of accesses, number of denials, last access time, and detailed records.
 - **[UsedRecordDetail](arkts-ability-privacymanager-usedrecorddetail-i-sys.md):** Single access record detail object, used to return
 information such as access status, timestamp, access duration, and usage type.
 - **[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md):** Permission usage status change event
 object, to return details of permission active status changes.
 - **[PermissionUsedTypeInfo](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md):** Permission usage type information
 object, used to return the usage type when an application accesses a sensitive permission.
 - **[AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md):** Optional parameter
 object for adding a permission usage record, used to specify the sensitive permission usage type and extension
 identity.
 - **[PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md):** Optional parameter object for
 permission usage, used to specify the extension identity.
 ###### Core Function Types
 - **[addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md):** Adds a permission usage record.
 - **[getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md):** Queries permission usage records.
 - **[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md):** Sets the
 permission usage record toggle status.
 - **[getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md):** Queries the
 permission usage record toggle status.
 - **[startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md):** Marks the start of using a sensitive
 permission.
 - **[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md):** Marks the stop of using a sensitive
 permission.
 - **[checkPermissionInUse](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md):** Checks whether a specified permission is
 currently being used.
 - **[on](arkts-ability-privacymanager-on-f-sys.md):** Subscribes to permission usage status change events.
 - **[off](arkts-ability-privacymanager-off-f-sys.md):** Unsubscribes from permission usage status change events.
 - **[getPermissionUsedTypeInfos](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md):** Queries sensitive permission
 access type information.
 ###### Core Class
 - **privacyManager:** Provides the core class for privacy management.
 


**Since:** 9

**System capability:** SystemCapability.Security.AccessToken

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addPermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md) |
| [addPermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md) |
| [checkPermissionInUse(Privacy Management)](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md) |
| [getPermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md) |
| [getPermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md) |
| [getPermissionUsedRecordToggleStatus(Privacy Management)](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md) |
| [getPermissionUsedRecordToggleStatus(Privacy Management)](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md) |
| [getPermissionUsedTypeInfos(Privacy Management)](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md) |
| off(Privacy Management) |
| on(Privacy Management) |
| [setPermissionUsedRecordToggleStatus(Privacy Management)](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md) |
| [setPermissionUsedRecordToggleStatus(Privacy Management)](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md) |
| [startUsingPermission(Privacy Management)](arkts-ability-privacymanager-startusingpermission-f-sys.md) |
| [startUsingPermission(Privacy Management)](arkts-ability-privacymanager-startusingpermission-f-sys.md) |
| [startUsingPermission(Privacy Management)](arkts-ability-privacymanager-startusingpermission-f-sys.md) |
| [startUsingPermission(Privacy Management)](arkts-ability-privacymanager-startusingpermission-f-sys.md) |
| [stopUsingPermission(Privacy Management)](arkts-ability-privacymanager-stopusingpermission-f-sys.md) |
| [stopUsingPermission(Privacy Management)](arkts-ability-privacymanager-stopusingpermission-f-sys.md) |
| [stopUsingPermission(Privacy Management)](arkts-ability-privacymanager-stopusingpermission-f-sys.md) |
| [stopUsingPermission(Privacy Management)](arkts-ability-privacymanager-stopusingpermission-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActiveChangeResponse(Privacy Management)](arkts-ability-privacymanager-activechangeresponse-i-sys.md) |
| [AddPermissionUsedRecordOptions(Privacy Management)](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) |
| [BundleUsedRecord(Privacy Management)](arkts-ability-privacymanager-bundleusedrecord-i-sys.md) |
| [PermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-permissionusedrecord-i-sys.md) |
| [PermissionUsedRequest(Privacy Management)](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) |
| [PermissionUsedResponse(Privacy Management)](arkts-ability-privacymanager-permissionusedresponse-i-sys.md) |
| [PermissionUsedTypeInfo(Privacy Management)](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md) |
| [PermissionUsingOptions(Privacy Management)](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) |
| [UsedRecordDetail(Privacy Management)](arkts-ability-privacymanager-usedrecorddetail-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PermissionActiveStatus(Privacy Management)](arkts-ability-privacymanager-permissionactivestatus-e-sys.md) |
| [PermissionUsageFlag(Privacy Management)](arkts-ability-privacymanager-permissionusageflag-e-sys.md) |
| [PermissionUsedType(Privacy Management)](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | Enumerates the means for using a sensitive permission.  \| Name \| Value\| Description \| \| ----------------------- \| -- \| ---------------- \| \| NORMAL_TYPE \| 0 \| The sensitive permission is used after authorization through a dialog box or a system settings page. \| \| PICKER_TYPE \| 1 \| Indicates that a sensitive permission is used through a PICKER service, but this method does not grant the permission. \| \| SECURITY_COMPONENT_TYPE \| 2 \| Indicates that a sensitive permission is used through security component authorization. A security component is a system-provided authorization component; after the user taps it, the application can temporarily obtain the corresponding permission. \|
<!--DelEnd-->
