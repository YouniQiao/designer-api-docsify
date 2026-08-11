# FileFilter

Defines the file name filtering interface used by listFileExt().

**Since:** 26.0.0

<!--Device-unnamed-export interface FileFilter--><!--Device-unnamed-export interface FileFilter-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## filter

```TypeScript
filter(name: string): boolean
```

Filtering function, which determines whether the specified file name should be included in the file list.

Note: This function is frequently invoked. Avoid time-consuming operations, such as file I/O and network requests.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileFilter-filter(name: string): boolean--><!--Device-FileFilter-filter(name: string): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
