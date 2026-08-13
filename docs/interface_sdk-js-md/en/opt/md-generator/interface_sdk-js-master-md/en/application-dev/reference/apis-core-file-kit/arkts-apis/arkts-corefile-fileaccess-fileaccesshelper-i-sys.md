# FileAccessHelper (System API)

Provides a **FileAccessHelper** object.

**Since:** 9

**Deprecated since:** 23

<!--Device-fileAccess-interface FileAccessHelper--><!--Device-fileAccess-interface FileAccessHelper-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fileAccess } from '@kit.CoreFileKit';
```

## access

```TypeScript
access(sourceFileUri: string) : Promise<boolean>
```

Checks whether a file or directory exists. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** access(path: string, mode?: AccessModeType)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-access(sourceFileUri: string) : Promise<boolean>--><!--Device-FileAccessHelper-access(sourceFileUri: string) : Promise<boolean>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceFileUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

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
// A built-in storage directory is used as an example.
// In the sample code, sourceDir indicates a file in the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
async function accessFunc() {
  let sourceDir: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Checks whether a file or directory exists. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** access(path: string, callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-access(sourceFileUri: string, callback: AsyncCallback<boolean>): void--><!--Device-FileAccessHelper-access(sourceFileUri: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceFileUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

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
// A built-in storage directory is used as an example.
// In the sample code, sourceDir indicates a directory in the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceDir: string = "file://docs/storage/Users/currentUser/Download/test";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Copies a file or directory. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** copy(srcUri: string, destUri: string, options?: CopyOptions)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, force?: boolean): Promise<Array<CopyResult>>--><!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, force?: boolean): Promise<Array<CopyResult>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| force | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; |

## copy

```TypeScript
copy(sourceUri: string, destUri: string, callback: AsyncCallback<Array<CopyResult>>): void
```

Copies a file or directory. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** copy(srcUri: string, destUri: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, callback: AsyncCallback<Array<CopyResult>>): void--><!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, callback: AsyncCallback<Array<CopyResult>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
// A built-in storage directory is used as an example.
// In the sample code, sourceFile indicates the file (directory) in the Download directory to copy, destFile indicates the destination directory in the Download directory, and URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Copies a file or directory. If a file with the same name already exists, you can choose whether to forcibly overwrite the original file. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<CopyResult>>): void--><!--Device-FileAccessHelper-copy(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<CopyResult>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| force | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
// A built-in storage directory is used as an example.
// In the sample code, sourceFile indicates the file (directory) in the Download directory to copy, destFile indicates the destination directory in the Download directory, and URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Copies a file with an alternative file name. This API uses a promise to return the result.

**Since:** 11

**Deprecated since:** 23

**Substitutes:** copyFile(src: string | number, dest: string | number, mode?: number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileAccessHelper-copyFile(sourceUri: string, destUri: string, fileName: string): Promise<string>--><!--Device-FileAccessHelper-copyFile(sourceUri: string, destUri: string, fileName: string): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| fileName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
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

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
// A built-in storage directory is used as an example.
// In the sample code, sourceFile indicates the file (directory) in the Download directory to copy, destFile indicates the destination directory in the Download directory, and URI is the URI in fileInfo.
// You can use the URI obtained.
async function copyFunc01() {
  let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
  let fileName: string = "2.txt";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
  let fileAccessHelper : fileAccess.FileAccessHelper|undefined;
  try {
    if (fileAccessHelper != undefined) {
      let copyResult = await fileAccessHelper.copyFile(sourceFile, destFile, fileName);
      console.info("copyResult uri: " + copyResult);
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("copy failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## copyFile

```TypeScript
copyFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void
```

Copies a file with an alternative file name. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** 23

**Substitutes:** copyFile(src: string | number, dest: string | number, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileAccessHelper-copyFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-copyFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| fileName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
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

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
// A built-in storage directory is used as an example.
// In the sample code, sourceFile indicates the file (directory) in the Download directory to copy, destFile indicates the destination directory in the Download directory, and URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
let fileName: string = "2.txt";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Creates a file in a directory. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-createFile(uri: string, displayName: string) : Promise<string>--><!--Device-FileAccessHelper-createFile(uri: string, displayName: string) : Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| displayName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

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
async function createFile() {
  // A built-in storage directory is used as an example.
  // In the sample code, sourceUri indicates the Download directory. The URI is the URI in fileInfo.
  // You can use the URI obtained.
  let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
  let displayName: string = "file1";
  let fileUri: string;
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Creates a file in a directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** createRandomAccessFile(file: string | File, callback: AsyncCallback&lt;RandomAccessFile&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-createFile(uri: string, displayName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-createFile(uri: string, displayName: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

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
// A built-in storage directory is used as an example.
// In the sample code, sourceUri indicates the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
let displayName: string = "file1";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Deletes a file or directory. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [delete](arkts-corefile-file-fs-atomicfile-c.md#delete)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-delete(uri: string) : Promise<number>--><!--Device-FileAccessHelper-delete(uri: string) : Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

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
async function deleteFile01() {
  // A built-in storage directory is used as an example.
  // In the sample code, targetUri indicates a file in the Download directory. The URI is the URI in fileInfo.
  // You can use the URI obtained.
  let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Deletes a file or directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [delete](arkts-corefile-file-fs-atomicfile-c.md#delete)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-delete(uri: string, callback: AsyncCallback<number>): void--><!--Device-FileAccessHelper-delete(uri: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

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
// A built-in storage directory is used as an example.
// In the sample code, targetUri indicates a file in the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Obtains a **FileInfo** object based on a relative path. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getFileInfoFromRelativePath(relativePath: string) : Promise<FileInfo>--><!--Device-FileAccessHelper-getFileInfoFromRelativePath(relativePath: string) : Promise<FileInfo>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relativePath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;FileInfo & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// In the sample code, relativePath indicates the Download directory, which is the relativePath in fileInfo.
// You can use the relativePath obtained.
async function getRelativePath() {
  let relativePath: string = "Download/";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Obtains a **FileInfo** object based on a relative path. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getFileInfoFromRelativePath(relativePath: string, callback: AsyncCallback<FileInfo>) : void--><!--Device-FileAccessHelper-getFileInfoFromRelativePath(relativePath: string, callback: AsyncCallback<FileInfo>) : void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relativePath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileInfo&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// In the sample code, relativePath indicates the Download directory, which is the relativePath in fileInfo.
// You can use the relativePath obtained.
let relativePath: string = "Download/";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Obtains a **FileInfo** object based on a URI. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getFileInfoFromUri(uri: string) : Promise<FileInfo>--><!--Device-FileAccessHelper-getFileInfoFromUri(uri: string) : Promise<FileInfo>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;FileInfo & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// A built-in storage directory is used as an example.
// In the sample code, sourceUri indicates the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
async function getUri() {
  let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Obtains a **FileInfo** object based on a URI. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getFileInfoFromUri(uri: string, callback: AsyncCallback<FileInfo>) : void--><!--Device-FileAccessHelper-getFileInfoFromUri(uri: string, callback: AsyncCallback<FileInfo>) : void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileInfo&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// A built-in storage directory is used as an example.
// In the sample code, sourceUri indicates the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Obtains information about the device root nodes of the file management services associated with the **Helper** object. This API uses a promise to return a **RootIterator** object. You can use [next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next) to return [RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md#RootInfo-(System-API)).

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getRoots(): Promise<RootIterator>--><!--Device-FileAccessHelper-getRoots(): Promise<RootIterator>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md)&gt; |

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
async function getRoots() {
  let rootIterator: fileAccess.RootIterator;
  let rootinfos: Array<fileAccess.RootInfo> = [];
  let isDone: boolean = false;
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Obtains information about the device root nodes of the file management services associated with the **Helper** object. This API uses an asynchronous callback to return a **RootIterator** object. You can use [next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next) to return [RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md#RootInfo-(System-API)).

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-getRoots(callback: AsyncCallback<RootIterator>): void--><!--Device-FileAccessHelper-getRoots(callback: AsyncCallback<RootIterator>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md)&gt; | Yes |

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
async function getRoots() {
  let rootinfos: Array<fileAccess.RootInfo> = [];
  let isDone: boolean = false;
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Creates a directory in a specified directory. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** mkdir(path: string)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-mkDir(parentUri: string, displayName: string) : Promise<string>--><!--Device-FileAccessHelper-mkDir(parentUri: string, displayName: string) : Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parentUri | string | Yes |
| displayName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

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
// A built-in storage directory is used as an example.
// In the sample code, sourceUri indicates the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
async function createDirectory() {
  let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
  let dirName: string = "dirTest";
  let dirUri: string;
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Creates a directory in a specified directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** mkdir(path: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-mkDir(parentUri: string, displayName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-mkDir(parentUri: string, displayName: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parentUri | string | Yes |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

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
// A built-in storage directory is used as an example.
// In the sample code, sourceUri indicates the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceUri: string = "file://docs/storage/Users/currentUser/Download";
let dirName: string = "dirTest";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Moves a file or directory. This API uses a promise to return the result. Currently, this API does not support move of files or directories across devices.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, mode?: number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-move(sourceFile: string, destFile: string) : Promise<string>--><!--Device-FileAccessHelper-move(sourceFile: string, destFile: string) : Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceFile | string | Yes |
| [destFile](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

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
async function moveFile01() {
  // A built-in storage directory is used as an example.
  // In the sample code, sourceFile and destFile indicate the files and directories in the Download directory. The URI is the URI in fileInfo.
  // You can use the URI obtained.
  let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Moves a file or directory. This API uses an asynchronous callback to return the result. Currently, this API does not support move of files or directories across devices.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-move(sourceFile: string, destFile: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-move(sourceFile: string, destFile: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceFile | string | Yes |
| [destFile](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md) | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

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
// A built-in storage directory is used as an example.
// In the sample code, sourceFile and destFile indicate the files and directories in the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceFile: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destFile: string = "file://docs/storage/Users/currentUser/Download/test";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Moves a file, and renames it if a file with the same name already exists in the destination directory. This API uses a promise to return the result. If a file with the same name exists (that is, a file moving conflict occurs), you can rename the file to be moved and save it to the destination directory. Currently, this API does not support move of files across devices.

**Since:** 11

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, mode?: number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileAccessHelper-moveFile(sourceUri: string, destUri: string, fileName: string): Promise<string>--><!--Device-FileAccessHelper-moveFile(sourceUri: string, destUri: string, fileName: string): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| fileName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
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

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
async function moveFile01() {
  // A built-in storage directory is used as an example.
  // In the sample code, sourceUri and destUri indicate the files or directories in the Download directory. The URI is the URI in fileInfo.
  // You can use the URI obtained.
  let sourceUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  let destUri: string = "file://docs/storage/Users/currentUser/Download/test";
  let fileName: string = "2.txt";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Moves a file, and renames it if a file with the same name already exists in the destination directory. This API uses an asynchronous callback to return the result. If a file with the same name exists (that is, a file moving conflict occurs), you can rename the file to be moved and save it to the destination directory. Currently, this API does not support move of files across devices.

**Since:** 11

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileAccessHelper-moveFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-moveFile(sourceUri: string, destUri: string, fileName: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| fileName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
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

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// A built-in storage directory is used as an example.
// In the sample code, sourceUri and destUri indicate the files or directories in the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destUri: string = "file://docs/storage/Users/currentUser/Download/test";
let fileName: string = "2.txt";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Moves a file or directory. This API uses a promise to return the result. You can forcibly overwrite the file with the same name in the destination directory. Currently, this API does not support move of files or directories across devices.

**Since:** 11

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, mode?: number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, force?: boolean): Promise<Array<MoveResult>>--><!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, force?: boolean): Promise<Array<MoveResult>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| force | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
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

Moves a file or directory. This API uses an asynchronous callback to return the result. Currently, this API does not support move of files or directories across devices.

**Since:** 11

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, callback: AsyncCallback<Array<MoveResult>>): void--><!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, callback: AsyncCallback<Array<MoveResult>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
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

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
// A built-in storage directory is used as an example.
// In the sample code, sourceFile indicates the file (directory) in the Download directory to copy, destFile indicates the destination directory in the Download directory, and URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destUri: string = "file://docs/storage/Users/currentUser/Download/test";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Moves a file or directory. This API uses an asynchronous callback to return the result. You can forcibly overwrite the file with the same name in the destination directory. Currently, this API does not support move of files or directories across devices.

**Since:** 11

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<MoveResult>>): void--><!--Device-FileAccessHelper-moveItem(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<MoveResult>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| force | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900018 |
| 13900019 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
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

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
// A built-in storage directory is used as an example.
// In the sample code, sourceFile indicates the file (directory) in the Download directory to copy, destFile indicates the destination directory in the Download directory, and URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
let destUri: string = "file://docs/storage/Users/currentUser/Download/test";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Opens a file. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** open(path: string, mode?: number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-openFile(uri: string, flags: OPENFLAGS) : Promise<number>--><!--Device-FileAccessHelper-openFile(uri: string, flags: OPENFLAGS) : Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| flags | [OPENFLAGS](arkts-corefile-fileaccess-openflags-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

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
async function openFile01() {
  // A built-in storage directory is used as an example.
  // In the sample code, targetUri indicates a file in the Download directory. The URI is the URI in fileInfo.
  // You can use the URI obtained.
  let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Opens a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** open(path: string, callback: AsyncCallback&lt;File&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-openFile(uri: string, flags: OPENFLAGS, callback: AsyncCallback<number>): void--><!--Device-FileAccessHelper-openFile(uri: string, flags: OPENFLAGS, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| flags | [OPENFLAGS](arkts-corefile-fileaccess-openflags-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

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
// A built-in storage directory is used as an example.
// In the sample code, targetUri indicates a file in the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Queries the attribute information about a file or directory based on a URI. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-query(uri: string, metaJson: string) : Promise<string>--><!--Device-FileAccessHelper-query(uri: string, metaJson: string) : Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| metaJson | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
async function getQuery01() {
  let imageFileRelativePath: string = "/storage/Users/currentUser/Download/queryTest/image/01.jpg";
  let jsonStrSingleRelativepath: string = JSON.stringify({ [fileAccess.FileKey.RELATIVE_PATH]: "" });
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Queries the attribute information about a file or directory based on a URI. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-query(uri: string, metaJson: string, callback: AsyncCallback<string>) : void--><!--Device-FileAccessHelper-query(uri: string, metaJson: string, callback: AsyncCallback<string>) : void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| metaJson | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
async function getQuery02() {
  let imageFileRelativePath: string = "/storage/Users/currentUser/Download/queryTest/image/01.jpg";
  let jsonStrSingleRelativepath: string = JSON.stringify({ [fileAccess.FileKey.RELATIVE_PATH]: "" });
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Registers a callback to listen for a URI. URIs and callbacks can be in many-to-many relationships. You are advised to use one callback to listen for one URI.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** createWatcher

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-registerObserver(uri: string, notifyForDescendants: boolean, callback: Callback<NotifyMessage>): void--><!--Device-FileAccessHelper-registerObserver(uri: string, notifyForDescendants: boolean, callback: Callback<NotifyMessage>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| notifyForDescendants | boolean | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 14300002 |

## rename

```TypeScript
rename(uri: string, displayName: string) : Promise<string>
```

Renames a file or directory. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** rename(oldPath: string, newPath: string)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-rename(uri: string, displayName: string) : Promise<string>--><!--Device-FileAccessHelper-rename(uri: string, displayName: string) : Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| displayName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

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
async function renameFile01() {
  // A built-in storage directory is used as an example.
  // In the sample code, sourceDir indicates a file in the Download directory. The URI is the URI in fileInfo.
  // You can use the URI obtained.
  let sourceDir: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  // Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Renames a file or directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** rename(oldPath: string, newPath: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-rename(uri: string, displayName: string, callback: AsyncCallback<string>): void--><!--Device-FileAccessHelper-rename(uri: string, displayName: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

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
// A built-in storage directory is used as an example.
// In the sample code, sourceDir indicates a file in the Download directory. The URI is the URI in fileInfo.
// You can use the URI obtained.
let sourceDir: string = "file://docs/storage/Users/currentUser/Download/1.txt";
// Obtain fileAccessHelper by referring to the sample code of fileAccess.createFileAccessHelper.
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

Unregisters a callback that is used to listen for the specified URI.

**Since:** 10

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-FileAccessHelper-unregisterObserver(uri: string, callback?: Callback<NotifyMessage>): void--><!--Device-FileAccessHelper-unregisterObserver(uri: string, callback?: Callback<NotifyMessage>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| 14300002 |
