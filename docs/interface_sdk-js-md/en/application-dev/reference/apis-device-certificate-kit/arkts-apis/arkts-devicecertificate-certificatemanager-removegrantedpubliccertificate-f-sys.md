# removeGrantedPublicCertificate (System API)

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## removeGrantedPublicCertificate

```TypeScript
function removeGrantedPublicCertificate(keyUri: string, clientAppUid: int) : Promise<void>
```

移除应用使用用户公共凭据的权限，仅证书管理应用调用。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function removeGrantedPublicCertificate(keyUri: string, clientAppUid: int) : Promise<void>--><!--Device-certificateManager-function removeGrantedPublicCertificate(keyUri: string, clientAppUid: int) : Promise<void>-End-->

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
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

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
  certificateManager.removeGrantedPublicCertificate(keyUri, clientAppUid).then(() => {
    console.info('Succeeded in removing granted public certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to remove granted public certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to remove granted public certificate. Code: ${error.code}, message: ${error.message}`);
}
```

