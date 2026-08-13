# getUserDocumentDir

## getUserDocumentDir

```TypeScript
function getUserDocumentDir(): string
```

获取当前用户预授权文档目录的沙箱路径。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** 
- API版本11：ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY

<!--Device-Environment-function getUserDocumentDir(): string--><!--Device-Environment-function getUserDocumentDir(): string-End-->

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getUserDocumentDirExample() {
  try {
    let path = Environment.getUserDocumentDir();
    console.info(`Succeeded in getUserDocumentDir, path is ${path}`);
  } catch (err) {
    console.error(`Failed to getUserDocumentDir. Code: ${err.code}, message: ${err.message}`);
  }
}
```
