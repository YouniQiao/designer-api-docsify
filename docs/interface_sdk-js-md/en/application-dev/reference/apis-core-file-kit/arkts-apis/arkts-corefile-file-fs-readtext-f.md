# readText

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## readText

```TypeScript
declare function readText(
  filePath: string,
  options?: ReadTextOptions
): Promise<string>
```

基于文本方式读取文件（即直接读取文件的文本内容），使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readText(  filePath: string,  options?: ReadTextOptions): Promise<string>--><!--Device-unnamed-declare function readText(  filePath: string,  options?: ReadTextOptions): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | 文件的应用沙箱路径。 |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | No | 支持如下选项：&lt;br/&gt;- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。&lt;br/&gt;- length ，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。&lt;br/&gt;- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认'utf-8'，仅支持'utf-8' 。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回读取文件的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900019 | Is a directory |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |


## readText

```TypeScript
declare function readText(filePath: string, callback: AsyncCallback<string>): void
```

基于文本方式读取文件内容，使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readText(filePath: string, callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(filePath: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | 文件的应用沙箱路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回读取文件的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900019 | Is a directory |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |


## readText

```TypeScript
declare function readText(
  filePath: string,
  options: ReadTextOptions,
  callback: AsyncCallback<string>
): void
```

基于文本方式读取文件内容，使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readText(  filePath: string,  options: ReadTextOptions,  callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(  filePath: string,  options: ReadTextOptions,  callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | 文件的应用沙箱路径。 |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | Yes | 支持如下选项：&lt;br/&gt;- offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。&lt;br/&gt;- length ，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。&lt;br/&gt;- encoding，string类型，表示数据的编码方式，默认'utf-8'，仅支持'utf-8'。<br>**Since:** 11 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回读取文件的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900019 | Is a directory |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |

