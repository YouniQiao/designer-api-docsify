# fdatasync

## 导入模块

```TypeScript
```

## fdatasync

```TypeScript
declare function fdatasync(fd: number): Promise<void>
```

实现文件内容数据同步，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [fdatasync](arkts-corefile-file-fs-fdatasync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## fdatasync

```TypeScript
declare function fdatasync(fd: number, callback: AsyncCallback<void>): void
```

实现文件内容数据同步，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [fdatasync](arkts-corefile-file-fs-fdatasync-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
