# ftruncateSync

## ftruncateSync

```TypeScript
declare function ftruncateSync(fd: number, len?: number): void
```

以同步方法基于文件描述符截断文件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:truncateSync](arkts-corefile-fileio-truncatesync-f.md#truncatesync)

<!--Device-unnamed-declare function ftruncateSync(fd: number, len?: number): void--><!--Device-unnamed-declare function ftruncateSync(fd: number, len?: number): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| len | number | 否 |
