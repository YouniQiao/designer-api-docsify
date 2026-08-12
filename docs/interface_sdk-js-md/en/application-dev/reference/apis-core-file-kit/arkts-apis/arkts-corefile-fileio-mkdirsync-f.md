# mkdirSync

## mkdirSync

```TypeScript
declare function mkdirSync(path: string, mode?: number): void
```

Creates a directory. This API returns the result synchronously.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [mkdirSync](arkts-corefile-file-fs-mkdirsync-f.md#mkdirSync)

<!--Device-unnamed-declare function mkdirSync(path: string, mode?: number): void--><!--Device-unnamed-declare function mkdirSync(path: string, mode?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| mode | number | No | Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (\|). The default value is **0o775**.&lt;br&gt;- **0o775**: The owner has the read, write, and execute permissions, and other users have the read and execute permissions.&lt;br&gt;- **0o700**: The owner has the read, write, and execute permissions.&lt;br&gt;- **0o400**: The owner has the read permission.&lt;br&gt;- **0o200**: The owner has the write permission.&lt;br&gt;- **0o100**: The owner has the execute permission.&lt;br&gt;- **0o070**: The user group has the read, write, and execute permissions.&lt;br&gt;- **0o040**: The user group has the read permission.&lt;br&gt;- **0o020**: The user group has the write permission.&lt;br&gt;- **0o010**: The user group has the execute permission.&lt;br &gt;- **0o007**: Other users have the read, write, and execute permissions.&lt;br&gt;- **0o004**: Other users have the read permission.&lt;br&gt;- **0o002**: Other users have the write permission.&lt;br&gt;- **0o001**: Other users have the execute permission. |

