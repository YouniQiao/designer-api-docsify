# DataMigrationCallback (System API)

Callback API type used during data migration, defining the callback methods for the data migration process. You must implement all methods of this API to receive heartbeat notifications, progress updates, and the final result during migration.

**Since:** 23

<!--Device-fontManager-interface DataMigrationCallback--><!--Device-fontManager-interface DataMigrationCallback-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## onHeartBeat

```TypeScript
onHeartBeat(): void
```

Callback function that is periodically invoked during the execution of the data migration task to notify you that the migration task is still running normally. You can use it to update UI prompts or execute other business logic.

**Since:** 23

<!--Device-DataMigrationCallback-onHeartBeat(): void--><!--Device-DataMigrationCallback-onHeartBeat(): void-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Examples**

```TypeScript
import { fontManager } from '@kit.LocalizationKit';

async function dataMigration() {
  const callback: fontManager.DataMigrationCallback = {
    onHeartBeat: () => {
      console.info('onHeartBeat callback');
    },
    onProgress: (progress : fontManager.DataMigrationProgress) => {
      console.info('onProgress callback');
    },
    onResult: (result : number) => {
      console.info('onResult callback');
    }
  }
  try {
    let res = await fontManager.dataMigration(callback);
    console.info('dataMigration suc. res is ' + res);
  } catch (error) {
    console.error('dataMigration err.' + error.code);
  }
}
```

## onProgress

```TypeScript
onProgress(progress : DataMigrationProgress): void
```

Callback function that is periodically invoked during the execution of the data migration task to notify you of the current migration progress and estimated remaining time. This callback can be used when progress bars, remaining time, and other information need to be displayed on the UI.

**Since:** 23

<!--Device-DataMigrationCallback-onProgress(progress : DataMigrationProgress): void--><!--Device-DataMigrationCallback-onProgress(progress : DataMigrationProgress): void-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progress | [DataMigrationProgress](arkts-localization-fontmanager-datamigrationprogress-i-sys.md) | Yes |

**Examples**

```TypeScript
import { fontManager } from '@kit.LocalizationKit';

async function dataMigration() {
  const callback: fontManager.DataMigrationCallback = {
    onHeartBeat: () => {
      console.info('onHeartBeat callback');
    },
    onProgress: (progress : fontManager.DataMigrationProgress) => {
      console.info('onProgress callback');
    },
    onResult: (result : number) => {
      console.info('onResult callback');
    }
  }
  try {
    let res = await fontManager.dataMigration(callback);
    console.info('dataMigration suc. res is ' + res);
  } catch (error) {
    console.error('dataMigration err.' + error.code);
  }
}
```

## onResult

```TypeScript
onResult(result : number): void
```

Callback function that is invoked after the data migration task is completed (whether successful or failed) to notify you of the final migration result. This callback can be used when subsequent operations (such as updating the UI, logging, notifying users, etc.) need to be performed after migration is complete.

**Since:** 23

<!--Device-DataMigrationCallback-onResult(result : int): void--><!--Device-DataMigrationCallback-onResult(result : int): void-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | number | Yes |

**Examples**

```TypeScript
import { fontManager } from '@kit.LocalizationKit';

async function dataMigration() {
  const callback: fontManager.DataMigrationCallback = {
    onHeartBeat: () => {
      console.info('onHeartBeat callback');
    },
    onProgress: (progress : fontManager.DataMigrationProgress) => {
      console.info('onProgress callback');
    },
    onResult: (result : number) => {
      console.info('onResult callback');
    }
  }
  try {
    let res = await fontManager.dataMigration(callback);
    console.info('dataMigration suc. res is ' + res);
  } catch (error) {
    console.error('dataMigration err.' + error.code);
  }
}
```
