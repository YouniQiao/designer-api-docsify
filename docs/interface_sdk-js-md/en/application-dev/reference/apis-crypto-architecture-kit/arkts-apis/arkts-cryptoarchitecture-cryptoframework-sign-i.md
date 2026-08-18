# Sign

Signing interface, defining methods for signing data using a private key. Before use, you must create a **Sign** instance by using [createSign(algName: string): Sign](arkts-cryptoarchitecture-cryptoframework-createsign-f.md). Invoke **init()**, **update()**, and **sign()** in this class in sequence to complete the signing operation. For details about the sample code, see Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode) . <br>The **Sign** instance does not support repeated initialization. When a new key is used for signing, you must create a new **Sign** instance and call **init()** for initialization. <br>The signing mode is determined by **createSign()**, and the key is set by **init()**. <br>If a small amount of data is to be signed, you can directly call **sign()** to pass in the data for signing after **init()**. <br>If a large amount of data is to be signed, you can use **update()** to pass in the data by segment, and then use **sign()** to sign the entire data. <br>When **update()** is used, the **sign()** API supports only **DataBlob** in versions earlier than API version 10 and starts to support **null** since API version 10. After all the data is passed in by using **update()**, call **sign()** to sign the data. <br>If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, the **update()** operation is not supported. If **update()** is called in this case, the error code **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 23

<!--Device-cryptoFramework-interface Sign--><!--Device-cryptoFramework-interface Sign-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## getSignSpec

```TypeScript
getSignSpec(itemType: SignSpecItem): string | int
```

Obtains signing specifications. Currently, only RSA is supported.

**Since:** 23

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | This operation is not supported. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

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

Initializes the **Sign** object using a private key. This API uses an asynchronous callback to return the result. **init**, **update**, and **sign** must be used together. **init** and **sign** are mandatory, and **update** is optional. <br>The **Sign** instance does not support repeated use of **init**.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-init(priKey: PriKey, callback: AsyncCallback<void>): void--><!--Device-Sign-init(priKey: PriKey, callback: AsyncCallback<void>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | Private key used for the initialization. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: <br>1. Incorrect key type.<br>**Applicable version:** 26.0.0 and later |

## init

```TypeScript
init(priKey: PriKey): Promise<void>
```

Initializes the **Sign** object using a private key. This API uses a promise to return the result. **init**, **update**, and **sign** must be used together. **init** and **sign** are mandatory, and **update** is optional. <br>The **Sign** instance does not support repeated use of **init**.

**Since:** 23

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: <br>1. Incorrect key type.<br>**Applicable version:** 26.0.0 and later |

## initSync

```TypeScript
initSync(priKey: PriKey): void
```

Initializes the **Sign** instance with a private key. This API returns the result synchronously. **initSync**, **updateSync**, and **signSync** must be used together. **initSync** and **signSync** are mandatory, and **updateSync** is optional. <br>The **Sign** instance does not support repeated use of **initSync**. <br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, init. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Sign-initSync(priKey: PriKey): void--><!--Device-Sign-initSync(priKey: PriKey): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | Private key used for the initialization. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. Possible causes: <br>1. Incorrect key type.<br>**Applicable version:** 26.0.0 and later |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: int): void
```

Sets signing specifications. You can use this API to set signing parameters that cannot be set by [createSign](arkts-cryptoarchitecture-cryptoframework-createsign-f.md). <br>Currently, only RSA and SM2 are supported. Since API version 11, SM2 signing parameters can be set.

**Since:** 10

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | This operation is not supported. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testSetSignSpec() {
  let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1_SHA256');
  let setN = 20;
  signer.setSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
}
```

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array): void
```

Sets the specified parameter for the Sign instance. <br>Currently, only PSS_SALT_LEN in RSA and USER_ID in SM2 are supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array): void--><!--Device-Sign-setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes | Indicates the specified parameter type. |
| itemValue | int \| Uint8Array | Yes | The value of the specified parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | This operation is not supported. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call.<br>**Applicable version:** 26.0.0 and later |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters.<br>**Applicable version:** 26.0.0 and later |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: int | Uint8Array | boolean): void
```

Sets the specified parameter for the Sign instance. <br>Currently, only PSS_SALT_LEN in RSA, USER_ID in SM2, and ML_DSA_DETERMINISTIC, ML_DSA_MU, and ML_DSA_CONTEXT in ML-DSA are supported.

