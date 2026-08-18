# ReadTextOptions

Defines the options used in **readText()**. It inherits from [ReadOptions](../../apis-na/arkts-apis/arkts-na-file-fs-readoptions-i.md).

**Inheritance/Implementation:** ReadTextOptions extends [ReadOptions](../../apis-na/arkts-apis/arkts-na-file-fs-readoptions-i.md)

**Since:** 11

<!--Device-unnamed-export interface ReadTextOptions--><!--Device-unnamed-export interface ReadTextOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## encoding

```TypeScript
encoding?: string
```

Format of the data to be encoded. This parameter is valid only when the data type is string. The default value is **'utf-8'**, which is the only value supported.

**Type:** string

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReadTextOptions-encoding?: string--><!--Device-ReadTextOptions-encoding?: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

