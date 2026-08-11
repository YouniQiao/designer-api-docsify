# fsyncSync

## fsyncSync

```TypeScript
declare function fsyncSync(fd: number): void
```

以同步方法将文件系统缓存数据写入磁盘。

**起始版本：** 9

<!--Device-unnamed-declare function fsyncSync(fd: number): void--><!--Device-unnamed-declare function fsyncSync(fd: number): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |
