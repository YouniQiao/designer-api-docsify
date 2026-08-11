# Sign

Signing interface, defining methods for signing data using a private key. Before use, you must create a **Sign**instance by using [createSign(algName: string): Sign](arkts-cryptoarchitecture-cryptoframework-createsign-f.md#createsign). Invoke **init()**,  
**update()**, and **sign()** in this class in sequence to complete the signing operation.For details about the sample code, see  
[Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode)](../../../security/CryptoArchitectureKit/crypto-rsa-sign-sig-verify.md).

&lt;br&gt;The **Sign** instance does not support repeated initialization. When a new key is used for signing, you must create a new **Sign** instance and call **init()** for initialization.

&lt;br&gt;The signing mode is determined by **createSign()**, and the key is set by **init()**.

&lt;br&gt;If a small amount of data is to be signed, you can directly call **sign()** to pass in the data for signing after **init()**.

&lt;br&gt;If a large amount of data is to be signed, you can use **update()** to pass in the data by segment, and then use **sign()** to sign the entire data.

&lt;br&gt;When **update()** is used, the **sign()** API supports only **DataBlob** in versions earlier than API version10 and starts to support **null** since API version 10. After all the data is passed in by using **update()**, call  
**sign()** to sign the data.

&lt;br&gt;If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, the **update()** operation is not supported. If **update()** is called in this case, the error code **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface Sign--><!--Device-cryptoFramework-interface Sign-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## getSignSpec

ArkTS-Dyn:
```TypeScript
getSignSpec(itemType: SignSpecItem): string | number
```

ArkTS-Sta:
```TypeScript
getSignSpec(itemType: SignSpecItem): string | int
```

Obtains signing specifications. Currently, only RSA is supported.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-getSignSpec(itemType: SignSpecItem): string | int--><!--Device-Sign-getSignSpec(itemType: SignSpecItem): string | int-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes | Signing parameter to obtain. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the value of the signing parameter obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGetSignSpec() {
  let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1_SHA256');
  let setN = 32;
  signer.setSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
  signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM);
}
```

## init

```TypeScript
init(priKey: PriKey, callback: AsyncCallback<void>): void
```

Initializes the **Sign** object using a private key. This API uses an asynchronous callback to return the result.  
**init**, **update**, and **sign** must be used together. **init** and **sign** are mandatory, and **update** is optional.

&lt;br&gt;The **Sign** instance does not support repeated use of **init**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-init(priKey: PriKey, callback: AsyncCallback<void>): void--><!--Device-Sign-init(priKey: PriKey, callback: AsyncCallback<void>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | Private key used for the initialization. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: &lt;br&gt;1. Incorrect key type.<br>**Applicable version:** 26.0.0 and later |

## init

```TypeScript
init(priKey: PriKey): Promise<void>
```

Initializes the **Sign** object using a private key. This API uses a promise to return the result.

**init**, **update**, and **sign** must be used together. **init** and **sign** are mandatory, and **update** is optional.

&lt;br&gt;The **Sign** instance does not support repeated use of **init**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-init(priKey: PriKey): Promise<void>--><!--Device-Sign-init(priKey: PriKey): Promise<void>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | Private key used for the initialization. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: &lt;br&gt;1. Incorrect key type.<br>**Applicable version:** 26.0.0 and later |

## initSync

```TypeScript
initSync(priKey: PriKey): void
```

Initializes the **Sign** instance with a private key. This API returns the result synchronously.

**initSync**, **updateSync**, and **signSync** must be used together. **initSync** and **signSync** are mandatory, and **updateSync** is optional.

&lt;br&gt;The **Sign** instance does not support repeated use of **initSync**.

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, {@link init}. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-initSync(priKey: PriKey): void--><!--Device-Sign-initSync(priKey: PriKey): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | Private key used for the initialization. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: &lt;br&gt;1. Incorrect key type.<br>**Applicable version:** 26.0.0 and later |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: int): void
```

