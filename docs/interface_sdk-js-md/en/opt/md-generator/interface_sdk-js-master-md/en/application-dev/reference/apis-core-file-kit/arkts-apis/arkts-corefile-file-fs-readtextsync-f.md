# readTextSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## readTextSync

```TypeScript
declare function readTextSync(
  filePath: string,
  options?: ReadTextOptions
): string
```

Reads the text content of a file. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: ReadTextOptions): string--><!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: ReadTextOptions): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900019 |
| 13900024 |
| 13900025 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900044 |
| 13900013 |
| 13900008 |
| 13900041 |
| 13900010 |
| 13900042 |
