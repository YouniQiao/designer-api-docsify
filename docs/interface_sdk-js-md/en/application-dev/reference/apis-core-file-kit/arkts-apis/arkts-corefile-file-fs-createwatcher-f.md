# createWatcher

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## createWatcher

```TypeScript
declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher
```

Creates a **Watcher** object to listen for file or directory changes.

**Since:** 10

<!--Device-unnamed-declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher--><!--Device-unnamed-declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or directory to observe. |
| events | number | Yes | Events to observe. Multiple events can be separated by vertical bars ( |
| listener | [WatchEventListener](arkts-corefile-file-fs-watcheventlistener-i.md) | Yes | Callback invoked when an observed event occurs. The callback will be invoked each time an observed event occurs. |

**Return value:**

| Type | Description |
| --- | --- |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) | Watcher** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900015 | File exists |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |
| 13900021 | File table overflow |
| 13900022 | Too many open files |
| 13900025 | No space left on device |
| 13900030 | File name too long |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo as fs, WatchEvent } from '@kit.CoreFileKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let watcher = fs.createWatcher(filePath, 0x2 | 0x10, (watchEvent: WatchEvent) => {
  if (watchEvent.event == 0x2) {
    console.info(watchEvent.fileName + 'was modified');
  } else if (watchEvent.event == 0x10) {
    console.info(watchEvent.fileName + 'was closed');
  }
});
watcher.start();
fs.writeSync(file.fd, 'test');
fs.closeSync(file);
watcher.stop();
```

