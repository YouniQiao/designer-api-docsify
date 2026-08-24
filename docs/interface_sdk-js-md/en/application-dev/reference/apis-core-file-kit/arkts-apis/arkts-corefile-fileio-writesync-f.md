# writeSync

## Modules to Import

```TypeScript
```

## writeSync

```TypeScript
declare function writeSync(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
  }
): number
```

Writes data to a file. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [writeSync](arkts-corefile-file-fs-writesync-f.md)

<!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): number--><!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | No | The options are as follows:<br>- **offset** (number): offset of the write position relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br>- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length minus the offset.<br>- **position** (number): start position to write the data into the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>Constraints: offset + length &lt;= Buffer size |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data written in the file, in bytes. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
let num = fileio.writeSync(fd, "hello, world");
```

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath,"r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let num = ss.writeSync("hello, world", option);
```

