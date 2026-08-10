# IncrementalBackupSession (System API)

增量备份流程对象，用于支撑应用增量备份流程。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-backup-class IncrementalBackupSession--><!--Device-backup-class IncrementalBackupSession-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## appendBundles

```TypeScript
appendBundles(bundlesToBackup: Array<IncrementalBackupData>): Promise<void>
```

添加需要增量备份的应用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-appendBundles(bundlesToBackup: Array<IncrementalBackupData>): Promise<void>--><!--Device-IncrementalBackupSession-appendBundles(bundlesToBackup: Array<IncrementalBackupData>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundlesToBackup | Array&lt;IncrementalBackupData&gt; | Yes | 需要增量备份的应用数据列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13900025 | No space left on device |
| 13600001 | IPC error |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## Examples

```TypeScript
import { fileIo, backup} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let generalCallbacks: backup.GeneralCallbacks = {
  onFileReady: (err: BusinessError, file: backup.File) => {
    if (err) {
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onFileReady success');
    fileIo.closeSync(file.fd);
  },
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleBegin success');
  },
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleEnd success');
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onAllBundlesEnd success');
  },
  onBackupServiceDied: () => {
    console.info('service died');
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  }
};
let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.
let incrementalBackupData: backup.IncrementalBackupData = {
  bundleName: "com.example.hiworld",
  lastIncrementalTime: 1700107870, // Timestamp of the last backup.
  manifestFd:1 // FD of the manifest file of the last backed.
}
let incrementalBackupDataArray: backup.IncrementalBackupData[] = [incrementalBackupData];
incrementalBackupSession.appendBundles(incrementalBackupDataArray).then(() => {
  console.info('appendBundles success');
}).catch((err: BusinessError) => {
  console.error(`appendBundles failed. Code: ${err.code}, message: ${err.message}`);
}); // Appends the applications that require incremental backup.
```

## appendBundles

```TypeScript
appendBundles(bundlesToAppend: Array<IncrementalBackupData>, infos: string[]): Promise<void>
```

添加需要增量备份的应用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-appendBundles(bundlesToAppend: Array<IncrementalBackupData>, infos: string[]): Promise<void>--><!--Device-IncrementalBackupSession-appendBundles(bundlesToAppend: Array<IncrementalBackupData>, infos: string[]): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundlesToAppend | Array&lt;IncrementalBackupData&gt; | Yes | 需要增量备份的应用数据列表。 |
| infos | string[] | Yes | 增量备份时各应用所需扩展信息的数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3. Parameter verification failed. |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 201 | Permission verification failed. This error code is usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 13900025 | No space left on device |
| 13600001 | IPC error |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## Examples

```TypeScript
import { fileIo, backup} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let generalCallbacks: backup.GeneralCallbacks = {
  onFileReady: (err: BusinessError, file: backup.File) => {
    if (err) {
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onFileReady success');
    fileIo.closeSync(file.fd);
  },
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleBegin success');
  },
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleEnd success');
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onAllBundlesEnd success');
  },
  onBackupServiceDied: () => {
    console.info('service died');
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  }
};
let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.
let incrementalBackupData: backup.IncrementalBackupData = {
  bundleName: "com.example.hiworld",
  lastIncrementalTime: 1700107870, // Timestamp of the last backup.
  manifestFd:1 // FD of the manifest file of the last backed.
}
    let infos: Array<string> = [
      `
      {
      "infos": [
          {
              "details": [
                  {
                      "detail": [
                          {
                              "key1": "value1",
                              "key2": "value2"
                          }
                      ]
                  }
              ],
              "type": "unicast",
              "bundleName": "com.example.hiworld"
          }
      ]
  },
  {
      "infos": [
          {
              "details": [
                  {
                      "detail": [
                          {
                              "key1": "value1",
                              "key2": "value2"
                          }
                      ]
                  }
              ],
              "type": "unicast",
              "bundleName": "com.example.myApp"
          }
      ]
  }
    `
  ]
let incrementalBackupDataArray: backup.IncrementalBackupData[] = [incrementalBackupData];
// Appends the applications that require incremental backup.
incrementalBackupSession.appendBundles(incrementalBackupDataArray, infos).then(() => {
  console.info('appendBundles success');
}).catch((err: BusinessError) => {
  console.error(`appendBundles failed. Code: ${err.code}, message: ${err.message}`);
});
```

## cancel

ArkTS-Dyn:
```TypeScript
cancel(bundleName: string): number
```

ArkTS-Sta:
```TypeScript
cancel(bundleName: string): int
```

取消指定应用的增量备份任务。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-cancel(bundleName: string): int--><!--Device-IncrementalBackupSession-cancel(bundleName: string): int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 需要取消任务的应用名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 取消结果，0表示成功，13500011表示失败，13500012表示没有对应任务。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { fileIo, backup} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let generalCallbacks: backup.GeneralCallbacks = {
  onFileReady: (err: BusinessError, file: backup.File) => {
    if (err) {
      // If the FD fails to be passed, call the cancel API to cancel the incremental backup task of the application.
      let result = incrementalBackupSession.cancel(err.name);
      console.info('cancel result:' + result);
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onFileReady success');
    fileIo.closeSync(file.fd);
  },
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleBegin success');
  },
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleEnd success');
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onAllBundlesEnd success');
  },
  onBackupServiceDied: () => {
    console.info('service died');
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  }
};
let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.
let backupBundles: Array<backup.IncrementalBackupData> = [];
let bundleData: backup.IncrementalBackupData = {
  bundleName: "com.example.helloWorld",
  lastIncrementalTime: 1700107870, // Timestamp of the last backup.
  manifestFd: 1 // FD of the manifest file of the last backed.
}
backupBundles.push(bundleData);
incrementalBackupSession.appendBundles(backupBundles);
```

## cleanBundleTempDir

```TypeScript
cleanBundleTempDir(bundleName: string): Promise<boolean>
```

清理指定应用的临时目录。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-cleanBundleTempDir(bundleName: string): Promise<boolean>--><!--Device-IncrementalBackupSession-cleanBundleTempDir(bundleName: string): Promise<boolean>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 需要清理临时目录的应用名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | 清理结果，true表示成功，false表示失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { fileIo, backup} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function cleanBundleTempDir(bundleName: string) {
  try {
    let res = await incrementalBackupSession.cleanBundleTempDir(bundleName);
    if (res) {
      console.info(`cleanBundleTempDir succeeded.`);
    } else {
      console.info(`cleanBundleTempDir fail.`);
    }
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`cleanBundleTempDir failed. Code: ${err.code}, message: ${err.message}`);
  }
}

let generalCallbacks: backup.GeneralCallbacks = { // Define general callbacks to be used in the backup or restore process.
  // Callback when the file is sent successfully.
  onFileReady: (err: BusinessError, file: backup.File) => {
    if (err) {
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`onFileReady succeeded.`);
    fileIo.closeSync(file.fd);
  },
  // Callback when the application backup or restore starts.
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`onBundleBegin succeeded.`);
  },
  // Callback when the application backup or restore is complete. cleanBundleTempDir is called for cleanup.
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    cleanBundleTempDir(bundleName);
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`onAllBundlesEnd success`);
  },
  onBackupServiceDied: () => {
    console.info(`service died`);
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  }
};
let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.
```

