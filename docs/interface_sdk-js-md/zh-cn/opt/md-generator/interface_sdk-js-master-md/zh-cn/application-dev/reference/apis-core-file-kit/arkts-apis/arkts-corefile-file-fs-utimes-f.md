# utimes

## utimes

```TypeScript
declare function utimes(path: string, mtime: number): void
```

更改文件上次修改该文件的时间。

**起始版本：** 11

**废弃版本：** -1

<!--Device-unnamed-declare function utimes(path: string, mtime: number): void--><!--Device-unnamed-declare function utimes(path: string, mtime: number): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mtime | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900042 |
| 13900027 |
