# getAllPublicCertificates（系统接口）

## getAllPublicCertificates

```TypeScript
function getAllPublicCertificates() : Promise<CMResult>
```

获取所有用户的公共凭据，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManager-function getAllPublicCertificates() : Promise<CMResult>--><!--Device-certificateManager-function getAllPublicCertificates() : Promise<CMResult>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [17500001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-内部错误) |

## 示例

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.getAllPublicCertificates().then((cmResult: certificateManager.CMResult) => {
    if (cmResult === undefined) { // 用户公共凭据个数为0时，返回cmResult为undefined。
      console.info('The count of public certificates is 0.');
    } else if (cmResult.credentialDetailList == undefined) {
      console.info('The result of getting all public certificates is undefined.');
    } else {
      let list: Array<certificateManager.Credential> = cmResult.credentialDetailList;
      console.info('Succeeded in getting all public certificates.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get all public certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get all public certificates. Code: ${error.code}, message: ${error.message}`);
}
```
