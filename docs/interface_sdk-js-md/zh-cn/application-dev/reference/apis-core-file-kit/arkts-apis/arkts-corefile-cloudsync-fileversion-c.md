# FileVersion

端云文件版本管理类。支持对端云文件的历史版本进行管理，提供获取文件历史版本信息列表的能力，通过历史版本信息，可将历史版本下载到本地；并提供历史版本文件替换当前本地文件的能力，针对版本冲突，提供查询冲突标志，解除冲突标志的能力。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## 导入模块

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## clearFileConflict

```TypeScript
clearFileConflict(uri: string): Promise<void>
```

清除本地文件版本冲突标志。如果产生冲突，本地解决冲突后需要调用此方法来清除冲突标记，后续才可以触发自动同步机制，和云上保持一致。使用Promise异步回调。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900002 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400005 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

let isConflict = false;
fileVersion.isFileConflict(uri).then((isConflictRet: boolean) => {
  isConflict = isConflictRet;
  console.info("current file is conflict: " + isConflictRet);
}).catch((err: BusinessError) => {
  console.error(`get current file conflict flag failed with error message: ${err.message}, error code: ${err.code}`);
});
fileVersion.clearFileConflict(uri).then(() => {
  console.info("clean file conflict flag success");
}).catch((err: BusinessError) => {
  console.error("clean file conflict flag failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
let isConflict: boolean = false;
fileVersion.isFileConflict(uri).then<boolean>((isConflictRet: boolean): void => {
  isConflict = isConflictRet;
  console.info("current file is conflict: " + isConflictRet);
}).catch((err: BusinessError<void>): void => {
  console.error(`get current file conflict flag failed with error message: ${err.message}, error code: ${err.code}`);
});
fileVersion.clearFileConflict(uri).then<void>((): void => {
  console.info("clean file conflict flag success");
}).catch((err: BusinessError<void>): void => {
  console.error("clean file conflict flag failed with error message: " + err.message + ", error code: " + err.code);
});
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a FileVersion object.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**错误码：**

| 错误码ID |
| --- |
| 22400005 |

**示例**

```TypeScript
let fileSync = new cloudSync.FileSync()
```

```TypeScript
let fileCache = new cloudSync.CloudFileCache();
```

```TypeScript
let fileVersion = new cloudSync.FileVersion();
```

```TypeScript
let gallerySync = new cloudSync.GallerySync()
```

```TypeScript
let download = new cloudSync.Download()
```

```TypeScript
let fileSync = new cloudSync.FileSync("com.ohos.demo")
```

```TypeScript
let fileCache = new cloudSync.CloudFileCache("com.ohos.demo");
```

## downloadHistoryVersion

```TypeScript
downloadHistoryVersion(uri: string, versionId: string, callback: Callback<VersionDownloadProgress>): Promise<string>
```

根据版本号获取指定文件的某一版本的文件内容。用户通过版本号指定云上某一版本，将其下载到本地临时存储路径，临时文件由应用自行决定是否替换原始文件，也可以选择保留或直接删除。callback返回文件下载进度，Promise返回历史 版本临时文件的URI。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| versionId | string | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VersionDownloadProgress](arkts-corefile-cloudsync-versiondownloadprogress-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900002 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400002 |
| 22400005 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let versionId = '123456'; // 以 getHistoryVersionList 方法返回的格式为准，此处仅作为 demo 示例。

let callback = (data: cloudSync.VersionDownloadProgress) => {
  if (data.state == cloudSync.State.RUNNING) {
    console.info("download progress: " + data.progress);
  } else if (data.state == cloudSync.State.FAILED) {
    console.info("download failed errType: " + data.errType);
  } else if (data.state == cloudSync.State.COMPLETED) {
    console.info("download version file success");
  }
};

fileVersion.downloadHistoryVersion(uri, versionId, callback).then((fileUri: string) => {
  console.info("success to begin download, downloadFileUri: " + fileUri);
}).catch((err: BusinessError) => {
  console.error("download history version file failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
let versionId: string = '123456'; // 以 getHistoryVersionList 方法返回的格式为准，此处仅作为 demo 示例。
let callback = (data: cloudSync.VersionDownloadProgress): void => {
  if (data.state == cloudSync.State.RUNNING) {
    console.info("download progress: " + data.progress);
  } else if (data.state == cloudSync.State.FAILED) {
    console.info("download failed errType: " + data.errType);
  } else if (data.state == cloudSync.State.COMPLETED) {
    console.info("download version file success");
  }
};
fileVersion.downloadHistoryVersion(uri, versionId, callback).then<string>((fileUri: string): void => {
  console.info("success to begin download, downloadFileUri: " + fileUri);
}).catch((err: BusinessError<void>): void => {
  console.error("download history version file failed with error message: " + err.message + ", error code: " + err.code);
});
```

## getHistoryVersionList

ArkTS-Dyn:
```TypeScript
getHistoryVersionList(uri: string, versionNumLimit: number): Promise<Array<HistoryVersion>>
```

ArkTS-Sta:
```TypeScript
getHistoryVersionList(uri: string, versionNumLimit: int): Promise<Array<HistoryVersion>>
```

获取历史版本列表，返回内容按修改时间排序，修改时间越早，位置越靠后。使用Promise异步回调。当云上版本数量小于传入的长度限制时，按照实际版本数量返回历史版本列表。当云上版本数量大于等于传入的长度限制时，则返回最新的versionNumLimit个版本。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| versionNumLimit | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[HistoryVersion](arkts-corefile-cloudsync-historyversion-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900002 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400002 |
| 22400005 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let limit = 10;

fileVersion.getHistoryVersionList(uri, limit).then((versionList: Array<cloudSync.HistoryVersion>) => {
  for(let i = 0, len = versionList.length; i < len; i++) {
    console.info("get history versionId: " + versionList[i].versionId);
  }
}).catch((err: BusinessError) => {
  console.error("get history version failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
let limit: int = 10;
fileVersion.getHistoryVersionList(uri, limit).then<Array<cloudSync.HistoryVersion>>((versionList: Array<cloudSync.HistoryVersion>): void => {
  for(let i = 0, len = versionList.length; i < len; i++) {
    console.info("get history versionId: " + versionList[i].versionId);
  }
}).catch((err: BusinessError<void>): void => {
  console.error("get history version failed with error message: " + err.message + ", error code: " + err.code);
});
```

## isFileConflict

```TypeScript
isFileConflict(uri: string): Promise<boolean>
```

获取本地文件版本冲突标志。使用Promise异步回调。此方法只有应用在配置手动解冲突后才会生效，否则默认自动解冲突，返回值为false，由同步流程自动完成解冲突；当应用配置手动解冲突后，调用此方法会返回当前文件是否与云侧文件产生冲突，并且由应用提示用户对冲突进行处理，在冲突解决前不会再自动同步上云。当处理完冲突后，需要调用 [clearFileConflict](#clearfileconflict)方法来清除冲突标志，后续才会继续触发同步，与云端保持一致。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900002 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400005 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

fileVersion.isFileConflict(uri).then((isConflict: boolean) => {
  console.info("current file is conflict: " + isConflict);
}).catch((err: BusinessError) => {
  console.error("get current file conflict flag failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
fileVersion.isFileConflict(uri).then<boolean>((isConflict: boolean): void => {
  console.info("current file is conflict: " + isConflict);
}).catch((err: BusinessError<void>): void => {
  console.error("get current file conflict flag failed with error message: " + err.message + ", error code: " + err.code);
});
```

## replaceFileWithHistoryVersion

```TypeScript
replaceFileWithHistoryVersion(originalUri: string, versionUri: string): Promise<void>
```

提供使用历史版本文件替换本地文件的能力。在替换前，需要调用[downloadHistoryVersion](#downloadhistoryversion)方法对选择的历史 版本进行下载并拿到versionUri；直接调用此接口或者versionUri非法会产生异常；替换完成后会删除临时存储文件。使用Promise异步回调。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| originalUri | string | 是 |
| versionUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900002 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400005 |
| 22400007 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let versionId = '123456'; // 以 getHistoryVersionList 方法返回的格式为准，此处仅作为 demo 示例。

let callback = (data: cloudSync.VersionDownloadProgress) => {
  if (data.state == cloudSync.State.RUNNING) {
    console.info("download progress: " + data.progress);
  } else if (data.state == cloudSync.State.FAILED) {
    console.info("download failed errType: " + data.errType);
  } else if (data.state == cloudSync.State.COMPLETED) {
    console.info("download version file success");
  }
};

let versionUri = "";
fileVersion.downloadHistoryVersion(uri, versionId, callback).then((fileUri: string) => {
  versionUri = fileUri;
  console.info("success to begin download, downloadFileUri: " + fileUri);
}).catch((err: BusinessError) => {
  console.error(`download history version file failed with error message: ${err.message}, error code: ${err.code}`);
});
fileVersion.replaceFileWithHistoryVersion(uri, versionUri).then(() => {
  console.info("replace file with history version success.");
}).catch((err: BusinessError) => {
  console.error("replace file with history version failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
let versionId: string = '123456'; // 以 getHistoryVersionList 方法返回的格式为准，此处仅作为 demo 示例。
let callback = (data: cloudSync.VersionDownloadProgress): void => {
  if (data.state == cloudSync.State.RUNNING) {
    console.info("download progress: " + data.progress);
  } else if (data.state == cloudSync.State.FAILED) {
    console.info("download failed errType: " + data.errType);
  } else if (data.state == cloudSync.State.COMPLETED) {
    console.info("download version file success");
  }
};
let versionUri: string = "";
fileVersion.downloadHistoryVersion(uri, versionId, callback).then<string>((fileUri: string): void => {
  versionUri = fileUri;
  console.info("success to begin download, downloadFileUri: " + fileUri);
}).catch((err: BusinessError<void>): void => {
  console.error(`download history version file failed with error message: ${err.message}, error code: ${err.code}`);
});
fileVersion.replaceFileWithHistoryVersion(uri, versionUri).then<void>((): void => {
  console.info("replace file with history version success.");
}).catch((err: BusinessError<void>): void => {
  console.error("replace file with history version filed with error message: " + err.message + ", error code: " + err.code);
});
```
