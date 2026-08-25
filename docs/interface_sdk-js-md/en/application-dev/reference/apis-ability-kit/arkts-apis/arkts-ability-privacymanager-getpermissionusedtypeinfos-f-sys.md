# getPermissionUsedTypeInfos (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## getPermissionUsedTypeInfos

```TypeScript
function getPermissionUsedTypeInfos(
    tokenId?: number | null,
    permissionName?: Permissions): Promise<Array<PermissionUsedTypeInfo>>
```

Obtains information about how a sensitive permission is used by an application.

**Since:** 12

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenId | number \| null | No |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PermissionUsedTypeInfo](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
