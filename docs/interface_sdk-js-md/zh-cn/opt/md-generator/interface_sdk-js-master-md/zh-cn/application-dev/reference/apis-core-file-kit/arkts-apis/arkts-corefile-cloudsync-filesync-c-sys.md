# FileSync

云盘同步对象，用于支撑文件管理器应用完成云盘文件的端云同步流程。在使用前，需要先创建FileSync实例。

**起始版本：** 12

<!--Device-cloudSync-class FileSync--><!--Device-cloudSync-class FileSync-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## constructor

```TypeScript
constructor(bundleName: string)
```

端云同步流程的构造函数，用于获取FileSync类的实例。

**起始版本：** 12

<!--Device-FileSync-constructor(bundleName: string)--><!--Device-FileSync-constructor(bundleName: string)-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let fileSync = new cloudSync.FileSync("com.ohos.demo")
```

## getUploadList

```TypeScript
getUploadList(uris: Array<string>): Promise<Array<UploadProgress>>
```

获取文件上传列表和进度信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDFILE_SYNC

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileSync-getUploadList(uris: Array<string>): Promise<Array<UploadProgress>>--><!--Device-FileSync-getUploadList(uris: Array<string>): Promise<Array<UploadProgress>>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | Array&lt;string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;UploadProgress&gt;&gt; |

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

let fileSync = new cloudSync.FileSync("com.ohos.demo");
let uris: string[] = ["file:///data/storage/el2/cloud/1.txt", "file:///data/storage/el2/cloud/2.jpg"];

fileSync.getUploadList(uris).then((progressList: cloudSync.UploadProgress[]) => {
  console.info("get upload list successfully, count: " + progressList.length);
  for (let i = 0; i < progressList.length; i++) {
    console.info("file uri: " + progressList[i].uri + ", state: " + progressList[i].state);
  }
}).catch((error: BusinessError) => {
  console.error("get upload list failed with error message: " + error.message + ", error code: " + error.code);
});
```

## pauseUpload

```TypeScript
pauseUpload(uri: string): void
```

暂停云文件上传。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDFILE_SYNC

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileSync-pauseUpload(uri: string): void--><!--Device-FileSync-pauseUpload(uri: string): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 14000002 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileSync = new cloudSync.FileSync("com.ohos.demo");
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileSync.pauseUpload(uri);
  console.info("pause upload successfully.");
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("pause upload failed with error message: " + error.message + ", error code: " + error.code);
}
```

## registerUploadProgress

```TypeScript
registerUploadProgress(callback: Callback<UploadProgress>): void
```

注册上传进度回调函数，用于监听文件上传进度变化。使用callback异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDFILE_SYNC

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileSync-registerUploadProgress(callback: Callback<UploadProgress>): void--><!--Device-FileSync-registerUploadProgress(callback: Callback<UploadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UploadProgress&gt; | 是 |

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

let fileSync = new cloudSync.FileSync("com.ohos.demo");

try {
  fileSync.registerUploadProgress((progress: cloudSync.UploadProgress) => {
    console.info(`upload progress - uri: ${progress.uri}, state: ${progress.state}`);
    console.info(`processed: ${progress.processed}, size: ${progress.size}`);
    console.info(`error: ${progress.error}`);
  });
  console.info("register upload progress successfully");
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`register upload progress failed with error message: ${error.message}, error code: ${error.code}`);
}
```

## resumeUpload

```TypeScript
resumeUpload(uri: string): void
```

恢复云文件上传。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDFILE_SYNC

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileSync-resumeUpload(uri: string): void--><!--Device-FileSync-resumeUpload(uri: string): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 14000002 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileSync = new cloudSync.FileSync("com.ohos.demo");
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileSync.resumeUpload(uri);
  console.info("resume upload successfully.");
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("resume upload failed with error message: " + error.message + ", error code: " + error.code);
}
```

## unregisterUploadProgress

```TypeScript
unregisterUploadProgress(): void
```

取消注册上传进度回调函数。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDFILE_SYNC

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileSync-unregisterUploadProgress(): void--><!--Device-FileSync-unregisterUploadProgress(): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync("com.ohos.demo");

try {
  fileSync.unregisterUploadProgress();
  console.info("unregister upload progress successfully");
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("unregister upload progress failed with error message: " + error.message + ", error code: " + error.code);
}
```
