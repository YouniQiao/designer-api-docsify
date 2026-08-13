# DfsListeners

Provides APIs for observing events. listening for the distributed file system status.

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-export interface DfsListeners--><!--Device-unnamed-export interface DfsListeners-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## onStatus

```TypeScript
onStatus(networkId: string, status: number): void
```

Called to return the specified status. Its parameters are passed in by [connectDfs](arkts-corefile-file-fs-connectdfs-f.md#connectDfs).

**Since:** 12

**Deprecated since:** -1

<!--Device-DfsListeners-onStatus(networkId: string, status: number): void--><!--Device-DfsListeners-onStatus(networkId: string, status: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |
| status | number | Yes |
