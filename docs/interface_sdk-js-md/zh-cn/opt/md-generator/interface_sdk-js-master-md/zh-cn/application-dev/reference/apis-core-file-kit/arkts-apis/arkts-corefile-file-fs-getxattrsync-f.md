# getxattrSync

## getxattrSync

```TypeScript
declare function getxattrSync(path: string, key: string): string
```

使用同步接口获取文件或目录的扩展属性。

**起始版本：** 12

<!--Device-unnamed-declare function getxattrSync(path: string, key: string): string--><!--Device-unnamed-declare function getxattrSync(path: string, key: string): string-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 13900037 |
| 13900038 |
| 13900007 |
| 13900002 |
| 13900012 |
| 13900031 |
| 13900042 |
