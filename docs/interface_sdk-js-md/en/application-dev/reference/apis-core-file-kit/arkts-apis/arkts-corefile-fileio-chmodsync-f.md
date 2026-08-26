# chmodSync

## Modules to Import

```TypeScript
```

## chmodSync

```TypeScript
declare function chmodSync(path: string, mode: number): void
```

Changes file permissions. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|).   - **0o700**: The owner has the read, write, and execute permissions.   - **0o400**: The owner has the read permission.   - **0o200**: The owner has the write permission.   - **0o100**: The owner has the execute permission.   - **0o070**: The user group has the read, write, and execute permissions.   - **0o040**: The user group has the read permission.   - **0o020**: The user group has the write permission.   - **0o010**: The user group has the execute permission.   - **0o007**: Other users have the read, write, and execute permissions.   - **0o004**: Other users have the read permission.   - **0o002**: Other users have the write permission.   - **0o001**: Other users have the execute permission. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
fileio.chmodSync(filePath, 0o700);
```
