# generateControlledDevicePackage (System API)

## generateControlledDevicePackage

```TypeScript
export function generateControlledDevicePackage(permissionQuery: PermissionQuery[]): Promise<RemoteAuthPackage[]>
```

生成受控设备的授权包。根据权限查询列表生成远程授权包。生成的包可以发送到控制器设备进行权限验证。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function generateControlledDevicePackage(permissionQuery: PermissionQuery[]): Promise<RemoteAuthPackage[]>--><!--Device-abilityToolAccessCtrl-export function generateControlledDevicePackage(permissionQuery: PermissionQuery[]): Promise<RemoteAuthPackage[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionQuery | [PermissionQuery](arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md)[] | Yes | 权限查询列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;RemoteAuthPackage[]&gt; | Promise用于返回\\${RemoteAuthPackage[]}。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denial. The interface caller does not have permission "ohos.permission.QUERY_TOOL_PERMISSIONS". |
| 202 | The caller is not a system application. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010003 | The account is not logged in, network is unavailable, timeout, etc. |
| 24010000 | Invalid parameter. Permission exceeds 256 characters, specificied tokenId is invalid, etc. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |

