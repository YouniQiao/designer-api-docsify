# PhotoAssetCustomRecordManager (System API)

Provides APIs for custom user behavior recording for Gallery.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-class PhotoAssetCustomRecordManager--><!--Device-photoAccessHelper-class PhotoAssetCustomRecordManager-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
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
[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md#PhotoAssetCustomRecord). This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetCustomRecordManager-addLcdJumpCount(ids: Array<int>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-addLcdJumpCount(ids: Array<int>): Promise<Array<int>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ids | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | Yes | Array of file IDs in [PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md#PhotoAssetCustomRecord). |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the file ID in the custom user behavior recordings that fail to be updated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |
| [23800151](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The ids list is empty. &lt;br&gt;2. The number of ids lists exceeds 500. |

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
[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md#PhotoAssetCustomRecord). This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetCustomRecordManager-addShareCount(ids: Array<int>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-addShareCount(ids: Array<int>): Promise<Array<int>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ids | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | Yes | Array of file IDs in [PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md#PhotoAssetCustomRecord). |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the file ID in the custom user behavior recordings that fail to be updated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |
| [23800151](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The ids list is empty. 2. The number of ids lists exceeds 500. |

## createCustomRecords

```TypeScript
createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>
```

Adds custom user behavior recordings. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetCustomRecordManager-createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>--><!--Device-PhotoAssetCustomRecordManager-createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customRecords | Array&lt;[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md)&gt; | Yes | Custom user behavior recordings. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |
| [23800151](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The value range of mandatory parameters in photoAssetCustomRecord does not meet the requirements. &lt;br&gt;2. The transferred record already exists. 3. The number of transferred records exceeds 200. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager--><!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |

**Return value:**

| Type | Description |
| --- | --- |
| [PhotoAssetCustomRecordManager](arkts-medialibrary-photoaccesshelper-photoassetcustomrecordmanager-c-sys.md) | Custom user behavior recording instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800107](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800107-context-is-empty-or-invalid) | Context is invalid |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |

## Examples

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

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager | null--><!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |

**Return value:**

| Type | Description |
| --- | --- |
| [PhotoAssetCustomRecordManager](arkts-medialibrary-photoaccesshelper-photoassetcustomrecordmanager-c-sys.md) | Returns media asset custom record manager instance if operation fails, return null. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800107](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800107-context-is-empty-or-invalid) | Context is invalid @static |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |

## getCustomRecords

```TypeScript
getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>
```

Obtains custom user behavior recordings based on retrieval options. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetCustomRecordManager-getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>--><!--Device-PhotoAssetCustomRecordManager-getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| optionCheck | FetchOptions | Yes | Retrieval options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FetchResult&lt;[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md)&gt;&gt; | Promise used to return the collection of custom user behavior recordings. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |
| [23800151](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scenario parameters fail to pass the verification.Possible causes: 1. The filter criteria or fetchColumns that are not supported by options are transferred. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetCustomRecordManager-removeCustomRecords(optionCheck: FetchOptions): Promise<void>--><!--Device-PhotoAssetCustomRecordManager-removeCustomRecords(optionCheck: FetchOptions): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| optionCheck | FetchOptions | Yes | Retrieval options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |
| [23800151](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The filter criteria or fetchColumns that are not supported by options are transferred. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetCustomRecordManager-setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<int>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customRecords | Array&lt;[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md)&gt; | Yes | Custom user behavior recordings. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the file ID in the custom user behavior recordings that fail to be updated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |
| [23800151](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The value range of mandatory parameters in photoAssetCustomRecord does not meet the requirements. &lt;br&gt;2. The number of transferred records exceeds 200. |

## Examples

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

