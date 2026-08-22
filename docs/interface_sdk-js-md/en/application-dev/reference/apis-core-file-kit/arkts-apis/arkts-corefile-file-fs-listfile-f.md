# listFile

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## listFile

```TypeScript
declare function listFile(
  path: string,
  options?: ListFileOptions
): Promise<string[]>
```

Lists the names of all files and directories in the current path. Filtering is supported. This API uses a promise to return the result.

You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function listFile(  path: string,  options?: ListFileOptions): Promise<string[]>--><!--Device-unnamed-declare function listFile(  path: string,  options?: ListFileOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) | No | Options for filtering files. The files are not filtered by default.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise used to return the file name array, which is encoded in UTF-8 format by default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Filter, ListFileOptions } from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
}
fs.listFile(pathDir, listFileOption).then((filenames: Array<string>) => {
  console.info("listFile succeed");
  for (let i = 0; i < filenames.length; i++) {
    console.info("fileName: %s", filenames[i]);
  }
}).catch((err: BusinessError) => {
  console.error("list file failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Filter, ListFileOptions } from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
};
fs.listFile(pathDir, listFileOption, (err: BusinessError, filenames: Array<string>) => {
  if (err) {
    console.error("list file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("listFile succeed");
    for (let i = 0; i < filenames.length; i++) {
      console.info("filename: %s", filenames[i]);
    }
  }
});
```


## listFile

```TypeScript
declare function listFile(path: string, callback: AsyncCallback<string[]>): void
```

Lists the names of all files and directories in the current path. Filtering is supported. This API uses an asynchronous callback to return the result.

You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function listFile(path: string, callback: AsyncCallback<string[]>): void--><!--Device-unnamed-declare function listFile(path: string, callback: AsyncCallback<string[]>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string[]&gt; | Yes | Callback used to return the file names listed. The files are encoded in UTF-8 by default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900042 | Unknown error |

**Examples**

See [listFile](#listfile)


## listFile

```TypeScript
declare function listFile(
  path: string,
  options: ListFileOptions,
  callback: AsyncCallback<string[]>
): void
```

Lists the names of all files and directories in the current path. Filtering is supported. This API uses an asynchronous callback to return the result.

You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function listFile(  path: string,  options: ListFileOptions,  callback: AsyncCallback<string[]>): void--><!--Device-unnamed-declare function listFile(  path: string,  options: ListFileOptions,  callback: AsyncCallback<string[]>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) | Yes | Options for filtering files. The files are not filtered by default.<br>**Since:** 11 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string[]&gt; | Yes | Callback used to return the file names listed. The files are encoded in UTF-8 by default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900042 | Unknown error |

**Examples**

See [listFile](#listfile)

