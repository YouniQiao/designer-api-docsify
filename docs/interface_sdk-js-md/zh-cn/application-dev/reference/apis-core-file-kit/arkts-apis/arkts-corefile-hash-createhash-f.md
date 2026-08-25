# createHash

## 导入模块

```TypeScript
import { hash } from 'kits/@kit.CoreFileKit';
```

## createHash

```TypeScript
function createHash(algorithm: string): HashStream
```

创建并返回HashStream对象，用于生成哈希摘要。可以指定哈希计算采用的算法。HashStream采用流式处理机制，支持分批次更新数据，适用于大文件或数据流的哈希计算，避免一次性加载大文件到内存。

> **说明：**&gt;
> HashStream采用流式处理机制，支持分批次更新数据，适用于大文件或数据流的哈希计算，避免一次性加载大文件到内存。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [HashStream](arkts-corefile-hash-hashstream-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900020 |
| 13900042 |
