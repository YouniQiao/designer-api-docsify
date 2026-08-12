# fsync

## fsync

```TypeScript
declare function fsync(fd: number): Promise<void>
```

同步文件数据，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [fsync](arkts-corefile-file-fs-fsync-f.md#fsync)

<!--Device-unnamed-declare function fsync(fd: number): Promise<void>--><!--Device-unnamed-declare function fsync(fd: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## fsync

```TypeScript
declare function fsync(fd: number, callback: AsyncCallback<void>): void
```

同步文件数据，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [fsync](arkts-corefile-file-fs-fsync-f.md#fsync)

<!--Device-unnamed-declare function fsync(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function fsync(fd: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
