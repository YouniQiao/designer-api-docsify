# getxattr

## getxattr

```TypeScript
declare function getxattr(path: string, key: string): Promise<string>
```

获取文件或目录的扩展属性。使用promise异步回调。

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-declare function getxattr(path: string, key: string): Promise<string>--><!--Device-unnamed-declare function getxattr(path: string, key: string): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900037 |
| 13900038 |
| 13900007 |
| 13900002 |
| 13900012 |
| 13900031 |
| 13900042 |
