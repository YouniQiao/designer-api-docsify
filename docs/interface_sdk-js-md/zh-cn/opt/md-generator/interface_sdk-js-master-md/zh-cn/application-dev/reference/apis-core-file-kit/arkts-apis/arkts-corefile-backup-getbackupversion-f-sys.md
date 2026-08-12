# getBackupVersion（系统接口）

## getBackupVersion

```TypeScript
function getBackupVersion(): string
```

获取备份版本信息。

**起始版本：** 18

**需要权限：** ohos.permission.BACKUP

<!--Device-backup-function getBackupVersion(): string--><!--Device-backup-function getBackupVersion(): string-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backup } from '@kit.CoreFileKit';

function getBackupVersion() {
  try {
    let result = backup.getBackupVersion();
    console.info('getBackupVersion success, result: ' + result);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getBackupVersion failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

内容示例：

```TypeScript
{ "backupVersion" : "16.0" }
```
