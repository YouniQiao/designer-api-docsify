# getPersistentPolicy (System API)

## Modules to Import

```TypeScript
import { fileShare } from '@kit.CoreFileKit';
```

## getPersistentPolicy

```TypeScript
function getPersistentPolicy(tokenID: int): Promise<Array<PolicyInfo>>
```

Get all persistence permissions for the application.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_FILE_ACCESS_PERSIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileShare-function getPersistentPolicy(tokenID: int): Promise<Array<PolicyInfo>>--><!--Device-fileShare-function getPersistentPolicy(tokenID: int): Promise<Array<PolicyInfo>>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Token ID of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt;&gt; | Returns all persistence policy information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid tokenID |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 13900001 | Operation not permitted. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed, usually the result returned by VerifyAccessToken. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13900011 | Out of memory |

