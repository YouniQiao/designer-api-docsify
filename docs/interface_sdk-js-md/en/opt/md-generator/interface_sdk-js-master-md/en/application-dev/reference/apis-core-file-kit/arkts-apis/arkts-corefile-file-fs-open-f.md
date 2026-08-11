# open

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## open

```TypeScript
declare function open(path: string, mode?: number): Promise<File>
```

Opens a file or directory. This API uses a promise to return the result. This API supports the use of a URI.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function open(path: string, mode?: number): Promise<File>--><!--Device-unnamed-declare function open(path: string, mode?: number): Promise<File>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | number | No | [Mode](../../../reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for opening the file or directory. You must specify one of the following options. By default, the file is opened in read-only mode.&lt;br&gt;- **OpenMode.READ_ONLY(0o0)**: Open the file in read-only mode.&lt;br&gt;- **OpenMode.WRITE_ONLY(0o1)**: Open the file in write-only mode.&lt;br&gt;- **OpenMode.READ_WRITE(0o2)**: Open the file in read/write mode.&lt;br&gt;You can also specify the following options, separated by a bitwise OR operator (\|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;File&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900044 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |


## open

```TypeScript
declare function open(path: string, callback: AsyncCallback<File>): void
```

Opens a file or directory. This API uses an asynchronous callback to return the result. This API supports the use of a URI.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function open(path: string, callback: AsyncCallback<File>): void--><!--Device-unnamed-declare function open(path: string, callback: AsyncCallback<File>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;File&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |


## open

```TypeScript
declare function open(path: string, mode: number, callback: AsyncCallback<File>): void
```

Opens a file or directory with the specified mode. This API uses an asynchronous callback to return the result.

This API supports the use of a URI.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function open(path: string, mode: number, callback: AsyncCallback<File>): void--><!--Device-unnamed-declare function open(path: string, mode: number, callback: AsyncCallback<File>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | number | Yes | [Mode](../../../reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for opening the file or directory. You must specify one of the following options. By default, the file is opened in read-only mode.&lt;br&gt;- **OpenMode.READ_ONLY(0o0)**: Open the file in read-only mode.&lt;br&gt;- **OpenMode.WRITE_ONLY(0o1)**: Open the file in write-only mode.&lt;br&gt;- **OpenMode.READ_WRITE(0o2)**: Open the file in read/write mode.&lt;br&gt;You can also specify the following options, separated by a bitwise OR operator (\|
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;File&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |
