# createKem

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## createKem

```TypeScript
function createKem(algNameId: KemAlgNameId): Kem
```

Creates a Kem instance for key encapsulation and decapsulation operations.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-cryptoFramework-function createKem(algNameId: KemAlgNameId): Kem--><!--Device-cryptoFramework-function createKem(algNameId: KemAlgNameId): Kem-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| algNameId | [KemAlgNameId](arkts-cryptoarchitecture-cryptoframework-kemalgnameid-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Kem](arkts-cryptoarchitecture-cryptoframework-kem-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620003-parameter-check-failed) |

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
