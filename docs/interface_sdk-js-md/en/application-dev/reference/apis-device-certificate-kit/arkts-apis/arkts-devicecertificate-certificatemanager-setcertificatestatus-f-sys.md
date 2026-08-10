# setCertificateStatus (System API)

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## setCertificateStatus

```TypeScript
function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>
```

设置CA证书的状态，当前仅支持设置用户CA证书状态，仅证书管理应用调用。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_USER_TRUSTED_CERT

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>--><!--Device-certificateManager-function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| certUri | string | Yes | 表示证书的唯一标识符。当前仅支持用户CA证书。 |
| certType | [CertType](../../apis-network-kit/arkts-apis/arkts-network-http-certtype-e.md) | Yes | 表示证书类型。当前仅支持设置用户CA证书（CA_CERT_USER）的状态。 |
| enabled | boolean | Yes | 表示证书状态是否启用。true：已启用，false：已禁用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter verification failed. &lt;br&gt;Possible causes: the URI is null or the URI format is wrong, &lt;br&gt; the certType's value is invalid or not supported. |
| 201 | Permission verification failed. &lt;br&gt;The application does not have the permission required to call the API. |
| 17500002 | The certificate does not exist. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; &lt;br&gt;2. Memory operation error; 3. File operation error. Please try again. |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certUri: string = 'test'; /* Unique identifier of the user CA certificate. */
try {
  /* Set the user CA certificate status to enabled. */
  certificateManager.setCertificateStatus(certUri, certificateManager.CertType.CA_CERT_USER, true).then(() => {
    console.info('Succeeded in setting certificate status.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to set certificate status. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to set certificate status. Code: ${error.code}, message: ${error.message}`);
}
```

