# fdopenStreamSync

## Modules to Import

```TypeScript
```

## fdopenStreamSync

```TypeScript
declare function fdopenStreamSync(fd: number, mode: string): Stream
```

Opens a stream based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [fdopenStreamSync](arkts-corefile-file-fs-fdopenstreamsync-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the target file. |
| mode | string | Yes | r**: Open a file for reading. The file must exist.   - **r+**: Open a file for both reading and writing. The file must exist.   - **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.   - **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.   - **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).   - **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved). |

**Return value:**

| Type | Description |
| --- | --- |
| [Stream](arkts-corefile-fileio-stream-depr-i.md) | File stream. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let ss = fileio.fdopenStreamSync(fd, "r+");
```
