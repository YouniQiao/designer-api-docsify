# FileUri

FileUri represents the uri of the file.

**Inheritance/Implementation:** FileUri extends [uri.URI](uri.URI)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-fileUri-class FileUri extends uri.URI--><!--Device-fileUri-class FileUri extends uri.URI-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

## Modules to Import

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor(uriOrPath: string)
```

Constructor for obtaining the instance of the FileUri class.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-constructor(uriOrPath: string)--><!--Device-FileUri-constructor(uriOrPath: string)-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uriOrPath | string | Yes | Uri or Path. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 14300002 | Invalid uri |
| 13900042 | Unknown error |

## Examples

```TypeScript
let path = pathDir + '/test';
let uri = fileUri.getUriFromPath(path);  // file://<packageName>/data/storage/el2/base/haps/entry/files/test
let fileUriObject = new fileUri.FileUri(uri);
console.info("The name of FileUri is " + fileUriObject.name);
```

## getFullDirectoryUri

```TypeScript
getFullDirectoryUri(): string
```

Get the full directory uri where the file URI is located

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-getFullDirectoryUri(): string--><!--Device-FileUri-getFullDirectoryUri(): string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the directory uri |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900042 | Unknown error |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let path = pathDir + '/test.txt';
  let fileUriObject = new fileUri.FileUri(path);
  let directoryUri = fileUriObject.getFullDirectoryUri();
  console.info(`success to getFullDirectoryUri: ${JSON.stringify(directoryUri)}`);
} catch (error) {
  console.error(`failed to getFullDirectoryUri because: ${JSON.stringify(error)}`);
}
```

## isRemoteUri

```TypeScript
isRemoteUri(): boolean
```

Check whether the incoming URI is a remote URI

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-isRemoteUri(): boolean--><!--Device-FileUri-isRemoteUri(): boolean-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return true or false |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900042 | Unknown error |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
function isRemoteUriExample() {
  let uri = "file://com.example.demo/data/storage/el2/base/test.txt?networkid=xxxx";// ?networkid identifies a remote device.
  let fileUriObject = new fileUri.FileUri(uri);
  let ret = fileUriObject.isRemoteUri();
  if (ret) {
      console.info(`It is a remote uri.`);
  }
}
```

## toString

```TypeScript
toString(): string
```

Converts this URI into an encoded string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileUri-toString(): string--><!--Device-FileUri-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | URI in a serialized string. |

## Examples

```TypeScript
let path = pathDir + '/test';
let fileUriObject = new fileUri.FileUri(path);
console.info("The uri of FileUri is " + fileUriObject.toString());
```

## name

```TypeScript
get name(): string
```

Obtains the file name of uri.

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-get name(): string--><!--Device-FileUri-get name(): string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

