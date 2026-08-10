# writeSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## writeSync

```TypeScript
declare function writeSync(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: WriteOptions
): number
```

以同步方法将数据写入文件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: WriteOptions): number--><!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: WriteOptions): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 已打开的文件描述符。 |
| buffer | ArrayBuffer \| string | Yes | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | No | 支持如下选项：&lt;br/&gt;- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。&lt;br/&gt;- length， number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。&lt;br/&gt;- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认'utf-8'。当前仅支持?'utf- 8'。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回实际写入的数据长度，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |

