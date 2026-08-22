# closeSync

## Modules to Import

```TypeScript
```

## closeSync

```TypeScript
declare function closeSync(fd: number): void
```

Closes a file. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [closeSync](arkts-corefile-file-fs-closesync-f.md)

<!--Device-unnamed-declare function closeSync(fd: number): void--><!--Device-unnamed-declare function closeSync(fd: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to close. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.closeSync(fd);
```

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.closeSync();
```

```TypeScript
dir.closeSync();
```

