# FetchResult

FetchResult provides APIs to manage the file retrieval result.

**Since:** 10

<!--Device-photoAccessHelper-interface FetchResult<T>--><!--Device-photoAccessHelper-interface FetchResult<T>-End-->

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

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-close(): void--><!--Device-FetchResult-close(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| object | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## getAllObjects

```TypeScript
getAllObjects(callback: AsyncCallback<Array<T>>): void
```

Obtains all the file assets in the result set. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getAllObjects(callback: AsyncCallback<Array<T>>): void--><!--Device-FetchResult-getAllObjects(callback: AsyncCallback<Array<T>>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;T&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getAllObjects

```TypeScript
getAllObjects(): Promise<Array<T>>
```

Obtains all the file assets in the result set. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getAllObjects(): Promise<Array<T>>--><!--Device-FetchResult-getAllObjects(): Promise<Array<T>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;T & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getCount

```TypeScript
getCount(): number
```

Obtains the total number of files in the result set.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getCount(): int--><!--Device-FetchResult-getCount(): int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getFirstObject

```TypeScript
getFirstObject(callback: AsyncCallback<T>): void
```

Obtains the first file asset in the result set. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getFirstObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getFirstObject(callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getFirstObject

```TypeScript
getFirstObject(): Promise<T>
```

Obtains the first file asset in the result set. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getFirstObject(): Promise<T>--><!--Device-FetchResult-getFirstObject(): Promise<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getIndex

```TypeScript
getIndex(object: T): Promise<number>
```

Obtains the index of a specified file asset in the result set. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FetchResult-getIndex(object: T): Promise<int>--><!--Device-FetchResult-getIndex(object: T): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| object | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getLastObject

```TypeScript
getLastObject(callback: AsyncCallback<T>): void
```

Obtains the last file asset in the result set. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getLastObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getLastObject(callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getLastObject

```TypeScript
getLastObject(): Promise<T>
```

Obtains the last file asset in the result set. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getLastObject(): Promise<T>--><!--Device-FetchResult-getLastObject(): Promise<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getNextObject

```TypeScript
getNextObject(callback: AsyncCallback<T>): void
```

Obtains the next file asset in the result set. This API uses an asynchronous callback to return the result.

Before using this API, you must use [isAfterLast()](#isAfterLast) to check whether the current position is the end of the result set.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getNextObject(callback: AsyncCallback<T>): void--><!--Device-FetchResult-getNextObject(callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getNextObject

```TypeScript
getNextObject(): Promise<T>
```

Obtains the next file asset in the result set. This API uses a promise to return the result.

Before using this API, you must use [isAfterLast()](#isAfterLast) to check whether the current position is the end of the result set.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getNextObject(): Promise<T>--><!--Device-FetchResult-getNextObject(): Promise<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getObjectByPosition

```TypeScript
getObjectByPosition(index: number, callback: AsyncCallback<T>): void
```

Obtains a file asset with the specified index in the result set. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getObjectByPosition(index: int, callback: AsyncCallback<T>): void--><!--Device-FetchResult-getObjectByPosition(index: int, callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getObjectByPosition

```TypeScript
getObjectByPosition(index: number): Promise<T>
```

Obtains a file asset with the specified index in the result set. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-getObjectByPosition(index: int): Promise<T>--><!--Device-FetchResult-getObjectByPosition(index: int): Promise<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |

## getObjectsByIndexSet

```TypeScript
getObjectsByIndexSet(indexSet: number[]): Promise<T[]>
```

Obtains the file asset array corresponding to the specified index set in the result set. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FetchResult-getObjectsByIndexSet(indexSet: int[]): Promise<T[]>--><!--Device-FetchResult-getObjectsByIndexSet(indexSet: int[]): Promise<T[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| indexSet | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## getRangeObjects

```TypeScript
getRangeObjects(index: number, offset: number): Promise<T[]>
```

Obtains the file asset array of a specified length (second parameter) from the specified index (first parameter) in the result set. This API uses a promise to return the result.

**Since:** 23

<!--Device-FetchResult-getRangeObjects(index: int, offset: int): Promise<T[]>--><!--Device-FetchResult-getRangeObjects(index: int, offset: int): Promise<T[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## isAfterLast

```TypeScript
isAfterLast(): boolean
```

Checks whether the cursor is in the last row of the result set.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FetchResult-isAfterLast(): boolean--><!--Device-FetchResult-isAfterLast(): boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000011 |
