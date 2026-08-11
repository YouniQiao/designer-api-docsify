# fdopenStreamSync

## fdopenStreamSync

```TypeScript
declare function fdopenStreamSync(fd: number, mode: string): Stream
```

Opens a stream based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:fdopenStreamSync](arkts-corefile-fileio-fdopenstreamsync-f.md#fdopenstreamsync)

<!--Device-unnamed-declare function fdopenStreamSync(fd: number, mode: string): Stream--><!--Device-unnamed-declare function fdopenStreamSync(fd: number, mode: string): Stream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the target file. |
| mode | string | Yes | r**: Open a file for reading. The file must exist.&lt;br&gt;- **r+**: Open a file for both reading and writing. The file must exist.&lt;br&gt;- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.&lt;br&gt;- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.&lt;br&gt;- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).&lt;br&gt;- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved). |

**Return value:**

| Type | Description |
| --- | --- |
| [Stream](arkts-corefile-file-fs-stream-i.md) | File stream. |

