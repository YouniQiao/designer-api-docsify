# Watcher

Provides APIs for observing the changes of files or directories. Before using the APIs of **Watcher**, call **createWatcher()** to create a **Watcher** object.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-export interface Watcher--><!--Device-unnamed-export interface Watcher-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## start

```TypeScript
start(): void
```

Starts listening.

**Since:** 10

**Deprecated since:** -1

<!--Device-Watcher-start(): void--><!--Device-Watcher-start(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900005 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900042 |
| 13900011 |

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```

## stop

```TypeScript
stop(): void
```

Stops listening and removes the **Watcher** object.

**Since:** 10

**Deprecated since:** -1

<!--Device-Watcher-stop(): void--><!--Device-Watcher-stop(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900005 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900042 |
| 13900011 |

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```
