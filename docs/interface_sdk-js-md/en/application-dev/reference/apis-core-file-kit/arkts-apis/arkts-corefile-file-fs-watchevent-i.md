# WatchEvent

Defines the event to observe.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-export interface WatchEvent--><!--Device-unnamed-export interface WatchEvent-End-->

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

## cookie

```TypeScript
readonly cookie: number
```

Cookie bound with the event. Currently, only the **IN_MOVED_FROM** and **IN_MOVED_TO** events are supported. The **IN_MOVED_FROM** and **IN_MOVED_TO** events of the same file have the same **cookie** value.

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-WatchEvent-readonly cookie: number--><!--Device-WatchEvent-readonly cookie: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## event

```TypeScript
readonly event: number
```

Events to observe. Multiple events can be separated by vertical bars (

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-WatchEvent-readonly event: number--><!--Device-WatchEvent-readonly event: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## fileName

```TypeScript
readonly fileName: string
```

Sandbox path of the file to observe. The sandbox path contains the file name.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-WatchEvent-readonly fileName: string--><!--Device-WatchEvent-readonly fileName: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

