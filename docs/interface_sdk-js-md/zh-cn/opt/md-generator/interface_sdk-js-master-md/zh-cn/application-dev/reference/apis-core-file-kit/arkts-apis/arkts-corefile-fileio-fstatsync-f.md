# fstatSync

## fstatSync

```TypeScript
declare function fstatSync(fd: number): Stat
```

以同步方法基于文件描述符获取文件状态信息。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [statSync](arkts-corefile-file-fs-statsync-f.md#statSync)

<!--Device-unnamed-declare function fstatSync(fd: number): Stat--><!--Device-unnamed-declare function fstatSync(fd: number): Stat-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Stat](arkts-corefile-fileio-stat-depr-i.md) |
