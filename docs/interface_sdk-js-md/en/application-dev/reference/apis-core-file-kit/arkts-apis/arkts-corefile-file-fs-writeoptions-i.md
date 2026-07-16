# WriteOptions

Defines the options used in **write()**. It inherits from [Options](arkts-corefile-file-fs-options-i.md).

**Inheritance/Implementation:** WriteOptions extends [Options](arkts-corefile-file-fs-options-i.md)

**Since:** 11

<!--Device-unnamed-export interface WriteOptions extends Options--><!--Device-unnamed-export interface WriteOptions extends Options-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## length

```TypeScript
length?: number
```

Length of the data to write, in bytes. This parameter is optional. The default value is the buffer length.

**Type:** number

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WriteOptions-length?: number--><!--Device-WriteOptions-length?: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## offset

```TypeScript
offset?: number
```

Start position of the file to write (current **filePointer** plus **offset**), in bytes. This parameter is optional. By default, data is written from the **filePointer**.

**Type:** number

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WriteOptions-offset?: number--><!--Device-WriteOptions-offset?: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

