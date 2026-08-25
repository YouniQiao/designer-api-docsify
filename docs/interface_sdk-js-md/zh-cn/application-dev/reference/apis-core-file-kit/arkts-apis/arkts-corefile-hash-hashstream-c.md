# HashStream

HashStream类是用于创建数据的哈希摘要的实用工具。由 [createHash](arkts-corefile-hash-createhash-f.md) 接口获得。该类采用增量式哈希计算设计，通过update方法多次添加数据块， 最后通过digest方法计算最终哈希值，适用于处理大文件或持续产生的数据流。

**继承/实现关系：** HashStream extends [stream.Transform](../../apis-arkts/arkts-apis/arkts-arkts-stream-transform-c.md)

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { hash } from 'kits/@kit.CoreFileKit';
```

## digest

```TypeScript
digest(): string
```

计算传递给哈希处理的所有数据的摘要，返回最终的哈希值。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900042 |

## update

```TypeScript
update(data: ArrayBuffer): void
```

使用给定的数据更新哈希内容，可多次调用。每次调用的数据将被追加到已计算的哈希内容中，最终通过digest方法获取完整的哈希摘要。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900042 |
