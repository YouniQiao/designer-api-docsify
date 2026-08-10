# grantPublicCertificate (System API)

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## grantPublicCertificate

```TypeScript
function grantPublicCertificate(keyUri: string, clientAppUid: int) : Promise<CMResult>
```

授予应用使用用户公共凭据的权限，仅证书管理应用调用。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function grantPublicCertificate(keyUri: string, clientAppUid: int) : Promise<CMResult>--><!--Device-certificateManager-function grantPublicCertificate(keyUri: string, clientAppUid: int) : Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyUri | string | Yes | 表示用户公共凭据的唯一标识符。 |
| clientAppUid | int | Yes | 表示应用UID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CMResult&gt; | Promise对象，返回授予应用使用用户公共凭据权限的结果，返回值为 [CMResult]{ |

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
let clientAppUid: number = 1001; /* Application UID */
try {
  certificateManager.grantPublicCertificate(keyUri, clientAppUid).then((cmResult: certificateManager.CMResult) => {
    let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
    console.info('Succeeded in granting public certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to grant public certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to grant public certificate. Code: ${error.code}, message: ${error.message}`);
}
```

