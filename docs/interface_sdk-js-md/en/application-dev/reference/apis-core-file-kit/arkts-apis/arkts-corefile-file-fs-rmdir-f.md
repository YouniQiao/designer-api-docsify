# rmdir

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## rmdir

```TypeScript
declare function rmdir(path: string): Promise<void>
```

Removes a directory and all its subdirectories and files. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be used to remove a single file. However, you are advised to use **unlink()** instead.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function rmdir(path: string): Promise<void>--><!--Device-unnamed-declare function rmdir(path: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900014 | Device or resource busy |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |
| 13900027 | Read-only file system |
| 13900030 | File name too long |
| 13900032 | Directory not empty |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.rmdir(dirPath).then(() => {
  console.info("rmdir succeed");
}).catch((err: BusinessError) => {
  console.error("rmdir failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.rmdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error("rmdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("rmdir succeed");
  }
});
```


## rmdir

```TypeScript
declare function rmdir(path: string, callback: AsyncCallback<void>): void
```

Removes a directory and all its subdirectories and files. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be used to remove a single file. However, you are advised to use **unlink()** instead.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function rmdir(path: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function rmdir(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900014 | Device or resource busy |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |
| 13900027 | Read-only file system |
| 13900030 | File name too long |
| 13900032 | Directory not empty |
| 13900042 | Unknown error |

**Examples**

See [rmdir](#rmdir)

