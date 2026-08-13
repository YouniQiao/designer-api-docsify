# fdatasync

## fdatasync

```TypeScript
declare function fdatasync(fd: number): Promise<void>
```

实现文件内容数据同步，使用promise异步回调。

**起始版本：** 9

**废弃版本：** -1

<!--Device-unnamed-declare function fdatasync(fd: number): Promise<void>--><!--Device-unnamed-declare function fdatasync(fd: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |


## fdatasync

```TypeScript
declare function fdatasync(fd: number, callback: AsyncCallback<void>): void
```

实现文件内容数据同步，使用callback异步回调。

**起始版本：** 9

**废弃版本：** -1

<!--Device-unnamed-declare function fdatasync(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function fdatasync(fd: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |
