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
 - **[addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord):** Adds a permission usage record.
 - **[getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getpermissionusedrecord):** Queries permission usage records.
 - **[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus):** Sets the
 permission usage record toggle status.
 - **[getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getpermissionusedrecordtogglestatus):** Queries the
 permission usage record toggle status.
 - **[startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission):** Marks the start of using a sensitive
 permission.
 - **[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission):** Marks the stop of using a sensitive
 permission.
 - **[checkPermissionInUse](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md#checkpermissioninuse):** Checks whether a specified permission is
 currently being used.
 - **[on](privacyManager.on):** Subscribes to permission usage status change events.
 - **[off](privacyManager.off):** Unsubscribes from permission usage status change events.
 - **[getPermissionUsedTypeInfos](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md#getpermissionusedtypeinfos):** Queries sensitive permission
 access type information.
 ###### Core Class
 - **privacyManager:** Provides the core class for privacy management.
 ![image_privacyManager](../../../reference/apis-ability-kit/figures/privacyManager.png)


**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace privacyManager--><!--Device-unnamed-declare namespace privacyManager-End-->

**System capability:** SystemCapability.Security.AccessToken

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord) | When an application protected by a permission is called by another service or application, this API can be used to add a permission usage record. It is recommended to call this API after accessing a sensitive permission, so that the system records the corresponding sensitive permission access event. This API uses a promise to return the result.  The permission usage record includes the application identity of the caller, the name of the application permission,and the number of successful and failed accesses to this application by the caller.  > **NOTE：** > The permission usage record is controlled by the toggle status set by [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus). When the toggle is off, calling this API will not generate a permission usage record. |
| [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord-1) | When an application protected by a permission is called by another service or application, this API can be used to add a permission usage record. It is recommended to call this API after accessing a sensitive permission, so that the system records the corresponding sensitive permission access event. This API uses an asynchronous callback to return the result.  The permission usage record includes the application identity of the caller, the name of the application permission used, and the number of successful and failed accesses to this application by the caller.  The permission usage record is controlled by the toggle status set by  [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus). When the toggle is off, calling this API will not generate a permission usage record. |
| [checkPermissionInUse](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md#checkpermissioninuse) | Queries whether a specified sensitive permission is currently being used. It can be used in scenarios such as displaying the real-time permission usage status on the permission management interface. The judgment is based on whether there is currently an active call that has been marked as started by  [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission) and has not yet been marked as stopped by  [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission). |
| [getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getpermissionusedrecord) | Obtains historical permission usage records, which can be used in permission auditing or security monitoring scenarios, such as checking an application's usage of sensitive permissions within a specified time period.This API uses a promise to return the result. |
| [getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getpermissionusedrecord-1) | Obtains historical permission usage records, which can be used in permission auditing or security monitoring scenarios, such as checking an application's usage of sensitive permissions within a specified time period.This API uses an asynchronous callback to return the result. |
| [getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getpermissionusedrecordtogglestatus) | A system application can call this API to obtain the current user's permission usage record toggle status, for example, to display the current toggle setting status on the permission management interface. This API uses a promise to return the result. |
| [getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getpermissionusedrecordtogglestatus-1) | A system application can call this API to obtain the permission usage record toggle status for a specified sub-profile, for example, to display the current toggle setting status on the permission management interface.This API uses a promise to return the result. |
| [getPermissionUsedTypeInfos](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md#getpermissionusedtypeinfos) | Obtains information about how a sensitive permission is used by an application. |
| [off](arkts-ability-privacymanager-off-f-sys.md#off) | Unsubscribes from permission usage status change events for a specified permission list. After a successful unsubscription, status change notifications for the specified permission list will no longer be received.  When unsubscribing, if no callback function is passed in, all callback functions under the permissionList are deleted in batch.  > **NOTE：** > This API is typically used in conjunction with [on](privacyManager.on) to cancel the listening relationship  created by on. |
| [offActiveStateChange](arkts-ability-privacymanager-offactivestatechange-f-sys.md#offactivestatechange) | Unsubscribes from permission usage status change events for a specified permission list. After a successful unsubscription, status change notifications for the specified permission list will no longer be received.  When unsubscribing, if no callback function is passed in, all callback functions under the permissionList are deleted in batch.  > **NOTE：** > This API is typically used in conjunction with [onActiveStateChange](privacyManager.onActiveStateChange) to  cancel the listening relationship created by onActiveStateChange. |
| [on](arkts-ability-privacymanager-on-f-sys.md#on) | Subscribes to permission usage status change events for a specified permission list. Permission usage status changes are triggered by calls to [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission) and  [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission). After a successful subscription, when the permission usage status changes, the callback function is triggered, returning an  [ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md) object containing details of the permission usage status change. This API uses an asynchronous callback to return the result.  Multiple callback functions are allowed to be subscribed for the same permissionList.  > **NOTE：** > It is not allowed to subscribe the same callback function using two permissionLists that have an intersection. > That is, if two permissionLists contain the same permission name, the same callback function cannot be used for subscription.  > This API is typically used in conjunction with [off](privacyManager.off). > When listening is no longer needed, off should be called to unsubscribe. |
| [onActiveStateChange](arkts-ability-privacymanager-onactivestatechange-f-sys.md#onactivestatechange) | Subscribes to permission usage status change events for a specified permission list. Permission usage status changes are triggered by calls to [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission) and  [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission). After a successful subscription, when the permission usage status changes, the callback function is triggered, returning an  [ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md) object containing details of the permission usage status change. This API uses an asynchronous callback to return the result.  Multiple callback functions are allowed to be subscribed for the same permissionList.  > **NOTE：** > It is not allowed to subscribe the same callback function using two permissionLists that have an intersection. > That is, if two permissionLists contain the same permission name, the same callback function cannot be used for subscription.  > This API is typically used in conjunction with [offActiveStateChange](privacyManager.offActiveStateChange).  When listening is no longer needed, offActiveStateChange should be called to unsubscribe. |
| [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus) | Sets whether to record the permission usage of this user. Sets the permission usage record switch for this user.This API uses a promise to return the result.  When **status** is **true**, the [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord) API can add usage records normally; when **status** is **false**, the  [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord) API does not generate permission usage records, and deletes the current user's historical records. |
| [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus-1) | Sets whether permission usage records are collected for a specified sub-profile. A system application can call this API to set the permission usage record switch status for the specified sub-profile. This API uses a promise to return the result.  When **status** is **true**, the [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord) API can add usage records normally; when **status** is **false**, the  [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addpermissionusedrecord) API does not generate permission usage records, and deletes the historical records of the specified sub-profile. |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission) | A system application can call this API to report the application's permission usage status in the foreground or background to the system. The privacy service notifies all subscribers of this permission usage status change event (refer to [on](privacyManager.on) for the subscription method). This API uses a promise to return the result.  After starting to use a permission, [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission) must be called to stop using the permission when the usage ends. |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-1) | A system application can call this API to report the application's permission usage status in the foreground or background to the system. The privacy service notifies all subscribers of this permission usage status change event (refer to [on](privacyManager.on) for the subscription method). This API uses a promise to return the result.  After starting to use a permission, [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission) must be called to stop using the permission when the usage ends. |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-2) | A system application can call this API to report the application's permission usage status in the foreground or background to the system. The privacy service notifies all subscribers of this permission usage status change event (refer to [on](privacyManager.on) for the subscription method). This API uses a promise to return the result.  After starting to use a permission, [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission) must be called to stop using the permission when the usage ends.  When a pid is passed in, the pid must be the same as the pid passed into  [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission). If the pairing relationship is not satisfied,error code 12100004 is returned. |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-3) | A system application can call this API to report the application's permission usage status in the foreground or background to the system. The privacy service notifies all subscribers of this permission usage status change event (refer to [on](privacyManager.on) for the subscription method). This API uses an asynchronous callback to return the result.  After starting to use a permission, [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission) must be called to stop using the permission when the usage ends. |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission) | A system application calls this API to mark that the specified permission is no longer in use. After a successful call, the privacy service notifies all subscribers of this permission usage status change event of this status change. It is suitable for notifying the system that permission usage has ended when an application completes a sensitive operation or exits the foreground. This API uses a promise to return the result.  This API must be used in conjunction with [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission). |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission-1) | A system application calls this API to mark that the specified permission is no longer in use. After a successful call, the privacy service notifies all subscribers of this permission usage status change event of this status change. It is suitable for notifying the system that permission usage has ended when an application completes a sensitive operation or exits the foreground. This API uses an asynchronous callback to return the result.  This API must be used in conjunction with [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission). |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission-2) | A system application calls this API to mark that the specified permission is no longer in use. After a successful call, the privacy service notifies all subscribers of this permission usage status change event of this status change. It is suitable for notifying the system that permission usage has ended when an application completes a sensitive operation or exits the foreground. This API uses a promise to return the result.  The PID must be the same as the PID passed in [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission). |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission-3) | A system application calls this API to mark that the specified permission is no longer in use. After a successful call, the privacy service notifies all subscribers of this permission usage status change event of this status change. It is suitable for notifying the system that permission usage has ended when an application completes a sensitive operation or exits the foreground. This API uses a promise to return the result.  The pid must be the same as the pid passed into [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission). |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md) | Defines the detailed permission usage information. |
| [AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) | Represents the options for adding a permission usage record. |
| [BundleUsedRecord](arkts-ability-privacymanager-bundleusedrecord-i-sys.md) | Represents the access records of an application or device. |
| [PermissionUsedRecord](arkts-ability-privacymanager-permissionusedrecord-i-sys.md) | Represents the access records of a permission. |
| [PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) | Represents the request for querying permission usage records. |
| [PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md) | Represents the access records of all applications or devices. |
| [PermissionUsedTypeInfo](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md) | Represents detailed information about the use of a permission. |
| [PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) | Represents the optional parameter set for using a permission. |
| [UsedRecordDetail](arkts-ability-privacymanager-usedrecorddetail-i-sys.md) | Represents the details of a single access record. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [PermissionActiveStatus](arkts-ability-privacymanager-permissionactivestatus-e-sys.md) | Enumerates the types of permission usage status changes. It is used to describe the change type of permission usage status, returned in the callback of subscribing to permission usage status change events (via  [on('activeStateChange')](privacyManager.on)), helping system applications sense the status switch of a permission from unused to foreground use and background use. |
| [PermissionUsageFlag](arkts-ability-privacymanager-permissionusageflag-e-sys.md) | Enumerates the modes for querying the permission usage records. |
| [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | Enumerates the means for using a sensitive permission.  \| Name \| Value\| Description \|  \| ----------------------- \| -- \| ---------------- \|  \| NORMAL_TYPE \| 0 \| The sensitive permission is used after authorization through a dialog box or a system settings page. \|  \| PICKER_TYPE \| 1 \| Indicates that a sensitive permission is used through a PICKER service, but this method does not grant the permission. \|  \| SECURITY_COMPONENT_TYPE \| 2 \| Indicates that a sensitive permission is used through security component authorization. A security component is a system-provided authorization component; after the user taps it, the application can temporarily obtain the corresponding permission. \| |
<!--DelEnd-->

