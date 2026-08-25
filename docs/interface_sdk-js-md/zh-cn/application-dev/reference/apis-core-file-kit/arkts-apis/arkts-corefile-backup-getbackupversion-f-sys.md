# getBackupVersion（系统接口）

## 导入模块

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## getBackupVersion

```TypeScript
function getBackupVersion(): string
```

获取备份版本信息。

**起始版本：** 18

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
