# generateControlledDevicePackage (System API)

## Modules to Import

```TypeScript
```

## generateControlledDevicePackage

```TypeScript
export function generateControlledDevicePackage(permissionQuery: PermissionQuery[]): Promise<RemoteAuthPackage[]>
```

Generates an authorization package for the controlled device. This function generates a remote authorization package based on the permission query list. The generated package can be sent to the controller device for permission verification.

**Since:** 26.1.0

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionQuery | [PermissionQuery](arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md)[] | Yes | Permission query list. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[RemoteAuthPackage](arkts-ability-abilitytoolaccessctrl-remoteauthpackage-i-sys.md)[]&gt; | Promise used to return \\${RemoteAuthPackage[]}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denial. The interface caller does not have permission "ohos.permission.QUERY_TOOL_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 24010000 | Invalid parameter. Permission exceeds 256 characters, specified tokenId is invalid, etc. |
| 24010001 | Service is abnormal. Possible cause: IPC failed. |
| 24010002 | Common internal error. Possible cause: dependent service unavailable, resource access failure, etc. |
| 24010003 | The account is not logged in, network is unavailable, timeout, etc. |
