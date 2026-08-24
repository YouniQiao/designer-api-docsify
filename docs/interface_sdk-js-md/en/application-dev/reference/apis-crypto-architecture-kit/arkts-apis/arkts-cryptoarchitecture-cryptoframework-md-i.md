# Md

Message digest interface, defining methods for calculating message digests. Before use, you must create an **Md** instance by using [createMd](arkts-cryptoarchitecture-cryptoframework-createmd-f.md).

**Since:** 23

<!--Device-cryptoFramework-interface Md--><!--Device-cryptoFramework-interface Md-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## digest

```TypeScript
digest(callback: AsyncCallback<DataBlob>): void
```

Generates a message digest. This API uses an asynchronous callback to return the result.

**Since:** 23

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-digest(callback: AsyncCallback<DataBlob>): void--><!--Device-Md-digest(callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the message digest obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function mdByCallback() {
  let md = cryptoFramework.createMd('SHA256');
  md.update({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) }, (err) => {
    md.digest((err, digestOutput) => {
      console.info('[Callback]: MD result: ' + digestOutput.data);
      console.info('[Callback]: MD len: ' + md.getMdLength());
    });
  });
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function mdByPromise() {
  let md = cryptoFramework.createMd('SHA256');
  await md.update({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) });
  let mdOutput = await md.digest();
  console.info('[Promise]: MD result: ' + mdOutput.data);
  console.info('[Promise]: MD len: ' + md.getMdLength());
}
```

## digest

```TypeScript
digest(): Promise<DataBlob>
```

Generates a message digest. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-digest(): Promise<DataBlob>--><!--Device-Md-digest(): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataBlob&gt; | Promise used to return the message digest generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

See [digest](#digest)

## digestSync

```TypeScript
digestSync(): DataBlob
```

Generates a message digest. This API returns the result synchronously.<br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, [digest](#digest). Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Md-digestSync(): DataBlob--><!--Device-Md-digestSync(): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.MessageDigest

**Return value:**

| Type | Description |
| --- | --- |
| DataBlob | Message digest generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function mdBySync() {
  let md = cryptoFramework.createMd('SHA256');
  md.updateSync({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) });
  let mdOutput = md.digestSync();
  console.info('[Sync]: MD result: ' + mdOutput.data);
  console.info('[Sync]: MD len: ' + md.getMdLength());
}
```

## getMdLength

```TypeScript
getMdLength(): int
```

Obtains the message digest length, in bytes.

**Since:** 23

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-getMdLength(): int--><!--Device-Md-getMdLength(): int-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| Type | Description |
| --- | --- |
| int | Message digest length obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function getLength() {
  let md = cryptoFramework.createMd('SHA256');
  console.info('[Promise]: MD len: ' + md.getMdLength());
}
```

## update

```TypeScript
update(input: DataBlob, callback: AsyncCallback<void>): void
```

Updates the message digest status. This API uses an asynchronous callback to return the result. **update** must be used with **digest** together. **digest** is mandatory, and **update** is optional.

> **NOTE：**&gt;
> For details about the code for calling **update** multiple times in a message digest operation, see
> [Generating an MD by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#generating-an-md-by-passing-in-data-by-segment)
> .

**Since:** 23

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-update(input: DataBlob, callback: AsyncCallback<void>): void--><!--Device-Md-update(input: DataBlob, callback: AsyncCallback<void>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | DataBlob | Yes | Data to pass in. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

## update

```TypeScript
update(input: DataBlob): Promise<void>
```

Updates the message digest status. This API uses a promise to return the result. **update** must be used with **digest** together. **digest** is mandatory, and **update** is optional.

> **NOTE：**&gt;
> For details about the code for calling **update** multiple times in a message digest operation, see
> [Generating an MD by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#generating-an-md-by-passing-in-data-by-segment)
> .

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-update(input: DataBlob): Promise<void>--><!--Device-Md-update(input: DataBlob): Promise<void>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | DataBlob | Yes | Data to pass in. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

## updateSync

```TypeScript
updateSync(input: DataBlob): void
```

Updates the message digest status. This API returns the result synchronously. **updateSync** must be used with **digestSync** together. **digestSync** is mandatory, and **updateSync** is optional.

> **NOTE：**&gt;
> For details about the code for calling **updateSync** multiple times in a message digest operation, see
> [Generating an MD by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#generating-an-md-by-passing-in-data-by-segment)
> .
<br><br>**NOTE：**<br>It is recommended to prioritize the use of asynchronous API, update. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Md-updateSync(input: DataBlob): void--><!--Device-Md-updateSync(input: DataBlob): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.MessageDigest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | DataBlob | Yes | Data to pass in. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-readonly algName: string--><!--Device-Md-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

