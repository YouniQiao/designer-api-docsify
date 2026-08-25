# FetchResult

Provides APIs to manage the file retrieval result.

**Inheritance/Implementation:** FetchResult extends lang.ISendable

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { sendablePhotoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## close

```TypeScript
close(): void
```

Closes this FetchResult instance to invalidate it. After this instance is closed, the APIs in this instance cannot be invoked.

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Error codes:**

| Error Code ID |
| --- |
| 14000011 |

## getAllObjects

```TypeScript
getAllObjects(): Promise<Array<T>>
```

Obtains all the file assets in the result set. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;T & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 14000011 |

## getCount

```TypeScript
getCount(): number
```

Obtains the total number of files in the result set.

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 14000011 |

## getFirstObject

```TypeScript
getFirstObject(): Promise<T>
```

Obtains the first asset in the result set. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 14000011 |

## getLastObject

```TypeScript
getLastObject(): Promise<T>
```

Obtains the last asset in the result set. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 14000011 |

## getNextObject

```TypeScript
getNextObject(): Promise<T>
```

Obtains the next asset in the result set. This API uses a promise to return the result.Before using this API, you must use [isAfterLast()](#isafterlast) to check whether the current position is the end of the result set.

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 14000011 |

## getObjectByPosition

```TypeScript
getObjectByPosition(index: number): Promise<T>
```

Obtains the asset with the given index in the result set. This API uses a promise to return the result.

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000011 |

## isAfterLast

```TypeScript
isAfterLast(): boolean
```

Checks whether the cursor is in the last row of the result set.

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 14000011 |
