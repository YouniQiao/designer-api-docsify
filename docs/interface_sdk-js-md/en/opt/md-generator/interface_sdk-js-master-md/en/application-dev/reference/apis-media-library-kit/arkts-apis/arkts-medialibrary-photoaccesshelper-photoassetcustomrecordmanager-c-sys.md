# PhotoAssetCustomRecordManager (System API)

Provides APIs for custom user behavior recording for Gallery.

**Since:** 20

<!--Device-photoAccessHelper-class PhotoAssetCustomRecordManager--><!--Device-photoAccessHelper-class PhotoAssetCustomRecordManager-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## addLcdJumpCount

```TypeScript
addLcdJumpCount(ids: Array<number>): Promise<Array<number>>
```

Increases the value of **LcdJumpCount** by 1 for the data in the database based on **fileId** in   
[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md#PhotoAssetCustomRecord). This API uses a promise to return the result.

**Since:** 20

<!--Device-PhotoAssetCustomRecordManager-addLcdJumpCount(ids: Array<int>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-addLcdJumpCount(ids: Array<int>): Promise<Array<int>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ids | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## addShareCount

```TypeScript
addShareCount(ids: Array<number>): Promise<Array<number>>
```

Increases the value of **shareCount** by 1 for the data in the database based on **fileId** in   
[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md#PhotoAssetCustomRecord). This API uses a promise to return the result.

**Since:** 20

<!--Device-PhotoAssetCustomRecordManager-addShareCount(ids: Array<int>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-addShareCount(ids: Array<int>): Promise<Array<int>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ids | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## createCustomRecords

```TypeScript
createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>
```

Adds custom user behavior recordings. This API uses a promise to return the result.

**Since:** 20

<!--Device-PhotoAssetCustomRecordManager-createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>--><!--Device-PhotoAssetCustomRecordManager-createCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customRecords | Array&lt;[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

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

<!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager--><!--Device-PhotoAssetCustomRecordManager-static getCustomRecordManagerInstance(context: Context): PhotoAssetCustomRecordManager-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PhotoAssetCustomRecordManager](arkts-medialibrary-photoaccesshelper-photoassetcustomrecordmanager-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [23800107](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800107-context-is-empty-or-invalid) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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

## getCustomRecords

```TypeScript
getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>
```

Obtains custom user behavior recordings based on retrieval options. This API uses a promise to return the result.

**Since:** 20

<!--Device-PhotoAssetCustomRecordManager-getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>--><!--Device-PhotoAssetCustomRecordManager-getCustomRecords(optionCheck: FetchOptions): Promise<FetchResult<PhotoAssetCustomRecord>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| optionCheck | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

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

<!--Device-PhotoAssetCustomRecordManager-removeCustomRecords(optionCheck: FetchOptions): Promise<void>--><!--Device-PhotoAssetCustomRecordManager-removeCustomRecords(optionCheck: FetchOptions): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| optionCheck | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

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

```TypeScript
setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<number>>
```

Updates the existing database fields based on custom user behavior recordings. This API uses a promise to return the result.

**Since:** 20

<!--Device-PhotoAssetCustomRecordManager-setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<int>>--><!--Device-PhotoAssetCustomRecordManager-setCustomRecords(customRecords: Array<PhotoAssetCustomRecord>): Promise<Array<int>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customRecords | Array&lt;[PhotoAssetCustomRecord](arkts-medialibrary-photoaccesshelper-photoassetcustomrecord-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

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
