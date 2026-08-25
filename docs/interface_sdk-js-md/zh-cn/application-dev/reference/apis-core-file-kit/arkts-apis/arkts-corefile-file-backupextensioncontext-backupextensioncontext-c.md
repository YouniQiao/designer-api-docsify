# BackupExtensionContext

BackupExtensionAbility的上下文环境，继承自ExtensionContext。 用于在备份恢复过程中获取EL1（设备级加密区）或EL2（用户级加密区）对应的临时目录。@extends ExtensionContext

**继承/实现关系：** BackupExtensionContext extends ExtensionContext

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

## 导入模块

```TypeScript
import { BackupExtensionContext } from '@kit.CoreFileKit';
```

## backupDir

```TypeScript
readonly backupDir: string
```

获取备份恢复时的临时路径。该路径仅允许在备份恢复过程中临时使用，目前仅支持EL1、EL2路径。

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup
