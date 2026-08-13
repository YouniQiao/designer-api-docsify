# lseek

## lseek

```TypeScript
declare function lseek(fd: number, offset: number, whence?: WhenceType): number
```

调整文件偏移指针位置。

**起始版本：** 11

**废弃版本：** -1

<!--Device-unnamed-declare function lseek(fd: number, offset: number, whence?: WhenceType): number--><!--Device-unnamed-declare function lseek(fd: number, offset: number, whence?: WhenceType): number-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| offset | number | 是 |
| whence | [WhenceType](arkts-corefile-file-fs-whencetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900038 |
| 13900008 |
| 13900026 |
| 13900042 |
