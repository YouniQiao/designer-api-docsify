# createAsyKeyGeneratorBySpec

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createAsyKeyGeneratorBySpec

```TypeScript
function createAsyKeyGeneratorBySpec(asyKeySpec: AsyKeySpec): AsyKeyGeneratorBySpec
```

创建指定密钥规格的非对称密钥生成器实例。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| asyKeySpec | [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AsyKeyGeneratorBySpec](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
