# DataMigrationCallback (System API)

Callback API type used during data migration, defining the callback methods for the data migration process. You must implement all methods of this API to receive heartbeat notifications, progress updates, and the final result during migration.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fontManager-interface DataMigrationCallback--><!--Device-fontManager-interface DataMigrationCallback-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fontManager } from '@kit.LocalizationKit';
```

## onHeartBeat

```TypeScript
onHeartBeat(): void
```

Callback function that is periodically invoked during the execution of the data migration task to notify you that the migration task is still running normally. You can use it to update UI prompts or execute other business logic.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DataMigrationCallback-onHeartBeat(): void--><!--Device-DataMigrationCallback-onHeartBeat(): void-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Examples

```TypeScript
import { fontManager } from '@kit.LocalizationKit';

dataMigration() {
  const callback: fontManager.DataMigrationCallback = {
    onHeartBeat: () => {
      console.info('onHeartBeat callback');
    },
    onProgress(progress : fontManager.DataMigrationProgress) => {
      console.info('onProgress callback');
    },
    onResult(result : int) => {
      console.info('onResult callback');
    }
  }
  try {
    let res = await fontManager.dataMigration(callback);
    console.info('dataMigration suc. res is ' + res);
  } catch (error) {
    console.error('dataMigration err.' + error.code);
  }
  return;
}
```

## onProgress

```TypeScript
onProgress(progress : DataMigrationProgress): void
```

Callback function that is periodically invoked during the execution of the data migration task to notify you of the current migration progress and estimated remaining time. This callback can be used when progress bars, remaining time, and other information need to be displayed on the UI.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DataMigrationCallback-onProgress(progress : DataMigrationProgress): void--><!--Device-DataMigrationCallback-onProgress(progress : DataMigrationProgress): void-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | [DataMigrationProgress](arkts-localization-fontmanager-datamigrationprogress-i-sys.md) | Yes | Data migration progress. |

## Examples

```TypeScript
import { fontManager } from '@kit.LocalizationKit';

dataMigration() {
  const callback: fontManager.DataMigrationCallback = {
    onHeartBeat: () => {
      console.info('onHeartBeat callback');
    },
    onProgress(progress : fontManager.DataMigrationProgress) => {
      console.info('onProgress callback');
    },
    onResult(result : int) => {
      console.info('onResult callback');
    }
  }
  try {
    let res = await fontManager.dataMigration(callback);
    console.info('dataMigration suc. res is ' + res);
  } catch (error) {
    console.error('dataMigration err.' + error.code);
  }
  return;
}
```

## onResult

ArkTS-Dyn:
```TypeScript
onResult(result : number): void
```

ArkTS-Sta:
```TypeScript
onResult(result : int): void
```

Callback function that is invoked after the data migration task is completed (whether successful or failed) to notify you of the final migration result. This callback can be used when subsequent operations (such as updating the UI, logging, notifying users, etc.) need to be performed after migration is complete.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DataMigrationCallback-onResult(result : int): void--><!--Device-DataMigrationCallback-onResult(result : int): void-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Data migration result. &lt;br&gt;**0**: Data migration succeeded. &lt;br&gt;**1**: No data migration is required. &lt;br&gt;**2**: Failed to obtain the user ID. &lt;br&gt;**3**: Failed to check the directory. &lt;br&gt;**4**: Failed to initialize the cache directory. &lt;br&gt;**5**: Failed to open the source file. &lt;br&gt;**6**: Failed to copy the file. &lt;br&gt;**7**: Failed to rename the file. &lt;br&gt;**8**: Failed to delete the file. |

## Examples

```TypeScript
import { fontManager } from '@kit.LocalizationKit';

dataMigration() {
  const callback: fontManager.DataMigrationCallback = {
    onHeartBeat: () => {
      console.info('onHeartBeat callback');
    },
    onProgress(progress : fontManager.DataMigrationProgress) => {
      console.info('onProgress callback');
    },
    onResult(result : int) => {
      console.info('onResult callback');
    }
  }
  try {
    let res = await fontManager.dataMigration(callback);
    console.info('dataMigration suc. res is ' + res);
  } catch (error) {
    console.error('dataMigration err.' + error.code);
  }
  return;
}
```

