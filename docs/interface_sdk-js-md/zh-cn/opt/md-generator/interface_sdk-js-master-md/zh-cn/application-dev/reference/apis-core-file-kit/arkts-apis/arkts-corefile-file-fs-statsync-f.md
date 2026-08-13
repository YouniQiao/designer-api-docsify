# statSync

## statSync

```TypeScript
declare function statSync(file: string | number): Stat
```

以同步方法获取文件或目录详细属性信息。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function statSync(file: string | number): Stat--><!--Device-unnamed-declare function statSync(file: string | number): Stat-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| number | 是 |

**返回值：**

| 类型 |
| --- |
| [Stat](arkts-corefile-file-fs-stat-i.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |
| 13900011 |
