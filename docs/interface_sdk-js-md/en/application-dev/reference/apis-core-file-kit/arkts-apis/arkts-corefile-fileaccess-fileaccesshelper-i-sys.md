# FileAccessHelper (System API)

Provides a **FileAccessHelper** object.

**Since:** 9

**Deprecated since:** 23

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fileAccess } from 'kits/@kit.CoreFileKit';
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
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## access

```TypeScript
access(sourceFileUri: string, callback: AsyncCallback<boolean>): void
```

Checks whether a file or directory exists. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** access(path: string, callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceFileUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## copy

```TypeScript
copy(sourceUri: string, destUri: string, force?: boolean): Promise<Array<CopyResult>>
```

Copies a file or directory. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** copy(srcUri: string, destUri: string, options?: CopyOptions)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | No |

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

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; | Yes |

## copy

```TypeScript
copy(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<CopyResult>>): void
```

Copies a file or directory. If a file with the same name already exists, you can choose whether to forcibly overwrite the original file. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; | Yes |

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900014 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

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

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| fileName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900014 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## createFile

```TypeScript
createFile(uri: string, displayName: string) : Promise<string>
```

Creates a file in a directory. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

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
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## createFile

```TypeScript
createFile(uri: string, displayName: string, callback: AsyncCallback<string>): void
```

Creates a file in a directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** createRandomAccessFile(file: string | File, callback: AsyncCallback&lt;RandomAccessFile&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## delete

```TypeScript
delete(uri: string) : Promise<number>
```

Deletes a file or directory. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [delete](arkts-corefile-file-fs-atomicfile-c.md#delete)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

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
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## delete

```TypeScript
delete(uri: string, callback: AsyncCallback<number>): void
```

Deletes a file or directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [delete](arkts-corefile-file-fs-atomicfile-c.md#delete)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## getFileInfoFromRelativePath

```TypeScript
getFileInfoFromRelativePath(relativePath: string) : Promise<FileInfo>
```

Obtains a **FileInfo** object based on a relative path. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

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

## getFileInfoFromRelativePath

```TypeScript
getFileInfoFromRelativePath(relativePath: string, callback: AsyncCallback<FileInfo>) : void
```

Obtains a **FileInfo** object based on a relative path. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relativePath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileInfo&gt; | Yes |

## getFileInfoFromUri

```TypeScript
getFileInfoFromUri(uri: string) : Promise<FileInfo>
```

Obtains a **FileInfo** object based on a URI. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

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

## getFileInfoFromUri

```TypeScript
getFileInfoFromUri(uri: string, callback: AsyncCallback<FileInfo>) : void
```

Obtains a **FileInfo** object based on a URI. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileInfo&gt; | Yes |

## getRoots

```TypeScript
getRoots(): Promise<RootIterator>
```

Obtains information about the device root nodes of the file management services associated with the **Helper** object. This API uses a promise to return a **RootIterator** object. You can use [next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next) to return [RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md).

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## getRoots

```TypeScript
getRoots(callback: AsyncCallback<RootIterator>): void
```

Obtains information about the device root nodes of the file management services associated with the **Helper** object. This API uses an asynchronous callback to return a **RootIterator** object. You can use [next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next) to return [RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md).

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## mkDir

```TypeScript
mkDir(parentUri: string, displayName: string) : Promise<string>
```

Creates a directory in a specified directory. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** mkdir(path: string)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

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
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## mkDir

```TypeScript
mkDir(parentUri: string, displayName: string, callback: AsyncCallback<string>): void
```

Creates a directory in a specified directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** mkdir(path: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parentUri | string | Yes |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## move

```TypeScript
move(sourceFile: string, destFile: string) : Promise<string>
```

Moves a file or directory. This API uses a promise to return the result. Currently, this API does not support move of files or directories across devices.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, mode?: number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceFile | string | Yes |
| [destFile](arkts-corefile-file-fs-conflictfiles-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## move

```TypeScript
move(sourceFile: string, destFile: string, callback: AsyncCallback<string>): void
```

Moves a file or directory. This API uses an asynchronous callback to return the result. Currently, this API does not support move of files or directories across devices.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** moveFile(src: string, dest: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceFile | string | Yes |
| [destFile](arkts-corefile-file-fs-conflictfiles-i.md) | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900014 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

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

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| fileName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900014 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

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

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900014 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

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

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900014 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

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

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceUri | string | Yes |
| destUri | string | Yes |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900014 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900042 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## openFile

```TypeScript
openFile(uri: string, flags: OPENFLAGS) : Promise<number>
```

Opens a file. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** open(path: string, mode?: number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

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
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## openFile

```TypeScript
openFile(uri: string, flags: OPENFLAGS, callback: AsyncCallback<number>): void
```

Opens a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** open(path: string, callback: AsyncCallback&lt;File&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| flags | [OPENFLAGS](arkts-corefile-fileaccess-openflags-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## query

```TypeScript
query(uri: string, metaJson: string) : Promise<string>
```

Queries the attribute information about a file or directory based on a URI. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

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

## query

```TypeScript
query(uri: string, metaJson: string, callback: AsyncCallback<string>) : void
```

Queries the attribute information about a file or directory based on a URI. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| metaJson | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## registerObserver

```TypeScript
registerObserver(uri: string, notifyForDescendants: boolean, callback: Callback<NotifyMessage>): void
```

Registers a callback to listen for a URI. URIs and callbacks can be in many-to-many relationships. You are advised to use one callback to listen for one URI.

**Since:** 10

**Deprecated since:** 23

**Substitutes:** createWatcher

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| notifyForDescendants | boolean | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md)&gt; | Yes |

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
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## rename

```TypeScript
rename(uri: string, displayName: string, callback: AsyncCallback<string>): void
```

Renames a file or directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** rename(oldPath: string, newPath: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## unregisterObserver

```TypeScript
unregisterObserver(uri: string, callback?: Callback<NotifyMessage>): void
```

Unregisters a callback that is used to listen for the specified URI.

**Since:** 10

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| 14300002 |
