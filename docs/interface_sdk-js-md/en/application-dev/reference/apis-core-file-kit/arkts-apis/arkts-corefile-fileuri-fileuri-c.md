# FileUri

FileUri表示文件的URI，继承自uri.URI。

**Inheritance/Implementation:** FileUri extends [uri.URI](../../apis-arkts/arkts-apis/arkts-arkts-uri-uri-c.md/arkts-arkts-uri-uri-c.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-fileUri-class FileUri extends uri.URI--><!--Device-fileUri-class FileUri extends uri.URI-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

## Modules to Import

```TypeScript
import { fileUri } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor(uriOrPath: string)
```

FileUri的构造函数，用于创建FileUri实例。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-constructor(uriOrPath: string)--><!--Device-FileUri-constructor(uriOrPath: string)-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uriOrPath | string | Yes | URI或路径。 |

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

获取当前文件URI所在路径的完整目录URI。URI指向目录时直接返回原URI。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-getFullDirectoryUri(): string--><!--Device-FileUri-getFullDirectoryUri(): string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回文件所在路径的目录URI；URI指向目录时返回当前URI。 |

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

判断当前URI是否为包含远端标识networkid的远端URI。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-isRemoteUri(): boolean--><!--Device-FileUri-isRemoteUri(): boolean-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示远端URI，返回false表示本地URI。 |

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

将当前URI转换为序列化字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileUri-toString(): string--><!--Device-FileUri-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回字符串类型的URI。 |

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

通过传入的URI获取文件名称。如果文件名中存在百分号编码字符，将解码后拼接在原处。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileUri-get name(): string--><!--Device-FileUri-get name(): string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

