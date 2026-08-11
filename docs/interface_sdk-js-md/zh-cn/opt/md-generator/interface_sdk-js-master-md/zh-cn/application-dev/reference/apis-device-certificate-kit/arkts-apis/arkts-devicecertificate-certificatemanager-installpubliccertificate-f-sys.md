# installPublicCertificate（系统接口）

## installPublicCertificate

```TypeScript
function installPublicCertificate(keystore: Uint8Array, keystorePwd: string) : Promise<CMResult>
```

安装用户的公共凭据，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManager-function installPublicCertificate(keystore: Uint8Array, keystorePwd: string) : Promise<CMResult>--><!--Device-certificateManager-function installPublicCertificate(keystore: Uint8Array, keystorePwd: string) : Promise<CMResult>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keystore | Uint8Array | 是 |
| keystorePwd | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;CMResult&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17500008](../errorcode-certManager.md#17500008-密码错误) |
| [17500003](../errorcode-certManager.md#17500003-证书或凭据无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500004](../errorcode-certManager.md#17500004-证书或凭据数量达到上限) |

## 示例

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据。 */
let keystore: Uint8Array = new Uint8Array([
    0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let keystorePwd: string = "123456";
try {
  certificateManager.installPublicCertificate(keystore, keystorePwd).then((cmResult: certificateManager.CMResult) => {
    let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
    console.info('Succeeded in installing public certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to install public certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to install public certificate. Code: ${error.code}, message: ${error.message}`);
}
```
