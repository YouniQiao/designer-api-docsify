# readLines

## readLines

```TypeScript
declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>
```

逐行读取文件文本内容，使用promise异步回调。只支持读取utf-8格式文件。

**起始版本：** 11

**废弃版本：** -1

<!--Device-unnamed-declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>--><!--Device-unnamed-declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [Options](arkts-corefile-file-fs-options-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900019 |
| 13900030 |
| 13900025 |
| 13900027 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900044 |
| 13900015 |
| 13900041 |
| 13900042 |


## readLines

```TypeScript
declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void
```

逐行读取文件文本内容，使用callback异步回调，只支持读取utf-8格式文件。

**起始版本：** 11

**废弃版本：** -1

<!--Device-unnamed-declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void--><!--Device-unnamed-declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900033 |
| 13900002 |
| 13900019 |
| 13900012 |
| 13900030 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |


## readLines

```TypeScript
declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void
```

逐行读取文件文本内容，使用callback异步回调，只支持读取utf-8格式文件。

**起始版本：** 11

**废弃版本：** -1

<!--Device-unnamed-declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void--><!--Device-unnamed-declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [Options](arkts-corefile-file-fs-options-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900033 |
| 13900002 |
| 13900019 |
| 13900012 |
| 13900030 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |
