# createReadStream

## createReadStream

```TypeScript
declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream
```

以同步方法打开文件可读流。

**起始版本：** 12

<!--Device-unnamed-declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream--><!--Device-unnamed-declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| options | [ReadStreamOptions](arkts-corefile-file-fs-readstreamoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ReadStream](arkts-corefile-file-fs-readstream-c.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900022 |
| 13900017 |
| 13900019 |
| 13900030 |
| 13900024 |
| 13900004 |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| 13900038 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900044 |
| 13900041 |
| 13900042 |
| 13900011 |
