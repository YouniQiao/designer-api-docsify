# lstatSync

## lstatSync

```TypeScript
declare function lstatSync(path: string): Stat
```

以同步方法获取符号链接文件信息。

**起始版本：** 9

<!--Device-unnamed-declare function lstatSync(path: string): Stat--><!--Device-unnamed-declare function lstatSync(path: string): Stat-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Stat](arkts-corefile-file-fs-stat-i.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900030 |
| 13900008 |
| 13900042 |
| 13900011 |
