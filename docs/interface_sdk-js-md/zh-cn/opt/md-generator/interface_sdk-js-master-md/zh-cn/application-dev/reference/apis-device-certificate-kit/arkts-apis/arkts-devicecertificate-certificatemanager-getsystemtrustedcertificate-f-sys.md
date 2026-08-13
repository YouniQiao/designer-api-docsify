# getSystemTrustedCertificate（系统接口）

## getSystemTrustedCertificate

```TypeScript
function getSystemTrustedCertificate(certUri: string): Promise<CMResult>
```

获取系统信任的CA证书详情，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManager-function getSystemTrustedCertificate(certUri: string): Promise<CMResult>--><!--Device-certificateManager-function getSystemTrustedCertificate(certUri: string): Promise<CMResult>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| certUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17500002](../errorcode-certManager.md#17500002-证书不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |

## 示例

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certUri: string = 'test'; /* 证书的唯一标识符，可通过getSystemTrustedCertificateList接口获取 */
try {
  certificateManager.getSystemTrustedCertificate(certUri).then((cmResult: certificateManager.CMResult) => {
    if (cmResult?.certInfo == undefined) {
      console.info('The result of getting system trusted certificate is undefined.');
    } else {
      let cert: certificateManager.CertInfo = cmResult.certInfo;
      console.info('Succeeded in getting system trusted certificate.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get system trusted certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get system trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```
