# setCertificateStatus（系统接口）

## setCertificateStatus

```TypeScript
function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>
```

设置CA证书的状态，当前仅支持设置用户CA证书状态，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_USER_TRUSTED_CERT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManager-function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>--><!--Device-certificateManager-function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| certUri | string | 是 |
| certType | [CertType](arkts-devicecertificate-certificatemanager-certtype-e.md) | 是 |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17500002](../errorcode-certManager.md#17500002-证书不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |

## 示例

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certUri: string = 'test'; /* 用户CA证书的唯一标识符 */
try {
  /* 设置用户CA证书状态为启用 */
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
