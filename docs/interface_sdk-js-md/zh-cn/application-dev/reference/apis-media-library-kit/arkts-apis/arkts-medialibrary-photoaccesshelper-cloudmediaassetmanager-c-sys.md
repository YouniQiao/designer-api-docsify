# CloudMediaAssetManager（系统接口）

A class used for cloud media asset management. It is used to manage download tasks for media assets stored in the cloud and delete local data and files pertaining to these cloud-based assets.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-class CloudMediaAssetManager--><!--Device-photoAccessHelper-class CloudMediaAssetManager-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## cancelDownloadCloudMedia

```TypeScript
cancelDownloadCloudMedia(): Promise<void>
```

Cancels a task that downloads cloud media assets.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-CloudMediaAssetManager-cancelDownloadCloudMedia(): Promise<void>--><!--Device-CloudMediaAssetManager-cancelDownloadCloudMedia(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 14000011 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; 2 &lt;br&gt;. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('cancelDownloadCloudMediaDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    await cloudMediaAssetManagerInstance.cancelDownloadCloudMedia();
  } catch (err) {
    console.error(`cancelDownloadCloudMediaDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## cancelDownloadSpecificCloudMedia

```TypeScript
cancelDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>
```

Cancels a batch download for the specified cloud media assets. This API uses a promise to return the result.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-cancelDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>--><!--Device-CloudMediaAssetManager-cancelDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assetUris | string[] \| null | 是 | Array of URIs pointing to the original-quality images and videos to be canceled. &lt;br&gt;If null, undefined, or an empty list is passed, it represents all existing individual download items. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 23800151 | The scenario parameter verification fails. Possible causes: The assetUris array size is bigger than 500. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('CancelDownloadSpecificCloudMediaDemo');
  try {
    let assetURIs: Array<string> = [
       'file://media/Photo/12/IMG_1755046662_091/IMG_20250801_175331.jpg'];
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    await cloudMediaAssetManagerInstance.cancelDownloadSpecificCloudMedia(assetURIs);
  } catch (err) {
    console.error(`failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getCloudMediaAssetManagerInstance

```TypeScript
static getCloudMediaAssetManagerInstance(context: Context): CloudMediaAssetManager
```

Obtains a CloudMediaAssetManager instance.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-CloudMediaAssetManager-static getCloudMediaAssetManagerInstance(context: Context): CloudMediaAssetManager--><!--Device-CloudMediaAssetManager-static getCloudMediaAssetManagerInstance(context: Context): CloudMediaAssetManager-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | 是 | Context of the ability instance. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CloudMediaAssetManager](arkts-medialibrary-photoaccesshelper-cloudmediaassetmanager-c-sys.md) | CloudMediaAssetManager instance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 202 | Called by non-system application |
| 14000011 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('getCloudMediaAssetManagerInstanceDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    await cloudMediaAssetManagerInstance.pauseDownloadCloudMedia();
  } catch (err) {
    console.error(`getCloudMediaAssetManagerInstanceDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getCloudMediaAssetManagerInstance

```TypeScript
static getCloudMediaAssetManagerInstance(context: Context): CloudMediaAssetManager | null
```

Obtains a CloudMediaAssetManager instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-CloudMediaAssetManager-static getCloudMediaAssetManagerInstance(context: Context): CloudMediaAssetManager | null--><!--Device-CloudMediaAssetManager-static getCloudMediaAssetManagerInstance(context: Context): CloudMediaAssetManager | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | 是 | Obtains a CloudMediaAssetManager instance. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CloudMediaAssetManager](arkts-medialibrary-photoaccesshelper-cloudmediaassetmanager-c-sys.md) | Returns cloud media asset manager instance, if the operation fails, returns null |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |

## getCloudMediaAssetStatus

```TypeScript
getCloudMediaAssetStatus(): Promise<CloudMediaAssetStatus>
```

Obtains the status of a task that downloads cloud media assets.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-getCloudMediaAssetStatus(): Promise<CloudMediaAssetStatus>--><!--Device-CloudMediaAssetManager-getCloudMediaAssetStatus(): Promise<CloudMediaAssetStatus>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;CloudMediaAssetStatus&gt; | Promise used to return the task status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 14000011 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('getCloudMediaAssetStatusDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    const cloudMediaAssetStatus: photoAccessHelper.CloudMediaAssetStatus = await cloudMediaAssetManagerInstance.getCloudMediaAssetStatus();
    let taskStatus = cloudMediaAssetStatus.taskStatus;
    let taskInfo = cloudMediaAssetStatus.taskInfo;
    let errorCode = cloudMediaAssetStatus.errorCode;
    let message = `taskStatus: ${taskStatus}, taskInfo: ${taskInfo}, errorCode: ${errorCode}`;
    console.info(message);
  } catch (err) {
    console.error(`getCloudMediaAssetStatusDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## offDownloadProgressChange

```TypeScript
offDownloadProgressChange(callback?: Callback<CloudAssetDownloadProgressInfo>): void
```

Unregisters a callback to monitor changes in the progress of a batch download for cloud media assets.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-offDownloadProgressChange(callback?: Callback<CloudAssetDownloadProgressInfo>): void--><!--Device-CloudMediaAssetManager-offDownloadProgressChange(callback?: Callback<CloudAssetDownloadProgressInfo>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CloudAssetDownloadProgressInfo&gt; | 否 | Callback to unregister, which is registered by [onDownloadProgressChange](photoAccessHelper.CloudMediaAssetManager.on). If this parameter is left empty, all progress-related callbacks are unregistered. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('OffDownloadProgressChangeDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    cloudMediaAssetManagerInstance.offDownloadProgressChange();
  } catch (err) {
    console.error(`failed with error: ${err.code}, ${err.message}`);
  }
}
```

## onDownloadProgressChange

```TypeScript
onDownloadProgressChange(callback: Callback<CloudAssetDownloadProgressInfo>): void
```

Registers a callback to monitor changes in the progress of a batch download for cloud media assets.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-onDownloadProgressChange(callback: Callback<CloudAssetDownloadProgressInfo>): void--><!--Device-CloudMediaAssetManager-onDownloadProgressChange(callback: Callback<CloudAssetDownloadProgressInfo>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CloudAssetDownloadProgressInfo&gt; | 是 | Callback to register. The callback returns progress information of the batch download. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |

## 示例

```TypeScript
let onCallback = (changeData: photoAccessHelper.CloudAssetDownloadProgressInfo) => {
  console.info('batchdownload downloadProgressChange onCallback success, changData: ' + JSON.stringify(changeData));
}
async function example(context: Context) {
  console.info('OnDownloadProgressChangeDemo');
  try {
      let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
        = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
      // 注册onCallback监听。
      cloudMediaAssetManagerInstance.onDownloadProgressChange(onCallback);
  } catch (err) {
    console.error(`failed with error: ${err.code}, ${err.message}`);
  }
}
```

## pauseDownloadCloudMedia

```TypeScript
pauseDownloadCloudMedia(): Promise<void>
```

Suspends a task that downloads cloud media assets.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-CloudMediaAssetManager-pauseDownloadCloudMedia(): Promise<void>--><!--Device-CloudMediaAssetManager-pauseDownloadCloudMedia(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 14000011 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('pauseDownloadCloudMediaDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    await cloudMediaAssetManagerInstance.pauseDownloadCloudMedia();
  } catch (err) {
    console.error(`pauseDownloadCloudMediaDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## pauseDownloadSpecificCloudMedia

```TypeScript
pauseDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>
```

Pauses a batch download for the specified cloud media assets. This API uses a promise to return the result.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-pauseDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>--><!--Device-CloudMediaAssetManager-pauseDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assetUris | string[] \| null | 是 | Array of URIs pointing to the original-quality images and videos to be paused. &lt;br&gt;If null, undefined, or an empty list is passed, it represents all existing individual download items. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 23800151 | The scenario parameter verification fails. Possible causes: The assetUris array size is bigger than 500. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('PauseDownloadSpecificCloudMediaDemo');
  try {
    let assetURIs: Array<string> = [
       'file://media/Photo/12/IMG_1755046662_091/IMG_20250801_175331.jpg'];
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    await cloudMediaAssetManagerInstance.pauseDownloadSpecificCloudMedia(assetURIs);
  } catch (err) {
    console.error(`failed with error: ${err.code}, ${err.message}`);
  }
}
```

## queryDownloadSpecificCloudMediaDetails

```TypeScript
queryDownloadSpecificCloudMediaDetails(predicates: dataSharePredicates.DataSharePredicates): Promise<CloudAssetDownloadStatus>
```

Obtains the details of a batch download for cloud media assets. This API uses a promise to return the result.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-queryDownloadSpecificCloudMediaDetails(predicates: dataSharePredicates.DataSharePredicates): Promise<CloudAssetDownloadStatus>--><!--Device-CloudMediaAssetManager-queryDownloadSpecificCloudMediaDetails(predicates: dataSharePredicates.DataSharePredicates): Promise<CloudAssetDownloadStatus>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | 是 | Predicates that specify the fetch criteria. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;CloudAssetDownloadStatus&gt; | Promise used to return the details obtained. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |

## 示例

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

async function example(context: Context) {
  console.info('QueryDownloadSpecificCloudMediaDetailsDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.orderByAsc("file_id");
    let taskListStatus : photoAccessHelper.CloudAssetDownloadStatus =
       await cloudMediaAssetManagerInstance.queryDownloadSpecificCloudMediaDetails(predicates);
  } catch (err) {
    console.error(`failed with error: ${err.code}, ${err.message}`);
  }
}
```

## queryDownloadSpecificCloudMediaTaskCount

ArkTS-Dyn:
```TypeScript
queryDownloadSpecificCloudMediaTaskCount(predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

ArkTS-Sta:
```TypeScript
queryDownloadSpecificCloudMediaTaskCount(predicates: dataSharePredicates.DataSharePredicates): Promise<int>
```

Obtains the number of batch download tasks for cloud media assets. This API uses a promise to return the result.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-queryDownloadSpecificCloudMediaTaskCount(predicates: dataSharePredicates.DataSharePredicates): Promise<int>--><!--Device-CloudMediaAssetManager-queryDownloadSpecificCloudMediaTaskCount(predicates: dataSharePredicates.DataSharePredicates): Promise<int>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | 是 | Predicates that specify the fetch criteria. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the number of batch download tasks. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |

## 示例

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

async function example(context: Context) {
  console.info('QueryDownloadSpecificCloudMediaTaskCountDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.orderByAsc("file_id");
    let count : number =
       await cloudMediaAssetManagerInstance.queryDownloadSpecificCloudMediaTaskCount(predicates);
  } catch (err) {
    console.error(`failed with error: ${err.code}, ${err.message}`);
  }
}
```

## resumeDownloadSpecificCloudMedia

```TypeScript
resumeDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>
```

Resumes a batch download for the specified cloud media assets. This API uses a promise to return the result.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-resumeDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>--><!--Device-CloudMediaAssetManager-resumeDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assetUris | string[] \| null | 是 | Array of URIs pointing to the original-quality images and videos to be resumed. &lt;br&gt;If null, undefined, or an empty list is passed, it represents all existing individual download items. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 23800151 | The scenario parameter verification fails. Possible causes: The assetUris array size is bigger than 500. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('ResumeDownloadSpecificCloudMediaDemo');
  try {
    let assetURIs: Array<string> = [
       'file://media/Photo/12/IMG_1755046662_091/IMG_20250801_175331.jpg'];
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    await cloudMediaAssetManagerInstance.resumeDownloadSpecificCloudMedia(assetURIs);
  } catch (err) {
    console.error(`failed with error: ${err.code}, ${err.message}`);
  }
}
```

## retainCloudMediaAsset

```TypeScript
retainCloudMediaAsset(retainType: CloudMediaRetainType): Promise<void>
```

Deletes local metadata and files of cloud media assets.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-CloudMediaAssetManager-retainCloudMediaAsset(retainType: CloudMediaRetainType): Promise<void>--><!--Device-CloudMediaAssetManager-retainCloudMediaAsset(retainType: CloudMediaRetainType): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| retainType | [CloudMediaRetainType](arkts-medialibrary-photoaccesshelper-cloudmediaretaintype-e-sys.md) | 是 | Mode for deleting cloud media assets. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 14000011 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('retainCloudMediaAssetDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    await cloudMediaAssetManagerInstance.retainCloudMediaAsset(photoAccessHelper.CloudMediaRetainType.RETAIN_FORCE);
  } catch (err) {
    console.error(`retainCloudMediaAssetDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## startDownloadCloudMedia

```TypeScript
startDownloadCloudMedia(downloadType: CloudMediaDownloadType): Promise<void>
```

Starts or resumes a task to download cloud media assets.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-CloudMediaAssetManager-startDownloadCloudMedia(downloadType: CloudMediaDownloadType): Promise<void>--><!--Device-CloudMediaAssetManager-startDownloadCloudMedia(downloadType: CloudMediaDownloadType): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| downloadType | [CloudMediaDownloadType](arkts-medialibrary-photoaccesshelper-cloudmediadownloadtype-e-sys.md) | 是 | Type of the download task. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 14000011 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('startDownloadCloudMediaDemo');
  try {
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    await cloudMediaAssetManagerInstance.startDownloadCloudMedia(photoAccessHelper.CloudMediaDownloadType.DOWNLOAD_FORCE);
  } catch (err) {
    console.error(`startDownloadCloudMediaDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## startDownloadSpecificCloudMedia

```TypeScript
startDownloadSpecificCloudMedia(assetUris: string[]): Promise<Map<string, CloudAssetDownloadCode>>
```

Starts a batch download for the specified cloud media assets. This API uses a promise to return the result.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudMediaAssetManager-startDownloadSpecificCloudMedia(assetUris: string[]): Promise<Map<string, CloudAssetDownloadCode>>--><!--Device-CloudMediaAssetManager-startDownloadSpecificCloudMedia(assetUris: string[]): Promise<Map<string, CloudAssetDownloadCode>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assetUris | string[] | 是 | Array of URIs pointing to the original-quality images and videos to be downloaded. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Map&lt;string, CloudAssetDownloadCode&gt;&gt; | Promise used to return a map, where each key is a URI and its value indicates the status of that individual download item. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 23800151 | The scenario parameter verification fails. Possible causes: &lt;br&gt;1. The assetUris array is empty; &lt;br&gt;2. The assetUris array size is bigger than 500. |

## 示例

```TypeScript
async function example(context: Context) {
  console.info('StartDownloadSpecificCloudMediaDemo');
  try {
    let assetURIs: Array<string> = [
       'file://media/Photo/12/IMG_1755046662_091/IMG_20250801_175331.jpg'];
    let cloudMediaAssetManagerInstance: photoAccessHelper.CloudMediaAssetManager
      = photoAccessHelper.CloudMediaAssetManager.getCloudMediaAssetManagerInstance(context);
    let taskRespMap : Map<string, photoAccessHelper.CloudAssetDownloadCode> =
      await cloudMediaAssetManagerInstance.startDownloadSpecificCloudMedia(assetURIs);
  } catch (err) {
    console.error(`failed with error: ${err.code}, ${err.message}`);
  }
}
```

