# getLocalCapabilities (System API)

## Modules to Import

```TypeScript
import backup from '@kit.CoreFileKit';
```

## getLocalCapabilities

```TypeScript
function getLocalCapabilities(): Promise<FileData>
```

Obtain a Json file that describes local capabilities.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; | A FileData holding all the local capabilities. The returned file is a temporal file that will be deleted automatically when closed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13600001 | IPC error |
| 13900005 | I/O error |
| 13900011 | Out of memory |
| 13900025 | No space left on device |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

async function getLocalCapabilities() {
  try {
    let fileData = await backup.getLocalCapabilities();
    console.info('getLocalCapabilities success');
    console.info('fileData info:' + fileData.fd);
    fileIo.closeSync(fileData.fd);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

The capability file can be obtained by using fileIo.stat of the [@ohos.file.fs](arkts-corefile-fileio-n.md) module. The following is an example of the capability file.

```TypeScript
{
 "backupVersion" : "16.0",
 "bundleInfos" :[{
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

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
  let sessionBackup = new backup.SessionBackup(generalCallbacks); // Create a backup process.
  let basePath = '/data/storage/el2/base/backup'; 
  let path = basePath + '/localCapabilities.json'; // Local path for storing capability files.
  try {
    let fileData = await sessionBackup.getLocalCapabilities(); // Obtain the local capability file.
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
    console.error(`parse failed. message: ${error.message}`);
  }
}
```

The capability file can be obtained by using fileIo.stat of the [@ohos.file.fs](arkts-corefile-fileio-n.md) module. The following is an example of the capability file.

```TypeScript
{
 "backupVersion" : "16.0",
 "bundleInfos" :[{
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

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
  let sessionRestore = new backup.SessionRestore(generalCallbacks); // Create a restore process.
  let basePath = '/data/storage/el2/base/backup';
  let path = basePath + '/localCapabilities.json'; // Local path for storing capability files.
  try {
    let fileData = await sessionRestore.getLocalCapabilities(); // Obtain the local capability file.
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
    console.error(`getLocalCapabilities failed with code: ${err.code}, message: ${err.message}`);
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
    console.error(`parse failed with code: ${error.code}, message: ${error.message}`);
  }
}
```

The capability file can be obtained by using fileIo.stat of the [@ohos.file.fs](arkts-corefile-fileio-n.md) module. The following is an example of the capability file.

```TypeScript
{
 "backupVersion" : "16.0",
 "bundleInfos" :[{
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

The capability file can be obtained by using fileIo.stat of the [@ohos.file.fs](arkts-corefile-fileio-n.md) module. The following is an example of the capability file.

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


## getLocalCapabilities

```TypeScript
function getLocalCapabilities(callback: AsyncCallback<FileData>): void
```

Obtain a Json file that describes local capabilities.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; | Yes | A callback method, the argument FileData will holding all the local capabilities. The returned file is a temporal file that will be deleted automatically when closed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13600001 | IPC error |
| 13900005 | I/O error |
| 13900011 | Out of memory |
| 13900025 | No space left on device |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

try {
  backup.getLocalCapabilities((err: BusinessError, fileData: backup.FileData) => {
    if (err) {
      console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('getLocalCapabilities success');
    console.info('fileData info:' + fileData.fd);
    fileIo.closeSync(fileData.fd);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
}
```

The capability file can be obtained by using fileIo.stat of the [@ohos.file.fs](arkts-corefile-fileio-n.md) module. The following is an example of the capability file.

```TypeScript
{
 "backupVersion" : "16.0",
 "bundleInfos" :[{
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


## getLocalCapabilities

```TypeScript
function getLocalCapabilities(dataList: Array<IncrementalBackupTime>): Promise<FileData>
```

Obtain a json file that describes local capabilities.

**Since:** 12

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataList | Array&lt;[IncrementalBackupTime](arkts-corefile-backup-incrementalbackuptime-i-sys.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; | A FileData holding all the local capabilities. The returned file is a temporal file that will be deleted automatically when closed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed, usually the result returned by VerifyAccessToken. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.  2. Incorrect parameter types. 3.Parameter verification failed. |
| 13600001 | IPC error |
| 13900005 | I/O error |
| 13900011 | Out of memory |
| 13900025 | No space left on device |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

async function getLocalCapabilities() {
  try {
    let backupApps: backup.IncrementalBackupTime[] = [{
      bundleName: "com.example.hiworld",
      lastIncrementalTime: 1700107870 // Time of the last incremental backup.
    }];
    let fileData = await backup.getLocalCapabilities(backupApps);
    console.info('getLocalCapabilities success');
    console.info('fileData info:' + fileData.fd);
    fileIo.closeSync(fileData.fd);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```
