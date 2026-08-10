# ListFileExtOptions

可选项类型，支持listFileExt接口使用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface ListFileExtOptions--><!--Device-unnamed-export interface ListFileExtOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## fileFilter

```TypeScript
fileFilter?: FileFilter
```

自定义文件名过滤的规则，默认为空，表示不进行过滤。

**Type:** [FileFilter](arkts-corefile-file-fs-filefilter-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFileExtOptions-fileFilter?: FileFilter--><!--Device-ListFileExtOptions-fileFilter?: FileFilter-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## listNum

```TypeScript
listNum?: long
```

列出文件名数量，默认为0，表示列出所有文件。

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFileExtOptions-listNum?: long--><!--Device-ListFileExtOptions-listNum?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## recursion

```TypeScript
recursion?: boolean
```

是否递归子目录下的文件名，默认为false。

false：返回当前目录下满足过滤要求的文件名及目录名。

true：返回该目录下所有符合过滤条件的文件的相对路径，相对路径以“/”开头。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFileExtOptions-recursion?: boolean--><!--Device-ListFileExtOptions-recursion?: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

