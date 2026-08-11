# truncate

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## truncate

```TypeScript
declare function truncate(file: string | number, len?: number): Promise<void>
```

Truncates a file. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function truncate(file: string | number, len?: number): Promise<void>--><!--Device-unnamed-declare function truncate(file: string | number, len?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| file | string \| number | Yes |
| len | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900023 |
| 13900018 |
| 13900019 |
| 13900030 |
| 13900024 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |


## truncate

```TypeScript
declare function truncate(file: string | number, callback: AsyncCallback<void>): void
```

Truncates a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function truncate(file: string | number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function truncate(file: string | number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| file | string \| number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900023 |
| 13900018 |
| 13900019 |
| 13900030 |
| 13900024 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |


## truncate

```TypeScript
declare function truncate(file: string | number, len: number, callback: AsyncCallback<void>): void
```

Truncates a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function truncate(file: string | number, len: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function truncate(file: string | number, len: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| file | string \| number | Yes |
| len | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900023 |
| 13900018 |
| 13900019 |
| 13900030 |
| 13900024 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |
