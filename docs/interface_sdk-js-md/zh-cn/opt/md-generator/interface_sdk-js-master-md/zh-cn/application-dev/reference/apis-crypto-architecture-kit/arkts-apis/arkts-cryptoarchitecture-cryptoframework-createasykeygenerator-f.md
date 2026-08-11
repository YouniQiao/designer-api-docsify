# createAsyKeyGenerator

## createAsyKeyGenerator

```TypeScript
function createAsyKeyGenerator(algName: string): AsyKeyGenerator
```

创建对应算法的非对称密钥生成器实例。

&lt;br&gt;支持的规格详见  
[非对称密钥生成和转换规格](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-cryptoFramework-function createAsyKeyGenerator(algName: string): AsyKeyGenerator--><!--Device-cryptoFramework-function createAsyKeyGenerator(algName: string): AsyKeyGenerator-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| algName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [AsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-asykeygenerator-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |

## 示例

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
```
