# CloudFileCache

云盘文件缓存对象，用来支撑文件管理应用原文件下载流程。

**起始版本：** 11

<!--Device-cloudSync-class CloudFileCache--><!--Device-cloudSync-class CloudFileCache-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## cleanCache

```TypeScript
cleanCache(uri: string): void
```

同步方法删除文件缓存。

**起始版本：** 11

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-CloudFileCache-cleanCache(uri: string): void--><!--Device-CloudFileCache-cleanCache(uri: string): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 13900002 |
| 14000002 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache("com.ohos.demo");
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileCache.cleanCache(uri);
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`clean cache failed with error message: ${error.message}, error code: ${error.code}`);
}
```

## constructor

```TypeScript
constructor(bundleName: string)
```

A constructor used to create a CloudFileCache object.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CloudFileCache-constructor(bundleName: string)--><!--Device-CloudFileCache-constructor(bundleName: string)-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let fileCache = new cloudSync.CloudFileCache("com.ohos.demo");
```

## getDownloadList

```TypeScript
getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>
```

获取文件下载进度列表。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDFILE_SYNC

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CloudFileCache-getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>--><!--Device-CloudFileCache-getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | Array&lt;string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;DownloadProgress&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path1 = "/data/storage/el2/cloud/1.txt";
let path2 = "/data/storage/el2/cloud/2.txt";
let uri1 = fileUri.getUriFromPath(path1);
let uri2 = fileUri.getUriFromPath(path2);
let uriArray = [uri1, uri2];

try {
  fileCache.getDownloadList(uriArray).then((downloadList: Array<cloudSync.DownloadProgress>) => {
    console.info("get download list successfully");
    for (let i = 0; i < downloadList.length; i++) {
      console.info("download progress - uri: ".concat(downloadList[i].uri, ", state: ").concat(downloadList[i].state.toString()));
      console.info("processed: ".concat(downloadList[i].processed.toString(), ", size: ").concat(downloadList[i].size.toString()));
      console.info("error: ".concat(downloadList[i].error.toString()));
    }
  }).catch((error: BusinessError) => {
    console.error("get download list failed with error message: " + error.message + ", error code: " + error.code);
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("get download list failed with error message: " + error.message + ", error code: " + error.code);
}
```
