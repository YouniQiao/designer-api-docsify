# Watcher

Provides APIs for observing the changes of files or directories. Before using the APIs of **Watcher**, call **createWatcher()** to create a **Watcher** object.

**Since:** 10

<!--Device-unnamed-export interface Watcher--><!--Device-unnamed-export interface Watcher-End-->

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

## start

```TypeScript
start(): void
```

Starts listening.

**Since:** 10

<!--Device-Watcher-start(): void--><!--Device-Watcher-start(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900021 | File table overflow |
| 13900022 | Too many open files |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900005 | I/O error |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let watcher = fs.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```

## stop

```TypeScript
stop(): void
```

Stops listening and removes the **Watcher** object.

**Since:** 10

<!--Device-Watcher-stop(): void--><!--Device-Watcher-stop(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900021 | File table overflow |
| 13900022 | Too many open files |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900005 | I/O error |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let watcher = fs.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```

