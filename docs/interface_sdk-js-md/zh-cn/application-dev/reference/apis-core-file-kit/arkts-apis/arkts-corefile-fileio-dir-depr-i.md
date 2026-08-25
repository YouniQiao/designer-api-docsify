# Dir

管理目录，在调用Dir的方法前，需要先通过opendir方法（同步或异步）来构建一个Dir实例。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
```

## close

```TypeScript
close(): Promise<void>
```

异步关闭目录，使用promise形式返回结果。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

异步关闭目录，使用callback形式返回结果。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## closeSync

```TypeScript
closeSync(): void
```

用于关闭目录。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

## read

```TypeScript
read(): Promise<Dirent>
```

读取下一个目录项，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Dirent](arkts-corefile-fileio-dirent-depr-i.md)&gt; |

## read

```TypeScript
read(callback: AsyncCallback<Dirent>): void
```

读取下一个目录项，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Dirent](arkts-corefile-fileio-dirent-depr-i.md)&gt; | 是 |

## readSync

```TypeScript
readSync(): Dirent
```

同步读取下一个目录项。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| [Dirent](arkts-corefile-fileio-dirent-depr-i.md) |
