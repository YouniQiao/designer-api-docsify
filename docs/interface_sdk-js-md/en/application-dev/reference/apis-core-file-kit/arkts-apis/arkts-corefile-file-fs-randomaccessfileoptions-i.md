# RandomAccessFileOptions

Defines the options used in **createRandomAccessFile()**.

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## end

```TypeScript
end?: number
```

End position to read the data, in bytes. This parameter is optional. The default value is the end of the file.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO

## start

```TypeScript
start?: number
```

Start position to read the data, in bytes. This parameter is optional. By default, data is read from the current position.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO
