# revokePermission (System API)

## Modules to Import

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## revokePermission

```TypeScript
function revokePermission(tokenID: number): Promise<void>
```

Revoke all persistence permissions for the application.

**Since:** 26.0.0

**Required permissions:** ohos.permission.REVOKE_FILE_ACCESS_PERSIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileShare-function revokePermission(tokenID: int): Promise<void>--><!--Device-fileShare-function revokePermission(tokenID: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 13900001 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function revokeAllPermissionExample() {
  try {
    let tokenID = 537688848; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system app, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system app.
    fileShare.revokePermission(tokenID).then(() => {
      console.info('revoke persist permission successfully.');
    }).catch((err: BusinessError) => {
      console.error(`revoke persist permission failed, Code: ${err.code}, message: ${err.message}`);
    });
  } catch (error) {
    console.error(`revoke persist permission failed error, Code: ${error.code}, message: ${error.message}`);
  }
}
```


## revokePermission

```TypeScript
function revokePermission(tokenID: number, policies: Array<PolicyInfo>): Promise<void>
```

Revoke persistence permissions for the URI.

**Since:** 26.0.0

**Required permissions:** ohos.permission.REVOKE_FILE_ACCESS_PERSIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileShare-function revokePermission(tokenID: int, policies: Array<PolicyInfo>): Promise<void>--><!--Device-fileShare-function revokePermission(tokenID: int, policies: Array<PolicyInfo>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| policies | Array&lt;PolicyInfo&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 13900001 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function revokeSpecificPermissionExample() {
  try {
    let tokenID = 537688848; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system app, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system app.
    let policyInfo: fileShare.PolicyInfo = {
      uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
      operationMode: fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.revokePermission(tokenID, policies).then(() => {
      console.info('revoke persist permission successfully.');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`revoke persist permission failed. Code: ${err.code}, message: ${err.message}`);
      if (err.code === 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error(`error code: ${JSON.stringify(err.data[i].code)}`);
          console.error(`error URI: ${JSON.stringify(err.data[i].uri)}`);
          console.error(`error reason: ${JSON.stringify(err.data[i].message)}`);
        }
      }
    });
  } catch (error) {
    console.error(`revokePermission error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
