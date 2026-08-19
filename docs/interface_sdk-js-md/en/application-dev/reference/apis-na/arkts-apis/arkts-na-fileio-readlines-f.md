# readLines

## Modules to Import

```TypeScript
```

## readLines

```TypeScript
function readLines(filePath: string, options?: Options): Promise<ReaderIterator>
```

Reads a file text line by line. Only the files in UTF-8 format are supported. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function readLines(filePath: string, options?: Options): Promise<ReaderIterator>--><!--Device-fileIo-function readLines(filePath: string, options?: Options): Promise<ReaderIterator>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [Options](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-options-i.md) | No | Options for reading the text. The options are as follows: <br>- **encoding** (string): format of the data to be encoded. <br>It is valid only when the data is of the string type. <br>The default value is **'utf-8'**, which is the only value supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ReaderIterator](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readeriterator-i.md)&gt; | Promise used to return the **ReaderIterator** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900044 | Network is unreachable |
| 13900015 | File exists |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |


## readLines

```TypeScript
function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void
```

Reads a file text line by line. Only the files in UTF-8 format are supported. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void--><!--Device-fileIo-function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[ReaderIterator](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readeriterator-i.md)&gt; | Yes | Callback used to return a **ReaderIterator** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900019 | Is a directory |
| 13900012 | Permission denied |
| 13900030 | File name too long |
| 13900015 | File exists |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900027 | Read-only file system |


## readLines

```TypeScript
function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void
```

Reads a file text line by line. Read options can be configured. Only the files in UTF-8 format are supported. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void--><!--Device-fileIo-function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [Options](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-options-i.md) | Yes | Read options. The options are as follows: <br>- **encoding** (string): format of the data to be encoded. <br>It is valid only when the data is of the string type. <br>The default value is **'utf-8'**, which is the only value supported. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[ReaderIterator](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readeriterator-i.md)&gt; | Yes | Callback used to return a **ReaderIterator** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900019 | Is a directory |
| 13900012 | Permission denied |
| 13900030 | File name too long |
| 13900015 | File exists |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900027 | Read-only file system |

