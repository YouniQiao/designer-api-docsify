# fileSystemServiceRequest（系统接口）

## 导入模块

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## fileSystemServiceRequest

```TypeScript
function fileSystemServiceRequest(config: FileSystemRequestConfig): Promise<number>
```

根据指定配置请求文件系统执行碎片清理。

**起始版本：** 23

**需要权限：** ohos.permission.BACKUP

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [FileSystemRequestConfig](arkts-corefile-backup-filesystemrequestconfig-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
