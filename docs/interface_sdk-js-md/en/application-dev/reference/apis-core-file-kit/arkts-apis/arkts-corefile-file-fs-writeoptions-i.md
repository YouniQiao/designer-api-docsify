# WriteOptions

Defines the options used in **write()**. It inherits from [Options](arkts-corefile-file-fs-options-i.md#options).

**Inheritance/Implementation:** WriteOptions extends [Options](arkts-corefile-file-fs-options-i.md#options)

**Since:** 11

<!--Device-unnamed-export interface WriteOptions--><!--Device-unnamed-export interface WriteOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { ConflictFiles } from 'ConflictFiles';
import { FileFilter } from 'FileFilter';
import { Filter } from 'Filter';
import { Options } from 'Options';
import { ReaderIteratorResult } from 'ReaderIteratorResult';
import { WatchEvent } from 'WatchEvent';
import { WatchEventListener } from 'WatchEventListener';
import { Watcher } from 'Watcher';
import { ReadOptions } from 'ReadOptions';
import { ReadTextOptions } from 'ReadTextOptions';
import { WriteOptions } from 'WriteOptions';
import { ListFileExtOptions } from 'ListFileExtOptions';
import { ListFileOptions } from 'ListFileOptions';
import { DfsListeners } from 'DfsListeners';
import { TaskSignal } from 'TaskSignal';
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

