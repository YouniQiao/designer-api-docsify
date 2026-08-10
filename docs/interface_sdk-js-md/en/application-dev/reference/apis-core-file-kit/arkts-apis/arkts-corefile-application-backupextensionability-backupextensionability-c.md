# BackupExtensionAbility

备份恢复扩展能力。应用可通过该类实现自定义备份、恢复、进度上报和安全退出逻辑。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class BackupExtensionAbility--><!--Device-unnamed-declare class BackupExtensionAbility-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## Modules to Import

```TypeScript
import { BundleVersion } from 'kits/@kit.CoreFileKit';
```

## onBackup

```TypeScript
onBackup(): void
```

Extension生命周期回调，在执行备份数据时回调，由开发者实现自定义备份数据处理。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-onBackup(): void--><!--Device-BackupExtensionAbility-onBackup(): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## Examples

```TypeScript
class BackupExt extends BackupExtensionAbility {
  async onBackup() {
    console.info('onBackup');
  }
}
```

## onBackupEx

```TypeScript
onBackupEx(backupInfo: string): string | Promise<string>
```

备份恢复框架在备份时向应用传递扩展参数，由开发者实现自定义备份处理。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-onBackupEx(backupInfo: string): string | Promise<string>--><!--Device-BackupExtensionAbility-onBackupEx(backupInfo: string): string | Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| backupInfo | string | Yes | 备份时框架传递给应用的扩展信息，参数为JSON格式字符串。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 应用执行自定义备份操作的信息，返回值为JSON格式字符串， 包含type、errorCode和errorInfo字段，支持同步返回或使用Promise异步返回。 |

## Examples

```TypeScript
import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

interface ErrorInfo {
  type: string,
  errorCode: number,
  errorInfo: string
}
class BackupExt extends BackupExtensionAbility {
  onBackupEx(backupInfo: string): string {
    try {
      if (backupInfo == "") {
        // If backupInfo is empty, the application processes the data based on the service.
        console.info("backupInfo is empty");
      }
      console.info(`onBackupEx ok`);
      let errorInfo: ErrorInfo = {
        type: "ErrorInfo",
        errorCode: 0,
        errorInfo: "app customized error info"
      }
      return JSON.stringify(errorInfo);
    } catch (err) {
      console.error(`BackupExt error. Code:${err.code}, message:${err.message}`);
    }
    return "";
  }
}
```

```TypeScript
import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

interface ErrorInfo {
  type: string,
  errorCode: number,
  errorInfo: string
}
class BackupExt extends BackupExtensionAbility {
  // Asynchronous implementation
  async onBackupEx(backupInfo: string): Promise<string> {
    try {
      if (backupInfo == "") {
        // If backupInfo is empty, the application processes the data based on the service.
        console.info("backupInfo is empty");
      }
      console.info(`onBackupEx ok`);
      let errorInfo: ErrorInfo = {
        type: "ErrorInfo",
        errorCode: 0,
        errorInfo: "app customized error info"
      }
      return JSON.stringify(errorInfo);
    } catch (err) {
      console.error(`BackupExt error. Code:${err.code}, message:${err.message}`);
    }
    return "";
  }
}
```

## onProcess

```TypeScript
onProcess(): string
```

返回应用执行备份或恢复业务的进度信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-onProcess(): string--><!--Device-BackupExtensionAbility-onProcess(): string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Return value:**

| Type | Description |
| --- | --- |
| string | 应用处理数据的进度信息，返回值为JSON格式字符串。 |

## Examples

```TypeScript
import { BackupExtensionAbility } from '@kit.CoreFileKit';
import { taskpool } from '@kit.ArkTS';

@Sendable
class MigrateProgressInfo {
  private migrateProgress: string = '';
  private name: string = "test"; // appName
  private processed: number = 0; // Processed data
  private total: number = 100; // Total number
  private isPercentage: boolean = true // (Optional) The value true means to display the progress in percentage; the value false or an unimplemented field means to display the progress by the number of items.

  getMigrateProgress(): string {
    this.migrateProgress = `{"progressInfo": [{"name": ${this.name}, "processed": ${this.processed}, "total": ${
      this.total}, "isPercentage": ${this.isPercentage}}]}`;
    return this.migrateProgress;
  }

  updateProcessed(processed: number) {
    this.processed = processed;
  }
}

class BackupExt extends BackupExtensionAbility {
  private progressInfo: MigrateProgressInfo = new MigrateProgressInfo();

  // In the following code, the appJob method is the simulated service code, and args specifies the parameters of appJob(). This method is used to start a worker thread in the task pool.
  async onBackup() {
    console.info(`onBackup begin`);
    let args = 100; // args is a parameter of appJob().
    let jobTask: taskpool.Task = new taskpool.LongTask(appJob, this.progressInfo, args);
    try {
      await taskpool.execute(jobTask, taskpool.Priority.LOW);
    } catch (error) {
      console.error("onBackup error." + error.message);
    }
    taskpool.terminateTask(jobTask); // Manually destroy the task.
    console.info(`onBackup end`);
  }

  async onRestore() {
    console.info(`onRestore begin`);
    let args = 100; // args is a parameter of appJob().
    let jobTask: taskpool.Task = new taskpool.LongTask(appJob, this.progressInfo, args);
    try {
      await taskpool.execute(jobTask, taskpool.Priority.LOW);
    } catch (error) {
      console.error("onRestore error." + error.message);
    }
    taskpool.terminateTask(jobTask); // Manually destroy the task.
    console.info(`onRestore end`);
  }


  onProcess(): string {
    console.info(`onProcess begin`);
    return this.progressInfo.getMigrateProgress();
  }
}

@Concurrent
function appJob(progressInfo: MigrateProgressInfo, args: number) : string {
  console.info(`appJob begin, args is: ` + args);
  // Update the processing progress during service execution.
  let currentProcessed: number = 0;
  // Simulate the actual service logic.
  for (let i = 0; i < args; i++) {
    currentProcessed = i;
    progressInfo.updateProcessed(currentProcessed);
  }
  return "ok";
}
```