## constructor

```TypeScript
constructor(callbacks: GeneralCallbacks)
```

构造IncrementalBackupSession实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-constructor(callbacks: GeneralCallbacks)--><!--Device-IncrementalBackupSession-constructor(callbacks: GeneralCallbacks)-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbacks | [GeneralCallbacks](arkts-corefile-backup-generalcallbacks-i-sys.md) | Yes | 备份流程所需的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { fileIo, backup} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let generalCallbacks: backup.GeneralCallbacks = {
  onFileReady: (err: BusinessError, file: backup.File) => {
    if (err) {
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onFileReady success');
    fileIo.closeSync(file.fd);
  },
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleBegin success');
  },
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleEnd success');
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onAllBundlesEnd success');
  },
  onBackupServiceDied: () => {
    console.info('service died');
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  }
};
let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.
```

## getBackupDataSize

```TypeScript
getBackupDataSize(isPreciseScan: boolean, dataList: Array<IncrementalBackupTime>): Promise<void>
```

获取应用待备份数据量。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-getBackupDataSize(isPreciseScan: boolean, dataList: Array<IncrementalBackupTime>): Promise<void>--><!--Device-IncrementalBackupSession-getBackupDataSize(isPreciseScan: boolean, dataList: Array<IncrementalBackupTime>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isPreciseScan | boolean | Yes | 是否精确扫描，true表示精确扫描，false表示非精确扫描。 |
| dataList | Array&lt;IncrementalBackupTime&gt; | Yes | 备份应用列表及其最后一次增量备份时间。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 13900001 | Operation not permitted |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13600001 | IPC error |
| 13900042 | Internal error |

## Examples

```TypeScript
import { fileIo, backup} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface scannedInfos { // Parse the scanning result.
  scanned: [];
  scanning: string;
}

interface ScannedInfo { // Parse the scanning result of an application.
  bundleName: string;
  dataSize: number;
  incDataSize: number;
}

