# uninstallSystemAppCertificate（系统接口）

## uninstallSystemAppCertificate

```TypeScript
function uninstallSystemAppCertificate(keyUri: string) : Promise<void>
```

卸载系统应用的凭据，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_SYSTEM_APP_CERT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManager-function uninstallSystemAppCertificate(keyUri: string) : Promise<void>--><!--Device-certificateManager-function uninstallSystemAppCertificate(keyUri: string) : Promise<void>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [17500002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500002-证书不存在) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [17500001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-内部错误) |

## 示例

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* 系统应用凭据的唯一标识符 */
try {
  certificateManager.uninstallSystemAppCertificate(keyUri).then(() => {
    console.info('Succeeded in uninstalling system app certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to uninstall system app certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to uninstall system app certificate. Code: ${error.code}, message: ${error.message}`);
}
```
