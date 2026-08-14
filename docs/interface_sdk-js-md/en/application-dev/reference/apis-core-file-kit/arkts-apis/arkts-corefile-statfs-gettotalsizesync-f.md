# getTotalSizeSync

## Modules to Import

```TypeScript
import { statfs } from 'statfs';
```

## getTotalSizeSync

```TypeScript
function getTotalSizeSync(path: string): long
```

Obtains the total size of the specified file system, in bytes. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-statfs-function getTotalSizeSync(path: string): long--><!--Device-statfs-function getTotalSizeSync(path: string): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | File path of the file system. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Total size obtained, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
let number = statfs.getTotalSizeSync(path);
console.info("getTotalSizeSync succeed, Size: " + number);
```

