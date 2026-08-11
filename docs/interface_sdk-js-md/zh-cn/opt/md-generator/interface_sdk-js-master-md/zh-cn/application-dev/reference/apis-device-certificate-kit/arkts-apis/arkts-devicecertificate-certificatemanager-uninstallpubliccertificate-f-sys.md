# uninstallPublicCertificate（系统接口）

## uninstallPublicCertificate

```TypeScript
function uninstallPublicCertificate(keyUri: string) : Promise<void>
```

卸载用的户公共凭据，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManager-function uninstallPublicCertificate(keyUri: string) : Promise<void>--><!--Device-certificateManager-function uninstallPublicCertificate(keyUri: string) : Promise<void>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyUri | string | 是 |

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

let keyUri: string = 'test'; /* 用户公共凭据的唯一标识符 */
try {
  certificateManager.uninstallPublicCertificate(keyUri).then(() => {
    console.info('Succeeded in uninstalling public certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to uninstall public certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to uninstall public certificate. Code: ${error.code}, message: ${error.message}`);
}
```
