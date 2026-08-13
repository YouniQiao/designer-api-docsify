# WatchEvent

Defines the event to observe.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface WatchEvent--><!--Device-unnamed-export interface WatchEvent-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## cookie

```TypeScript
readonly cookie: int
```

Cookie bound with the event. Currently, only the **IN_MOVED_FROM** and **IN_MOVED_TO** events are supported. The **IN_MOVED_FROM** and **IN_MOVED_TO** events of the same file have the same **cookie** value.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WatchEvent-readonly cookie: int--><!--Device-WatchEvent-readonly cookie: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## event

```TypeScript
readonly event: int
```

Events to observe. Multiple events can be separated by vertical bars (|). - **0x1: IN_ACCESS**: A file is accessed. - **0x2: IN_MODIFY**: The file content is modified. - **0x4: IN_ATTRIB**: The file metadata is modified. - **0x8: IN_CLOSE_WRITE**: A file is opened, written with data, and then closed. - **0x10: IN_CLOSE_NOWRITE**: A file or directory is opened and then closed without data written. - **0x20: IN_OPEN**: A file or directory is opened. - **0x40: IN_MOVED_FROM**: A file in the observed directory is moved. - **0x80: IN_MOVED_TO**: A file is moved to the observed directory. - **0x100: IN_CREATE**: A file or directory is created in the observed directory. - **0x200: IN_DELETE**: A file or directory is deleted from the observed directory. - **0x400: IN_DELETE_SELF**: The observed directory is deleted. After the directory is deleted, the listening stops. - **0x800: IN_MOVE_SELF**: The observed file or directory is moved. After the file or directory is moved, the listening continues. - **0xfff: IN_ALL_EVENTS**: All events.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WatchEvent-readonly event: int--><!--Device-WatchEvent-readonly event: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## fileName

```TypeScript
readonly fileName: string
```

Sandbox path of the file to observe. The sandbox path contains the file name.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WatchEvent-readonly fileName: string--><!--Device-WatchEvent-readonly fileName: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

