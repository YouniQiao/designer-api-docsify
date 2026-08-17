# ReadOptions

Defines the options used in **read()**.

**Since:** 11

<!--Device-unnamed-export interface ReadOptions--><!--Device-unnamed-export interface ReadOptions-End-->

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

Length of the data to read, in bytes. This parameter is optional. The default value is the buffer length.

**Type:** number

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReadOptions-length?: number--><!--Device-ReadOptions-length?: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## offset

```TypeScript
offset?: number
```

Start position of the file to read, in bytes. This parameter is optional. By default, data is read from the current position.

**Type:** number

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReadOptions-offset?: number--><!--Device-ReadOptions-offset?: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

