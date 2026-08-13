# truncateSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## truncateSync

```TypeScript
declare function truncateSync(file: string | number, len?: number): void
```

Truncates the file content. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function truncateSync(file: string | number, len?: number): void--><!--Device-unnamed-declare function truncateSync(file: string | number, len?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| number | Yes |
| len | number | No |

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
