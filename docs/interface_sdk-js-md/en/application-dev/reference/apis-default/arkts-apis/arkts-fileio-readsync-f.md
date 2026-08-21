# readSync

## Modules to Import

```TypeScript
```

## readSync

```TypeScript
function readSync(
  fd: int,
  buffer: ArrayBuffer,
  options?: ReadOptions
): long
```

Reads data from a file synchronously and returns the number of bytes read.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function readSync(  fd: int,  buffer: ArrayBuffer,  options?: ReadOptions): long--><!--Device-fileIo-function readSync(  fd: int,  buffer: ArrayBuffer,  options?: ReadOptions): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](arkts-file-fs-readoptions-i.md) | No | The options are as follows: <br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position. <br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900042 | Unknown error |
| 13900044 | Network is unreachable |

