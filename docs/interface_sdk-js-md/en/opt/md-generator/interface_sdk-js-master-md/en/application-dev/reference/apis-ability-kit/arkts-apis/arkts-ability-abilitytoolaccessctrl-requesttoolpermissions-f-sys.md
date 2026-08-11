# requestToolPermissions (System API)

## requestToolPermissions

```TypeScript
export function requestToolPermissions(permissionQuery: PermissionQuery): Promise<PermissionQueryResult>
```

Queries tool permissions based on the specified operations.This function checks the permission status for CLI commands or APIs specified in permissionQuery.operationInfo.For each operation, it returns the permission status, authorization status, and whether a user dialog is required.When needTicket is set to true, a ticket will be generated for remote authorization.

**Since:** 26.0.0

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function requestToolPermissions(permissionQuery: PermissionQuery): Promise<PermissionQueryResult>--><!--Device-abilityToolAccessCtrl-export function requestToolPermissions(permissionQuery: PermissionQuery): Promise<PermissionQueryResult>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionQuery | [PermissionQuery](arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PermissionQueryResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 24010006 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 24010002 |
| 24010003 |
| 24010000 |
| 24010001 |
