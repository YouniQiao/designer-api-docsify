# readSync

## Modules to Import

```TypeScript
```

## readSync

```TypeScript
declare function readSync(
  fd: number,
  buffer: ArrayBuffer,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
  }
): number
```

Reads data from a file. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [readSync](arkts-corefile-file-fs-readsync-f.md)

<!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): number--><!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to read. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | {     offset?: number;     length?: number;     position?: number;   } | No | The options are as follows:<br>- **offset** (number): position to store the data read in the buffer relative to the start address of the buffer, in bytes. This parameter is optional. The default value is **0**.<br>- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset, in bytes.<br>- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position, in bytes.<br> Constraints: offset + length &lt;= Buffer size |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data read, in bytes. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o2);
let buf = new ArrayBuffer(4096);
let num = fileio.readSync(fd, buf);
```

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let buf = new ArrayBuffer(4096)
let num = ss.readSync(buf, option);
```

```TypeScript
let dirent = dir.readSync();
```