let generalCallbacks: backup.GeneralCallbacks = {
  onFileReady: (err: BusinessError, file: backup.File) => { // Define the universal callbacks to be used in the backup or restore process.
    if (err) {
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onFileReady success');
    fileIo.closeSync(file.fd);
  },
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleBegin success');
  },
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleEnd success');
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onAllBundlesEnd success');
  },
  onBackupServiceDied: () => {
    console.info('service died');
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  },
  onBackupSizeReport: (OnBackupSizeReport) => { // The callback function is used together with getBackupDataSize to return the obtained application data size and the bundle name of the application whose data size is being retrieved. onBackupSizeReport in generalCallbacks returns the scan result every 5 seconds, or immediately if the data retrieval process is completed within 5 seconds, until all application data in dataList is returned.
    console.info('dataSizeCallback success');
    const jsonObj: scannedInfos | null = JSON.parse(OnBackupSizeReport); // Parse and print the returned information.
    if (jsonObj) {
      const infos: ScannedInfo [] = jsonObj.scanned;
      for (let i = 0; i < infos.length; i++) {
        console.info('name: ' + infos[i].bundleName);
        console.info('dataSize: ' + infos[i].dataSize);
        console.info('incDataSize: ' + infos[i].incDataSize);
      }
      const scanning: string = jsonObj.scanning;
      console.info('scanning: ' + scanning);
    }
  }
};

let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.

let backupApps: backup.IncrementalBackupTime[] = [{
  bundleName: "com.example.hiworld",
  lastIncrementalTime: 1700107870 // Time of the last incremental backup.
}];
try {
  incrementalBackupSession.getBackupDataSize(true, backupApps); // Obtain the amount of specified application data to be backed up in backupApps. The value true indicates that accurate scanning is used.
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getBackupDataSize failed. Code: ${err.code}, message: ${err.message}`);
}
```

Example of a JSON string returned asynchronously:

```TypeScript
{
 "scanned": [ // Scanned application. The result will not be returned in the next callback.
     {
         "name": "com.example.hiworld", // Application name.
         "dataSize": 1006060, // Data size.
         "incDataSize": 50800 // Incremental data size.
     },
     {
         "name": "com.example.myAPP",
         "dataSize": 5000027,
         "incDataSize": 232344
     }
 ],
 "scanning" :"com.example.smartAPP" // Application that is being scanned. This field is empty when the last result is returned.
}
```

## getCompatibilityInfo

```TypeScript
getCompatibilityInfo(bundleName: string, extInfo: string): Promise<string>
```

获取指定应用的兼容性信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-getCompatibilityInfo(bundleName: string, extInfo: string): Promise<string>--><!--Device-IncrementalBackupSession-getCompatibilityInfo(bundleName: string, extInfo: string): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 需要获取兼容性信息的应用名称。 |
| extInfo | string | Yes | 传递给应用的额外信息，由应用自行处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回应用的兼容性信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
import { fileIo, backup } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let generalCallbacks: backup.GeneralCallbacks = { // Define general callbacks to be used in the backup or restore process.
  onFileReady: (err: BusinessError, file: backup.File) => {
    if (err) {
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`onFileReady succeeded.`);
    fileIo.closeSync(file.fd);
  },
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`onBundleBegin succeeded.`);
  },
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`onBundleEnd succeeded.`);
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`onAllBundlesEnd success`);
  },
  onBackupServiceDied: () => {
    console.info(`service died`);
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  }
};

