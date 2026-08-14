# ReaderIteratorResult

Represents the information obtained by the **ReaderIterator** object.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-unnamed-export interface ReaderIteratorResult--><!--Device-unnamed-export interface ReaderIteratorResult-End-->

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

## done

```TypeScript
done: boolean
```

Whether the iteration is complete. The value **true** means the iteration is complete; the value **false** means the opposite.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-ReaderIteratorResult-done: boolean--><!--Device-ReaderIteratorResult-done: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## value

```TypeScript
value: string
```

File text content read line by line.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-ReaderIteratorResult-value: string--><!--Device-ReaderIteratorResult-value: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

