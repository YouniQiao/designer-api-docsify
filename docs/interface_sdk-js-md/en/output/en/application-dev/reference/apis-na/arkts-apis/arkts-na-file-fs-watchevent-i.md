# WatchEvent

Defines the event to observe.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface WatchEvent--><!--Device-unnamed-export interface WatchEvent-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## cookie

```TypeScript
readonly cookie: int
```

Cookie bound with the event. Currently, only the IN\_MOVED\_FROM and IN\_MOVED\_TO events are supported. The IN\_MOVED\_FROM and IN\_MOVED\_TO events of the same file have the same cookie value.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WatchEvent-readonly cookie: int--><!--Device-WatchEvent-readonly cookie: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## event

```TypeScript
readonly event: int
```

Events to observe. Multiple events can be separated by a bitwise OR operator (|). 0x1: IN\_ACCESS: A file is accessed. 0x2: IN\_MODIFY: The file content is modified. 0x4: IN\_ATTRIB: The file metadata is modified. 0x8: IN\_CLOSE\_WRITE: A file is opened, written with data, and then closed. 0x10: IN\_CLOSE\_NOWRITE: A file or directory is opened and then closed without data written. 0x20: IN\_OPEN: A file or directory is opened. 0x40: IN\_MOVED\_FROM: A file in the observed directory is moved. 0x80: IN\_MOVED\_TO: A file is moved to the observed directory. 0x100: IN\_CREATE: A file or directory is created in the observed directory. 0x200: IN\_DELETE: A file or directory is deleted from the observed directory. 0x400: IN\_DELETE\_SELF: The observed directory is deleted. After the directory is deleted, the listening stops. 0x800: IN\_MOVE\_SELF: The observed file or directory is moved. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_After the file or directory is moved, the listening continues. 0xfff: IN\_ALL\_EVENTS: All events.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

<!--Device-WatchEvent-readonly fileName: string--><!--Device-WatchEvent-readonly fileName: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

