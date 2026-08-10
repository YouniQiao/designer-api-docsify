# createKem

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createKem

```TypeScript
function createKem(algNameId: KemAlgNameId): Kem
```

创建一个用于密钥封装和解封装操作的Kem实例。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-cryptoFramework-function createKem(algNameId: KemAlgNameId): Kem--><!--Device-cryptoFramework-function createKem(algNameId: KemAlgNameId): Kem-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algNameId | [KemAlgNameId](arkts-cryptoarchitecture-cryptoframework-kemalgnameid-e.md) | Yes | KEM的算法名称ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Kem](arkts-cryptoarchitecture-cryptoframework-kem-i.md) | 返回对应算法的Kem实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620002 | 获取Native对象失败或参数转换失败。 |
| 17620003 | 参数检查失败。 |

## Examples

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

