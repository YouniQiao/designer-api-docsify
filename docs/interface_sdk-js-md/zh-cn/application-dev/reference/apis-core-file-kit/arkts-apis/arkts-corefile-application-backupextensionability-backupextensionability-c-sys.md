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

## getBackupCompatibilityInfo

```TypeScript
getBackupCompatibilityInfo(extInfo: string) : Promise<string>
```

在应用备份阶段，调用方获取应用自定义兼容性信息时执行，由应用实现返回。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| extInfo | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getBackupInfo

```TypeScript
getBackupInfo(): string
```

在调用方查询应用数据时执行，由应用返回自定义备份信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

## getRestoreCompatibilityInfo

```TypeScript
getRestoreCompatibilityInfo(extInfo: string) : Promise<string>
```

在应用恢复阶段，调用方获取应用自定义兼容性信息时执行，由应用实现返回。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| extInfo | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |
