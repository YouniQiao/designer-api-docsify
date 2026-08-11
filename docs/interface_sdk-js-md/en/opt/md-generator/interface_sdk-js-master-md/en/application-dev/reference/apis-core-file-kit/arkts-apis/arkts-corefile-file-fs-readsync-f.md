# readSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## readSync

```TypeScript
declare function readSync(
  fd: number,
  buffer: ArrayBuffer,
  options?: ReadOptions
): number
```

Reads data from a file. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: ReadOptions): number--><!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: ReadOptions): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer | Yes |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900034 |
| 13900019 |
| 13900044 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |
