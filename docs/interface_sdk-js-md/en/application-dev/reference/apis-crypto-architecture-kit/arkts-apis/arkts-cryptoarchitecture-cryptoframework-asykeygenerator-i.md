# AsyKeyGenerator

Asymmetric key generator interface, defining methods for generating asymmetric keys. Before use, you must create an **AsyKeyGenerator** instance by using [createAsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-createasykeygenerator-f.md).

**Since:** 9

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## convertKey

```TypeScript
convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void
```

Converts asymmetric key data to a key pair object. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertKey

```TypeScript
convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void
```

Converts data into an asymmetric key pair. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertKey

```TypeScript
convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>
```

Converts asymmetric key data to a key pair object. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertKey

```TypeScript
convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>
```

Converts data into an asymmetric key pair. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertKeySync

```TypeScript
convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair
```

Converts data into an asymmetric key pair. This API returns the result synchronously.

**NOTE：**It is recommended to prioritize the use of asynchronous API, convertKey. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertPemKey

```TypeScript
convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>
```

Converts data into an asymmetric key pair. This API uses a promise to return the result.

> **NOTE：**&gt;
> 1. When **convertPemKey()** is used to convert an external string into an asymmetric key object defined by
> the Crypto framework, the public key must comply with the ASN.1 syntax, X.509 specifications, and PEM
> encoding format, and the private key must comply with the ASN.1 syntax, PKCS #8 specifications, and PEM
> encoding format.
> 2. In **convertPemKey()**, you can pass in either **pubKey** or **priKey**, or both of them. If one of them is
> passed in, the returned **KeyPair** instance contains only the key converted from the data you passed in.
> 3. When **convertPemKey** is used to convert an external string into an asymmetric key object defined by the
> Crypto framework, the system does not verify whether the specifications of the generated key object are the
> same as the key specifications specified for the asymmetric key generator.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertPemKey

```TypeScript
convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>
```

Converts data into an asymmetric key pair. Encrypted private keys are supported. The private key password is synchronously passed to decrypt the private key. This API uses a promise to return the result.

> **NOTE：**&gt;
> 1. When **convertPemKey()** is used to convert an external string into an asymmetric key object defined by
> the Crypto framework, the public key must comply with the ASN.1 syntax, X.509 specifications, and PEM
> encoding format, and the private key must comply with the ASN.1 syntax, PKCS #8 specifications, and PEM
> encoding format.
> 2. In **convertPemKey()**, you can pass in either **pubKey** or **priKey**, or both of them. If one of them is
> passed in, the returned **KeyPair** instance contains only the key converted from the data you passed in.
> 3. When **convertPemKey** is used to convert an external string into an asymmetric key object defined by the
> Crypto framework, the system does not verify whether the specifications of the generated key object are the
> same as the key specifications specified for the asymmetric key generator.
> 4. If **password** is passed in, it can be used to decrypt the encrypted private key.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | Yes |
| password | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## convertPemKeySync

```TypeScript
convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair
```

Converts data into an asymmetric key pair. This API returns the result synchronously.

> **NOTE：**
> The precautions for using **convertPemKeySync** are the same as those for **convertPemKey**. For details, see
> the description of
> [convertPemKey](#convertpemkey)
> .

**NOTE：**It is recommended to prioritize the use of asynchronous API, [convertPemKey](#convertpemkey). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertPemKeySync

```TypeScript
convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair
```

Converts data into an asymmetric key pair. Encrypted private keys are supported. The private key password is synchronously passed to decrypt the private key.

> **NOTE：**
> The precautions for using **convertPemKeySync** are the same as those for
> [convertPemKey](#convertpemkey)
> .

**NOTE：**It is recommended to prioritize the use of asynchronous API, [convertPemKey](#convertpemkey). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | Yes |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | Yes |
| password | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generateKeyPair

```TypeScript
generateKeyPair(callback: AsyncCallback<KeyPair>): void
```

Generates a random key pair using this asymmetric key generator. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generateKeyPair

```TypeScript
generateKeyPair(): Promise<KeyPair>
```

Generates a random key pair using this asymmetric key generator. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generateKeyPairSync

```TypeScript
generateKeyPairSync(): KeyPair
```

Generates a random key pair using this asymmetric key generator. This API returns the result synchronously.

**NOTE：**It is recommended to prioritize the use of asynchronous API, generateKeyPair. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## algName

```TypeScript
readonly algName: string
```

The algName of the AsyKeyGenerator.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework
