# Cipher

Encryption and decryption interface, defining methods for symmetric and asymmetric encryption and decryption. Before use, you must create a **Cipher** instance by using [createCipher(transformation: string): Cipher](arkts-cryptoarchitecture-cryptoframework-createcipher-f.md). Call the [init()](#init), [update()](#update), and [doFinal()](#dofinal) APIs in this class as needed to complete encryption or decryption operations.

For details about the complete encryption and decryption process, see Encryption and Decryption Overview.

A complete symmetric encryption/decryption process is slightly different from the asymmetric encryption/decryption process.  
- Symmetric encryption and decryption: **init()** and **doFinal()** are mandatory. **update()** is optional and can  
be called multiple times to encrypt or decrypt big data. After **doFinal()** is called to complete an encryption or decryption operation, **init()** can be called to start a new encryption or decryption operation.  
- RSA or SM2 asymmetric encryption and decryption: **init()** and **doFinal()** are mandatory, and **update()** is  
not supported. **doFinal()** can be called multiple times to encrypt or decrypt big data. **init()** cannot be called repeatedly. If the encryption/decryption mode or padding mode is changed, a new **Cipher** object must be created.

**Since:** 9

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## doFinal

```TypeScript
doFinal(data: DataBlob, callback: AsyncCallback<DataBlob>): void
```

Finishes the crypto operation, encrypts or decrypts the input data, and then feeds back the output data. Data cannot be updated after the crypto operation is finished. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
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

## doFinal

```TypeScript
doFinal(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void
```

Finishes the crypto operation, encrypts or decrypts the input data, and then feeds back the output data. Data cannot be updated after the crypto operation is finished. This API uses an asynchronous callback to return the result.

(1) Processes the remaining data and the data passed in this time, and completes the encryption or decryption operation for symmetric encryption and decryption. This API uses an asynchronous callback to return the encrypted or decrypted data. If a small amount of data needs to be encrypted or decrypted, you can use **doFinal()** to pass in all the data without using **update()**. If all the data has been passed in by [update()](#update), you can pass in **null** in **data** of **doFinal()**. The output of **doFinal()** varies with the symmetric block cipher mode in use. This API uses an asynchronous callback to return the result.  
- In a single encryption process with GCM or CCM mode, concatenating the results of each **update()** and  
**doFinal()** produces the ciphertext and **authTag**. In GCM mode, **authTag** is the last 16 bytes. In CCM mode, **authTag** is the last 12 bytes. The rest part is the ciphertext. If **data** passed to **doFinal()** is **null**, the **doFinal()** result is only the **authTag**. During decryption, **authTag** must be set in [GcmParamsSpec](arkts-cryptoarchitecture-cryptoframework-gcmparamsspec-i.md) or [CcmParamsSpec](arkts-cryptoarchitecture-cryptoframework-ccmparamsspec-i.md), and the ciphertext must be set in **data**.  
- For other symmetric encryption and decryption modes and GCM and CCM decryption modes, concatenating the results  
of **update()** and **doFinal()** throughout the process will yield the complete plaintext or ciphertext.(2) Encrypts or decrypts the data passed in this time in RSA and SM2 asymmetric encryption or decryption. This API uses an asynchronous callback to return the encrypted or decrypted data. If a large amount of data needs to be encrypted/decrypted, call **doFinal()** multiple times and concatenate the result of each **doFinal()** to obtain the complete plaintext/ciphertext.

> **NOTE：**&gt;
> 1. In symmetric encryption and decryption, after **doFinal** is called, the encryption and decryption process
> is complete and the [Cipher](#cipher) instance is cleared. When a new encryption and
> decryption process is started, **init()** must be called with a complete parameter list for initialization.
> Even if the same symmetric key is used to encrypt and decrypt the same **Cipher** instance, the **params**
> parameter must be set when **init** is called during decryption.
> 2. If a decryption fails, check whether the data to be encrypted and decrypted matches the parameters in
> **init()**. For the GCM mode, check whether the **authTag** obtained after encryption is obtained from the
> **GcmParamsSpec** for decryption.
> 3. The result of **doFinal()** may be **null**. To avoid exceptions, determine whether the result is **null**
> before using the **.data** field to access the **doFinal()** result.
> For encryption in CFB, OFB, or CTR mode, if **doFinal()** passes in **null**, the returned result is **null**.
> For decryption in GCM, CCM, CFB, OFB, or CTR mode, if **doFinal()** passes in **null**, the returned result is
> **null**. For decryption in other modes, if **update** is called to pass in all the plaintext, which is an
> integer multiple of the encryption block size, and **doFinal()** is called to pass in **null**, the returned
> result is **null**.
> 4. For details about the sample code for calling **doFinal** multiple times in asymmetric encryption and
> decryption, see Encryption and Decryption by Segment with an RSA Asymmetric Key Pair.
> The operations are similar for SM2 and RSA.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
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

## doFinal

```TypeScript
doFinal(data: DataBlob): Promise<DataBlob>
```

Finishes the crypto operation, encrypts or decrypts the input data, and then feeds back the output data. Data cannot be updated after the crypto operation is finished. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
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

## doFinal

```TypeScript
doFinal(data: DataBlob | null): Promise<DataBlob>
```

Finishes the crypto operation, encrypts or decrypts the input data, and then feeds back the output data. Data cannot be updated after the crypto operation is finished. This API uses a promise to return the result.

(1) Encrypts or decrypts the remaining data (generated by the block cipher mode) and the data passed in this time to finalize the symmetric encryption or decryption. This API uses a promise to return the result.If a small amount of data needs to be encrypted or decrypted, you can use **doFinal()** to pass in data without using **update()**. If all the data has been passed in by **update()**, you can pass in **null** in **data** of **doFinal()**.The output of **doFinal()** varies with the symmetric encryption/decryption mode in use.  
- Symmetric encryption in GCM and CCM mode: The result consists of the ciphertext and **authTag** (the last 16  
bytes for GCM and the last 12 bytes for CCM). If **data** in **doFinal** is null, the result of **doFinal** is **authTag**.During decryption, **authTag** must be set in [GcmParamsSpec](arkts-cryptoarchitecture-cryptoframework-gcmparamsspec-i.md) or [CcmParamsSpec](arkts-cryptoarchitecture-cryptoframework-ccmparamsspec-i.md), and the ciphertext must be set in **data**.  
- For other symmetric encryption and decryption modes and GCM and CCM decryption modes, concatenating the results  
of **update()** and **doFinal()** throughout the process will yield the complete plaintext or ciphertext.(2) Encrypts or decrypts the data passed in RSA and SM2 asymmetric encryption or decryption. This API uses a promise to return the encrypted or decrypted data. If a large amount of data is to be processed, call **doFinal()** multiple times and concatenate the results to obtain the complete plaintext or ciphertext.

> **NOTE：**&gt;
> 1. In symmetric encryption and decryption, after **doFinal** is called, the encryption and decryption process
> is complete and the [Cipher](#cipher) instance is cleared. When a new encryption and
> decryption process is started, **init()** must be called with a complete parameter list for initialization.
> Even if the same symmetric key is used to encrypt and decrypt the same **Cipher** instance, the **params**
> parameter must be set when **init** is called during decryption.
> 2. If a decryption fails, check whether the data to be encrypted and decrypted matches the parameters in
> **init()**. For the GCM mode, check whether the **authTag** obtained after encryption is obtained from the
> **GcmParamsSpec** for decryption.
> 3. The result of **doFinal()** may be **null**. To avoid exceptions, determine whether the result is **null**
> before using the **.data** field to access the **doFinal()** result.
> For encryption in CFB, OFB, or CTR mode, if **doFinal()** passes in **null**, the returned result is **null**.
> For decryption in GCM, CCM, CFB, OFB, or CTR mode, if **doFinal()** passes in **null**, the returned result is
> **null**. For decryption in other modes, if **update** is called to pass in all the plaintext, which is an
> integer multiple of the encryption block size, and **doFinal()** is called to pass in **null**, the returned
> result is **null**.
> 4. For details about the sample code for calling **doFinal** multiple times in asymmetric encryption and
> decryption, see Encryption and Decryption by Segment with an RSA Asymmetric Key Pair.
> The operations are similar for SM2 and RSA.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
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

## doFinalSync

```TypeScript
doFinalSync(data: DataBlob | null): DataBlob
```

Finishes the crypto operation, encrypts or decrypts the input data, and then feeds back the output data. Data cannot be updated after the crypto operation is finished.

(1) Processes the remaining data and the data passed in this time, and completes the encryption or decryption operation for symmetric encryption and decryption. This API returns the encrypted or decrypted data synchronously.If a small amount of data is to be processed, you can pass in all the data at a time in **doFinalSync()** without using **updateSync()**. If data has been passed in by using [updateSync](#updatesync) in the current encryption and decryption process, you can pass in **null** to the **data** parameter of **doFinalSync()**.The output of **doFinalSync()** varies with the symmetric block cipher mode in use.  
- In a single encryption process with GCM or CCM mode, concatenating the results of each **updateSync()** and  
**doFinalSync()** produces the ciphertext and **authTag**. In GCM mode, **authTag** is the last 16 bytes. In CCM mode, **authTag** is the last 12 bytes. The rest part is the ciphertext. If **data** in **doFinalSync()** is **null**, the result of **doFinalSync()** is **authTag**.  
- During decryption, **authTag** must be set in [GcmParamsSpec](arkts-cryptoarchitecture-cryptoframework-gcmparamsspec-i.md) or  
[CcmParamsSpec](arkts-cryptoarchitecture-cryptoframework-ccmparamsspec-i.md), and the ciphertext must be set in **data**.  
- For other symmetric encryption and decryption modes and GCM and CCM decryption modes, concatenating the results  
of **updateSync()** and **doFinalSync()** throughout the process will yield the complete plaintext or ciphertext.(2) Encrypts or decrypts the input data for RSA or SM2 asymmetric encryption/decryption. This API returns the encrypted or decrypted data synchronously. If a large amount of data is to be processed, call **doFinalSync()** multiple times and concatenate the results to obtain the complete plaintext or ciphertext.

See **NOTE：**in [doFinal()](#dofinal) for other precautions.

**NOTE：**It is recommended to prioritize the use of asynchronous API, doFinal. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

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

## getCipherSpec

```TypeScript
getCipherSpec(itemType: CipherSpecItem): string | Uint8Array
```

Obtains cipher specifications. Currently, only RSA and SM2 (available since API version 11) are supported.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [itemType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | [CipherSpecItem](arkts-cryptoarchitecture-cryptoframework-cipherspecitem-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string \| Uint8Array |

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
init(opMode: CryptoMode, key: Key, params: ParamsSpec, callback: AsyncCallback<void>): void
```

Initializes the crypto operation with the given crypto mode, key and parameters. This API uses an asynchronous callback to return the result.

**init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| opMode | [CryptoMode](arkts-cryptoarchitecture-cryptoframework-cryptomode-e.md) | Yes |
| key | [Key](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-key-i.md) | Yes |
| params | [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md) | Yes |
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
init(opMode: CryptoMode, key: Key, params: ParamsSpec | null, callback: AsyncCallback<void>): void
```

Initializes the [cipher](#cipher) object for encryption and decryption. This API uses an asynchronous callback to return the result.

**init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| opMode | [CryptoMode](arkts-cryptoarchitecture-cryptoframework-cryptomode-e.md) | Yes |
| key | [Key](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-key-i.md) | Yes |
| params | [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md) \| null | Yes |
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
init(opMode: CryptoMode, key: Key, params: ParamsSpec): Promise<void>
```

Initializes the crypto operation with the given crypto mode, key and parameters. This API uses a promise to return the result.

**init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| opMode | [CryptoMode](arkts-cryptoarchitecture-cryptoframework-cryptomode-e.md) | Yes |
| key | [Key](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-key-i.md) | Yes |
| params | [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md) | Yes |

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

## init

```TypeScript
init(opMode: CryptoMode, key: Key, params: ParamsSpec | null): Promise<void>
```

Initializes the cipher object for encryption and decryption. This API uses a promise to return the result.

**init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| opMode | [CryptoMode](arkts-cryptoarchitecture-cryptoframework-cryptomode-e.md) | Yes |
| key | [Key](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-key-i.md) | Yes |
| params | [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md) \| null | Yes |

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
initSync(opMode: CryptoMode, key: Key, params: ParamsSpec | null): void
```

Initializes a [cipher](#cipher) instance. This API returns the result synchronously.

**initSync**, **updateSync**, and **doFinalSync** must be used together. **initSync** and **doFinalSync** are mandatory, and **updateSync** is optional.

**NOTE：**It is recommended to prioritize the use of asynchronous API, init. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| opMode | [CryptoMode](arkts-cryptoarchitecture-cryptoframework-cryptomode-e.md) | Yes |
| key | [Key](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-key-i.md) | Yes |
| params | [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## setCipherSpec

```TypeScript
setCipherSpec(itemType: CipherSpecItem, itemValue: Uint8Array): void
```

Sets cipher specifications. You can use this API to set cipher specifications that cannot be set by [createCipher](arkts-cryptoarchitecture-cryptoframework-createcipher-f.md). Currently, only RSA is supported.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [itemType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | [CipherSpecItem](arkts-cryptoarchitecture-cryptoframework-cipherspecitem-e.md) | Yes |
| itemValue | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## update

```TypeScript
update(data: DataBlob, callback: AsyncCallback<DataBlob>): void
```

Updates the data to encrypt or decrypt by segment. This API uses an asynchronous callback to return the result.

This API can be called only after the [Cipher](#cipher) instance is initialized by using [init()](#init).

> **NOTE：**&gt;
> 1. The results of **update()** and **doFinal()** may vary with the block mode used. If you are not familiar
> with the block modes, you are advised to check each **update()** and **doFinal()** result to ensure that the
> results are not **null**. When a valid result is returned, extract and concatenate the data to form a complete
> ciphertext or plaintext.
> 
For example, in ECB and CBC modes, encryption and decryption are performed by block regardless of whether the  
> data input by **update()** is an integer multiple of the block size, and **update()** returns the newly
> processed block data.
> 
That is, data is returned as number as the data passed in by **update()** reaches the size of a block. Otherwise,  
> **null** is returned and the data will be retained until a block is formed in the next **update()** or
> **doFinal()**.
> 
In the final **doFinal()** operation, the remaining unprocessed data is padded based on the padding mode set in  
> [createCipher](arkts-cryptoarchitecture-cryptoframework-createcipher-f.md) to the integer multiple of the block size to produce the
> final encrypted or decrypted data.
> 
For block cipher modes that can be converted to stream mode, the ciphertext length may be the same as the  
> plaintext length.
> 2. You can call **update()** multiple times or skip calling **update()** (call **doFinal()** directly after
> **init()**), depending on the data volume.
> 
The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a  
> large amount of data, you are advised to pass data in multiple **update()** calls rather than processing it all
> at once.
> 
For details about the sample code for passing data in multiple **update()** calls, see  
> Encryption and Decryption by Segment with an AES Symmetric Key (GCM Mode).
> 3. RSA or SM2 asymmetric encryption and decryption do not support **update()**.
> 4. If CCM is used in symmetric encryption or decryption, **update()** can be called only once. In the
> encryption process, you can either use **update()** to encrypt data and use **doFinal()** to obtain **authTag**
> or use **doFinal()** without using **update()**. In the decryption process, you can either use **update()** or
> **doFinal()** once to decrypt data and verify the tag.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
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

## update

```TypeScript
update(data: DataBlob): Promise<DataBlob>
```

Updates the data to encrypt or decrypt by segment. This API uses a promise to return the result.

This API can be called only after the [Cipher](#cipher) instance is initialized by using [init()](#init).

> **NOTE：**&gt;
> 1. The results of **update()** and **doFinal()** may vary with the block mode used. If you are not familiar
> with the block modes, you are advised to check each **update()** and **doFinal()** result to ensure that the
> results are not **null**. When a valid result is returned, extract and concatenate the data to form a complete
> ciphertext or plaintext.
> 
For example, in ECB and CBC modes, encryption and decryption are performed by block regardless of whether the  
> data input by **update()** is an integer multiple of the block size, and **update()** returns the newly
> processed block data.
> 
That is, data is returned as number as the data passed in by **update()** reaches the size of a block. Otherwise,  
> **null** is returned and the data will be retained until a block is formed in the next **update()** or
> **doFinal()**.
> 
In the final **doFinal()** operation, the remaining unprocessed data is padded based on the padding mode set in  
> [createCipher](arkts-cryptoarchitecture-cryptoframework-createcipher-f.md) to the integer multiple of the block size to produce the
> final encrypted or decrypted data.
> 
For block cipher modes that can be converted to stream mode, the ciphertext length may be the same as the  
> plaintext length.
> 2. You can call **update()** multiple times or skip calling **update()** (call **doFinal()** directly after
> **init()**), depending on the data volume.
> 
The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a  
> large amount of data, you are advised to pass data in multiple **update()** calls rather than processing it all
> at once.
> 
For details about the sample code for passing data in multiple **update()** calls, see  
> Encryption and Decryption by Segment with an AES Symmetric Key (GCM Mode).
> 3. RSA or SM2 asymmetric encryption and decryption do not support **update()**.
> 4. If CCM is used in symmetric encryption or decryption, **update()** can be called only once. In the
> encryption process, you can either use **update()** to encrypt data and use **doFinal()** to obtain **authTag**
> or use **doFinal()** without using **update()**. In the decryption process, you can either use **update()** or
> **doFinal()** once to decrypt data and verify the tag.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
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

## updateSync

```TypeScript
updateSync(data: DataBlob): DataBlob
```

Updates the data to encrypt or decrypt by segment.

This API can be called only after the [Cipher](#cipher) instance is initialized by using [initSync()](#initsync).

See **NOTE：**in **update()** for other precautions.

**NOTE：**It is recommended to prioritize the use of asynchronous API, update. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

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

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name of the cipher object.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework
