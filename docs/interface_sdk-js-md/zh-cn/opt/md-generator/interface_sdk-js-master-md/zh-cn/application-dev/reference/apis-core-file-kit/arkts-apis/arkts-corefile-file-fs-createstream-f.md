# createStream

## createStream

```TypeScript
declare function createStream(path: string, mode: string): Promise<Stream>
```

基于文件路径创建文件流，使用promise异步回调。需要配合[Stream](arkts-corefile-file-fs-stream-i.md)中的close()函数关闭文件流。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function createStream(path: string, mode: string): Promise<Stream>--><!--Device-unnamed-declare function createStream(path: string, mode: string): Promise<Stream>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Stream&gt; |

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


## createStream

```TypeScript
declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void
```

基于文件路径创建文件流，使用callback异步回调。需要配合[Stream](arkts-corefile-file-fs-stream-i.md)中的close()函数关闭文件流。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void--><!--Device-unnamed-declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Stream&gt; | 是 |

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
