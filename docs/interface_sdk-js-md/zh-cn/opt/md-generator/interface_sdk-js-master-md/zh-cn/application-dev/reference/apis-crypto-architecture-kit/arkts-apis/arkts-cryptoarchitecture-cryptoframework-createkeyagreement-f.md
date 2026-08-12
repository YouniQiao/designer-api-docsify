# createKeyAgreement

## createKeyAgreement

```TypeScript
function createKeyAgreement(algName: string): KeyAgreement
```

创建密钥协商实例。

&lt;br&gt;支持的规格详见[密钥协商规格](../../../security/CryptoArchitectureKit/crypto-key-agreement-overview.md)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-cryptoFramework-function createKeyAgreement(algName: string): KeyAgreement--><!--Device-cryptoFramework-function createKeyAgreement(algName: string): KeyAgreement-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| algName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [KeyAgreement](arkts-cryptoarchitecture-cryptoframework-keyagreement-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-内存操作失败) |

## 示例

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
```
