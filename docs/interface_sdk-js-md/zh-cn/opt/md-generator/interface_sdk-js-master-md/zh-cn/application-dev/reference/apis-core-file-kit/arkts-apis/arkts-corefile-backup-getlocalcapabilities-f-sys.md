# getLocalCapabilities（系统接口）

## 导入模块

```TypeScript
```

## getLocalCapabilities

```TypeScript
function getLocalCapabilities(): Promise<FileData>
```

获取描述本地能力的JSON文件。

**起始版本：** 23

**需要权限：** ohos.permission.BACKUP

<!--Device-backup-function getLocalCapabilities(): Promise<FileData>--><!--Device-backup-function getLocalCapabilities(): Promise<FileData>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900025 |
| 13600001 |
| 13900042 |
| 13900011 |

**示例**

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

能力文件可以通过[@ohos.file.fs](arkts-corefile-fileio-n.md#fileio)提供的fileIo.stat等相关接口获取，能力文件内容示例：

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
function getLocalCapabilities(callback: AsyncCallback<FileData>): void
```

获取描述本地能力的JSON文件。

**起始版本：** 23

**需要权限：** ohos.permission.BACKUP

<!--Device-backup-function getLocalCapabilities(callback: AsyncCallback<FileData>): void--><!--Device-backup-function getLocalCapabilities(callback: AsyncCallback<FileData>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900025 |
| 13600001 |
| 13900042 |
| 13900011 |

**示例**

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

能力文件可以通过[@ohos.file.fs](arkts-corefile-fileio-n.md#fileio)提供的fileIo.stat等相关接口获取，能力文件内容示例：

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

获取描述本地能力的JSON文件。

**起始版本：** 23

**需要权限：** ohos.permission.BACKUP

<!--Device-backup-function getLocalCapabilities(dataList: Array<IncrementalBackupTime>): Promise<FileData>--><!--Device-backup-function getLocalCapabilities(dataList: Array<IncrementalBackupTime>): Promise<FileData>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataList | Array&lt;[IncrementalBackupTime](arkts-corefile-backup-incrementalbackuptime-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900005 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900025 |
| 13600001 |
| 13900042 |
| 13900011 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

async function getLocalCapabilities() {
  try {
    let backupApps: backup.IncrementalBackupTime[] = [{
      bundleName: 'com.example.hiworld',
      lastIncrementalTime: 1700107870 // 调用者根据上次记录的增量备份时间
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
