# ReaderIteratorResult

Represents the information obtained by the **ReaderIterator** object.

**Since:** 11

<!--Device-unnamed-export interface ReaderIteratorResult--><!--Device-unnamed-export interface ReaderIteratorResult-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## done

```TypeScript
done: boolean
```

Whether the iteration is complete. The value **true** means the iteration is complete; the value **false** means the opposite.

**Type:** boolean

**Since:** 11

<!--Device-ReaderIteratorResult-done: boolean--><!--Device-ReaderIteratorResult-done: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## value

```TypeScript
value: string
```

File text content read line by line.

**Type:** string

**Since:** 11

<!--Device-ReaderIteratorResult-value: string--><!--Device-ReaderIteratorResult-value: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

