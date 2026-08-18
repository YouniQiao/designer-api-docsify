# CloudEnhancement（系统接口）

云增强管理类，该类用于生成AI云增强照片任务的管理、获取原照片与AI云增强照片的关联关系。

**起始版本：** 23

<!--Device-photoAccessHelper-class CloudEnhancement--><!--Device-photoAccessHelper-class CloudEnhancement-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## cancelAllCloudEnhancementTasks

```TypeScript
cancelAllCloudEnhancementTasks(): Promise<void>
```

取消全部云增强任务。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-CloudEnhancement-cancelAllCloudEnhancementTasks(): Promise<void>--><!--Device-CloudEnhancement-cancelAllCloudEnhancementTasks(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('cancelAllCloudEnhancementTasksDemo');
  try {
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    await cloudEnhancementInstance.cancelAllCloudEnhancementTasks();
  } catch (err) {
    console.error(`cancelAllCloudEnhancementTasksDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## cancelCloudEnhancementTasks

```TypeScript
cancelCloudEnhancementTasks(photoAssets: Array<PhotoAsset>): Promise<void>
```

取消指定云增强任务。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-CloudEnhancement-cancelCloudEnhancementTasks(photoAssets: Array<PhotoAsset>): Promise<void>--><!--Device-CloudEnhancement-cancelCloudEnhancementTasks(photoAssets: Array<PhotoAsset>): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoAssets | Array & lt;PhotoAsset & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('cancelCloudEnhancementTasksDemo');
  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  // 查询进行中的云增强任务。
  photoPredicates.equalTo(photoAccessHelper.PhotoKeys.CE_AVAILABLE, 2);
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  try {
    let fetchResult = await phAccessHelper.getAssets(photoFetchOptions);
    let asset = await fetchResult.getLastObject();
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    await cloudEnhancementInstance.cancelCloudEnhancementTasks([asset]);
  } catch (err) {
    console.error(`cancelCloudEnhancementTasksDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getCloudEnhancementInstance

```TypeScript
static getCloudEnhancementInstance(context: Context): CloudEnhancement
```

获取云增强类实例。

**起始版本：** 13

<!--Device-CloudEnhancement-static getCloudEnhancementInstance(context: Context): CloudEnhancement--><!--Device-CloudEnhancement-static getCloudEnhancementInstance(context: Context): CloudEnhancement-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CloudEnhancement](arkts-medialibrary-photoaccesshelper-cloudenhancement-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('getCloudEnhancementInstanceDemo');
  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  try {
    let fetchResult = await phAccessHelper.getAssets(photoFetchOptions);
    let asset = await fetchResult.getLastObject();
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    let hasCloudWatermark = true;
    await cloudEnhancementInstance.submitCloudEnhancementTasks([asset], hasCloudWatermark);
  } catch (err) {
    console.error(`getCloudEnhancementInstanceDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getCloudEnhancementInstance

```TypeScript
static getCloudEnhancementInstance(context: Context): CloudEnhancement | null
```

获取云增强类实例。

**起始版本：** 23

<!--Device-CloudEnhancement-static getCloudEnhancementInstance(context: Context): CloudEnhancement | null--><!--Device-CloudEnhancement-static getCloudEnhancementInstance(context: Context): CloudEnhancement | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CloudEnhancement](arkts-medialibrary-photoaccesshelper-cloudenhancement-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getCloudEnhancementPair

```TypeScript
getCloudEnhancementPair(asset: PhotoAsset): Promise<PhotoAsset>
```

查询云增强配对照片。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudEnhancement-getCloudEnhancementPair(asset: PhotoAsset): Promise<PhotoAsset>--><!--Device-CloudEnhancement-getCloudEnhancementPair(asset: PhotoAsset): Promise<PhotoAsset>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [asset](../../apis-asset-store-kit/arkts-apis/arkts-security-asset.md) | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('getCloudEnhancementPairDemo');
  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  // 查询已完成的云增强任务。
  photoPredicates.equalTo(photoAccessHelper.PhotoKeys.CE_AVAILABLE, 5);
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  try {
    let fetchResult = await phAccessHelper.getAssets(photoFetchOptions);
    let asset = await fetchResult.getLastObject();
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    let photoAsset: photoAccessHelper.PhotoAsset
      = await cloudEnhancementInstance.getCloudEnhancementPair(asset);
  } catch (err) {
    console.error(`getCloudEnhancementPairDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## prioritizeCloudEnhancementTask

```TypeScript
prioritizeCloudEnhancementTask(photoAsset: PhotoAsset): Promise<void>
```

提升指定云增强任务的优先级。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-CloudEnhancement-prioritizeCloudEnhancementTask(photoAsset: PhotoAsset): Promise<void>--><!--Device-CloudEnhancement-prioritizeCloudEnhancementTask(photoAsset: PhotoAsset): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoAsset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('prioritizeCloudEnhancementTaskDemo');
  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  // 查询进行中的云增强任务。
  photoPredicates.equalTo(photoAccessHelper.PhotoKeys.CE_AVAILABLE, 2);
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  try {
    let fetchResult = await phAccessHelper.getAssets(photoFetchOptions);
    let asset = await fetchResult.getLastObject();
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    let hasCloudWatermark = true;
    await cloudEnhancementInstance.prioritizeCloudEnhancementTask(asset);
  } catch (err) {
    console.error(`prioritizeCloudEnhancementTaskDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## queryCloudEnhancementTaskState

```TypeScript
queryCloudEnhancementTaskState(photoAsset: PhotoAsset): Promise<CloudEnhancementTaskState>
```

查询云增强任务信息。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudEnhancement-queryCloudEnhancementTaskState(photoAsset: PhotoAsset): Promise<CloudEnhancementTaskState>--><!--Device-CloudEnhancement-queryCloudEnhancementTaskState(photoAsset: PhotoAsset): Promise<CloudEnhancementTaskState>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoAsset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CloudEnhancementTaskState](arkts-medialibrary-photoaccesshelper-cloudenhancementtaskstate-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('queryCloudEnhancementTaskStateDemo');
  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  // 查询进行中的云增强任务。
  photoPredicates.equalTo(photoAccessHelper.PhotoKeys.CE_AVAILABLE, 2);
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  try {
    let fetchResult = await phAccessHelper.getAssets(photoFetchOptions);
    let asset = await fetchResult.getLastObject();
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    const cloudEnhancementTaskState: photoAccessHelper.CloudEnhancementTaskState
      = await cloudEnhancementInstance.queryCloudEnhancementTaskState(asset);
    let taskStage = cloudEnhancementTaskState.taskStage;
    if (taskStage == photoAccessHelper.CloudEnhancementTaskStage.TASK_STAGE_EXCEPTION) {
      console.info("task has exception");
    } else if (taskStage == photoAccessHelper.CloudEnhancementTaskStage.TASK_STAGE_PREPARING) {
      console.info("task is preparing");
    } else if (taskStage == photoAccessHelper.CloudEnhancementTaskStage.TASK_STAGE_UPLOADING) {
      let transferredFileSize = cloudEnhancementTaskState.transferredFileSize;
      let totalFileSize = cloudEnhancementTaskState.totalFileSize;
      let message = `task is uploading, transferredFileSize: ${transferredFileSize}, totalFileSize: ${totalFileSize}`;
      console.info(message);
    } else if (taskStage == photoAccessHelper.CloudEnhancementTaskStage.TASK_STAGE_EXECUTING) {
      let expectedDuration = cloudEnhancementTaskState.expectedDuration;
      let message = `task is executing, expectedDuration: ${expectedDuration}`;
      console.info(message);
    } else if (taskStage == photoAccessHelper.CloudEnhancementTaskStage.TASK_STAGE_DOWNLOADING) {
      let transferredFileSize = cloudEnhancementTaskState.transferredFileSize;
      let totalFileSize = cloudEnhancementTaskState.totalFileSize;
      let message = `task is downloading, transferredFileSize: ${transferredFileSize}, totalFileSize: ${totalFileSize}`;
      console.info(message);
    } else if (taskStage == photoAccessHelper.CloudEnhancementTaskStage.TASK_STAGE_FAILED) {
      let errCode = cloudEnhancementTaskState.statusCode;
      let message = `task is failed, errCode: ${errCode}`;
      console.info(message);
    } else if (taskStage == photoAccessHelper.CloudEnhancementTaskStage.TASK_STAGE_COMPLETED) {
      console.info("task is completed");
    }
  } catch (err) {
    console.error(`queryCloudEnhancementTaskStateDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## submitCloudEnhancementTasks

```TypeScript
submitCloudEnhancementTasks(photoAssets: Array<PhotoAsset>, hasCloudWatermark: boolean): Promise<void>
```

提交云增强任务。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-CloudEnhancement-submitCloudEnhancementTasks(photoAssets: Array<PhotoAsset>, hasCloudWatermark: boolean): Promise<void>--><!--Device-CloudEnhancement-submitCloudEnhancementTasks(photoAssets: Array<PhotoAsset>, hasCloudWatermark: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoAssets | Array & lt;PhotoAsset & gt; | 是 |
| hasCloudWatermark | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('submitCloudEnhancementTasksDemo');
  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  try {
    let fetchResult = await phAccessHelper.getAssets(photoFetchOptions);
    let asset = await fetchResult.getLastObject();
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    let hasCloudWatermark = true;
    await cloudEnhancementInstance.submitCloudEnhancementTasks([asset], hasCloudWatermark);
  } catch (err) {
    console.error(`submitCloudEnhancementTasksDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## submitCloudEnhancementTasks

```TypeScript
submitCloudEnhancementTasks(
      photoAssets: Array<PhotoAsset>,
      hasCloudWatermark: boolean,
      triggerMode?: number
    ): Promise<void>
```

提交云增强任务，支持选择云增强任务触发类型。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-CloudEnhancement-submitCloudEnhancementTasks(      photoAssets: Array<PhotoAsset>,      hasCloudWatermark: boolean,      triggerMode?: int    ): Promise<void>--><!--Device-CloudEnhancement-submitCloudEnhancementTasks(      photoAssets: Array<PhotoAsset>,      hasCloudWatermark: boolean,      triggerMode?: int    ): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoAssets | Array & lt;PhotoAsset & gt; | 是 |
| hasCloudWatermark | boolean | 是 |
| triggerMode | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('submitCloudEnhancementTasksDemo');
  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  try {
    let fetchResult = await phAccessHelper.getAssets(photoFetchOptions);
    let asset = await fetchResult.getLastObject();
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    let hasCloudWatermark = true;
    let triggerAuto = 1;
    await cloudEnhancementInstance.submitCloudEnhancementTasks([asset], hasCloudWatermark, triggerAuto);
  } catch (err) {
    console.error(`submitCloudEnhancementTasksDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## syncCloudEnhancementTaskStatus

```TypeScript
syncCloudEnhancementTaskStatus(): Promise<void>
```

同步云增强任务状态。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-CloudEnhancement-syncCloudEnhancementTaskStatus(): Promise<void>--><!--Device-CloudEnhancement-syncCloudEnhancementTaskStatus(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('syncCloudEnhancementTaskStatusDemo');
  try {
    let cloudEnhancementInstance: photoAccessHelper.CloudEnhancement
      = photoAccessHelper.CloudEnhancement.getCloudEnhancementInstance(context);
    await cloudEnhancementInstance.syncCloudEnhancementTaskStatus();
  } catch (err) {
    console.error(`syncCloudEnhancementTaskStatusDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```
