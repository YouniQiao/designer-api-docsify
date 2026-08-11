# rmdirSync

## rmdirSync

```TypeScript
declare function rmdirSync(path: string): void
```

以同步方法删除目录及其所有子目录和文件。

> **说明：**
> 
> 该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlinkSync接口删除单个文件。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function rmdirSync(path: string): void--><!--Device-unnamed-declare function rmdirSync(path: string): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900032 |
| 13900001 |
| 13900002 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900030 |
| 13900042 |
| 13900011 |
| 13900027 |