Sets signing specifications. You can use this API to set signing parameters that cannot be set by  
[createSign](arkts-cryptoarchitecture-cryptoframework-createsign-f.md#createsign).

&lt;br&gt;Currently, only RSA and SM2 are supported. Since API version 11, SM2 signing parameters can be set.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: int): void--><!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: int): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes | Signing parameter to set. |
| itemValue | int | Yes | Value of the signing parameter to set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testSetSignSpec() {
  let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1_SHA256');
  let setN = 20;
  signer.setSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
}
```

## setSignSpec

ArkTS-Dyn:
```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void
```

ArkTS-Sta:
```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array): void
```

Sets the specified parameter for the Sign instance.

&lt;br&gt;Currently, only PSS_SALT_LEN in RSA and USER_ID in SM2 are supported.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array): void--><!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes | Indicates the specified parameter type. |
| itemValue | ArkTS-Dyn: number \| Uint8Array  <br>ArkTS-Sta：int \| Uint8Array | Yes | The value of the specified parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call.<br>**Applicable version:** 26.0.0 and later |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters.<br>**Applicable version:** 26.0.0 and later |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array | boolean): void
```

Sets the specified parameter for the Sign instance.

&lt;br&gt;Currently, only PSS_SALT_LEN in RSA, USER_ID in SM2, and ML_DSA_DETERMINISTIC, ML_DSA_MU, and ML_DSA_CONTEXT in ML-DSA are supported.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array | boolean): void--><!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array | boolean): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes | Indicates the specified parameter type. |
| itemValue | int \| Uint8Array \| boolean | Yes | The value of the specified parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: boolean): void
```

Sets the specified parameter for the Sign instance.

&lt;br&gt;Currently, only ML_DSA_DETERMINISTIC and ML_DSA_MU in ML-DSA are supported. For ML_DSA_CONTEXT parameter,use [setSignSpec()](arkts-cryptoarchitecture-cryptoframework-sign-i.md#setsignspec).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: boolean): void--><!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: boolean): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes | Indicates the specified parameter type. |
| itemValue | boolean | Yes | The value of the specified parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. |

## sign

```TypeScript
sign(data: DataBlob, callback: AsyncCallback<DataBlob>): void
```

Signs the data, including data added via the update interface. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-sign(data: DataBlob, callback: AsyncCallback<DataBlob>): void--><!--Device-Sign-sign(data: DataBlob, callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | The data to be signed. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the signature obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## sign

```TypeScript
sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void
```

Signs data. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void--><!--Device-Sign-sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) \| null | Yes | Data to pass in. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the signature obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## sign

```TypeScript
sign(data: DataBlob): Promise<DataBlob>
```

Signs the data, including data added via the update interface. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-sign(data: DataBlob): Promise<DataBlob>--><!--Device-Sign-sign(data: DataBlob): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | The data to be signed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataBlob&gt; | Promise used to return the signature. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## sign

```TypeScript
sign(data: DataBlob | null): Promise<DataBlob>
```

Signs data. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-sign(data: DataBlob | null): Promise<DataBlob>--><!--Device-Sign-sign(data: DataBlob | null): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) \| null | Yes | Data to pass in. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataBlob&gt; | Promise used to return the signature. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## signSync

```TypeScript
signSync(data: DataBlob | null): DataBlob
```

Signs the data. This API returns the result synchronously.

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, {@link sign}. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-signSync(data: DataBlob | null): DataBlob--><!--Device-Sign-signSync(data: DataBlob | null): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) \| null | Yes | Data to pass in. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Signature. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## update

```TypeScript
update(data: DataBlob, callback: AsyncCallback<void>): void
```

Updates data to be signed. This API uses an asynchronous callback to return the result.

&lt;br&gt;This API can be called only after the [Sign](arkts-cryptoarchitecture-cryptoframework-sign-i.md) instance is initialized by using  
[init](arkts-cryptoarchitecture-cryptoframework-sign-i.md#init) or [initSync](arkts-cryptoarchitecture-cryptoframework-sign-i.md#initsync).

> **NOTE：**
> 
> You can call **update** multiple times or do not use **update** (call [sign](arkts-cryptoarchitecture-cryptoframework-sign-i.md) after
> [init](arkts-cryptoarchitecture-cryptoframework-sign-i.md#init)), depending on the data volume.
> 
> The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a
> large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This
> prevents too much memory from being requested at a time.
> 
> For details about the sample code for calling **update()** multiple times in signing, see
> [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](../../../security/CryptoArchitectureKit/crypto-rsa-sign-sig-verify.md)
> . The operations of other algorithms are similar.
> 
> **OnlySign** cannot be used with **update()**. If **OnlySign** is specified, use **sign()** to pass in data.
> 
> If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **update()** is not supported.
> If **update()** is called in this case, **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-update(data: DataBlob, callback: AsyncCallback<void>): void--><!--Device-Sign-update(data: DataBlob, callback: AsyncCallback<void>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | Data to pass in. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call.<br>**Applicable version:** 26.0.0 and later |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |

## update

```TypeScript
update(data: DataBlob): Promise<void>
```

Updates data to be signed. This API uses a promise to return the result.

&lt;br&gt;Before using this API, you must initialize the [Sign](arkts-cryptoarchitecture-cryptoframework-sign-i.md) instance by using  
[init()](arkts-cryptoarchitecture-cryptoframework-sign-i.md#init).

> **NOTE：**
> 
> You can call **update** multiple times or do not use **update** (call
> [sign](arkts-cryptoarchitecture-cryptoframework-sign-i.md#sign) after
> [init](arkts-cryptoarchitecture-cryptoframework-sign-i.md#init)), depending on the
> data volume.
> 
> The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a
> large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This
> prevents too much memory from being requested at a time.
> For details about the sample code for calling **update()** multiple times in signing, see
> [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](../../../security/CryptoArchitectureKit/crypto-rsa-sign-sig-verify.md)
> . The operations of other algorithms are similar.
> 
> **OnlySign** cannot be used with **update()**. If **OnlySign** is specified, use **sign()** to pass in data.
> 
> If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **update()** is not supported.
> If **update()** is called in this case, **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-update(data: DataBlob): Promise<void>--><!--Device-Sign-update(data: DataBlob): Promise<void>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | Data to pass in. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call.<br>**Applicable version:** 26.0.0 and later |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |

## updateSync

```TypeScript
updateSync(data: DataBlob): void
```

Updates data to be signed. This API returns the result synchronously.

&lt;br&gt;This API can be called only after the [Sign](arkts-cryptoarchitecture-cryptoframework-sign-i.md) instance is initialized by using  
[initSync()](arkts-cryptoarchitecture-cryptoframework-sign-i.md#initsync).

> **NOTE：**
> 
> You can call **updateSync** multiple times or do not use **updateSync** (call
> [signSync](arkts-cryptoarchitecture-cryptoframework-sign-i.md#signsync) after [initSync](arkts-cryptoarchitecture-cryptoframework-sign-i.md#initsync)),
> depending on the data volume.
> 
> The amount of the data to be passed in by **updateSync** (one-time or accumulative) is not limited. If there is
> a large amount of data, you are advised to call **updateSync** multiple times to pass in the data by segment.
> This prevents too much memory from being requested at a time.
> 
> For details about the sample code for calling **updateSync** multiple times in signing, see
> [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](../../../security/CryptoArchitectureKit/crypto-rsa-sign-sig-verify.md)
> . The operations of other algorithms are similar.
> 
> **OnlySign** cannot be used with **updateSync**. If **OnlySign** is specified, use **signSync** to pass in
> data.
> 
> If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **updateSync** is not
> supported. If **updateSync** is called in this case, **ERR_CRYPTO_OPERATION** will be returned.

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, {@link update}. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-updateSync(data: DataBlob): void--><!--Device-Sign-updateSync(data: DataBlob): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | Data to pass in. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call.<br>**Applicable version:** 26.0.0 and later |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name of the Sign instance.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-readonly algName: string--><!--Device-Sign-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

