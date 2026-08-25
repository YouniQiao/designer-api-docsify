# checkPathPermission (System API)

## Modules to Import

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## checkPathPermission

```TypeScript
function checkPathPermission(tokenID: number, policies: Array<PathPolicyInfo>, policyType: PolicyType): Promise<Array<boolean>>
```

Check permissions for the path.

**Since:** 15

**Required permissions:** ohos.permission.CHECK_SANDBOX_POLICY

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| policies | Array&lt;[PathPolicyInfo](arkts-corefile-fileshare-pathpolicyinfo-i.md)&gt; | Yes |
| [policyType](../../apis-mdm-kit/arkts-apis/arkts-mdm-systemmanager-otaupdatepolicy-i.md) | [PolicyType](../../apis-mdm-kit/arkts-apis/arkts-mdm-systemmanager-policytype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;boolean & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 13900042 |
