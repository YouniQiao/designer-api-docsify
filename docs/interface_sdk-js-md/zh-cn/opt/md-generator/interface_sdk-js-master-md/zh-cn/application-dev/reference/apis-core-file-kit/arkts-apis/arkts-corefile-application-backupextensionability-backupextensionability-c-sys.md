# BackupExtensionAbility

备份恢复扩展能力。应用可通过该类实现自定义备份、恢复、进度上报和安全退出逻辑。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare class BackupExtensionAbility--><!--Device-unnamed-declare class BackupExtensionAbility-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

## getBackupCompatibilityInfo

```TypeScript
getBackupCompatibilityInfo(extInfo: string) : Promise<string>
```

在应用备份阶段，调用方获取应用自定义兼容性信息时执行，由应用实现返回。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BackupExtensionAbility-getBackupCompatibilityInfo(extInfo: string) : Promise<string>--><!--Device-BackupExtensionAbility-getBackupCompatibilityInfo(extInfo: string) : Promise<string>-End-->

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BackupExtensionAbility-getBackupInfo(): string--><!--Device-BackupExtensionAbility-getBackupInfo(): string-End-->

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BackupExtensionAbility-getRestoreCompatibilityInfo(extInfo: string) : Promise<string>--><!--Device-BackupExtensionAbility-getRestoreCompatibilityInfo(extInfo: string) : Promise<string>-End-->

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
