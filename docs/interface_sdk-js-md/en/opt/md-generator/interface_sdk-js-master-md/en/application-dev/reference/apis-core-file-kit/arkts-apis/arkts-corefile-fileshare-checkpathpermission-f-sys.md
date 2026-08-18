# checkPathPermission (System API)

## Modules to Import

```TypeScript
```

## checkPathPermission

```TypeScript
function checkPathPermission(tokenID: number, policies: Array<PathPolicyInfo>, policyType: PolicyType): Promise<Array<boolean>>
```

Check permissions for the path.

**Since:** 23

**Required permissions:** ohos.permission.CHECK_SANDBOX_POLICY

<!--Device-fileShare-function checkPathPermission(tokenID: int, policies: Array<PathPolicyInfo>, policyType: PolicyType): Promise<Array<boolean>>--><!--Device-fileShare-function checkPathPermission(tokenID: int, policies: Array<PathPolicyInfo>, policyType: PolicyType): Promise<Array<boolean>>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| policies | Array&lt;[PathPolicyInfo](arkts-corefile-fileshare-pathpolicyinfo-i.md)&gt; | Yes |
| [policyType](../../apis-mdm-kit/arkts-apis/arkts-mdm-systemmanager-otaupdatepolicy-i.md) | [PolicyType](arkts-corefile-fileshare-policytype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;boolean & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900042 |

**Examples**

```TypeScript
import { fileShare } from '@kit.CoreFileKit';

async function checkPersistentPermissionExample() {
  try {
    let pathPolicyInfo1: fileShare.PathPolicyInfo = {
      path: '/storage/Users/currentUser/Documents/1.txt',
      operationMode: fileShare.OperationMode.READ_MODE,
    }
    let pathPolicyInfo2: fileShare.PathPolicyInfo = {
      path: '/storage/Users/currentUser/Desktop/2.txt',
      operationMode: fileShare.OperationMode.READ_MODE,
    }

    let policies: Array<fileShare.PathPolicyInfo> = [pathPolicyInfo1, pathPolicyInfo2];
    let policyType: fileShare.PolicyType = fileShare.PolicyType.PERSISTENT_TYPE;
    let tokenID = 537688848; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system app, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system app.

    fileShare.checkPathPermission(tokenID, policies, policyType).then((result: Array<boolean>) => {
      for (let hasPermission of result) {
        console.info('check permission result is', hasPermission);
      }
    });
    console.info('checkPathPermission finish');
  } catch (error) {
    console.info(`checkPathPermission error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
