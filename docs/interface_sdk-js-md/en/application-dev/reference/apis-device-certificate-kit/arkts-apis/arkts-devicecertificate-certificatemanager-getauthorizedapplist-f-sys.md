# getAuthorizedAppList (System API)

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getAuthorizedAppList

```TypeScript
function getAuthorizedAppList(keyUri: string) : Promise<CMResult>
```

获取用户公共凭据的授权应用列表，仅证书管理应用调用。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function getAuthorizedAppList(keyUri: string) : Promise<CMResult>--><!--Device-certificateManager-function getAuthorizedAppList(keyUri: string) : Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyUri | string | Yes | 表示用户公共凭据的唯一标识符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CMResult&gt; | Promise对象，返回获取授权应用列表的结果，返回值为 [CMResult]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter verification failed. &lt;br&gt; Possible causes: the URI is null or the URI format is wrong. |
| 201 | Permission verification failed. &lt;br&gt; The application does not have the permission required to call the API. |
| 17500002 | Indicates that the certificate does not exist. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; &lt;br&gt;2. Memory operation error; 3. File operation error. Please try again. |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* Unique identifier of the user public credential. */
try {
  certificateManager.getAuthorizedAppList(keyUri).then((cmResult: certificateManager.CMResult) => {
    if (cmResult?.appUidList == undefined) {
      console.info('The result of getting authorized app list is undefined.');
    } else {
      let appUidList: Array<string> = cmResult.appUidList;
      console.info('Succeeded in getting authorized app list.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get authorized app list. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get authorized app list. Code: ${error.code}, message: ${error.message}`);
}
```

