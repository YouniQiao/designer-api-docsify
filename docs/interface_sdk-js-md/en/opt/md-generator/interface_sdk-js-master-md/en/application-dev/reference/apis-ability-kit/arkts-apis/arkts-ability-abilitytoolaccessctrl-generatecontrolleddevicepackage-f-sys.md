# generateControlledDevicePackage (System API)

## generateControlledDevicePackage

```TypeScript
export function generateControlledDevicePackage(permissionQuery: PermissionQuery[]): Promise<RemoteAuthPackage[]>
```

Generates an authorization package for the controlled device.This function generates a remote authorization package based on the permission query list.The generated package can be sent to the controller device for permission verification.

**Since:** 26.1.0

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function generateControlledDevicePackage(permissionQuery: PermissionQuery[]): Promise<RemoteAuthPackage[]>--><!--Device-abilityToolAccessCtrl-export function generateControlledDevicePackage(permissionQuery: PermissionQuery[]): Promise<RemoteAuthPackage[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionQuery | [PermissionQuery](arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RemoteAuthPackage[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 24010002 |
| 24010003 |
| 24010000 |
| 24010001 |
