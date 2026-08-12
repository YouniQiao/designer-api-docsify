# getUserDownloadDir

## getUserDownloadDir

```TypeScript
function getUserDownloadDir(): string
```

获取当前用户预授权下载目录的沙箱路径。

**起始版本：** 11

**需要权限：** 
- API版本11：ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY

<!--Device-Environment-function getUserDownloadDir(): string--><!--Device-Environment-function getUserDownloadDir(): string-End-->

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getUserDownloadDirExample() {
  try {
    let path = Environment.getUserDownloadDir();
    console.info(`Succeeded in getUserDownloadDir, path is ${path}`);
  } catch (err) {
    console.error(`Failed to getUserDownloadDir. Code: ${err.code}, message: ${err.message}`);
  }
}
```
