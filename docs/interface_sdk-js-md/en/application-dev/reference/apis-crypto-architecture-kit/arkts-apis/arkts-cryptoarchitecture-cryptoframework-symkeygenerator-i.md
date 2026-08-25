# SymKeyGenerator

Symmetric key generator interface, defining methods for generating symmetric keys. Before use, you must create a **SymKeyGenerator** instance by using [createSymKeyGenerator](arkts-cryptoarchitecture-cryptoframework-createsymkeygenerator-f.md).

**Since:** 9

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## convertKey

```TypeScript
convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void
```

Converts specified data into a symmetric key. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> For symmetric keys used in the HMAC algorithm, if a hash algorithm (for example, **HMAC|SHA256**) is specified
> when the symmetric key generator is created, the binary key data passed in must match the hash length (for
> example, a 256-bit key for SHA256).
If no hash algorithm is specified when the symmetric key generator is created (for example, only **HMAC** is specified), any binary key data with a length of 1 to 4,096 bytes is supported.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertKey

```TypeScript
convertKey(key: DataBlob): Promise<SymKey>
```

Converts specified data into a symmetric key. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## convertKeySync

```TypeScript
convertKeySync(key: DataBlob): SymKey
```

Converts specified data into a symmetric key.

> **NOTE：**&gt;
> For symmetric keys used in the HMAC algorithm, if a hash algorithm (for example, **HMAC|SHA256**) is specified
> when the symmetric key generator is created, the binary key data passed in must match the hash length (for
> example, a 256-bit key for SHA256). If no hash algorithm is specified when the symmetric key generator is
> created (for example, only **HMAC** is specified), any binary key data with a length of 1 to 4,096 bytes is
> supported.

**NOTE：**It is recommended to prioritize the use of asynchronous API, convertKey. Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.SymKey

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |

## generateSymKey

```TypeScript
generateSymKey(callback: AsyncCallback<SymKey>): void
```

Generates a random key using this symmetric key generator. This API uses an asynchronous callback to return the result. OpenSSL RAND_priv_bytes() is currently used to generate random keys.

> **NOTE：**&gt;
> For symmetric keys used in the HMAC algorithm, if a hash algorithm (for example, **HMAC|SHA256**) is specified
> when the symmetric key generator is created, a binary key matching the hash length (for example, a 256-bit key)
> will be randomly generated. If no hash algorithm is specified, for example, only **HMAC** is specified, random
> symmetric key generation is not supported. You can generate symmetric key data using
> [convertKey](#convertkey).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) |

## generateSymKey

```TypeScript
generateSymKey(): Promise<SymKey>
```

Generates a random key using this symmetric key generator. This API uses a promise to return the result. OpenSSL RAND_priv_bytes() is currently used to generate random keys.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) |

## generateSymKeySync

```TypeScript
generateSymKeySync(): SymKey
```

Generates a random key using this symmetric key generator. This API returns the result synchronously. OpenSSL RAND_priv_bytes() is currently used to generate random keys.

> **NOTE：**&gt;
> For symmetric keys used in the HMAC algorithm, if a hash algorithm (for example, **HMAC|SHA256**) is specified
> when the symmetric key generator is created, a binary key matching the hash length (for example, a 256-bit key)
> will be randomly generated.
If no hash algorithm is specified, for example, only **HMAC** is specified, random symmetric key generation is not supported. You can generate symmetric key data using [convertKeySync](#convertkeysync).

**NOTE：**It is recommended to prioritize the use of asynchronous API, [generateSymKey](#generatesymkey). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.CryptoFramework.Key.SymKey

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620004](../errorcode-crypto-framework.md#17620004-invalid-function-call) |

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name of the SymKeyGenerator object.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework
