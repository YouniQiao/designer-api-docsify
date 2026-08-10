# PhotoAssetCustomRecordManager（系统接口）

Provides APIs for custom user behavior recording for Gallery.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-class PhotoAssetCustomRecordManager--><!--Device-photoAccessHelper-class PhotoAssetCustomRecordManager-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## addLcdJumpCount

ArkTS-Dyn:
```TypeScript
addLcdJumpCount(ids: Array<number>): Promise<Array<number>>
```

ArkTS-Sta:
```TypeScript
addLcdJumpCount(ids: Array<int>): Promise<Array<int>>
```

Increases the value of **LcdJumpCount** by 1 for the data in the database based on **fileId** in   
[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md). This API uses a promise to return the result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetCustomRecordManager-addLcdJumpCount(ids: Array<int>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-addLcdJumpCount(ids: Array<int>): Promise<Array<int>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | 是 | Array of file IDs in [PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the file ID in the custom user behavior recordings that fail to be updated. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The ids list is empty. &lt;br&gt;2. The number of ids lists exceeds 500. |

## addShareCount

ArkTS-Dyn:
```TypeScript
addShareCount(ids: Array<number>): Promise<Array<number>>
```

ArkTS-Sta:
```TypeScript
addShareCount(ids: Array<int>): Promise<Array<int>>
```

Increases the value of **shareCount** by 1 for the data in the database based on **fileId** in   
[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md). This API uses a promise to return the result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetCustomRecordManager-addShareCount(ids: Array<int>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-addShareCount(ids: Array<int>): Promise<Array<int>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | 是 | Array of file IDs in [PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the file ID in the custom user behavior recordings that fail to be updated. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The ids list is empty. 2. The number of ids lists exceeds 500. |

## createCustomRecords

```TypeScript
createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>
```

Adds custom user behavior recordings. This API uses a promise to return the result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetCustomRecordManager-createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>--><!--Device-PhotoAssetCustomRecordManager-createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customRecords | Array&lt;PhotoAssetCustomRecord&gt; | 是 | Custom user behavior recordings. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The value range of mandatory parameters in photoAssetCustomRecord does not meet the requirements. &lt;br&gt;2. The transferred record already exists. 3. The number of transferred records exceeds 200. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(context: Context) {
  console.info('createCustomRecords');
  let crManager = photoAccessHelper.PhotoAssetCustomRecordManager.getCustomRecordManagerInstance(context);
  let crArray:Array<photoAccessHelper.PhotoAssetCustomRecord> = [
    {fileId:1,shareCount:1,lcdJumpCount:1}
  ];
  crManager.createCustomRecords(crArray).then(() => {
    console.info('createCustomRecords successful');
  }).catch((err: BusinessError) => {
    console.error(`createCustomRecords fail with error: ${err.code}, ${err.message}`);
  });
}
```

## getCustomRecordManagerInstance

```TypeScript
static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager
```

Obtains an instance of custom user behavior recording for Gallery.

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

<!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager--><!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | 是 | Context of the ability instance. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoAssetCustomRecordManager](arkts-medialibrary-photoaccesshelper-photoassetcustomrecordmanager-c-sys.md) | Custom user behavior recording instance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800107 | Context is invalid |
| 202 | Called by non-system application |

## 示例

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(context: Context) {
  console.info('getCustomRecordManagerInstance');
  try {
    let crManager = photoAccessHelper.PhotoAssetCustomRecordManager.getCustomRecordManagerInstance(context);
  } catch(err) {
    console.error(`getCustomRecordManagerInstance failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getCustomRecordManagerInstance

```TypeScript
static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager | null
```

Get media asset custom record manager instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager | null--><!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | 是 | Context of the ability instance. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoAssetCustomRecordManager](arkts-medialibrary-photoaccesshelper-photoassetcustomrecordmanager-c-sys.md) | Returns media asset custom record manager instance if operation fails, return null. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800107 | Context is invalid @static |
| 202 | Called by non-system application |

## getCustomRecords

```TypeScript
getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>
```

Obtains custom user behavior recordings based on retrieval options. This API uses a promise to return the result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetCustomRecordManager-getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>--><!--Device-PhotoAssetCustomRecordManager-getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| optionCheck | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 | Retrieval options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;FetchResult&lt;PhotoAssetCustomRecord&gt;&gt; | Promise used to return the collection of custom user behavior recordings. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | Scenario parameters fail to pass the verification.Possible causes: 1. The filter criteria or fetchColumns that are not supported by options are transferred. |

## 示例

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(context: Context) {
  console.info('getCustomRecords');
  let crManager = photoAccessHelper.PhotoAssetCustomRecordManager.getCustomRecordManagerInstance(context);
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('file_id', 1);
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  crManager.getCustomRecords(fetchOption).then(async (fetchResult) => {
    let record = await fetchResult.getFirstObject();
    console.info('record file id is ' + record.fileId);
  }).catch((err: BusinessError) => {
    console.error('getCustomRecords fail with error: ${err.code}, ${err.message}');
  });
}
```

## removeCustomRecords

```TypeScript
removeCustomRecords(optionCheck: FetchOptions): Promise<void>
```

Removes custom user behavior recordings based on retrieval options. This API uses a promise to return the result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetCustomRecordManager-removeCustomRecords(optionCheck: FetchOptions): Promise<void>--><!--Device-PhotoAssetCustomRecordManager-removeCustomRecords(optionCheck: FetchOptions): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| optionCheck | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 | Retrieval options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The filter criteria or fetchColumns that are not supported by options are transferred. |

## 示例

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(context: Context) {
  console.info('removeCustomRecords');
  let crManager = photoAccessHelper.PhotoAssetCustomRecordManager.getCustomRecordManagerInstance(context);
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('file_id', 1);
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  crManager.removeCustomRecords(fetchOption).then(() => {
    console.info('removeCustomRecords successful');
  }).catch((err: BusinessError) => {
    console.error(`removeCustomRecords fail with error: ${err.code}, ${err.message}`);
  });
}
```

## setCustomRecords

ArkTS-Dyn:
```TypeScript
setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<number>>
```

ArkTS-Sta:
```TypeScript
setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<int>>
```

Updates the existing database fields based on custom user behavior recordings. This API uses a promise to return the result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetCustomRecordManager-setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<int>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customRecords | Array&lt;PhotoAssetCustomRecord&gt; | 是 | Custom user behavior recordings. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the file ID in the custom user behavior recordings that fail to be updated. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The value range of mandatory parameters in photoAssetCustomRecord does not meet the requirements. &lt;br&gt;2. The number of transferred records exceeds 200. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(context: Context) {
  console.info('setCustomRecords');
  let crManager = photoAccessHelper.PhotoAssetCustomRecordManager.getCustomRecordManagerInstance(context);
  let UpdateArray: Array<photoAccessHelper.PhotoAssetCustomRecord> = [
    {fileId:1,shareCount:2,lcdJumpCount:3},
    {fileId:2,shareCount:2,lcdJumpCount:3}
  ];
  crManager.setCustomRecords(UpdateArray).then((failIds) => {
    console.info('setCustomRecords successful');
  }).catch((err: BusinessError) => {
    console.error('setCustomRecords file with err: ${err.code}, ${err.message}');
  });
}
```

