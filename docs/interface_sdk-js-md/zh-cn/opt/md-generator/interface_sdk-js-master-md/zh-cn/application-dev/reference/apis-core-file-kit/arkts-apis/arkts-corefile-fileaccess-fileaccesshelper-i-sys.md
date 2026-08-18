# FileAccessHelper（系统接口）

FileAccessHelper对象。

**起始版本：** 9

**废弃版本：** 23

<!--Device-fileAccess-interface FileAccessHelper--><!--Device-fileAccess-interface FileAccessHelper-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## access

```TypeScript
access(sourceFileUri: string) : Promise<boolean>
```

以异步方法判断文件(夹)是否存在。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** access(path: string, mode?: AccessModeType)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-access(sourceFileUri: string) : Promise<boolean>--><!--Device-FileAccessHelper-access(sourceFileUri: string) : Promise<boolean>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceFileUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceDir表示Download目录下文件，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
async function accessFunc() {
  let sourceDir: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let existJudgment = await fileAccessHelper.access(sourceDir);
      if (existJudgment) {
        console.info("sourceDir exists");
      } else {
        console.info("sourceDir does not exist");
      }
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("access failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## access

```TypeScript
access(sourceFileUri: string, callback: AsyncCallback<boolean>): void
```

以异步方法判断文件(夹)是否存在。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** access(path: string, callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-access(sourceFileUri: string, callback: AsyncCallback<boolean>): void--><!--Device-FileAccessHelper-access(sourceFileUri: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceFileUri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceDir表示Download目录下文件夹，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let sourceDir: string = "file://docs/storage/Users/currentUser/Download/test";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.access(sourceDir, (err: BusinessError, existJudgment: boolean) => {
      if (err) {
        console.error("Failed to access in async, errCode:" + err.code + ", errMessage:" + err.message);
        return;
      }
      if (existJudgment)
        console.info("sourceDir exists");
      else
        console.info("sourceDir does not exist");
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("access failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## copy

```TypeScript
copy(sourceUri: string, destUri: string, force?: boolean): Promise<Array<CopyResult>>
```

复制文件或目录，使用 Promise 异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** copy(srcUri: string, destUri: string, options?: CopyOptions)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, force?: boolean): Promise<Array<CopyResult>>--><!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, force?: boolean): Promise<Array<CopyResult>>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| force | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; |

## copy

```TypeScript
copy(sourceUri: string, destUri: string, callback: AsyncCallback<Array<CopyResult>>): void
```

复制文件或目录，使用 callback 异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** copy(srcUri: string, destUri: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, callback: AsyncCallback<Array<CopyResult>>): void--><!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, callback: AsyncCallback<Array<CopyResult>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
// 以内置存储目录为例
// 示例代码中的sourceFile表示Download目录下的源文件(夹)，destFile表示Download目录下的目标文件夹，该uri对应fileInfo中的uri
// 开发者应根据自己实际获取的uri进行开发
let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.copy(sourceFile, destFile, async (err: BusinessError, copyResult: Array<fileAccess.CopyResult>) => {
      if (err) {
        console.error("copy failed, errCode:" + err.code + ", errMessage:" + err.message);
      }
      if (copyResult.length === 0) {
        console.info("copy success");
      } else {
        for (let i = 0; i < copyResult.length; i++) {
          console.error("errCode" + copyResult[i].errCode);
          console.error("errMsg" + copyResult[i].errMsg);
          console.error("sourceUri" + copyResult[i].sourceUri);
          console.error("destUri" + copyResult[i].destUri);
        }
      }
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("copy failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## copy

```TypeScript
copy(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<CopyResult>>): void
```

复制文件或目录，含有同名文件时可以选择是否强制覆盖原文件，使用 callback 异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<CopyResult>>): void--><!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<CopyResult>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| force | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
// 以内置存储目录为例
// 示例代码中的sourceFile表示Download目录下的源文件(夹)，destFile表示Download目录下的目标文件夹，该uri对应fileInfo中的uri
// 开发者应根据自己实际获取的uri进行开发
let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.copy(sourceFile, destFile, true, async (err: BusinessError, copyResult: Array<fileAccess.CopyResult>) => {
      if (err) {
        console.error("copy failed, errCode:" + err.code + ", errMessage:" + err.message);
      }
      if (copyResult.length === 0) {
        console.info("copy success");
      } else {
        for (let i = 0; i < copyResult.length; i++) {
          console.error("errCode" + copyResult[i].errCode);
          console.error("errMsg" + copyResult[i].errMsg);
          console.error("sourceUri" + copyResult[i].sourceUri);
          console.error("destUri" + copyResult[i].destUri);
        }
      }
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("copy failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## copyFile

```TypeScript
copyFile(sourceUri: string, destUri: string, fileName: string): Promise<string>
```

复制文件并传入备用文件名，使用Promise异步回调。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** copyFile(src: string | number, dest: string | number, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileAccessHelper-copyFile(sourceUri: string, destUri: string, fileName: string): Promise<string>--><!--Device-FileAccessHelper-copyFile(sourceUri: string, destUri: string, fileName: string): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| fileName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 13900042 |
| 14300004 |
| 13900011 |

## copyFile

```TypeScript
copyFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void
```

复制文件并传入备用文件名，使用callback异步回调。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** copyFile(src: string | number, dest: string | number, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileAccessHelper-copyFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-copyFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| fileName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 13900042 |
| 14300004 |
| 13900011 |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
// 以内置存储目录为例
// 示例代码中的sourceFile表示Download目录下的源文件(夹)，destFile表示Download目录下的目标文件夹，该uri对应fileInfo中的uri
// 开发者应根据自己实际获取的uri进行开发
let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
let fileName: string = "2.txt";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.copyFile(sourceFile, destFile, fileName, async (err: BusinessError, copyResult: string) => {
          console.info("copyResult uri: " + copyResult);
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("copy failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## createFile

```TypeScript
createFile(uri: string, displayName: string) : Promise<string>
```

以异步方法创建文件到指定目录，返回新文件uri。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-createFile(uri: string, displayName: string) : Promise<string>--><!--Device-FileAccessHelper-createFile(uri: string, displayName: string) : Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| displayName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
async function createFile() {
  // 以内置存储目录为例
  // 示例代码sourceUri表示Download目录，该uri是对应的fileInfo中uri
  // 开发者应根据自己实际获取的uri进行开发
  let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
  let displayName: string = "file1";
  let fileUri: string;
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
      if (fileAccessHelper != undefined) {
      fileUri = await fileAccessHelper.createFile(sourceUri, displayName);
      if (!fileUri) {
        console.error("createFile return undefined object");
        return;
      }
      console.info("createFile success, fileUri: " + JSON.stringify(fileUri));       
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("createFile failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## createFile

```TypeScript
createFile(uri: string, displayName: string, callback: AsyncCallback<string>): void
```

以异步方法创建文件到指定目录，返回新文件uri。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** createRandomAccessFile(file: string | File, callback: AsyncCallback&lt;RandomAccessFile&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-createFile(uri: string, displayName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-createFile(uri: string, displayName: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| displayName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceUri表示Download目录，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
let displayName: string = "file1";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.createFile(sourceUri, displayName, (err: BusinessError, fileUri: string) => {
      if (err) {
        console.error("Failed to createFile in async, errCode:" + err.code + ", errMessage:" + err.message);
      }
      console.info("createFile success, fileUri: " + JSON.stringify(fileUri));
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("createFile failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## delete

```TypeScript
delete(uri: string) : Promise<number>
```

以异步方法删除文件(夹)，返回错误码。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [delete](arkts-corefile-file-fs-atomicfile-c.md#delete)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-delete(uri: string) : Promise<number>--><!--Device-FileAccessHelper-delete(uri: string) : Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
async function deleteFile01() {
  // 以内置存储目录为例
  // 示例代码targetUri表示Download目录下文件，该uri是对应的fileInfo中uri
  // 开发者应根据自己实际获取的uri进行开发
  let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let code = await fileAccessHelper.delete(targetUri);
      if (code != 0)
        console.error("delete failed, code " + code);
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("delete failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## delete

```TypeScript
delete(uri: string, callback: AsyncCallback<number>): void
```

以异步方法删除文件(夹)，返回错误码。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [delete](arkts-corefile-file-fs-atomicfile-c.md#delete)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-delete(uri: string, callback: AsyncCallback<number>): void--><!--Device-FileAccessHelper-delete(uri: string, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码targetUri表示Download目录下文件，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.delete(targetUri, (err: BusinessError, code: number) => {
      if (err) {
        console.error("Failed to delete in async, errCode:" + err.code + ", errMessage:" + err.message);
      }
      console.info("delete success, code: " + code);
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("delete failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## getFileInfoFromRelativePath

```TypeScript
getFileInfoFromRelativePath(relativePath: string) : Promise<FileInfo>
```

以异步方法获取relativePath对应的FileInfo对象。使用promise异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getFileInfoFromRelativePath(relativePath: string) : Promise<FileInfo>--><!--Device-FileAccessHelper-getFileInfoFromRelativePath(relativePath: string) : Promise<FileInfo>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relativePath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;FileInfo & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 示例代码relativePath表示Download目录，该relativePath是对应的fileInfo中relativePath
// 开发者应根据自己实际获取的relativePath进行开发
async function getRelativePath() {
  let relativePath: string = "Download/";
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let fileInfo = await fileAccessHelper.getFileInfoFromRelativePath(relativePath);
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("getFileInfoFromRelativePath failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## getFileInfoFromRelativePath

```TypeScript
getFileInfoFromRelativePath(relativePath: string, callback: AsyncCallback<FileInfo>) : void
```

以异步方法获取relativePath对应的FileInfo对象。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getFileInfoFromRelativePath(relativePath: string, callback: AsyncCallback<FileInfo>) : void--><!--Device-FileAccessHelper-getFileInfoFromRelativePath(relativePath: string, callback: AsyncCallback<FileInfo>) : void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relativePath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileInfo&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 示例代码relativePath表示Download目录，该relativePath是对应的fileInfo中relativePath
// 开发者应根据自己实际获取的relativePath进行开发
let relativePath: string = "Download/";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.getFileInfoFromRelativePath(relativePath, (err: BusinessError, fileInfo: fileAccess.FileInfo) => {
      if (err) {
        console.error("Failed to getFileInfoFromRelativePath in async, errCode:" + err.code + ", errMessage:" + err.message);
        return;
      }
      console.info("getFileInfoFromRelativePath success, fileInfo: " + JSON.stringify(fileInfo));
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getFileInfoFromRelativePath failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## getFileInfoFromUri

```TypeScript
getFileInfoFromUri(uri: string) : Promise<FileInfo>
```

以异步方法获取uri对应的FileInfo对象。使用promise异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getFileInfoFromUri(uri: string) : Promise<FileInfo>--><!--Device-FileAccessHelper-getFileInfoFromUri(uri: string) : Promise<FileInfo>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;FileInfo & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceUri表示Download目录，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
async function getUri() {
  let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let fileInfo = await fileAccessHelper.getFileInfoFromUri(sourceUri);
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("getFileInfoFromUri failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## getFileInfoFromUri

```TypeScript
getFileInfoFromUri(uri: string, callback: AsyncCallback<FileInfo>) : void
```

以异步方法获取uri对应的FileInfo对象。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getFileInfoFromUri(uri: string, callback: AsyncCallback<FileInfo>) : void--><!--Device-FileAccessHelper-getFileInfoFromUri(uri: string, callback: AsyncCallback<FileInfo>) : void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileInfo&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceUri表示Download目录，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.getFileInfoFromUri(sourceUri, (err: BusinessError, fileInfo: fileAccess.FileInfo) => {
      if (err) {
        console.error("Failed to getFileInfoFromUri in async, errCode:" + err.code + ", errMessage:" + err.message);
        return;
      }
      console.info("getFileInfoFromUri success, fileInfo: " + JSON.stringify(fileInfo));
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getFileInfoFromUri failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## getRoots

```TypeScript
getRoots(): Promise<RootIterator>
```

以异步方法获取helper对象连接的文件管理服务类的设备根节点信息。使用Promise异步回调。 该方法返回迭代器对象RootIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回[RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md#rootinfo系统接口)。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getRoots(): Promise<RootIterator>--><!--Device-FileAccessHelper-getRoots(): Promise<RootIterator>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
async function getRoots() {
  let rootIterator: fileAccess.RootIterator;
  let rootinfos: Array<fileAccess.RootInfo> = [];
  let isDone: boolean = false;
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      rootIterator = await fileAccessHelper.getRoots();
      if (!rootIterator) {
        console.error("getRoots interface returns an undefined object");
      }
      while (!isDone) {
        let result = rootIterator.next();
        console.info("next result = " + JSON.stringify(result));
        isDone = result.done;
        if (!isDone) {
          rootinfos.push(result.value);
        }
      }     
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("getRoots failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## getRoots

```TypeScript
getRoots(callback: AsyncCallback<RootIterator>): void
```

以异步方法获取helper对象连接的文件管理服务类的设备根节点信息。使用callback异步回调。 callback带回迭代器对象RootIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回 [RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md#rootinfo系统接口)。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getRoots(callback: AsyncCallback<RootIterator>): void--><!--Device-FileAccessHelper-getRoots(callback: AsyncCallback<RootIterator>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
async function getRoots() {
  let rootinfos: Array<fileAccess.RootInfo> = [];
  let isDone: boolean = false;
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      fileAccessHelper.getRoots((err: BusinessError, rootIterator: fileAccess.RootIterator) => {
        if (err) {
          console.error("Failed to getRoots in async, errCode:" + err.code + ", errMessage:" + err.message);
        }
        while (!isDone) {
          let result = rootIterator.next();
          console.info("next result = " + JSON.stringify(result));
          isDone = result.done;
          if (!isDone) {
            rootinfos.push(result.value);
          }
        }
      });       
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("getRoots failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## mkDir

```TypeScript
mkDir(parentUri: string, displayName: string) : Promise<string>
```

以异步方法创建文件夹到指定目录，返回文件夹uri。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** mkdir(path: string)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-mkDir(parentUri: string, displayName: string) : Promise<string>--><!--Device-FileAccessHelper-mkDir(parentUri: string, displayName: string) : Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parentUri | string | 是 |
| displayName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceUri表示Download目录，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
async function createDirectory() {
  let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
  let dirName: string = "dirTest";
  let dirUri: string;
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      dirUri = await fileAccessHelper.mkDir(sourceUri, dirName);
      if (!dirUri) {
        console.error("mkDir return undefined object");
      } else {
        console.info("mkDir success, dirUri: " + JSON.stringify(dirUri));
      }
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("mkDir failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## mkDir

```TypeScript
mkDir(parentUri: string, displayName: string, callback: AsyncCallback<string>): void
```

以异步方法创建文件夹到指定目录，返回文件夹uri。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** mkdir(path: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-mkDir(parentUri: string, displayName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-mkDir(parentUri: string, displayName: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parentUri | string | 是 |
| displayName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceUri表示Download目录，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
let dirName: string = "dirTest";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.mkDir(sourceUri, dirName, (err: BusinessError, dirUri: string) => {
      if (err) {
        console.error("Failed to mkDir in async, errCode:" + err.code + ", errMessage:" + err.message);
      }
      console.info("mkDir success, dirUri: " + JSON.stringify(dirUri));
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("mkDir failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## move

```TypeScript
move(sourceFile: string, destFile: string) : Promise<string>
```

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用Promise异步回调。目前仅支持设备内移动，跨设备不支持移动。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-move(sourceFile: string, destFile: string) : Promise<string>--><!--Device-FileAccessHelper-move(sourceFile: string, destFile: string) : Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceFile | string | 是 |
| [destFile](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
async function moveFile01() {
  // 以内置存储目录为例
  // 示例代码sourceFile destFile表示Download目录下文件和文件夹，该uri是对应的fileInfo中uri
  // 开发者应根据自己实际获取的uri进行开发
  let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let fileUri = await fileAccessHelper.move(sourceFile, destFile);
      console.info("move success, fileUri: " + JSON.stringify(fileUri));
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("move failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## move

```TypeScript
move(sourceFile: string, destFile: string, callback: AsyncCallback<string>): void
```

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用callback异步回调。目前仅支持设备内移动，跨设备不支持移动。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-move(sourceFile: string, destFile: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-move(sourceFile: string, destFile: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceFile | string | 是 |
| [destFile](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceFile destFile表示Download目录下文件和文件夹，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.move(sourceFile, destFile, (err: BusinessError, fileUri: string) => {
      if (err) {
        console.error("Failed to move in async, errCode:" + err.code + ", errMessage:" + err.message);
      }
      console.info("move success, fileUri: " + JSON.stringify(fileUri));
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("move failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## moveFile

```TypeScript
moveFile(sourceUri: string, destUri: string, fileName: string): Promise<string>
```

以异步方法移动文件，返回移动后文件的uri。使用Promise异步回调。 当存在同名文件时（即发生文件移动冲突时），可以重命名待移动的文件，再保存到目标文件夹。 目前仅支持设备内移动，跨设备不支持移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileAccessHelper-moveFile(sourceUri: string, destUri: string, fileName: string): Promise<string>--><!--Device-FileAccessHelper-moveFile(sourceUri: string, destUri: string, fileName: string): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| fileName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 13900042 |
| 14300004 |
| 13900011 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
async function moveFile01() {
  // 以内置存储目录为例
  // 示例代码sourceUri destUri表示Download目录下文件和文件夹，该uri是对应的fileInfo中uri
  // 开发者应根据自己实际获取的uri进行开发
  let sourceUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  let destUri: string = "file://docs/storage/Users/currentUser/Download/test";
  let fileName: string = "2.txt";
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
  if (fileAccessHelper != undefined) {
      let fileUri = await fileAccessHelper.moveFile(sourceUri, destUri, fileName);
      console.info("moveFile success, fileUri: " + JSON.stringify(fileUri));
  }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("moveFile failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## moveFile

```TypeScript
moveFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void
```

以异步方法移动文件，返回移动后文件的uri。使用callback异步回调。 当存在同名文件时（即发生文件移动冲突时），可以重命名待移动的文件，再保存到目标文件夹。 当前仅支持设备内移动，不支持跨设备移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileAccessHelper-moveFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-moveFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| fileName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 13900042 |
| 14300004 |
| 13900011 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceUri destUri表示Download目录下文件和文件夹，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let sourceUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destUri: string = "file://docs/storage/Users/currentUser/Download/test";
let fileName: string = "2.txt";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.moveFile(sourceUri, destUri, fileName, (err: BusinessError, fileUri: string) => {
      if (err) {
        console.error("Failed to moveFile in async, errCode:" + err.code + ", errMessage:" + err.message);
      }
      console.info("moveFile success, fileUri: " + JSON.stringify(fileUri));
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("moveFile failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## moveItem

```TypeScript
moveItem(sourceUri: string, destUri: string, force?: boolean): Promise<Array<MoveResult>>
```

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用Promise异步回调。 当存在同名文件时，可以选择强制覆盖文件。 目前仅支持设备内移动，跨设备不支持移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, force?: boolean): Promise<Array<MoveResult>>--><!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, force?: boolean): Promise<Array<MoveResult>>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| force | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 13900042 |
| 14300004 |
| 13900011 |

## moveItem

```TypeScript
moveItem(sourceUri: string, destUri: string, callback: AsyncCallback<Array<MoveResult>>): void
```

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用callback异步回调。 当前仅支持设备内移动，不支持跨设备移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, callback: AsyncCallback<Array<MoveResult>>): void--><!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, callback: AsyncCallback<Array<MoveResult>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 13900042 |
| 14300004 |
| 13900011 |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
// 以内置存储目录为例
// 示例代码中的sourceFile表示Download目录下的源文件(夹)，destFile表示Download目录下的目标文件夹，该uri对应fileInfo中的uri
// 开发者应根据自己实际获取的uri进行开发
let sourceUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destUri: string = "file://docs/storage/Users/currentUser/Download/test";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.moveItem(sourceUri, destUri, async (err: BusinessError, moveResult: Array<fileAccess.MoveResult>) => {
      if (err) {
        console.error("moveItem failed, errCode:" + err.code + ", errMessage:" + err.message);
      }
      if (moveResult.length === 0) {
        console.info("moveItem success");
      } else {
        for (let i = 0; i < moveResult.length; i++) {
          console.error("errCode" + moveResult[i].errCode);
          console.error("errMsg" + moveResult[i].errMsg);
          console.error("sourceUri" + moveResult[i].sourceUri);
          console.error("destUri" + moveResult[i].destUri);
        }
      }
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("moveItem failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## moveItem

```TypeScript
moveItem(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<MoveResult>>): void
```

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用callback异步回调。 当存在同名文件时，可以选择强制覆盖文件。 当前仅支持设备内移动，不支持跨设备移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<MoveResult>>): void--><!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<MoveResult>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| force | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 13900042 |
| 14300004 |
| 13900011 |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
// 以内置存储目录为例
// 示例代码中的sourceFile表示Download目录下的源文件(夹)，destFile表示Download目录下的目标文件夹，该uri对应fileInfo中的uri
// 开发者应根据自己实际获取的uri进行开发
let sourceUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destUri: string = "file://docs/storage/Users/currentUser/Download/test";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.moveItem(sourceUri, destUri, true, async (err: BusinessError, moveResult: Array<fileAccess.MoveResult>) => {
      if (err) {
        console.error("moveItem failed, errCode:" + err.code + ", errMessage:" + err.message);
      }
      if (moveResult.length === 0) {
        console.info("moveItem success");
      } else {
        for (let i = 0; i < moveResult.length; i++) {
          console.error("errCode" + moveResult[i].errCode);
          console.error("errMsg" + moveResult[i].errMsg);
          console.error("sourceUri" + moveResult[i].sourceUri);
          console.error("destUri" + moveResult[i].destUri);
        }
      }
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("moveItem failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## openFile

```TypeScript
openFile(uri: string, flags: OPENFLAGS) : Promise<number>
```

以异步方法打开文件，返回文件描述符。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** open(path: string, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-openFile(uri: string, flags: OPENFLAGS) : Promise<number>--><!--Device-FileAccessHelper-openFile(uri: string, flags: OPENFLAGS) : Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flags | [OPENFLAGS](arkts-corefile-fileaccess-openflags-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
async function openFile01() {
  // 以内置存储目录为例
  // 示例代码targetUri表示Download目录下文件，该uri是对应的fileInfo中uri
  // 开发者应根据自己实际获取的uri进行开发
  let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let fd = await fileAccessHelper.openFile(targetUri, fileAccess.OPENFLAGS.READ);
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("openFile failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## openFile

```TypeScript
openFile(uri: string, flags: OPENFLAGS, callback: AsyncCallback<number>): void
```

以异步方法打开文件，返回文件描述符。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** open(path: string, callback: AsyncCallback&lt;File&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-openFile(uri: string, flags: OPENFLAGS, callback: AsyncCallback<number>): void--><!--Device-FileAccessHelper-openFile(uri: string, flags: OPENFLAGS, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flags | [OPENFLAGS](arkts-corefile-fileaccess-openflags-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码targetUri表示Download目录下文件，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.openFile(targetUri, fileAccess.OPENFLAGS.READ, (err: BusinessError, fd: number) => {
      if (err) {
        console.error("Failed to openFile in async, errCode:" + err.code + ", errMessage:" + err.message);
      }
      console.info("openFile success, fd: " + fd);
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("openFile failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## query

```TypeScript
query(uri: string, metaJson: string) : Promise<string>
```

通过uri查询文件或目录的相关信息，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-query(uri: string, metaJson: string) : Promise<string>--><!--Device-FileAccessHelper-query(uri: string, metaJson: string) : Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| metaJson | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
async function getQuery01() {
  let imageFileRelativePath: string = "/storage/Users/currentUser/Download/queryTest/image/01.jpg";
  let jsonStrSingleRelativepath: string = JSON.stringify({ [fileAccess.FileKey.RELATIVE_PATH]: "" });
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let fileInfo = await fileAccessHelper.getFileInfoFromRelativePath(imageFileRelativePath);
      let queryResult = await fileAccessHelper.query(fileInfo.uri, jsonStrSingleRelativepath);
      console.info("query_file_single faf query, queryResult.relative_path: " + JSON.parse(queryResult).relative_path);
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("query_file_single faf query failed, error.code :" + error.code + ", errorMessage :" + error.message);
  }
}
```

## query

```TypeScript
query(uri: string, metaJson: string, callback: AsyncCallback<string>) : void
```

通过uri查询文件或目录的相关信息，使用callback异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-query(uri: string, metaJson: string, callback: AsyncCallback<string>) : void--><!--Device-FileAccessHelper-query(uri: string, metaJson: string, callback: AsyncCallback<string>) : void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| metaJson | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
async function getQuery02() {
  let imageFileRelativePath: string = "/storage/Users/currentUser/Download/queryTest/image/01.jpg";
  let jsonStrSingleRelativepath: string = JSON.stringify({ [fileAccess.FileKey.RELATIVE_PATH]: "" });
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let fileInfo = await fileAccessHelper.getFileInfoFromRelativePath(imageFileRelativePath);
      fileAccessHelper.query(fileInfo.uri, jsonStrSingleRelativepath, (err: BusinessError, queryResult: string) => {
        if (err) {
          console.error(`query_file_single faf query Failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        console.info("query_file_single faf query, queryResult.relative_path: " + JSON.parse(queryResult).relative_path);
      })
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("query_file_single faf query failed, error.code :" + error.code + ", errorMessage :" + error.message);
  }
}
```

## registerObserver

```TypeScript
registerObserver(uri: string, notifyForDescendants: boolean, callback: Callback<NotifyMessage>): void
```

注册指定uri的callback。uri与callback可以为多对多的关系，推荐使用一个callback监听一个uri。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** createWatcher

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-registerObserver(uri: string, notifyForDescendants: boolean, callback: Callback<NotifyMessage>): void--><!--Device-FileAccessHelper-registerObserver(uri: string, notifyForDescendants: boolean, callback: Callback<NotifyMessage>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| notifyForDescendants | boolean | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 14300002 |

## rename

```TypeScript
rename(uri: string, displayName: string) : Promise<string>
```

以异步方法重命名文件(夹)，返回重命名后的文件(夹)的Uri。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** rename(oldPath: string, newPath: string)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-rename(uri: string, displayName: string) : Promise<string>--><!--Device-FileAccessHelper-rename(uri: string, displayName: string) : Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| displayName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
async function renameFile01() {
  // 以内置存储目录为例
  // 示例代码sourceDir表示Download目录下文件，该uri是对应的fileInfo中uri
  // 开发者应根据自己实际获取的uri进行开发
  let sourceDir: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  // fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let DestDir = await fileAccessHelper.rename(sourceDir, "testDir");
      console.info("rename success, DestDir: " + JSON.stringify(DestDir));
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("rename failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## rename

```TypeScript
rename(uri: string, displayName: string, callback: AsyncCallback<string>): void
```

以异步方法重命名文件(夹)，返回重命名后的文件(夹)的Uri。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** rename(oldPath: string, newPath: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-rename(uri: string, displayName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-rename(uri: string, displayName: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| displayName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// 以内置存储目录为例
// 示例代码sourceDir表示Download目录下文件，该uri是对应的fileInfo中uri
// 开发者应根据自己实际获取的uri进行开发
let sourceDir: string = "file://docs/storage/Users/currentUser/Download/1.txt";
// fileAccessHelper 参考 fileAccess.createFileAccessHelper 示例代码获取
let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
try {
  if (fileAccessHelper != undefined) {
    fileAccessHelper.rename(sourceDir, "testDir", (err: BusinessError, DestDir: string) => {
      if (err) {
        console.error("Failed to rename in async, errCode:" + err.code + ", errMessage:" + err.message);
      }
      console.info("rename success, DestDir: " + JSON.stringify(DestDir));
    });
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("rename failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## unregisterObserver

```TypeScript
unregisterObserver(uri: string, callback?: Callback<NotifyMessage>): void
```

取消注册指定的uri和callback。

**起始版本：** 10

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-unregisterObserver(uri: string, callback?: Callback<NotifyMessage>): void--><!--Device-FileAccessHelper-unregisterObserver(uri: string, callback?: Callback<NotifyMessage>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| 14300002 |
