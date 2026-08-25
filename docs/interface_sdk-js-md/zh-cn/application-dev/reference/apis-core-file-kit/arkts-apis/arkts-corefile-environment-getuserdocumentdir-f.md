# getUserDocumentDir

## 导入模块

```TypeScript
import { Environment } from 'kits/@kit.CoreFileKit';
```

## getUserDocumentDir

```TypeScript
function getUserDocumentDir(): string
```

获取当前用户预授权文档目录的沙箱路径。

**起始版本：** 11

**需要权限：** 
- API版本11：ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900042 |
