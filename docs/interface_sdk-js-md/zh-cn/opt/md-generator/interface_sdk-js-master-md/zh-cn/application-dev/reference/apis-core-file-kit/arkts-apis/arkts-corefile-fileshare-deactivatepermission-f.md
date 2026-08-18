# deactivatePermission

## 导入模块

```TypeScript
```

## deactivatePermission

```TypeScript
function deactivatePermission(policies: Array<PolicyInfo>): Promise<void>
```

取消激活多个已持久化授权的文件或目录，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

<!--Device-fileShare-function deactivatePermission(policies: Array<PolicyInfo>): Promise<void>--><!--Device-fileShare-function deactivatePermission(policies: Array<PolicyInfo>): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policies | Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function deactivatePermissionExample() {
  try {
    let uri = 'file://docs/storage/Users/username/tmp.txt';
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      // 可以组合取消激活多个权限，例如读写权限可使用fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.deactivatePermission(policies).then(() => {
      console.info('deactivatePermission successfully');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`deactivatePermission failed with error message: ${err.message}, error code: ${err.code}`);
      if (err.code === 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error(`error code: ${JSON.stringify(err.data[i].code)}`);
          console.error(`error URI: ${JSON.stringify(err.data[i].uri)}`);
          console.error(`error reason: ${JSON.stringify(err.data[i].message)}`);
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`deactivatePermission failed with err: ${JSON.stringify(err)}`);
  }
}
```
