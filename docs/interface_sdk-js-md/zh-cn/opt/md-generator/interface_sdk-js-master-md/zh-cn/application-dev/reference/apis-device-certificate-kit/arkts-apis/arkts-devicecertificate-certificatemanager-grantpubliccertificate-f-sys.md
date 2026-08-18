# grantPublicCertificate（系统接口）

## 导入模块

```TypeScript
```

## grantPublicCertificate

```TypeScript
function grantPublicCertificate(keyUri: string, clientAppUid: number) : Promise<CMResult>
```

授予应用使用用户公共凭据的权限，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManager-function grantPublicCertificate(keyUri: string, clientAppUid: int) : Promise<CMResult>--><!--Device-certificateManager-function grantPublicCertificate(keyUri: string, clientAppUid: int) : Promise<CMResult>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyUri | string | 是 |
| clientAppUid | number | 是 |

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

**示例**

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* 用户公共凭据的唯一标识符 */
let clientAppUid: number = 1001; /* 应用UID */
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