**Since:** 26.0.0

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
| [801](../../errorcode-universal.md#801-api-not-supported) | This operation is not supported. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed. |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: boolean): void
```

Sets the specified parameter for the Sign instance. <br>Currently, only ML_DSA_DETERMINISTIC and ML_DSA_MU in ML-DSA are supported. For ML_DSA_CONTEXT parameter, use [setSignSpec()](#setsignspec).

**Since:** 26.0.0

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-sign(data: DataBlob, callback: AsyncCallback<DataBlob>): void--><!--Device-Sign-sign(data: DataBlob, callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | DataBlob | Yes | The data to be signed. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;DataBlob&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the signature obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## sign

```TypeScript
sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void
```

Signs data. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void--><!--Device-Sign-sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | DataBlob \| null | Yes | Data to pass in. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;DataBlob&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the signature obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-sign(data: DataBlob): Promise<DataBlob>--><!--Device-Sign-sign(data: DataBlob): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | DataBlob | Yes | The data to be signed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataBlob&gt; | Promise used to return the signature. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## sign

```TypeScript
sign(data: DataBlob | null): Promise<DataBlob>
```

Signs data. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-sign(data: DataBlob | null): Promise<DataBlob>--><!--Device-Sign-sign(data: DataBlob | null): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | DataBlob \| null | Yes | Data to pass in. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataBlob&gt; | Promise used to return the signature. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## signSync

```TypeScript
signSync(data: DataBlob | null): DataBlob
```

Signs the data. This API returns the result synchronously. <br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, [sign](#sign). Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Sign-signSync(data: DataBlob | null): DataBlob--><!--Device-Sign-signSync(data: DataBlob | null): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | DataBlob \| null | Yes | Data to pass in. |

**Return value:**

| Type | Description |
| --- | --- |
| DataBlob | Signature. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) | Parameter check failed.<br>**Applicable version:** 26.0.0 and later |

## update

```TypeScript
update(data: DataBlob, callback: AsyncCallback<void>): void
```

Updates data to be signed. This API uses an asynchronous callback to return the result. <br>This API can be called only after the [Sign](#sign) instance is initialized by using [init](#init) or [initSync](#initsync). > **NOTE：**> > You can call **update** multiple times or do not use **update** (call [sign](#sign) after > [init](#init)), depending on the data volume. > > The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a > large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This > prevents too much memory from being requested at a time. > > For details about the sample code for calling **update()** multiple times in signing, see > Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode) > . The operations of other algorithms are similar. > > **OnlySign** cannot be used with **update()**. If **OnlySign** is specified, use **sign()** to pass in data. > > If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **update()** is not supported. > If **update()** is called in this case, **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-update(data: DataBlob, callback: AsyncCallback<void>): void--><!--Device-Sign-update(data: DataBlob, callback: AsyncCallback<void>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | DataBlob | Yes | Data to pass in. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call.<br>**Applicable version:** 26.0.0 and later |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |

## update

```TypeScript
update(data: DataBlob): Promise<void>
```

Updates data to be signed. This API uses a promise to return the result. <br>Before using this API, you must initialize the [Sign](#sign) instance by using [init()](#init). > **NOTE：**> > You can call **update** multiple times or do not use **update** (call > [sign](#sign) after > [init](#init)), depending on the > data volume. > > The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a > large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This > prevents too much memory from being requested at a time. > For details about the sample code for calling **update()** multiple times in signing, see > Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode) > . The operations of other algorithms are similar. > > **OnlySign** cannot be used with **update()**. If **OnlySign** is specified, use **sign()** to pass in data. > > If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **update()** is not supported. > If **update()** is called in this case, **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-update(data: DataBlob): Promise<void>--><!--Device-Sign-update(data: DataBlob): Promise<void>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | DataBlob | Yes | Data to pass in. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) | Invalid function call.<br>**Applicable version:** 26.0.0 and later |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |

## updateSync

```TypeScript
updateSync(data: DataBlob): void
```

Updates data to be signed. This API returns the result synchronously. <br>This API can be called only after the [Sign](#sign) instance is initialized by using [initSync()](#initsync). > **NOTE：**> > You can call **updateSync** multiple times or do not use **updateSync** (call > [signSync](#signsync) after [initSync](#initsync)), > depending on the data volume. > > The amount of the data to be passed in by **updateSync** (one-time or accumulative) is not limited. If there is > a large amount of data, you are advised to call **updateSync** multiple times to pass in the data by segment. > This prevents too much memory from being requested at a time. > > For details about the sample code for calling **updateSync** multiple times in signing, see > Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode) > . The operations of other algorithms are similar. > > **OnlySign** cannot be used with **updateSync**. If **OnlySign** is specified, use **signSync** to pass in > data. > > If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **updateSync** is not > supported. If **updateSync** is called in this case, **ERR_CRYPTO_OPERATION** will be returned. <br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, update. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Sign-updateSync(data: DataBlob): void--><!--Device-Sign-updateSync(data: DataBlob): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | DataBlob | Yes | Data to pass in. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
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

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Sign-readonly algName: string--><!--Device-Sign-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

