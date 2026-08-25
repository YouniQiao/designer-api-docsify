# FetchResult (System API)

Provides APIs to manage the file retrieval result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [FetchResult](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## close

```TypeScript
close(): void
```

Releases and invalidates the **FetchFileResult** instance. After this instance is released, the APIs in this instance cannot be invoked.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [close](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#close)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## getAllObject

```TypeScript
getAllObject(callback: AsyncCallback<Array<T>>): void
```

Obtains all the file assets in the result set. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getAllObjects](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getallobjects)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;T&gt;&gt; | Yes |

## getAllObject

```TypeScript
getAllObject(): Promise<Array<T>>
```

Obtains all the file assets in the result set. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getAllObjects](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getallobjects)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;T & gt; & gt; |

## getCount

```TypeScript
getCount(): number
```

Obtains the total number of files in the result set.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getCount](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getcount)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getFirstObject

```TypeScript
getFirstObject(callback: AsyncCallback<T>): void
```

Obtains the first file asset in the result set. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getFirstObject](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getfirstobject)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes |

## getFirstObject

```TypeScript
getFirstObject(): Promise<T>
```

Obtains the first file asset in the result set. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getFirstObject](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getfirstobject)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

## getLastObject

```TypeScript
getLastObject(callback: AsyncCallback<T>): void
```

Obtains the last file asset in the result set. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getLastObject](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getlastobject)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes |

## getLastObject

```TypeScript
getLastObject(): Promise<T>
```

Obtains the last file asset in the result set. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getLastObject](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getlastobject)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

## getNextObject

```TypeScript
getNextObject(callback: AsyncCallback<T>): void
```

Obtains the next file asset in the result set. This API uses an asynchronous callback to return the result.Before using this API, you must use [isAfterLast()](#isafterlast) to check whether the current position is the end of the result set.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getNextObject](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getnextobject)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes |

## getNextObject

```TypeScript
getNextObject(): Promise<T>
```

Obtains the next file asset in the result set. This API uses a promise to return the result.Before using this API, you must use [isAfterLast()](#isafterlast) to check whether the current position is the end of the result set.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getNextObject](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getnextobject)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

## getPositionObject

```TypeScript
getPositionObject(index: number, callback: AsyncCallback<T>): void
```

Obtains a file asset with the specified index in the result set. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getObjectByPosition](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getobjectbyposition)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getPositionObject

```TypeScript
getPositionObject(index: number): Promise<T>
```

Obtains a file asset with the specified index in the result set. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getObjectByPosition](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#getobjectbyposition)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

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

## isAfterLast

```TypeScript
isAfterLast(): boolean
```

Checks whether the cursor is in the last row of the result set.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [isAfterLast](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchresult-i.md#isafterlast)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
