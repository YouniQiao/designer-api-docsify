# dataMigration (System API)

## Modules to Import

```TypeScript
import { fontManager } from 'kits/@kit.LocalizationKit';
```

## dataMigration

```TypeScript
function dataMigration(callback: DataMigrationCallback): int
```

设备升级时使用的数据迁移接口，用于启动迁移任务，通过回调函数实时反馈迁移进度和结果。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function dataMigration(callback: DataMigrationCallback): int--><!--Device-fontManager-function dataMigration(callback: DataMigrationCallback): int-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DataMigrationCallback](arkts-localization-fontmanager-datamigrationcallback-i-sys.md) | Yes | 数据迁移的回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 迁移任务启动结果。 &lt;br&gt;- 0：迁移任务启动成功，迁移任务将在后台执行并通过回调通知进度和结果。 &lt;br&gt;- 其他值：迁移任务启动失败，请根据错误码排查原因。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 31100110 | Call failed due to system error. |
| 31100111 | Data migration is in progress. |
| 201 | Permission denied. |
| 202 | Non-system application. |

