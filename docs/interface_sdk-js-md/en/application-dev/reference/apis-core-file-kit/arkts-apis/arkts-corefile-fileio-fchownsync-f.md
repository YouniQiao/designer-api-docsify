# fchownSync

## Modules to Import

```TypeScript
```

## fchownSync

```TypeScript
declare function fchownSync(fd: number, uid: number, gid: number): void
```

Changes the file owner based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the target file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchownSync(fd, stat.uid, stat.gid);
```
