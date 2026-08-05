# checkPermissionInUse (System API)

## checkPermissionInUse

```TypeScript
function checkPermissionInUse(permissionName: Permissions): boolean
```

Queries whether a specified sensitive permission is currently being used. It can be used in scenarios such as displaying the real-time permission usage status on the permission management interface. The judgment is based on whether there is currently an active call that has been marked as started by [startUsingPermission]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and has not yet been marked as stopped by [stopUsingPermission]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

<!--Device-privacyManager-function checkPermissionInUse(permissionName: Permissions): boolean--><!--Device-privacyManager-function checkPermissionInUse(permissionName: Permissions): boolean-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Name of the permission to query. The permission name cannot be empty and its length cannot exceed 256 characters. An invalid value returns error code 12100001. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the specified sensitive permission is in use. true: The specified sensitive permission |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission"ohos.permission.PERMISSION\_\_\_ESCAPED\_UNDERSCORE\_\_\_USED\_\_\_ESCAPED\_UNDERSCORE\_\_\_STATS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system application. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionName is empty or exceeds 256 characters. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user\_\_\_ESCAPED\_UNDERSCORE\_\_\_grant permission. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

