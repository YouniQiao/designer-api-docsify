# Sign

Signing interface, defining methods for signing data using a private key. Before use, you must create a **Sign** instance by using [createSign(algName: string): Sign](arkts-cryptoarchitecture-cryptoframework-createsign-f.md). Invoke **init()**, **update()**, and **sign()** in this class in sequence to complete the signing operation. For details about the sample code, see Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode).

The **Sign** instance does not support repeated initialization. When a new key is used for signing, you must create a new **Sign** instance and call **init()** for initialization.

The signing mode is determined by **createSign()**, and the key is set by **init()**.

If a small amount of data is to be signed, you can directly call **sign()** to pass in the data for signing after **init()**.

If a large amount of data is to be signed, you can use **update()** to pass in the data by segment, and then use **sign()** to sign the entire data.

When **update()** is used, the **sign()** API supports only **DataBlob** in versions earlier than API version 10 and starts to support **null** since API version 10. After all the data is passed in by using **update()**, call **sign()** to sign the data.

If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, the **update()** operation is not supported. If **update()** is called in this case, the error code **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 9

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## getSignSpec

```TypeScript
getSignSpec(itemType: SignSpecItem): string | number
```

Obtains signing specifications. Currently, only RSA is supported.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [itemType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string \| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## init

```TypeScript
init(priKey: PriKey, callback: AsyncCallback<void>): void
```

Initializes the **Sign** object using a private key. This API uses an asynchronous callback to return the result. **init**, **update**, and **sign** must be used together. **init** and **sign** are mandatory, and **update** is optional.

The **Sign** instance does not support repeated use of **init**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## init

```TypeScript
init(priKey: PriKey): Promise<void>
```

Initializes the **Sign** object using a private key. This API uses a promise to return the result.  
**init**, **update**, and **sign** must be used together. **init** and **sign** are mandatory, and **update** is optional.

The **Sign** instance does not support repeated use of **init**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## initSync

```TypeScript
initSync(priKey: PriKey): void
```

Initializes the **Sign** instance with a private key. This API returns the result synchronously.  
**initSync**, **updateSync**, and **signSync** must be used together. **initSync** and **signSync** are mandatory, and **updateSync** is optional.

The **Sign** instance does not support repeated use of **initSync**.

**NOTE：**It is recommended to prioritize the use of asynchronous API, init. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: number): void
```

Sets signing specifications. You can use this API to set signing parameters that cannot be set by [createSign](arkts-cryptoarchitecture-cryptoframework-createsign-f.md).

Currently, only RSA and SM2 are supported. Since API version 11, SM2 signing parameters can be set.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [itemType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes |
| itemValue | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void
```

Sets the specified parameter for the Sign instance.

Currently, only PSS_SALT_LEN in RSA and USER_ID in SM2 are supported.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [itemType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes |
| itemValue | number \| Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## setSignSpec

```TypeScript
setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array | boolean): void
```

Sets the specified parameter for the Sign instance.

Currently, only PSS_SALT_LEN in RSA, USER_ID in SM2, and ML_DSA_DETERMINISTIC, ML_DSA_MU, and ML_DSA_CONTEXT in ML-DSA are supported.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [itemType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | Yes |
| itemValue | number \| Uint8Array \| boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## sign

```TypeScript
sign(data: DataBlob, callback: AsyncCallback<DataBlob>): void
```

Signs the data, including data added via the update interface. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## sign

```TypeScript
sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void
```

Signs data. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | DataBlob \| null | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## sign

```TypeScript
sign(data: DataBlob): Promise<DataBlob>
```

Signs the data, including data added via the update interface. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DataBlob & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## sign

```TypeScript
sign(data: DataBlob | null): Promise<DataBlob>
```

Signs data. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | DataBlob \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DataBlob & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## signSync

```TypeScript
signSync(data: DataBlob | null): DataBlob
```

Signs the data. This API returns the result synchronously.

**NOTE：**It is recommended to prioritize the use of asynchronous API, [sign](#sign). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | DataBlob \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## update

```TypeScript
update(data: DataBlob, callback: AsyncCallback<void>): void
```

Updates data to be signed. This API uses an asynchronous callback to return the result.

This API can be called only after the [Sign](#sign) instance is initialized by using [init](#init) or [initSync](#initsync).

> **NOTE：**&gt;
> You can call **update** multiple times or do not use **update** (call [sign](#sign) after
> [init](#init)), depending on the data volume.&gt;
> The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a
> large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This
> prevents too much memory from being requested at a time.&gt;
> For details about the sample code for calling **update()** multiple times in signing, see
> Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)
> . The operations of other algorithms are similar.&gt;
> **OnlySign** cannot be used with **update()**. If **OnlySign** is specified, use **sign()** to pass in data.&gt;
> If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **update()** is not supported.
> If **update()** is called in this case, **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) |

## update

```TypeScript
update(data: DataBlob): Promise<void>
```

Updates data to be signed. This API uses a promise to return the result.

Before using this API, you must initialize the [Sign](#sign) instance by using [init()](#init).

> **NOTE：**&gt;
> You can call **update** multiple times or do not use **update** (call
> [sign](#sign) after
> [init](#init)), depending on the
> data volume.&gt;
> The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a
> large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This
> prevents too much memory from being requested at a time.
> For details about the sample code for calling **update()** multiple times in signing, see
> Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)
> . The operations of other algorithms are similar.&gt;
> **OnlySign** cannot be used with **update()**. If **OnlySign** is specified, use **sign()** to pass in data.&gt;
> If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **update()** is not supported.
> If **update()** is called in this case, **ERR_CRYPTO_OPERATION** will be returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) |

## updateSync

```TypeScript
updateSync(data: DataBlob): void
```

Updates data to be signed. This API returns the result synchronously.

This API can be called only after the [Sign](#sign) instance is initialized by using [initSync()](#initsync).

> **NOTE：**&gt;
> You can call **updateSync** multiple times or do not use **updateSync** (call
> [signSync](#signsync) after [initSync](#initsync)),
> depending on the data volume.&gt;
> The amount of the data to be passed in by **updateSync** (one-time or accumulative) is not limited. If there is
> a large amount of data, you are advised to call **updateSync** multiple times to pass in the data by segment.
> This prevents too much memory from being requested at a time.&gt;
> For details about the sample code for calling **updateSync** multiple times in signing, see
> Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)
> . The operations of other algorithms are similar.&gt;
> **OnlySign** cannot be used with **updateSync**. If **OnlySign** is specified, use **signSync** to pass in
> data.&gt;
> If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **updateSync** is not
> supported. If **updateSync** is called in this case, **ERR_CRYPTO_OPERATION** will be returned.

**NOTE：**It is recommended to prioritize the use of asynchronous API, update. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) |

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name of the Sign instance.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework
