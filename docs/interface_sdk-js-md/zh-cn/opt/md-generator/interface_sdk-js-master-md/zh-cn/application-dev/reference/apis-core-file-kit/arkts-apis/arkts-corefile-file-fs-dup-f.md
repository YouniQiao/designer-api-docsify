# dup

## dup

```TypeScript
declare function dup(fd: number): File
```

复制文件描述符，并返回对应的File对象。

**起始版本：** 10

<!--Device-unnamed-declare function dup(fd: number): File--><!--Device-unnamed-declare function dup(fd: number): File-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| [File](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-file-i.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900022 |
| 13900014 |
| 13900008 |
| 13900042 |
