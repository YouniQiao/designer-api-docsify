# BackupExtensionAbility

备份恢复扩展能力。应用可通过该类实现自定义备份、恢复、进度上报和安全退出逻辑。

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

## 导入模块

```TypeScript
import { BackupExtensionAbility, BundleVersion } from 'kits/@kit.CoreFileKit';
import { BackupExtensionAbility } from 'kits/@kit.CoreFileKit';
import { BundleVersion } from 'kits/@kit.CoreFileKit';
```

## onBackup

```TypeScript
onBackup(): void
```

Extension生命周期回调，在执行备份数据时回调，由开发者实现自定义备份数据处理。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

## onBackupEx

```TypeScript
onBackupEx(backupInfo: string): string | Promise<string>
```

备份恢复框架在备份时向应用传递扩展参数，由开发者实现自定义备份处理。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| backupInfo | string | 是 |

**返回值：**

| 类型 |
| --- |
| string \| Promise & lt;string & gt; |

## onProcess

```TypeScript
onProcess(): string
```

返回应用执行备份或恢复业务的进度信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**返回值：**

| 类型 |
| --- |
| string |

## onRelease

```TypeScript
onRelease(scenario: number): Promise<void>
```

备份恢复框架安全退出回调，应用可在备份或恢复完成后清理临时文件。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scenario | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## onRestore

```TypeScript
onRestore(bundleVersion: BundleVersion): void
```

Extension生命周期回调，在执行恢复数据时回调，由开发者提供扩展的恢复数据操作。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleVersion | [BundleVersion](arkts-corefile-application-backupextensionability-bundleversion-i.md) | 是 |

## onRestoreEx

```TypeScript
onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string | Promise<string>
```

Extension生命周期回调，在执行恢复数据时回调，由开发者实现自定义恢复数据处理。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleVersion | [BundleVersion](arkts-corefile-application-backupextensionability-bundleversion-i.md) | 是 |
| restoreInfo | string | 是 |

**返回值：**

| 类型 |
| --- |
| string \| Promise & lt;string & gt; |

## context

```TypeScript
context: BackupExtensionContext
```

BackupExtensionAbility的上下文环境，继承自ExtensionContext。

**类型：** [BackupExtensionContext](arkts-corefile-file-backupextensioncontext-backupextensioncontext-c.md)

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup
