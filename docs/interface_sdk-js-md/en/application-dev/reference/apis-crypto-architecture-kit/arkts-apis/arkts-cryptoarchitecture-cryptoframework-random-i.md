# Random

Random interface, defining methods for generating random numbers. Before use, you must create a **Random** instance by using [createRandom](arkts-cryptoarchitecture-cryptoframework-createrandom-f.md).

**Since:** 9

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## enableHardwareEntropy

```TypeScript
enableHardwareEntropy(): void
```

Enables the hardware entropy source. Secure random numbers obtained from TEE will be used as the entropy source of this random instance.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.Security.CryptoFramework.Rand

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generateRandom

```TypeScript
generateRandom(len: number, callback: AsyncCallback<DataBlob>): void
```

Generates a random number of the specified length. This API uses an asynchronous callback to return the result.

**Since:** 9

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| len | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generateRandom

```TypeScript
generateRandom(len: number): Promise<DataBlob>
```

Generates a random number of the specified length. This API uses a promise to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| len | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DataBlob & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## generateRandomSync

```TypeScript
generateRandomSync(len: number): DataBlob
```

Generates a random number of the specified length. This API returns the result synchronously.

**NOTE：**It is recommended to prioritize the use of asynchronous API, [generateRandom](#generaterandom). Synchronous API may take a number time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 10

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 10 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| len | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## setSeed

```TypeScript
setSeed(seed: DataBlob): void
```

Sets a seed.

**Since:** 9

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| seed | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## algName

```TypeScript
readonly algName: string
```

Indicates the random generation algorithm name. Currently, only CTR_DRBG is supported.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 10 to 11: SystemCapability.Security.CryptoFramework
