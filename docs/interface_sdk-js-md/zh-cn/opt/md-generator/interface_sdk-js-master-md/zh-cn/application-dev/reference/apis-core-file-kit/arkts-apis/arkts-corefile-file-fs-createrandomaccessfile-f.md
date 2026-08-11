# createRandomAccessFile

## createRandomAccessFile

```TypeScript
declare function createRandomAccessFile(file: string | File, mode?: number,
  options?: RandomAccessFileOptions): Promise<RandomAccessFile>
```

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**起始版本：** 10

<!--Device-unnamed-declare function createRandomAccessFile(file: string | File, mode?: number,  options?: RandomAccessFileOptions): Promise<RandomAccessFile>--><!--Device-unnamed-declare function createRandomAccessFile(file: string | File, mode?: number,  options?: RandomAccessFileOptions): Promise<RandomAccessFile>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| file | string \| [File](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-file-i.md) | 是 |
| mode | number | 否 |
| options | [RandomAccessFileOptions](arkts-corefile-file-fs-randomaccessfileoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;RandomAccessFile&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900044 |
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
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |


## createRandomAccessFile

```TypeScript
declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void
```

基于文件路径或文件对象，以只读方式创建RandomAccessFile对象，使用callback异步回调。

**起始版本：** 10

<!--Device-unnamed-declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void--><!--Device-unnamed-declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| file | string \| [File](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-file-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RandomAccessFile&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
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
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |


## createRandomAccessFile

```TypeScript
declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void
```

基于文件路径或文件对象创建RandomAccessFile对象，使用callback异步回调。

**起始版本：** 10

<!--Device-unnamed-declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void--><!--Device-unnamed-declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| file | string \| [File](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-file-i.md) | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RandomAccessFile&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
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
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |
