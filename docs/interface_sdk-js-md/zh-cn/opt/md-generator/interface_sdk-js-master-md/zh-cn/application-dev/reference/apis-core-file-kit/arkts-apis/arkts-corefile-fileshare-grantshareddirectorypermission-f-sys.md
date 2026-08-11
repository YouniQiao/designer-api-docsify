# grantSharedDirectoryPermission（系统接口）

## grantSharedDirectoryPermission

```TypeScript
function grantSharedDirectoryPermission(): Promise<void>
```

授予应用捐献目录的临时访问权限。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_SHARED_FILE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileShare-function grantSharedDirectoryPermission(): Promise<void>--><!--Device-fileShare-function grantSharedDirectoryPermission(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function grantSharedDirectoryPermission() {
  try {
    fileShare.grantSharedDirectoryPermission().then(() => {
      console.info('grantSharedDirectoryPermission success');
    }).catch((err: BusinessError) => {
      console.error(`grantSharedDirectoryPermission err: ${JSON.stringify(err)}`);
    });
  } catch (error) {
    console.error(`grantSharedDirectoryPermission error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
