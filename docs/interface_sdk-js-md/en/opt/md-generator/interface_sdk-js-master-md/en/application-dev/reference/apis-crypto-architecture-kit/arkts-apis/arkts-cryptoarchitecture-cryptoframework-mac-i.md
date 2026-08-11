# Mac

Message authentication code (MAC) interface, defining methods for calculating MACs based on symmetric keys. Before use, you must create a **Mac** instance by using [createMac](arkts-cryptoarchitecture-cryptoframework-createmac-f.md#createmac).

**Since:** 9

<!--Device-cryptoFramework-interface Mac--><!--Device-cryptoFramework-interface Mac-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## doFinal

```TypeScript
doFinal(callback: AsyncCallback<DataBlob>): void
```

Finishes the MAC computation and obtains the MAC computation result. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-doFinal(callback: AsyncCallback<DataBlob>): void--><!--Device-Mac-doFinal(callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

For more HMAC operation examples, see [Generating an HMAC by Passing In Data by Segment](../../security/CryptoArchitectureKit/crypto-compute-hmac.md#generating-an-hmac-by-passing-in-data-by-segment).

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function hmacByCallback() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  symKeyGenerator.convertKey(keyBlob, (err, symKey) => {
    mac.init(symKey, (err) => {
      mac.update({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) }, (err) => {
        mac.doFinal((err, output) => {
          console.info('[Callback]: HMAC result: ' + output.data);
          console.info('[Callback]: MAC len: ' + mac.getMacLength());
        });
      });
    });
  });
}
```

## doFinal

```TypeScript
doFinal(): Promise<DataBlob>
```

Finishes the MAC computation and obtains the MAC computation result. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-doFinal(): Promise<DataBlob>--><!--Device-Mac-doFinal(): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;DataBlob&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

For more HMAC operation examples, see [Generating an HMAC by Passing In Data by Segment](../../security/CryptoArchitectureKit/crypto-compute-hmac.md#generating-an-hmac-by-passing-in-data-by-segment).

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function hmacByPromise() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = await symKeyGenerator.convertKey(keyBlob);
  await mac.init(symKey);
  await mac.update({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) });
  let macOutput = await mac.doFinal();
  console.info('[Promise]: HMAC result: ' + macOutput.data);
  console.info('[Promise]: MAC len: ' + mac.getMacLength());
}
```

## doFinalSync

```TypeScript
doFinalSync(): DataBlob
```

Finishes the MAC computation. This API returns the result synchronously.

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, {@link doFinal}. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-doFinalSync(): DataBlob--><!--Device-Mac-doFinalSync(): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |

## Examples

For more HMAC operation examples, see [Generating an HMAC by Passing In Data by Segment](../../security/CryptoArchitectureKit/crypto-compute-hmac.md#generating-an-hmac-by-passing-in-data-by-segment).

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function hmacBySync() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = symKeyGenerator.convertKeySync(keyBlob);
  mac.initSync(symKey);
  mac.updateSync({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) });
  let macOutput = mac.doFinalSync();
  console.info('[Sync]: HMAC result: ' + macOutput.data);
  console.info('[Sync]: MAC len: ' + mac.getMacLength());
}
```

## getMacLength

```TypeScript
getMacLength(): number
```

Obtains the MAC length, in bytes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-getMacLength(): int--><!--Device-Mac-getMacLength(): int-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testGetMacLength() {
  let mac = cryptoFramework.createMac('SHA256');
  console.info('Mac algName is: ' + mac.algName);
  let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  let keyBlob: cryptoFramework.DataBlob = { data: keyData };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let promiseConvertKey = symKeyGenerator.convertKey(keyBlob);
  promiseConvertKey.then(symKey => {
    let promiseMacInit = mac.init(symKey);
    return promiseMacInit;
  })
    .then(() => {
      let blob: cryptoFramework.DataBlob = { data: new Uint8Array([83]) };
      let promiseMacUpdate = mac.update(blob);
      return promiseMacUpdate;
    })
    .then(() => {
      let promiseMacDoFinal = mac.doFinal();
      return promiseMacDoFinal;
    })
    .then(macOutput => {
      console.info('[Promise]: HMAC result: ' + macOutput.data);
      let macLen = mac.getMacLength();
      console.info('MAC len: ' + macLen);
    })
    .catch((error: BusinessError) => {
      console.error(`[Promise] failed: errCode: ${error.code}, errMsg: ${error.message}`);
    });
}
```

## init

```TypeScript
init(key: SymKey, callback: AsyncCallback<void>): void
```

Initializes the MAC computation using a symmetric key. This API uses an asynchronous callback to return the result. **init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and  
**update** is optional.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-init(key: SymKey, callback: AsyncCallback<void>): void--><!--Device-Mac-init(key: SymKey, callback: AsyncCallback<void>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## init

```TypeScript
init(key: SymKey): Promise<void>
```

Initializes the MAC computation using a symmetric key. This API uses a promise to return the result. **init**,  
**update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-init(key: SymKey): Promise<void>--><!--Device-Mac-init(key: SymKey): Promise<void>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## initSync

```TypeScript
initSync(key: SymKey): void
```

Initializes the MAC computation using a symmetric key. This API returns the result synchronously. **initSync**,  
**updateSync**, and **doFinalSync** must be used together. **initSync** and **doFinalSync** are mandatory, and  
**updateSync** is optional.

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, {@link init}. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-initSync(key: SymKey): void--><!--Device-Mac-initSync(key: SymKey): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## update

```TypeScript
update(input: DataBlob, callback: AsyncCallback<void>): void
```

Updates the MAC status. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about the sample code for calling **update** multiple times in an HMAC operation, see
> [Generating an HMAC by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-compute-hmac.md#generating-an-hmac-by-passing-in-data-by-segment)
> .

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-update(input: DataBlob, callback: AsyncCallback<void>): void--><!--Device-Mac-update(input: DataBlob, callback: AsyncCallback<void>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## update

```TypeScript
update(input: DataBlob): Promise<void>
```

Updates the MAC status. This API uses a promise to return the result.

> **NOTE：**
> 
> For details about the sample code for calling **update** multiple times in an HMAC operation, see
> [Generating an HMAC by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-compute-hmac.md#generating-an-hmac-by-passing-in-data-by-segment)
> .

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-update(input: DataBlob): Promise<void>--><!--Device-Mac-update(input: DataBlob): Promise<void>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## updateSync

```TypeScript
updateSync(input: DataBlob): void
```

Updates the MAC status. This API returns the result synchronously.

> **NOTE：**
> 
> For details about the sample code for calling **updateSync** multiple times in an HMAC operation, see
> [Generating an HMAC by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-compute-hmac.md#generating-an-hmac-by-passing-in-data-by-segment)
> .

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, {@link update}. Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-updateSync(input: DataBlob): void--><!--Device-Mac-updateSync(input: DataBlob): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Mac-readonly algName: string--><!--Device-Mac-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework
