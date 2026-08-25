# getFreeBytes

## 导入模块

```TypeScript
```

## getFreeBytes

```TypeScript
function getFreeBytes(path: string, callback: AsyncCallback<number>): void
```

异步方法获取指定文件系统空闲字节数，使用callback形式返回结果。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getFreeBytes

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## getFreeBytes

```TypeScript
function getFreeBytes(path: string): Promise<number>
```

异步方法获取指定文件系统空闲字节数，以Promise形式返回结果。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getFreeBytes

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
