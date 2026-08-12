# FileUri

FileUri表示文件的URI，继承自uri.URI。

**继承/实现关系：** FileUri extends [uri.URI](uri.URI)

**起始版本：** 15

<!--Device-fileUri-class FileUri extends uri.URI--><!--Device-fileUri-class FileUri extends uri.URI-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService

## constructor

```TypeScript
constructor(uriOrPath: string)
```

FileUri的构造函数，用于创建FileUri实例。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-FileUri-constructor(uriOrPath: string)--><!--Device-FileUri-constructor(uriOrPath: string)-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uriOrPath | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900005 |
| 14300002 |
| 13900042 |

## 示例

```TypeScript
let pathDir = this.context.filesDir; // 获取应用沙箱路径。
let path = pathDir + '/test';
let uri = fileUri.getUriFromPath(path);  // file://<packageName>/data/storage/el2/base/haps/entry/files/test
let fileUriObject = new fileUri.FileUri(uri);
console.info(`The name of FileUri is ${fileUriObject.name}`);
```

## getFullDirectoryUri

```TypeScript
getFullDirectoryUri(): string
```

获取当前文件URI所在路径的完整目录URI。URI指向目录时直接返回原URI。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-FileUri-getFullDirectoryUri(): string--><!--Device-FileUri-getFullDirectoryUri(): string-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900012 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let pathDir = this.context.filesDir; // 获取应用沙箱路径。
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

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-FileUri-isRemoteUri(): boolean--><!--Device-FileUri-isRemoteUri(): boolean-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900042 |

## 示例

```TypeScript
function isRemoteUriExample() {
  let uri = 'file://com.example.demo/data/storage/el2/base/test.txt?networkid=xxxx'; // ?networkid设备id，远端URI的标识
  let fileUriObject = new fileUri.FileUri(uri);
  let ret = fileUriObject.isRemoteUri();
  if (ret) {
    console.info('It is a remote URI.');
  }
}
```

## name

```TypeScript
get name(): string
```

通过传入的URI获取文件名称。如果文件名中存在百分号编码字符，将解码后拼接在原处。

**类型：** string

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-FileUri-get name(): string--><!--Device-FileUri-get name(): string-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService
