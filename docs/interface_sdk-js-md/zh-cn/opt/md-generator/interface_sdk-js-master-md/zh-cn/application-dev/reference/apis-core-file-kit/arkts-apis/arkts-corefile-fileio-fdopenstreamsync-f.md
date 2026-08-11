# fdopenStreamSync

## fdopenStreamSync

```TypeScript
declare function fdopenStreamSync(fd: number, mode: string): Stream
```

以同步方法基于文件描述符打开文件流。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:fdopenStreamSync](arkts-corefile-fileio-fdopenstreamsync-f.md#fdopenstreamsync)

<!--Device-unnamed-declare function fdopenStreamSync(fd: number, mode: string): Stream--><!--Device-unnamed-declare function fdopenStreamSync(fd: number, mode: string): Stream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Stream](arkts-corefile-file-fs-stream-i.md) |
