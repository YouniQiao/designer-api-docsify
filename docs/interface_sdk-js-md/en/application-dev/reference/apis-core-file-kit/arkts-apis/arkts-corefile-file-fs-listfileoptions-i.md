# ListFileOptions

可选项类型，支持listFile接口使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ListFileOptions--><!--Device-unnamed-export interface ListFileOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## filter

```TypeScript
filter?: Filter
```

文件过滤配置项。 可选，设置过滤条件。

**Type:** [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ListFileOptions-filter?: Filter--><!--Device-ListFileOptions-filter?: Filter-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## listNum

```TypeScript
listNum?: long
```

列出文件名数量。可选，当设置0时，列出所有文件，默认为0。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ListFileOptions-listNum?: long--><!--Device-ListFileOptions-listNum?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## recursion

```TypeScript
recursion?: boolean
```

是否递归子目录下文件名。可选，默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及目录名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以“/”开头）。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ListFileOptions-recursion?: boolean--><!--Device-ListFileOptions-recursion?: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

