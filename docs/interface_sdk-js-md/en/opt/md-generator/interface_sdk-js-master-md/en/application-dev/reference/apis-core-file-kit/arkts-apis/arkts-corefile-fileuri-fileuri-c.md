# FileUri

FileUri represents the uri of the file.

**Inheritance/Implementation:** FileUri extends [uri.URI](uri.URI)

**Since:** 15

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

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-constructor(uriOrPath: string)--><!--Device-FileUri-constructor(uriOrPath: string)-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uriOrPath | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900005 |
| 14300002 |
| 13900042 |

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

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-getFullDirectoryUri(): string--><!--Device-FileUri-getFullDirectoryUri(): string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900012 |
| 13900042 |

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

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-isRemoteUri(): boolean--><!--Device-FileUri-isRemoteUri(): boolean-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900042 |

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

## name

```TypeScript
get name(): string
```

Obtains the file name of uri.

**Type:** string

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-get name(): string--><!--Device-FileUri-get name(): string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService
