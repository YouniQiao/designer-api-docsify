# renameSync

## renameSync

```TypeScript
declare function renameSync(oldPath: string, newPath: string): void
```

以同步方法重命名文件或目录。

> **说明：**
> 
> 该接口不支持在分布式文件路径下操作。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function renameSync(oldPath: string, newPath: string): void--><!--Device-unnamed-declare function renameSync(oldPath: string, newPath: string): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldPath | string | 是 |
| newPath | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900025 |
| 13900027 |
| 13900032 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
