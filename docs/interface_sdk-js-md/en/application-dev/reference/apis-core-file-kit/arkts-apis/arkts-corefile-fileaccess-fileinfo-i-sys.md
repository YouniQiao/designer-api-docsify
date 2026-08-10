# FileInfo (System API)

表示文件(夹)属性信息和接口能力。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

<!--Device-fileAccess-interface FileInfo--><!--Device-fileAccess-interface FileInfo-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fileAccess } from 'kits/@kit.CoreFileKit';
```

## listFile

```TypeScript
listFile(filter?: Filter): FileIterator
```

以同步方法从某个目录，基于过滤器，获取下一级符合条件的文件(夹)信息的迭代器对象FileIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回  
[FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md)。目前仅支持内置存储设备过滤，外置存储设备不支持过滤。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Substitutes:** [@ohos.file.fs:fileIo.listFile](arkts-corefile-fileio-listfile-f.md#listfile)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-listFile(filter?: Filter): FileIterator--><!--Device-FileInfo-listFile(filter?: Filter): FileIterator-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | No | Indicates the filter of file. |

**Return value:**

| Type | Description |
| --- | --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) | Returns the FileIterator Object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14000004 | File has been put into trash bin |
| 13900038 | Value too large for defined data type |
| 14000001 | Invalid display name |
| 13900033 | Too many symbolic links encountered |
| 13900034 | Operation would block |
| 14000003 | Invalid file extension |
| 14000002 | Invalid uri |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900023 | Text file busy |
| 13900017 | No such device |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900029 | Resource deadlock would occur |
| 13900030 | File name too long |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900004 | Interrupted system call |
| 13900006 | No such device or address |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 14300002 | Invalid uri |
| 13900013 | Bad address |
| 14300003 | Fail to get fileextension info |
| 13900014 | Device or resource busy |
| 13900015 | File exists |
| 14300001 | IPC error |
| 13900008 | Bad file descriptor |
| 14300004 | Get wrong result |
| 13900011 | Out of memory |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// fileInfoDir indicates information about a directory.
// let filter = { suffix : [".txt", ".jpg", ".xlsx"] };
let fileInfoDir :Array<fileAccess.FileInfo> = [];
let subfileInfos: Array<fileAccess.FileInfo> = [];
let isDone: boolean = false;
try {
  for (let i = 0; i < fileInfoDir.length; ++i) {
    let fileIterator = fileInfoDir[i].listFile();
    // listFile() with the filter implementation.
    // let fileIterator = fileInfoDir.listFile(filter);
    if (!fileIterator) {
      console.error("listFile interface returns an undefined object");
    }
    while (!isDone) {
      let result = fileIterator.next();
      console.info("next result = " + JSON.stringify(result));
      isDone = result.done;
      if (!isDone) {
        subfileInfos.push(result.value);
      }
    }
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("listFile failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## scanFile

```TypeScript
scanFile(filter?: Filter): FileIterator
```

以同步方法从某个目录，基于过滤器，递归获取符合条件的文件信息的迭代器对象FileIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回  
[FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md)。目前仅支持内置存储设备。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-scanFile(filter?: Filter): FileIterator--><!--Device-FileInfo-scanFile(filter?: Filter): FileIterator-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | No | Indicates the filter of file. |

**Return value:**

| Type | Description |
| --- | --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) | Returns the FileIterator Object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14000004 | File has been put into trash bin |
| 13900038 | Value too large for defined data type |
| 14000001 | Invalid display name |
| 13900033 | Too many symbolic links encountered |
| 13900034 | Operation would block |
| 14000003 | Invalid file extension |
| 14000002 | Invalid uri |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900023 | Text file busy |
| 13900017 | No such device |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900029 | Resource deadlock would occur |
| 13900030 | File name too long |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900004 | Interrupted system call |
| 13900006 | No such device or address |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 14300002 | Invalid uri |
| 13900013 | Bad address |
| 14300003 | Fail to get fileextension info |
| 13900014 | Device or resource busy |
| 13900015 | File exists |
| 14300001 | IPC error |
| 13900008 | Bad file descriptor |
| 14300004 | Get wrong result |
| 13900011 | Out of memory |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// fileInfoDir indicates information about a directory.
// let filter = {suffix : [".txt", ".jpg", ".xlsx"]};
let fileInfoDir: Array<fileAccess.FileInfo> = [];
let subfileInfos: Array<fileAccess.FileInfo> = [];
let isDone: boolean = false;
try {
  for (let i = 0; i < fileInfoDir.length; ++i) {
    let fileIterator = fileInfoDir[i].scanFile();
    // scanFile() with the filter implementation.
    // let fileIterator = fileInfoDir.scanFile(filter);
    if (!fileIterator) {
      console.error("scanFile interface returns an undefined object");
    }
    while (!isDone) {
      let result = fileIterator.next();
      console.info("next result = " + JSON.stringify(result));
      isDone = result.done;
      if (!isDone) {
        subfileInfos.push(result.value);
      }
    }
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("scanFile failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## fileName

```TypeScript
fileName: string
```

文件(夹)的名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-fileName: string--><!--Device-FileInfo-fileName: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## mimeType

```TypeScript
mimeType: string
```

文件(夹)的媒体资源类型。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-mimeType: string--><!--Device-FileInfo-mimeType: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## mode

```TypeScript
mode: number
```

文件(夹)的权限信息。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-mode: number--><!--Device-FileInfo-mode: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## mtime

```TypeScript
mtime: number
```

文件(夹)的修改时间。自1970年1月1日起至目标时间的毫秒数。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-mtime: number--><!--Device-FileInfo-mtime: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## relativePath

```TypeScript
relativePath: string
```

文件(夹)的相对路径。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-relativePath: string--><!--Device-FileInfo-relativePath: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## size

```TypeScript
size: number
```

文件(夹)的大小。（单位：字节）

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-size: number--><!--Device-FileInfo-size: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## uri

```TypeScript
uri: string
```

文件(夹)的uri。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-uri: string--><!--Device-FileInfo-uri: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

