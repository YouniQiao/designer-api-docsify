# FileAccessHelper（系统接口）

FileAccessHelper对象。

**起始版本：** 9

**废弃版本：** 23

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { fileAccess } from 'kits/@kit.CoreFileKit';
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

以异步方法判断文件(夹)是否存在。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** access(path: string, callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceFileUri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
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

复制文件或目录，使用 Promise 异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** copy(srcUri: string, destUri: string, options?: CopyOptions)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | 否 |

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

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; | 是 |

## copy

```TypeScript
copy(sourceUri: string, destUri: string, force: boolean, callback: AsyncCallback<Array<CopyResult>>): void
```

复制文件或目录，含有同名文件时可以选择是否强制覆盖原文件，使用 callback 异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[CopyResult](arkts-corefile-fileaccess-copyresult-i-sys.md)&gt;&gt; | 是 |

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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

复制文件并传入备用文件名，使用callback异步回调。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** copyFile(src: string | number, dest: string | number, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| fileName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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

以异步方法创建文件到指定目录，返回新文件uri。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

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

以异步方法创建文件到指定目录，返回新文件uri。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** createRandomAccessFile(file: string | File, callback: AsyncCallback&lt;RandomAccessFile&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| displayName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
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

以异步方法删除文件(夹)，返回错误码。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [delete](arkts-corefile-file-fs-atomicfile-c.md#delete)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

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

以异步方法删除文件(夹)，返回错误码。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [delete](arkts-corefile-file-fs-atomicfile-c.md#delete)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
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

以异步方法获取relativePath对应的FileInfo对象。使用promise异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

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

## getFileInfoFromRelativePath

```TypeScript
getFileInfoFromRelativePath(relativePath: string, callback: AsyncCallback<FileInfo>) : void
```

以异步方法获取relativePath对应的FileInfo对象。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relativePath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileInfo&gt; | 是 |

## getFileInfoFromUri

```TypeScript
getFileInfoFromUri(uri: string) : Promise<FileInfo>
```

以异步方法获取uri对应的FileInfo对象。使用promise异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

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

## getFileInfoFromUri

```TypeScript
getFileInfoFromUri(uri: string, callback: AsyncCallback<FileInfo>) : void
```

以异步方法获取uri对应的FileInfo对象。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileInfo&gt; | 是 |

## getRoots

```TypeScript
getRoots(): Promise<RootIterator>
```

以异步方法获取helper对象连接的文件管理服务类的设备根节点信息。使用Promise异步回调。 该方法返回迭代器对象RootIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回[RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md)。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
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

以异步方法获取helper对象连接的文件管理服务类的设备根节点信息。使用callback异步回调。 callback带回迭代器对象RootIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回 [RootInfo](arkts-corefile-fileaccess-rootinfo-i-sys.md)。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RootIterator](arkts-corefile-fileaccess-rootiterator-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
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

以异步方法创建文件夹到指定目录，返回文件夹uri。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** mkdir(path: string)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

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

以异步方法创建文件夹到指定目录，返回文件夹uri。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** mkdir(path: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parentUri | string | 是 |
| displayName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
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

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用Promise异步回调。目前仅支持设备内移动，跨设备不支持移动。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceFile | string | 是 |
| [destFile](arkts-corefile-file-fs-conflictfiles-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
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

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用callback异步回调。目前仅支持设备内移动，跨设备不支持移动。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceFile | string | 是 |
| [destFile](arkts-corefile-file-fs-conflictfiles-i.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
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

以异步方法移动文件，返回移动后文件的uri。使用Promise异步回调。 当存在同名文件时（即发生文件移动冲突时），可以重命名待移动的文件，再保存到目标文件夹。 目前仅支持设备内移动，跨设备不支持移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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

以异步方法移动文件，返回移动后文件的uri。使用callback异步回调。 当存在同名文件时（即发生文件移动冲突时），可以重命名待移动的文件，再保存到目标文件夹。 当前仅支持设备内移动，不支持跨设备移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| fileName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用Promise异步回调。 当存在同名文件时，可以选择强制覆盖文件。 目前仅支持设备内移动，跨设备不支持移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用callback异步回调。 当前仅支持设备内移动，不支持跨设备移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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

以异步方法移动文件(夹)，返回移动后文件(夹)的uri。使用callback异步回调。 当存在同名文件时，可以选择强制覆盖文件。 当前仅支持设备内移动，不支持跨设备移动。

**起始版本：** 11

**废弃版本：** 23

**替代接口：** moveFile(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceUri | string | 是 |
| destUri | string | 是 |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MoveResult](arkts-corefile-fileaccess-moveresult-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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

以异步方法打开文件，返回文件描述符。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** open(path: string, mode?: number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

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

以异步方法打开文件，返回文件描述符。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** open(path: string, callback: AsyncCallback&lt;File&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flags | [OPENFLAGS](arkts-corefile-fileaccess-openflags-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
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

通过uri查询文件或目录的相关信息，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

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

## query

```TypeScript
query(uri: string, metaJson: string, callback: AsyncCallback<string>) : void
```

通过uri查询文件或目录的相关信息，使用callback异步回调。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| metaJson | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## registerObserver

```TypeScript
registerObserver(uri: string, notifyForDescendants: boolean, callback: Callback<NotifyMessage>): void
```

注册指定uri的callback。uri与callback可以为多对多的关系，推荐使用一个callback监听一个uri。

**起始版本：** 10

**废弃版本：** 23

**替代接口：** createWatcher

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| notifyForDescendants | boolean | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md)&gt; | 是 |

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

以异步方法重命名文件(夹)，返回重命名后的文件(夹)的Uri。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** rename(oldPath: string, newPath: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| displayName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
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

取消注册指定的uri和callback。

**起始版本：** 10

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NotifyMessage](arkts-corefile-fileaccess-notifymessage-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| 14300002 |