async function getIncBackupCompatibilityInfo() {
  let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.
  let bundleName = "com.example.helloWorld";
  let extInfo = ""; // An empty string means no extra information needs to be passed to the application.
  try {
    let retInfo = await incrementalBackupSession.getCompatibilityInfo(bundleName, extInfo);
    if (retInfo) {
      console.info(`getCompatibilityInfo success ` + retInfo);
    } else {
      console.info(`bundle ` + bundleName + ' may not support getCompatibilityInfo');
    }
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getCompatibilityInfo failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## getLocalCapabilities

```TypeScript
getLocalCapabilities(): Promise<FileData>
```

获取描述本地能力的JSON文件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-getLocalCapabilities(): Promise<FileData>--><!--Device-IncrementalBackupSession-getLocalCapabilities(): Promise<FileData>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FileData&gt; | Promise对象，返回包含本地能力文件描述符的FileData。返回的文件为临时文件，关闭后将 自动删除。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900001 | Operation not permitted |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13600001 | IPC error |
| 13900042 | Internal error |

## Examples

```TypeScript
import { fileIo, backup} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface test { // Parse the capability file.
  bundleInfos: [];
  deviceType: string;
  systemFullName: string;
}

interface BundleInfo { // Obtain the local capability information of an application.
  name: string;
  appIndex: number;
  versionCode: number;
  versionName: string;
  spaceOccupied: number;
  allToBackup: boolean;
  increSpaceOccupied?: number;
  fullBackupOnly: boolean;
  extensionName: string;
  restoreDeps: string;
  supportScene: string;
  extraInfo: object;
}

let generalCallbacks: backup.GeneralCallbacks = { // Define general callbacks to be used in the backup or restore process.
  onFileReady: (err: BusinessError, file: backup.File) => {
    if (err) {
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onFileReady success');
    fileIo.closeSync(file.fd);
  },
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleBegin success');
  },
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleEnd success');
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onAllBundlesEnd success');
  },
  onBackupServiceDied: () => {
    console.info('service died');
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  }
};
async function getLocalCapabilitiesTest() {
  let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.
  let basePath = '/data/storage/el2/base/backup';
  let path = basePath + '/localCapabilities.json'; // Local path for storing capability files.
  try {
    let fileData = await incrementalBackupSession.getLocalCapabilities(); // Obtain the local capability file.
    if (fileData) {
      console.info('getLocalCapabilities success');
      console.info('fileData info:' + fileData.fd);
      if (!fileIo.accessSync(basePath)) {
        fileIo.mkdirSync(basePath);
        console.info('create success' + basePath);
      }
      fileIo.copyFileSync(fileData.fd, path); // Save the obtained local capability file to the local host.
      fileIo.closeSync(fileData.fd);
    }
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
  }
  let data = fileIo.readTextSync(path, 'utf8'); // Obtain information from the local capability file.
  try {
    const jsonsObj: test | null = JSON.parse(data); // Parse the local capability file and print some information.
    if (jsonsObj) {
      const infos:BundleInfo [] = jsonsObj.bundleInfos;
      for (let i = 0; i < infos.length; i++) {
        console.info('name: ' + infos[i].name);
        console.info('appIndex: ' + infos[i].appIndex);
        console.info('allToBackup: ' + infos[i].allToBackup);
      }
      const systemFullName: string = jsonsObj.systemFullName;
      console.info('systemFullName: ' + systemFullName);
      const deviceType: string = jsonsObj.deviceType;
      console.info('deviceType: ' + deviceType);
    }
  } catch (error) {
    console.error(`parse failed. Code: ${error.code}, message: ${error.message}`);
  }
}
```

The capability file can be obtained by using [fileIo.stat](js-apis-file-fs.md#fileiostat-1) of the [@ohos.file.fs](js-apis-file-fs.md) module. The following is an example of the capability file.

```TypeScript
{
 "backupVersion" : "16.0",
 "bundleInfos" : [{
   "allToBackup" : true,
   "extensionName" : "BackupExtensionAbility",
   "name" : "com.example.hiworld",
   "needToInstall" : false,
   "spaceOccupied" : 0,
   "versionCode" : 1000000,
   "versionName" : "1.0.0"
   }],
 "deviceType" : "default",
 "systemFullName" : "OpenHarmony-4.0.0.0"
}
```

## release

```TypeScript
release(): Promise<void>
```

结束增量备份流程，断开应用与备份恢复服务的连接。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKUP

<!--Device-IncrementalBackupSession-release(): Promise<void>--><!--Device-IncrementalBackupSession-release(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13600001 | IPC error |
| 13900042 | Unknown error |

## Examples

```TypeScript
import { fileIo, backup} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let generalCallbacks: backup.GeneralCallbacks = {
  onFileReady: (err: BusinessError, file: backup.File) => {
    if (err) {
      console.error(`onFileReady failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onFileReady success');
    fileIo.closeSync(file.fd);
  },
  onBundleBegin: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleBegin failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleBegin success');
  },
  onBundleEnd: (err: BusinessError<string|void>, bundleName: string) => {
    if (err) {
      console.error(`onBundleEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onBundleEnd success');
  },
  onAllBundlesEnd: (err: BusinessError) => {
    if (err) {
      console.error(`onAllBundlesEnd failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('onAllBundlesEnd success');
  },
  onBackupServiceDied: () => {
    console.info('service died');
  },
  onResultReport: (bundleName: string, result: string) => {
    console.info(`onResultReport success, bundleName: ${bundleName}, result: ${result}`);
  },
  onProcess: (bundleName: string, process: string) => {
    console.info(`onProcess success, bundleName: ${bundleName}, process: ${process}`);
  }
};
let incrementalBackupSession = new backup.IncrementalBackupSession(generalCallbacks); // Create a session for an incremental backup.
incrementalBackupSession.release(); // End the incremental backup process.
console.info('release success');
```

