# ReadStreamOptions

Defines the options used in **createReadStream()**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ReadStreamOptions--><!--Device-unnamed-export interface ReadStreamOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## end

```TypeScript
end?: long
```

End position to read the data, in bytes. This parameter is optional. The default value is the end of the file.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStreamOptions-end?: long--><!--Device-ReadStreamOptions-end?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## start

```TypeScript
start?: long
```

Start position to read the data, in bytes. This parameter is optional. By default, data is read from the current position.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStreamOptions-start?: long--><!--Device-ReadStreamOptions-start?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

