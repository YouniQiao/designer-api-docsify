# getPersistentPolicy (System API)

## Modules to Import

```TypeScript
import { fileShare } from '@kit.CoreFileKit';
```

## getPersistentPolicy

```TypeScript
function getPersistentPolicy(tokenID: number): Promise<Array<PolicyInfo>>
```

Get all persistence permissions for the application.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_FILE_ACCESS_PERSIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileShare-function getPersistentPolicy(tokenID: int): Promise<Array<PolicyInfo>>--><!--Device-fileShare-function getPersistentPolicy(tokenID: int): Promise<Array<PolicyInfo>>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 13900001 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function getPersistentPolicyExample() {
  try {
    let tokenID = 537688848; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system app, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system app.
    fileShare.getPersistentPolicy(tokenID).then((result: Array<fileShare.PolicyInfo>) => {
      for (let policy of result) {
        console.info(`get persist policy URI: ${policy.uri}, operationMode: ${policy.operationMode}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`get persist policy failed with error, Code: ${err.code}, message: ${err.message}`);
    });
  } catch (error) {
    console.error(`get persist policy failed with error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
