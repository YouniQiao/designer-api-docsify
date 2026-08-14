# ReadTextOptions

Defines the options used in **readText()**. It inherits from [ReadOptions](../../apis-na/arkts-apis/arkts-na-file-fs-readoptions-i.md#ReadOptions).

**Inheritance/Implementation:** ReadTextOptions extends [ReadOptions](../../apis-na/arkts-apis/arkts-na-file-fs-readoptions-i.md#ReadOptions)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-unnamed-export interface ReadTextOptions--><!--Device-unnamed-export interface ReadTextOptions-End-->

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

## encoding

```TypeScript
encoding?: string
```

Format of the data to be encoded. This parameter is valid only when the data type is string. The default value is **'utf-8'**, which is the only value supported.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReadTextOptions-encoding?: string--><!--Device-ReadTextOptions-encoding?: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

