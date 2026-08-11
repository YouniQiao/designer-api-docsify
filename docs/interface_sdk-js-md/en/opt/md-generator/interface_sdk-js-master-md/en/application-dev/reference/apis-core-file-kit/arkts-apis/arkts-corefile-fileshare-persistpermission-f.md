# persistPermission

## Modules to Import

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## persistPermission

```TypeScript
function persistPermission(policies: Array<PolicyInfo>): Promise<void>
```

Set persistence permissions for the URI

**Since:** 11

**Required permissions:** ohos.permission.FILE_ACCESS_PERSIST

<!--Device-fileShare-function persistPermission(policies: Array<PolicyInfo>): Promise<void>--><!--Device-fileShare-function persistPermission(policies: Array<PolicyInfo>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policies | Array&lt;PolicyInfo&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 13900001 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 13900042 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function persistPermissionExample() {
  try {
    let DocumentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(DocumentSelectOptions);
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris[0], 
      // Multiple permissions can be granted in combination. For example, the read and write permissions can be granted using fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE.
      operationMode: fileShare.OperationMode.READ_MODE
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.persistPermission(policies).then(() => {
      console.info("persistPermission successfully");
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("persistPermission failed with error message: " + err.message + ", error code: " + err.code);
      if (err.code == 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error("error code : " + JSON.stringify(err.data[i].code));
          console.error("error uri : " + JSON.stringify(err.data[i].uri));
          console.error("error reason : " + JSON.stringify(err.data[i].message));
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('persistPermission failed with err: ' + JSON.stringify(err));
  }
}
```
