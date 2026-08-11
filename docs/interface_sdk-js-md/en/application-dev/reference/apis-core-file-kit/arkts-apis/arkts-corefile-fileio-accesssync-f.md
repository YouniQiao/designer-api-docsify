# accessSync

## accessSync

```TypeScript
declare function accessSync(path: string, mode?: number): void
```

Checks whether this process can access a file. This API returns the result synchronously.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:accessSync](arkts-corefile-fileio-accesssync-f.md#accesssync)

<!--Device-unnamed-declare function accessSync(path: string, mode?: number): void--><!--Device-unnamed-declare function accessSync(path: string, mode?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | No | Options for accessing the file. You can specify multiple options, separated with a bitwise OR operator (\|). The default value is **0**.&lt;br&gt;The options are as follows:&lt;br&gt;- **0**: Check whether the file exists.&lt;br&gt;- **1**: Check whether the process has the execute permission on the file.&lt;br&gt;- **2**: Check whether the process has the write permission on the file.&lt;br&gt;- **4**: Check whether the process has the read permission on the file. |

