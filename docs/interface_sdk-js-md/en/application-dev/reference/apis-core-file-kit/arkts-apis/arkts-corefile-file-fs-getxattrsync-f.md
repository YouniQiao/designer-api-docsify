# getxattrSync

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
```

## getxattrSync

```TypeScript
declare function getxattrSync(path: string, key: string): string
```

Obtains an extended attribute of a file or directory. This API returns the result synchronously.

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or directory. |
| key | string | Yes | Key of the extended attribute to obtain. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Value of the extended attribute obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;  2.Incorrect parameter types. |
| 13900002 | No such file or directory |
| 13900007 | Arg list too number |
| 13900012 | Permission denied |
| 13900031 | Function not implemented |
| 13900037 | No data available |
| 13900038 | Value too large for defined data type |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

try {
  let attrValue = fileIo.getxattrSync(filePath, attrKey);
  console.info(`Succeeded in getting extended attribute, the value is: ${attrValue}`);
} catch (err) {
  console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
}
```
