# FetchResult

文件检索结果集。

**起始版本：** 23

<!--Device-photoAccessHelper-interface FetchResult--><!--Device-photoAccessHelper-interface FetchResult-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
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

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

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

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | T | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

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

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;T&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

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

| 类型 |
| --- |
| Promise & lt;Array & lt;T & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

## getCount

```TypeScript
getCount(): number
```

获取文件检索结果中的文件总数。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getCount(): int--><!--Device-FetchResult-getCount(): int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

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

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

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

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

## getIndex

```TypeScript
getIndex(object: T): Promise<number>
```

获取指定文件资产在文件检索结果中的索引。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getIndex(object: T): Promise<int>--><!--Device-FetchResult-getIndex(object: T): Promise<int>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | T | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

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

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

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

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

## getNextObject

```TypeScript
getNextObject(callback: AsyncCallback<T>): void
```

获取文件检索结果中的下一个文件资产。使用callback异步回调。 在调用此方法之前，必须使用[isAfterLast()](#isafterlast)来检查当前位置是否为最后一行。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getNextObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getNextObject(callback: AsyncCallback<T>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

## getNextObject

```TypeScript
getNextObject(): Promise<T>
```

获取文件检索结果中的下一个文件资产。使用Promise异步回调。 在调用此方法之前，必须使用[isAfterLast()](#isafterlast)来检查当前位置是否为最后一行。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getNextObject(): Promise<T>--><!--Device-FetchResult-getNextObject(): Promise<T>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

## getObjectByPosition

```TypeScript
getObjectByPosition(index: number, callback: AsyncCallback<T>): void
```

获取文件检索结果中具有指定索引的文件资产。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getObjectByPosition(index: int, callback: AsyncCallback<T>): void--><!--Device-FetchResult-getObjectByPosition(index: int, callback: AsyncCallback<T>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

## getObjectByPosition

```TypeScript
getObjectByPosition(index: number): Promise<T>
```

获取文件检索结果中指定索引的文件资产。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getObjectByPosition(index: int): Promise<T>--><!--Device-FetchResult-getObjectByPosition(index: int): Promise<T>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |

## getObjectsByIndexSet

```TypeScript
getObjectsByIndexSet(indexSet: number[]): Promise<T[]>
```

获取文件检索结果中指定索引集合对应的文件资产数组。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-FetchResult-getObjectsByIndexSet(indexSet: int[]): Promise<T[]>--><!--Device-FetchResult-getObjectsByIndexSet(indexSet: int[]): Promise<T[]>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| indexSet | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;T[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

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

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000011 |
