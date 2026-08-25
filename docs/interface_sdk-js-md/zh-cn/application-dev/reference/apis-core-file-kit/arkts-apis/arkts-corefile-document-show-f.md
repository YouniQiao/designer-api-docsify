# show

## 导入模块

```TypeScript
```

## show

```TypeScript
declare function show(uri: string, type: string): Promise<void>
```

异步打开URI对应的文件，使用promise形式返回结果。

**起始版本：** 6

**废弃版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| type | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## show

```TypeScript
declare function show(uri: string, type: string, callback: AsyncCallback<void>): void
```

异步打开URI对应的文件，使用callback形式返回结果。

**起始版本：** 6

**废弃版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| type | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
