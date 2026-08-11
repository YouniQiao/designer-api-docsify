# revokePermission (System API)

## Modules to Import

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## revokePermission

```TypeScript
function revokePermission(tokenID: int): Promise<void>
```

Revoke all persistence permissions for the application.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.REVOKE_FILE_ACCESS_PERSIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileShare-function revokePermission(tokenID: int): Promise<void>--><!--Device-fileShare-function revokePermission(tokenID: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Token ID of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid tokenID |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 13900001 | Operation not permitted. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed, usually the result returned by VerifyAccessToken. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |


## revokePermission

```TypeScript
function revokePermission(tokenID: int, policies: Array<PolicyInfo>): Promise<void>
```

Revoke persistence permissions for the URI.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.REVOKE_FILE_ACCESS_PERSIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileShare-function revokePermission(tokenID: int, policies: Array<PolicyInfo>): Promise<void>--><!--Device-fileShare-function revokePermission(tokenID: int, policies: Array<PolicyInfo>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Token ID of the application. |
| policies | Array&lt;PolicyInfo&gt; | Yes | Policy information to revoke permission on URIs. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid tokenID |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types; 3.Invalid policy size. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 13900001 | Operation not permitted. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed, usually the result returned by VerifyAccessToken. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13900011 | Out of memory |

