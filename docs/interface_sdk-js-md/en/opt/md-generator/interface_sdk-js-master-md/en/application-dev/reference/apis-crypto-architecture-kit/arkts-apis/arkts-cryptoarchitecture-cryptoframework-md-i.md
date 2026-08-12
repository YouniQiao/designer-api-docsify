# Md

Message digest interface, defining methods for calculating message digests. Before use, you must create an **Md**instance by using [createMd](arkts-cryptoarchitecture-cryptoframework-createmd-f.md#createMd).

**Since:** 9

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

**Since:** 9

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-digest(callback: AsyncCallback<DataBlob>): void--><!--Device-Md-digest(callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

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

## digest

```TypeScript
digest(): Promise<DataBlob>
```

Generates a message digest. This API uses a promise to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-digest(): Promise<DataBlob>--><!--Device-Md-digest(): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DataBlob & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

ArkTS example:

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

JS example:

```TypeScript
<div class="container">
    <text class="TestTitle">Crypto test</text>
    <input class="btn" @click="MdTest">Md asynchronous test</input>
</div>
```

```TypeScript
.container {
  width: 100%;
  height: 2000px;
  align-items: center;
  background-color: #fffefcfc;
  flex-direction: column;
  display: flex;
}

.TestTitle {
  width: 300px;
  height: 80px;
  text-align: center;
  background-color: white;
  color: #fff61515;
  font-size: 15fp;
}

.btn {
  width: 90%;
  height: 80px;
  text-align: center;
  background-color: #fff17f04;
  margin-top: 3px;
  color: white;
  font-size: 20fp;
}
```

```TypeScript
import cryptoFramework from '@ohos.security.cryptoFramework';

function StringToUint8Array(str) {
    let arr = [];
    for (let i = 0, j = str.length; i < j; ++i) {
        arr.push(str.charCodeAt(i));
    }
    return new Uint8Array(arr);
}

let plainText = "123456";

function mdTest() {
    let inData = StringToUint8Array(plainText);
    let md = cryptoFramework.createMd('SHA256');
    console.info("createMd " + typeof md);

    md.update({data: inData}, function (finishErr) {
        if (finishErr) {
            console.error("Digest update failed. Code:" + finishErr.code + " : " + finishErr.message);
        } else {
            console.info("Digest update successfully.");
        }
    })

    md.digest(function (finishErr, digestOutput){
        if (finishErr) {
            console.error("Digest failed. Code:" + finishErr.code + " : " + finishErr.message);
        } else {
            console.info("Digest successfully:" + digestOutput);
        }
    })
}

export default {
    data: {
        result: ''
    },
    MdTest() {
        mdTest();
    }
};
```

## digestSync

```TypeScript
digestSync(): DataBlob
```

Generates a message digest. This API returns the result synchronously.

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, [digest](#digest). Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-digestSync(): DataBlob--><!--Device-Md-digestSync(): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.MessageDigest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |

## Examples

ArkTS example:

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function mdBySync() {
  let md = cryptoFramework.createMd('SHA256');
  md.updateSync({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) });
  let mdOutput = md.digestSync();
  console.info('[Sync]: MD result: ' + mdOutput.data);
  console.info('[Sync]: MD len: ' + md.getMdLength());
}
```

JS example:

```TypeScript
<div class="container">
    <text class="TestTitle">Crypto test</text>
    <input class="btn" @click="MdTestSync">Md synchronous test</input>
</div>
```

```TypeScript
.container {
  width: 100%;
  height: 2000px;
  align-items: center;
  background-color: #fffefcfc;
  flex-direction: column;
  display: flex;
}

.TestTitle {
  width: 300px;
  height: 80px;
  text-align: center;
  background-color: white;
  color: #fff61515;
  font-size: 15fp;
}

.btn {
  width: 90%;
  height: 80px;
  text-align: center;
  background-color: #fff17f04;
  margin-top: 3px;
  color: white;
  font-size: 20fp;
}
```

```TypeScript
import cryptoFramework from '@ohos.security.cryptoFramework';

function StringToUint8Array(str) {
    let arr = [];
    for (let i = 0, j = str.length; i < j; ++i) {
        arr.push(str.charCodeAt(i));
    }
    return new Uint8Array(arr);
}

function mdTestSync() {
    let mdAlgName = 'SHA256';
    let message = 'mdTestMessage';
    let md = cryptoFramework.createMd(mdAlgName);
    md.updateSync({ data: StringToUint8Array(message) });
    let mdResult = md.digestSync();
    console.info('Digest successfully. result:' + mdResult.data);
    let mdLen = md.getMdLength();
    console.info("Digest successfully. md len: " + mdLen);
}

export default {
    data: {
        result: ''
    },
    MdTestSync() {
        mdTestSync();
    }
};
```

## getMdLength

```TypeScript
getMdLength(): number
```

Obtains the message digest length, in bytes.

**Since:** 9

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-getMdLength(): int--><!--Device-Md-getMdLength(): int-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## Examples

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

> **NOTE：**
> 
> For details about the code for calling **update** multiple times in a message digest operation, see
> [Generating an MD by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#generating-an-md-by-passing-in-data-by-segment)
> .

**Since:** 9

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-update(input: DataBlob, callback: AsyncCallback<void>): void--><!--Device-Md-update(input: DataBlob, callback: AsyncCallback<void>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## update

```TypeScript
update(input: DataBlob): Promise<void>
```

Updates the message digest status. This API uses a promise to return the result. **update** must be used with  
**digest** together. **digest** is mandatory, and **update** is optional.

> **NOTE：**
> 
> For details about the code for calling **update** multiple times in a message digest operation, see
> [Generating an MD by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#generating-an-md-by-passing-in-data-by-segment)
> .

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-update(input: DataBlob): Promise<void>--><!--Device-Md-update(input: DataBlob): Promise<void>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## updateSync

```TypeScript
updateSync(input: DataBlob): void
```

Updates the message digest status. This API returns the result synchronously. **updateSync** must be used with  
**digestSync** together. **digestSync** is mandatory, and **updateSync** is optional.

> **NOTE：**
> 
> For details about the code for calling **updateSync** multiple times in a message digest operation, see
> [Generating an MD by Passing In Data by Segment](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#generating-an-md-by-passing-in-data-by-segment)
> .

&lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, [update](update). Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore,it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-updateSync(input: DataBlob): void--><!--Device-Md-updateSync(input: DataBlob): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.MessageDigest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## algName

```TypeScript
readonly algName: string
```

Indicates the algorithm name.

**Type:** string

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Md-readonly algName: string--><!--Device-Md-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.MessageDigest
- API version 9 to 11: SystemCapability.Security.CryptoFramework
