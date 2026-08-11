# createWriteStream

## createWriteStream

```TypeScript
declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream
```

以同步方法打开文件可写流。

**起始版本：** 12

<!--Device-unnamed-declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream--><!--Device-unnamed-declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| options | [WriteStreamOptions](arkts-corefile-file-fs-writestreamoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [WriteStream](arkts-corefile-file-fs-writestream-c.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900017 |
| 13900019 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 13900038 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900041 |
| 13900042 |
| 13900011 |
