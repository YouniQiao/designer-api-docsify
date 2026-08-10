# BackupExtensionContext

BackupExtensionAbility的上下文环境，继承自ExtensionContext。用于在备份恢复过程中获取EL1（设备级加密区）或EL2（用户级加密区）对应的临时目录。

**Inheritance/Implementation:** BackupExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class BackupExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class BackupExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## Modules to Import

```TypeScript
import { BackupExtensionContext } from 'kits/@kit.CoreFileKit';
```

## backupDir

```TypeScript
readonly backupDir: string
```

获取备份恢复时的临时路径。该路径仅允许在备份恢复过程中临时使用，目前仅支持EL1、EL2路径。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionContext-readonly backupDir: string--><!--Device-BackupExtensionContext-readonly backupDir: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

