# createWatcher

## createWatcher

```TypeScript
function createWatcher(path: string, events: int, listener: WatchEventListener): Watcher
```

Creates a **Watcher** object to listen for file or directory changes such as creating, deleting, and modifying.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function createWatcher(path: string, events: int, listener: WatchEventListener): Watcher--><!--Device-fileIo-function createWatcher(path: string, events: int, listener: WatchEventListener): Watcher-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or director. |
| events | int | Yes | Events to observe. Multiple events can be separated by vertical bars (\|). <br>- **0x1: IN_ACCESS**: A file is accessed. <br>- **0x2: IN_MODIFY**: The file content is modified. <br>- **0x4: IN_ATTRIB**: The file metadata is modified. <br>- **0x8: IN_CLOSE_WRITE**: A file is opened, written with data, and then closed. <br>- **0x10: IN_CLOSE_NOWRITE**: A file or directory is opened and then closed without data written. <br>- **0x20: IN_OPEN**: A file or directory is opened. <br>- **0x40: IN_MOVED_FROM**: A file in the observed directory is moved. <br>- **0x80: IN_MOVED_TO**: A file is moved to the observed directory. <br>- **0x100: IN_CREATE**: A file or directory is created in the observed directory. <br>- **0x200: IN_DELETE**: A file or directory is deleted from the observed directory. <br>- **0x400: IN_DELETE_SELF**: The observed directory is deleted. After the directory is deleted, the listening stops. <br>- **0x800: IN_MOVE_SELF**: The observed file or directory is moved. After the file or directory is moved, the listening continues. <br>- **0xfff: IN_ALL_EVENTS**: All events. |
| listener | [WatchEventListener](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-watcheventlistener-i.md) | Yes | Callback invoked when an observed event occurs. The callback will be invoked each time an observed event occurs. |

**Return value:**

| Type | Description |
| --- | --- |
| [Watcher](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-watcher-i.md) | Watcher** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900021 | File table overflow |
| 13900022 | Too many open files |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

