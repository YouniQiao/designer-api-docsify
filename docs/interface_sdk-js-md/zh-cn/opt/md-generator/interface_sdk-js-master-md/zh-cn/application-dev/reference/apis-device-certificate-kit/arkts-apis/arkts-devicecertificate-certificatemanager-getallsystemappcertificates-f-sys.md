# getAllSystemAppCertificates（系统接口）

## getAllSystemAppCertificates

```TypeScript
function getAllSystemAppCertificates(): Promise<CMResult>
```

表示获取所有系统凭据列表。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function getAllSystemAppCertificates(): Promise<CMResult>--><!--Device-certificateManager-function getAllSystemAppCertificates(): Promise<CMResult>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;CMResult&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |

## 示例

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.getAllSystemAppCertificates().then((cmResult) => {
    if (cmResult === undefined) { // 系统凭据个数为0时，返回cmResult为undefined。
      console.info('The count of the system certificates is 0.');
    } else if (cmResult.credentialList == undefined) {
      console.info('The result of getting all system app certificates is undefined.');
    } else {
      let list = cmResult.credentialList;
      console.info('Succeeded in getting all system app certificates.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get all system app certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get all system app certificates. Code: ${error.code}, message: ${error.message}`);
}
```
