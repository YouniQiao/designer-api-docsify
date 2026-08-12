# dataMigration (System API)

## Modules to Import

```TypeScript
import { fontManager } from '@kit.LocalizationKit';
```

## dataMigration

```TypeScript
function dataMigration(callback: DataMigrationCallback): number
```

Data migration API used during device upgrades to start a migration task, providing real-time feedback on migration progress and results through a callback function.

**Since:** 23

**Required permissions:** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function dataMigration(callback: DataMigrationCallback): int--><!--Device-fontManager-function dataMigration(callback: DataMigrationCallback): int-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [DataMigrationCallback](arkts-localization-fontmanager-datamigrationcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [31100110](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-localization-kit/errorcode-font-manager.md#31100110-failed-to-call-the-api-due-to-system-errors) |
| [31100111](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-localization-kit/errorcode-font-manager.md#31100111-migration-task-being-executed) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
