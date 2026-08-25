# createStream

## 导入模块

```TypeScript
```

## createStream

```TypeScript
declare function createStream(path: string, mode: string): Promise<Stream>
```

基于文件路径打开文件流，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createStream](arkts-corefile-file-fs-createstream-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Stream](arkts-corefile-fileio-stream-depr-i.md)&gt; |


## createStream

```TypeScript
declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void
```

基于文件路径打开文件流，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createStream](arkts-corefile-file-fs-createstream-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stream](arkts-corefile-fileio-stream-depr-i.md)&gt; | 是 |