## onRelease

ArkTS-Dyn:
```TypeScript
onRelease(scenario: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
onRelease(scenario: int): Promise<void>
```

备份恢复框架安全退出回调，应用可在备份或恢复完成后清理临时文件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-onRelease(scenario: int): Promise<void>--><!--Device-BackupExtensionAbility-onRelease(scenario: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scenario | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 当前操作场景，值为1表示备份，值为2表示恢复。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

## Examples

```TypeScript
// The following describes an example of removing files.
import { BackupExtensionAbility, fileIo } from '@kit.CoreFileKit';

const SCENARIO_BACKUP: number = 1;
const SCENARIO_RESTORE: number = 2;
// Temporary directory to be removed.
let filePath: string = '/data/storage/el2/base/.temp/';

class BackupExt extends BackupExtensionAbility {
  async onRelease(scenario: number): Promise<void> {
    try {
      if (scenario == SCENARIO_BACKUP) {
        // In the backup scenario, the application implements the processing. The following describes how to remove temporary files generated during backup.
        console.info(`onRelease begin`);
        await fileIo.rmdir(filePath);
        console.info(`onRelease end, rmdir succeed`);
      }
      if (scenario == SCENARIO_RESTORE) {
        // In the restore scenario, the application implements the processing. The following describes how to remove temporary files generated during restoration.
        console.info(`onRelease begin`);
        await fileIo.rmdir(filePath);
        console.info(`onRelease end, rmdir succeed`);
      }
    } catch (error) {
      console.error(`onRelease failed with error. Code: ${error.code}, message: ${error.message}`);
    }
  }
}
```

## onRestore

```TypeScript
onRestore(bundleVersion: BundleVersion): void
```

Extension生命周期回调，在执行恢复数据时回调，由开发者提供扩展的恢复数据操作。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-onRestore(bundleVersion: BundleVersion): void--><!--Device-BackupExtensionAbility-onRestore(bundleVersion: BundleVersion): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleVersion | [BundleVersion](arkts-corefile-application-backupextensionability-bundleversion-i.md) | Yes | 恢复时应用数据所在的版本信息。 |

## Examples

```TypeScript
import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

class BackupExt extends BackupExtensionAbility {
  async onRestore(bundleVersion : BundleVersion) {
    console.info(`onRestore ok ${JSON.stringify(bundleVersion)}`);
  }
}
```

## onRestoreEx

```TypeScript
onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string | Promise<string>
```

Extension生命周期回调，在执行恢复数据时回调，由开发者实现自定义恢复数据处理。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string | Promise<string>--><!--Device-BackupExtensionAbility-onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string | Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleVersion | [BundleVersion](arkts-corefile-application-backupextensionability-bundleversion-i.md) | Yes | 恢复时应用数据所在的版本信息。 |
| restoreInfo | string | Yes | 恢复时框架传递给应用的扩展信息，参数为JSON格式字符串。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 应用执行自定义恢复操作的信息，返回值为JSON格式字符串， 包含type、errorCode和errorInfo字段，支持同步返回或使用Promise异步返回。 |

## Examples

```TypeScript
import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
interface ErrorInfo {
  type: string,
  errorCode: number,
  errorInfo: string
}
class BackupExt extends BackupExtensionAbility {
  // Asynchronous implementation
  async onRestoreEx(bundleVersion : BundleVersion, restoreInfo: string): Promise<string> {
    try {
      if (restoreInfo == "") {
        // If restoreInfo is empty, the application processes the data based on the service.
        console.info("restoreInfo is empty");
      }
      console.info(`onRestoreEx ok ${JSON.stringify(bundleVersion)}`);
      let errorInfo: ErrorInfo = {
        type: "ErrorInfo",
        errorCode: 0,
        errorInfo: "app customized error info"
      }
      return JSON.stringify(errorInfo);
    } catch (err) {
      console.error(`onRestoreEx error. Code:${err.code}, message:${err.message}`);
    }
    return "";
  }
}
```

```TypeScript
import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
interface ErrorInfo {
  type: string,
  errorCode: number,
  errorInfo: string
}

class BackupExt extends BackupExtensionAbility {
  // Synchronous implementation
  onRestoreEx(bundleVersion : BundleVersion, restoreInfo: string): string {
    try {
      if (restoreInfo == "") {
        // If restoreInfo is empty, the application processes the data based on the service.
        console.info("restoreInfo is empty");
      }
      console.info(`onRestoreEx ok ${JSON.stringify(bundleVersion)}`);
      let errorInfo: ErrorInfo = {
        type: "ErrorInfo",
        errorCode: 0,
        errorInfo: "app customized error info"
      }
      return JSON.stringify(errorInfo);
    } catch (err) {
      console.error(`onRestoreEx error. Code:${err.code}, message:${err.message}`);
    }
    return "";
  }
}
```

## context

```TypeScript
context: BackupExtensionContext
```

BackupExtensionAbility的上下文环境，继承自ExtensionContext。

**Type:** [BackupExtensionContext](arkts-corefile-file-backupextensioncontext-backupextensioncontext-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-context: BackupExtensionContext--><!--Device-BackupExtensionAbility-context: BackupExtensionContext-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

