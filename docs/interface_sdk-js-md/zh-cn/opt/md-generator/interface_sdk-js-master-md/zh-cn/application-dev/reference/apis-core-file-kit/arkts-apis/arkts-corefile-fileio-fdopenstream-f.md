# fdopenStream

## fdopenStream

```TypeScript
declare function fdopenStream(fd: number, mode: string): Promise<Stream>
```

基于文件描述符打开文件流，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [fdopenStream](arkts-corefile-file-fs-fdopenstream-f.md#fdopenStream)

<!--Device-unnamed-declare function fdopenStream(fd: number, mode: string): Promise<Stream>--><!--Device-unnamed-declare function fdopenStream(fd: number, mode: string): Promise<Stream>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Stream](arkts-corefile-fileio-stream-depr-i.md)&gt; |


## fdopenStream

```TypeScript
declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void
```

基于文件描述符打开文件流，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [fdopenStream](arkts-corefile-file-fs-fdopenstream-f.md#fdopenStream)

<!--Device-unnamed-declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void--><!--Device-unnamed-declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| mode | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stream](arkts-corefile-fileio-stream-depr-i.md)&gt; | 是 |
