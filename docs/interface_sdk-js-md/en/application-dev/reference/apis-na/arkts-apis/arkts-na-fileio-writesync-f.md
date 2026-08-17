# writeSync

## writeSync

```TypeScript
function writeSync(
  fd: int,
  buffer: ArrayBuffer | string,
  options?: WriteOptions
): long
```

Writes data to a file synchronously and returns the number of bytes written.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function writeSync(  fd: int,  buffer: ArrayBuffer | string,  options?: WriteOptions): long--><!--Device-fileIo-function writeSync(  fd: int,  buffer: ArrayBuffer | string,  options?: WriteOptions): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-writeoptions-i.md) | No | The options are as follows: <br>- **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. Bydefault, data is written from the current position. <br>- **length** (number): length of the data to write, in bytes. This parameter is optional. The default valueis the buffer length. <br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is**'utf-8'**, which is the only value supported currently. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |

