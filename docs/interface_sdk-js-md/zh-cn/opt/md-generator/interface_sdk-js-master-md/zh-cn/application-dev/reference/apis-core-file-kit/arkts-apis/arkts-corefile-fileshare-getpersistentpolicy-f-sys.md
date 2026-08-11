# getPersistentPolicy（系统接口）

## getPersistentPolicy

```TypeScript
function getPersistentPolicy(tokenID: number): Promise<Array<PolicyInfo>>
```

获取应用程序的持久化授权策略，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_FILE_ACCESS_PERSIST

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileShare-function getPersistentPolicy(tokenID: int): Promise<Array<PolicyInfo>>--><!--Device-fileShare-function getPersistentPolicy(tokenID: int): Promise<Array<PolicyInfo>>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;PolicyInfo&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900011 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function getPersistentPolicyExample() {
  try {
    let tokenID = 537688848; // 系统应用可以通过bundleManager.getApplicationInfo获取，普通应用可以通过bundleManager.getBundleInfoForSelf获取。
    fileShare.getPersistentPolicy(tokenID).then((result: Array<fileShare.PolicyInfo>) => {
      for (let policy of result) {
        console.info(`get persist policy URI: ${policy.uri}, operationMode: ${policy.operationMode}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`get persist policy failed with error, Code: ${err.code}, message: ${err.message}`);
    });
  } catch (error) {
    console.error(`get persist policy failed with error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
