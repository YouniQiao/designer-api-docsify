# DataMigrationCallback (System API)

Callback API type used during data migration, defining the callback methods for the data migration process. You must implement all methods of this API to receive heartbeat notifications, progress updates, and the final result during migration.

**Since:** 23

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fontManager } from 'kits/@kit.LocalizationKit';
```

## onHeartBeat

```TypeScript
onHeartBeat(): void
```

Callback function that is periodically invoked during the execution of the data migration task to notify you that the migration task is still running normally. You can use it to update UI prompts or execute other business logic.

**Since:** 23

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## onProgress

```TypeScript
onProgress(progress : DataMigrationProgress): void
```

Callback function that is periodically invoked during the execution of the data migration task to notify you of the current migration progress and estimated remaining time. This callback can be used when progress bars, remaining time, and other information need to be displayed on the UI.

**Since:** 23

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progress | [DataMigrationProgress](arkts-localization-fontmanager-datamigrationprogress-i-sys.md) | Yes |

## onResult

```TypeScript
onResult(result : number): void
```

Callback function that is invoked after the data migration task is completed (whether successful or failed) to notify you of the final migration result. This callback can be used when subsequent operations (such as updating the UI, logging, notifying users, etc.) need to be performed after migration is complete.

**Since:** 23

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | number | Yes |
