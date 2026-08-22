# FetchResult

文件检索结果集。

**起始版本：** 23

<!--Device-photoAccessHelper-interface FetchResult--><!--Device-photoAccessHelper-interface FetchResult-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## close

```TypeScript
close(): void
```

释放FetchResult实例并使其失效，释放后无法再调用其他方法。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-close(): void--><!--Device-FetchResult-close(): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

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

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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
    let fd: number = await photoAsset.getReadOnlyFd();
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

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

判断文件检索结果中是否包含指定的文件资产。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-contains(object: T): Promise<boolean>--><!--Device-FetchResult-contains(object: T): Promise<boolean>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | T | 是 | 指定的文件资产。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示指定的文件资产在文件检索结果中；返回false表示指定的文件资产不在文件检索结果中。 |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

获取文件检索结果中的所有文件资产。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getAllObjects(callback: AsyncCallback<Array<T>>): void--><!--Device-FetchResult-getAllObjects(callback: AsyncCallback<Array<T>>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;T&gt;&gt; | 是 | 回调函数。当获取结果集中的所有文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

获取文件检索结果中的所有文件资产。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getAllObjects(): Promise<Array<T>>--><!--Device-FetchResult-getAllObjects(): Promise<Array<T>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;T&gt;&gt; | Promise对象，返回所有文件资产的数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

参见 [getAllObjects](#getallobjects)

## getCount

```TypeScript
getCount(): int
```

获取文件检索结果中的文件总数。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getCount(): int--><!--Device-FetchResult-getCount(): int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 检索到的文件总数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

获取文件检索结果中的第一个文件资产。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getFirstObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getFirstObject(callback: AsyncCallback<T>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 | 回调函数。当获取结果集中的第一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

获取文件检索结果中的第一个文件资产。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getFirstObject(): Promise<T>--><!--Device-FetchResult-getFirstObject(): Promise<T>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T&gt; | Promise对象，返回结果集中第一个对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

参见 [getFirstObject](#getfirstobject)

## getIndex

```TypeScript
getIndex(object: T): Promise<int>
```

获取指定文件资产在文件检索结果中的索引。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getIndex(object: T): Promise<int>--><!--Device-FetchResult-getIndex(object: T): Promise<int>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | T | 是 | 指定的文件资产。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;int&gt; | Promise对象，返回查询结果。如果对象在文件检索结果中则返回对应的索引，不存在则返回-1。 |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

获取文件检索结果中的最后一个文件资产。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getLastObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getLastObject(callback: AsyncCallback<T>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 | 回调函数。当获取结果集中的最后一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

获取文件检索结果中的最后一个文件资产。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getLastObject(): Promise<T>--><!--Device-FetchResult-getLastObject(): Promise<T>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T&gt; | Promise对象，返回结果集中的最后一个对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

参见 [getLastObject](#getlastobject)

## getNextObject

```TypeScript
getNextObject(callback: AsyncCallback<T>): void
```

获取文件检索结果中的下一个文件资产。使用callback异步回调。

在调用此方法之前，必须使用[isAfterLast()](#isafterlast)来检查当前位置是否为最后一行。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getNextObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getNextObject(callback: AsyncCallback<T>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 | 回调函数。当获取结果集中的下一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

获取文件检索结果中的下一个文件资产。使用Promise异步回调。

在调用此方法之前，必须使用[isAfterLast()](#isafterlast)来检查当前位置是否为最后一行。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getNextObject(): Promise<T>--><!--Device-FetchResult-getNextObject(): Promise<T>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T&gt; | Promise对象，返回结果集中下一个对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

参见 [getNextObject](#getnextobject)

## getObjectByPosition

```TypeScript
getObjectByPosition(index: int, callback: AsyncCallback<T>): void
```

获取文件检索结果中具有指定索引的文件资产。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getObjectByPosition(index: int, callback: AsyncCallback<T>): void--><!--Device-FetchResult-getObjectByPosition(index: int, callback: AsyncCallback<T>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 要获取的文件的索引，从0开始。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 | 回调函数。当获取结果集中指定索引的文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

获取文件检索结果中指定索引的文件资产。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getObjectByPosition(index: int): Promise<T>--><!--Device-FetchResult-getObjectByPosition(index: int): Promise<T>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 要获取的文件的索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T&gt; | Promise对象，返回结果集中指定索引的一个对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

参见 [getObjectByPosition](#getobjectbyposition)

## getObjectsByIndexSet

```TypeScript
getObjectsByIndexSet(indexSet: int[]): Promise<T[]>
```

获取文件检索结果中指定索引集合对应的文件资产数组。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getObjectsByIndexSet(indexSet: int[]): Promise<T[]>--><!--Device-FetchResult-getObjectsByIndexSet(indexSet: int[]): Promise<T[]>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indexSet | int[] | 是 | 指定的索引集合。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T[]&gt; | Promise对象，返回指定索引集合所对应的文件资产数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) | The scenario parameter verification fails. Possible causes: <br>1.The indexSet is null, undefined or empty. <br>2.The indexSet length is bigger than 500. <br>3.The max value of indexSet is equal or bigger than the fetch result length. <br>4.The min value of indexSet is less than 0. |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

检查结果集是否指向最后一行。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-isAfterLast(): boolean--><!--Device-FetchResult-isAfterLast(): boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当结果集指向最后一行时返回true，否则返回false。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument |
| 14000011 | System inner fail |

**示例**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

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

