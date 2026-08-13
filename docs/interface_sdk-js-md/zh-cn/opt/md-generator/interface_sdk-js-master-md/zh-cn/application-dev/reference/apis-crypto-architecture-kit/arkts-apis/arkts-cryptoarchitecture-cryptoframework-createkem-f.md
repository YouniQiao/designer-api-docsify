# createKem

## createKem

```TypeScript
function createKem(algNameId: KemAlgNameId): Kem
```

创建一个用于密钥封装和解封装操作的Kem实例。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-cryptoFramework-function createKem(algNameId: KemAlgNameId): Kem--><!--Device-cryptoFramework-function createKem(algNameId: KemAlgNameId): Kem-End-->

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| algNameId | [KemAlgNameId](arkts-cryptoarchitecture-cryptoframework-kemalgnameid-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Kem](arkts-cryptoarchitecture-cryptoframework-kem-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## 示例

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function createKem() {
  try {
    let kem = cryptoFramework.createKem(cryptoFramework.KemAlgNameId.ML_KEM_768);
    console.info('create kem success');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`create kem failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```
