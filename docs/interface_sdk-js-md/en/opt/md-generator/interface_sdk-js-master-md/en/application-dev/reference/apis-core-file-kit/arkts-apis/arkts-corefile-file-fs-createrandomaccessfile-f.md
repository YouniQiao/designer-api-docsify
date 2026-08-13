# createRandomAccessFile

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## createRandomAccessFile

```TypeScript
declare function createRandomAccessFile(file: string | File, mode?: number,
  options?: RandomAccessFileOptions): Promise<RandomAccessFile>
```

Creates a **RandomAccessFile** instance based on the specified file path or file object. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function createRandomAccessFile(file: string | File, mode?: number,  options?: RandomAccessFileOptions): Promise<RandomAccessFile>--><!--Device-unnamed-declare function createRandomAccessFile(file: string | File, mode?: number,  options?: RandomAccessFileOptions): Promise<RandomAccessFile>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| [File](arkts-corefile-file-fs-file-i.md) | Yes |
| mode | number | No | Mode for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified: & lt;br & gt;- **OpenMode.READ_ONLY(0o0)**: Create the file in read-only mode. This is the default value. & lt;br & gt;- **OpenMode.WRITE_ONLY(0o1)**: Create the file in write-only mode. & lt;br & gt;- **OpenMode.READ_WRITE(0o2)**: Create the file in read/write mode. & lt;br & gt;You can also specify the following options, separated by a bitwise OR operator (\ |
| options | [RandomAccessFileOptions](arkts-corefile-file-fs-randomaccessfileoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RandomAccessFile](arkts-corefile-file-fs-randomaccessfile-i.md)&gt; |

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


## createRandomAccessFile

```TypeScript
declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void
```

Creates a **RandomAccessFile** object in read-only mode based on a file path or file object. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void--><!--Device-unnamed-declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| [File](arkts-corefile-file-fs-file-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RandomAccessFile](arkts-corefile-file-fs-randomaccessfile-i.md)&gt; | Yes |

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


## createRandomAccessFile

```TypeScript
declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void
```

Creates a **RandomAccessFile** instance based on a file path or file object. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void--><!--Device-unnamed-declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| [File](arkts-corefile-file-fs-file-i.md) | Yes |
| mode | number | Yes | Mode for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified: & lt;br & gt;- **OpenMode.READ_ONLY(0o0)**: Create the file in read-only mode. This is the default value. & lt;br & gt;- **OpenMode.WRITE_ONLY(0o1)**: Create the file in write-only mode. & lt;br & gt;- **OpenMode.READ_WRITE(0o2)**: Create the file in read/write mode. & lt;br & gt;You can also specify the following options, separated by a bitwise OR operator (\ |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RandomAccessFile](arkts-corefile-file-fs-randomaccessfile-i.md)&gt; | Yes |

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
