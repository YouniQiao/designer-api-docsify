# FileInfo (System API)

Provides APIs for managing file or directory attribute information.

**Since:** 9

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

Obtains a **FileIterator** object that lists the next-level files or directories matching the specified conditions of this directory. This API returns the result synchronously. [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md) is returned by [next()](arkts-corefile-fileaccess-fileiterator-i-sys.md#next). Currently, only built-in storage devices support the file filter.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** @ohos.file.fs:fileIo.listFile

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-listFile(filter?: Filter): FileIterator--><!--Device-FileInfo-listFile(filter?: Filter): FileIterator-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| 14000004 |
| 13900038 |
| 14000001 |
| 13900033 |
| 13900034 |
| 14000003 |
| 14000002 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 13900013 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 14300004 |
| 13900011 |

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

Obtains a **FileIterator** object that recursively retrieves the files matching the specified conditions of this directory. This API returns the result synchronously. [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md) is returned by   
[next()](arkts-corefile-fileaccess-fileiterator-i-sys.md#next). Currently, this API supports only built-in storage devices.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-scanFile(filter?: Filter): FileIterator--><!--Device-FileInfo-scanFile(filter?: Filter): FileIterator-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| 14000004 |
| 13900038 |
| 14000001 |
| 13900033 |
| 13900034 |
| 14000003 |
| 14000002 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 13900013 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 14300004 |
| 13900011 |

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

Name of the file or directory.

**Type:** string

**Since:** 9

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

Multipurpose Internet Mail Extensions (MIME) type of the file or directory.

**Type:** string

**Since:** 9

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

Permissions on the file or directory.

**Type:** number

**Since:** 9

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

Time when the file or directory was last modified.&lt;br&gt;Unit: ms.

**Type:** number

**Since:** 9

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

Relative path of the file or directory.

**Type:** string

**Since:** 10

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

Size of the file or directory.&lt;br&gt;Unit: Byte.

**Type:** number

**Since:** 9

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

URI of the file or directory.

**Type:** string

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileInfo-uri: string--><!--Device-FileInfo-uri: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.
