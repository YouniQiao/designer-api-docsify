# setxattr

## 导入模块

```TypeScript
```

## setxattr

```TypeScript
declare function setxattr(path: string, key: string, value: string): Promise<void>
```

设置文件或目录的扩展属性。使用promise异步回调。

**起始版本：** 12

<!--Device-unnamed-declare function setxattr(path: string, key: string, value: string): Promise<void>--><!--Device-unnamed-declare function setxattr(path: string, key: string, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900038 |
| 13900002 |
| 13900012 |
| 13900031 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900011 |
