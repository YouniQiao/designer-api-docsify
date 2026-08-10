# Filter

文件过滤配置项，支持listFile接口使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface Filter--><!--Device-unnamed-export interface Filter-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## displayName

```TypeScript
displayName?: Array<string>
```

文件名模糊匹配，各个关键词OR关系。当前仅支持通配符*。

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-displayName?: Array<string>--><!--Device-Filter-displayName?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## excludeMedia

```TypeScript
excludeMedia?: boolean
```

是否排除Media中已有的文件。true：排除Media中已有的文件；false：不排除Media中已有的文件。预留字段，暂不支持使用。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-excludeMedia?: boolean--><!--Device-Filter-excludeMedia?: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## fileSizeOver

```TypeScript
fileSizeOver?: long
```

文件大小匹配，大于指定大小的文件，单位为Byte。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-fileSizeOver?: long--><!--Device-Filter-fileSizeOver?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## lastModifiedAfter

```TypeScript
lastModifiedAfter?: double
```

文件最近修改时间匹配，在指定时间点及之后的文件。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-lastModifiedAfter?: double--><!--Device-Filter-lastModifiedAfter?: double-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## mimeType

```TypeScript
mimeType?: Array<string>
```

mime类型完全匹配，各个关键词OR关系。预留字段，暂不支持使用。

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-mimeType?: Array<string>--><!--Device-Filter-mimeType?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## suffix

```TypeScript
suffix?: Array<string>
```

文件后缀名完全匹配，各个关键词OR关系。

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-suffix?: Array<string>--><!--Device-Filter-suffix?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

