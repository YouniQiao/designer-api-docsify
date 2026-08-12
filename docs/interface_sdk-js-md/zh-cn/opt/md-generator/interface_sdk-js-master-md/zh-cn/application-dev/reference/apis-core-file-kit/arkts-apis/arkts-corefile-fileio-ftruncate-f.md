# ftruncate

## ftruncate

```TypeScript
declare function ftruncate(fd: number, len?: number): Promise<void>
```

基于文件描述符截断文件，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [truncate](arkts-corefile-file-fs-truncate-f.md#truncate)

<!--Device-unnamed-declare function ftruncate(fd: number, len?: number): Promise<void>--><!--Device-unnamed-declare function ftruncate(fd: number, len?: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| len | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## ftruncate

```TypeScript
declare function ftruncate(fd: number, callback: AsyncCallback<void>): void
```

基于文件描述符截断文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [truncate](arkts-corefile-file-fs-truncate-f.md#truncate)

<!--Device-unnamed-declare function ftruncate(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function ftruncate(fd: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## ftruncate

```TypeScript
declare function ftruncate(fd: number, len: number, callback: AsyncCallback<void>): void
```

基于文件描述符截断文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [truncate](arkts-corefile-file-fs-truncate-f.md#truncate)

<!--Device-unnamed-declare function ftruncate(fd: number, len: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function ftruncate(fd: number, len: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| len | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
