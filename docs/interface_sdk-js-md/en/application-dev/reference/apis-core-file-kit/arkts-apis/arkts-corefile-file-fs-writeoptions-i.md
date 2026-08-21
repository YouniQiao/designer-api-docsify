# WriteOptions

Defines the options used in **write()**. It inherits from [Options](../../apis-default/arkts-apis/arkts-file-fs-options-i.md).

**Inheritance/Implementation:** WriteOptions extends [Options](../../apis-default/arkts-apis/arkts-file-fs-options-i.md)

**Since:** 11

<!--Device-unnamed-export interface WriteOptions--><!--Device-unnamed-export interface WriteOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
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

Start position of the file to write, in bytes. This parameter is optional. By default, data is written from the current position.

**Type:** number

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WriteOptions-offset?: number--><!--Device-WriteOptions-offset?: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

