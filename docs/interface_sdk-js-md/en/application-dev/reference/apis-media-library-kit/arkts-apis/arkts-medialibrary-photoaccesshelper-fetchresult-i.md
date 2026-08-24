# FetchResult

FetchResult provides APIs to manage the file retrieval result.

**Since:** 23

<!--Device-photoAccessHelper-interface FetchResult--><!--Device-photoAccessHelper-interface FetchResult-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## close

```TypeScript
close(): void
```

Closes this FetchResult instance to invalidate it. After this instance is released, the APIs in this instance cannot be invoked.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-close(): void--><!--Device-FetchResult-close(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('close');
  try {
    let resultSet: photoAccessHelper.ResultSet = await phAccessHelper.query('SELECT * from Photos');
    resultSet.close();
  } catch (err) {
    console.error(`close failed with error: ${err.code}, ${err.message}`);
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('fetchResultCloseDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    fetchResult.close();
    console.info('close succeed.');
  } catch (err) {
    console.error(`close fail. error: ${err.code}, ${err.message}`);
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('closeDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let fd: number = await photoAsset.open('rw');
    console.info('file fd', fd);
    photoAsset.close(fd, (err) => {
      if (err === undefined) {
        console.info('asset close succeed.');
      } else {
        console.error(`close failed, error: ${err.code}, ${err.message}`);
      }
    });
  } catch (err) {
    console.error(`close failed, error: ${err.code}, ${err.message}`);
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('closeDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let fd = await asset.open('rw');
    console.info('file fd', fd);
    await asset.close(fd);
    console.info('asset close succeed.');
  } catch (err) {
    console.error(`close failed, error: ${err.code}, ${err.message}`);
  }
}
```

## contains

```TypeScript
contains(object: T): Promise<boolean>
```

Checks whether the specified file asset is contained in the result set. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FetchResult-contains(object: T): Promise<boolean>--><!--Device-FetchResult-contains(object: T): Promise<boolean>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| object | T | Yes | Specified file asset. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. **true** indicates that the specified file asset is contained in the result set, and **false** indicates the opposite. |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('fetchResultContainsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let ret: boolean = await fetchResult.contains(asset);
    console.info(`succeed. ${ret}`);
  } catch (err) {
    console.error(`fail. error: ${err.code}, ${err.message}`);
  }
}
```

## getAllObjects

```TypeScript
getAllObjects(callback: AsyncCallback<Array<T>>): void
```

Obtains all the file assets in the result set. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getAllObjects(callback: AsyncCallback<Array<T>>): void--><!--Device-FetchResult-getAllObjects(callback: AsyncCallback<Array<T>>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;T&gt;&gt; | Yes | Callback function. If all file assets in the result set are successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAllObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  fetchResult.getAllObjects((err, photoAssetList) => {
    if (photoAssetList !== undefined) {
      console.info('photoAssetList length: ', photoAssetList.length);
    } else {
      console.error(`photoAssetList failed with err:${err.code}, ${err.message}`);
    }
  });
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAllObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAssetList: Array<photoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
  console.info('photoAssetList length: ', photoAssetList.length);
}
```

## getAllObjects

```TypeScript
getAllObjects(): Promise<Array<T>>
```

Obtains all the file assets in the result set. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getAllObjects(): Promise<Array<T>>--><!--Device-FetchResult-getAllObjects(): Promise<Array<T>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;T&gt;&gt; | Promise used to return an array of all file assets. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

See [getAllObjects](#getallobjects)

## getCount

```TypeScript
getCount(): int
```

Obtains the total number of files in the result set.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getCount(): int--><!--Device-FetchResult-getCount(): int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Total number of files obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getCountDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let fetchCount = fetchResult.getCount();
  console.info('fetchCount = ', fetchCount);
}
```

## getFirstObject

```TypeScript
getFirstObject(callback: AsyncCallback<T>): void
```

Obtains the first file asset in the result set. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getFirstObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getFirstObject(callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes | Callback function. If the first file asset in the result set is successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getFirstObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  fetchResult.getFirstObject((err, photoAsset) => {
    if (photoAsset !== undefined) {
      console.info('photoAsset displayName: ', photoAsset.displayName);
    } else {
      console.error(`photoAsset failed with err:${err.code}, ${err.message}`);
    }
  });
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getFirstObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

## getFirstObject

```TypeScript
getFirstObject(): Promise<T>
```

Obtains the first file asset in the result set. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getFirstObject(): Promise<T>--><!--Device-FetchResult-getFirstObject(): Promise<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; | Promise used to return the first object in the result set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

See [getFirstObject](#getfirstobject)

## getIndex

```TypeScript
getIndex(object: T): Promise<int>
```

Obtains the index of a specified file asset in the result set. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FetchResult-getIndex(object: T): Promise<int>--><!--Device-FetchResult-getIndex(object: T): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| object | T | Yes | Specified file asset. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the result. If the object exists in the result set, the corresponding index is returned. Otherwise, **-1** is returned. |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('fetchResultGetIndexDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let ret: number = await fetchResult.getIndex(asset);
    console.info(`succeed. ${ret}`);
  } catch (err) {
    console.error(`fail. error: ${err.code}, ${err.message}`);
  }
}
```

## getLastObject

```TypeScript
getLastObject(callback: AsyncCallback<T>): void
```

Obtains the last file asset in the result set. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getLastObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getLastObject(callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes | Callback function. If the last file asset in the result set is successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getLastObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  fetchResult.getLastObject((err, photoAsset) => {
    if (photoAsset !== undefined) {
      console.info('photoAsset displayName: ', photoAsset.displayName);
    } else {
      console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
    }
  });
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getLastObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

## getLastObject

```TypeScript
getLastObject(): Promise<T>
```

Obtains the last file asset in the result set. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getLastObject(): Promise<T>--><!--Device-FetchResult-getLastObject(): Promise<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; | Promise used to return the last object in the result set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

See [getLastObject](#getlastobject)

## getNextObject

```TypeScript
getNextObject(callback: AsyncCallback<T>): void
```

Obtains the next file asset in the result set. This API uses an asynchronous callback to return the result.Before using this API, you must use [isAfterLast()](#isafterlast) to check whether the current position is the end of the result set.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getNextObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getNextObject(callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes | Callback function. If the next file asset in the result set is successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getNextObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  await fetchResult.getFirstObject();
  if (!fetchResult.isAfterLast()) {
    fetchResult.getNextObject((err, photoAsset) => {
      if (photoAsset !== undefined) {
        console.info('photoAsset displayName: ', photoAsset.displayName);
      } else {
        console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
      }
    });
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getNextObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  await fetchResult.getFirstObject();
  if (!fetchResult.isAfterLast()) {
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getNextObject();
    console.info('photoAsset displayName: ', photoAsset.displayName);
  }
}
```

## getNextObject

```TypeScript
getNextObject(): Promise<T>
```

Obtains the next file asset in the result set. This API uses a promise to return the result.Before using this API, you must use [isAfterLast()](#isafterlast) to check whether the current position is the end of the result set.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getNextObject(): Promise<T>--><!--Device-FetchResult-getNextObject(): Promise<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; | Promise used to return the next object in the result set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

See [getNextObject](#getnextobject)

## getObjectByPosition

```TypeScript
getObjectByPosition(index: int, callback: AsyncCallback<T>): void
```

Obtains a file asset with the specified index in the result set. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getObjectByPosition(index: int, callback: AsyncCallback<T>): void--><!--Device-FetchResult-getObjectByPosition(index: int, callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the file asset to obtain. The value starts from **0**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes | Callback function. If the file asset with the specified index in the result set is successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getObjectByPositionDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  fetchResult.getObjectByPosition(0, (err, photoAsset) => {
    if (photoAsset !== undefined) {
      console.info('photoAsset displayName: ', photoAsset.displayName);
    } else {
      console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
    }
  });
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getObjectByPositionDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  if (fetchResult === undefined) {
    console.error('fetchResult is undefined');
    return;
  }
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getObjectByPosition(0);
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

## getObjectByPosition

```TypeScript
getObjectByPosition(index: int): Promise<T>
```

Obtains a file asset with the specified index in the result set. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getObjectByPosition(index: int): Promise<T>--><!--Device-FetchResult-getObjectByPosition(index: int): Promise<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the file asset to obtain. The value starts from **0**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; | Promise used to return the file asset obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

See [getObjectByPosition](#getobjectbyposition)

## getObjectsByIndexSet

```TypeScript
getObjectsByIndexSet(indexSet: int[]): Promise<T[]>
```

Obtains the file asset array corresponding to the specified index set in the result set. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FetchResult-getObjectsByIndexSet(indexSet: int[]): Promise<T[]>--><!--Device-FetchResult-getObjectsByIndexSet(indexSet: int[]): Promise<T[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indexSet | int[] | Yes | Specified index set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T[]&gt; | Promise object, which returns the file asset array corresponding to the specified index set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | The scenario parameter verification fails. Possible causes: <br>1.The indexSet is null, undefined or empty. <br>2.The indexSet length is bigger than 500. <br>3.The max value of indexSet is equal or bigger than the fetch result length. <br>4.The min value of indexSet is less than 0. |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('fetchResultGetObjectsByIndexSetDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let indexSet: number[] = [0, 1];
    let ret: photoAccessHelper.PhotoAsset[] = await fetchResult.getObjectsByIndexSet(indexSet);
    console.info(`succeed. ${ret.length}`);
  } catch (err) {
    console.error(`fail. error: ${err.code}, ${err.message}`);
  }
}
```

## isAfterLast

```TypeScript
isAfterLast(): boolean
```

Checks whether the cursor is in the last row of the result set.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-isAfterLast(): boolean--><!--Device-FetchResult-isAfterLast(): boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** is returned if the cursor is in the last row of the result set; **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let fetchCount = fetchResult.getCount();
  console.info('count:' + fetchCount);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
  if (fetchResult.isAfterLast()) {
    console.info('photoAsset isAfterLast displayName = ', photoAsset.displayName);
  } else {
    console.info('photoAsset not isAfterLast.');
  }
}
```

