# createKdf

## createKdf

```TypeScript
function createKdf(algName: string): Kdf
```

创建密钥派生函数实例。

&lt;br&gt;支持的规格详见[密钥派生函数规格](../../../security/CryptoArchitectureKit/crypto-key-derivation-overview.md)。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-cryptoFramework-function createKdf(algName: string): Kdf--><!--Device-cryptoFramework-function createKdf(algName: string): Kdf-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Kdf
- API版本11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 指定密钥派生算法（包含HMAC配套的散列函数）：目前支持PBKDF2、HKDF、SCRYPT、X963KDF算法， 如"PBKDF2\|SHA256"、 "HKDF\|SHA256"、 "SCRYPT"和"X963KDF\|SHA256"等。&lt;br&gt;支持的规格详见 [密钥派生函数规格](../../../security/CryptoArchitectureKit/crypto-key-derivation-overview.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Kdf](arkts-cryptoarchitecture-cryptoframework-kdf-i.md) | 返回对应算法的Kdf实例。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) | 该操作不支持。 |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-内存操作失败) | 内存操作失败。 |

## 示例

PBKDF2算法

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
```

