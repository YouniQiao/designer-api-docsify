# uninstallUserTrustedCertificateSync

## uninstallUserTrustedCertificateSync

```TypeScript
function uninstallUserTrustedCertificateSync(certUri: string): void
```

卸载用户CA证书。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT

<!--Device-certificateManager-function uninstallUserTrustedCertificateSync(certUri: string): void--><!--Device-certificateManager-function uninstallUserTrustedCertificateSync(certUri: string): void-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| certUri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [17500002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500002-证书不存在) |
| [17500001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-内部错误) |

## 示例

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';

let certUri: string = "test"; /* 业务删除证书，需要使用证书的标识符，此处省略 */
try {
  certificateManager.uninstallUserTrustedCertificateSync(certUri);
} catch (error) {
  console.error(`Failed to uninstall user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```
