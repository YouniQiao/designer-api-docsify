# fchmodSync

## Modules to Import

```TypeScript
```

## fchmodSync

```TypeScript
declare function fchmodSync(fd: number, mode: number): void
```

Changes the file permissions based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the target file. |
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|).   - **0o700**: The owner has the read, write, and execute permissions.   - **0o400**: The owner has the read permission.   - **0o200**: The owner has the write permission.   - **0o100**: The owner has the execute permission.   - **0o070**: The user group has the read, write, and execute permissions.   - **0o040**: The user group has the read permission.   - **0o020**: The user group has the write permission.   - **0o010**: The user group has the execute permission.   - **0o007**: Other users have the read, write, and execute permissions.   - **0o004**: Other users have the read permission.   - **0o002**: Other users have the write permission.   - **0o001**: Other users have the execute permission. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmodSync(fd, mode);
```
