# Random

Random interface, defining methods for generating random numbers. Before use, you must create a **Random** instance by using [createRandom](arkts-cryptoarchitecture-cryptoframework-createrandom-f.md#createRandom).

**Since:** 23

**Deprecated since:** -1

<!--Device-cryptoFramework-interface Random--><!--Device-cryptoFramework-interface Random-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## enableHardwareEntropy

```TypeScript
enableHardwareEntropy(): void
```

Enables the hardware entropy source. Secure random numbers obtained from TEE will be used as the entropy source of this random instance.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Random-enableHardwareEntropy(): void--><!--Device-Random-enableHardwareEntropy(): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Rand

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
rand.enableHardwareEntropy();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error(`[Callback] generate random failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('[Callback]: generate random result: ' + randData.data);
    try {
      rand.setSeed(randData);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

## generateRandom

```TypeScript
generateRandom(len: number, callback: AsyncCallback<DataBlob>): void
```

Generates a random number of the specified length. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-generateRandom(len: int, callback: AsyncCallback<DataBlob>): void--><!--Device-Random-generateRandom(len: int, callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| len | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let rand = cryptoFramework.createRandom();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error(`[Callback] generate random failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('[Callback]: generate random result: ' + randData.data);
  }
});
```

## generateRandom

```TypeScript
generateRandom(len: number): Promise<DataBlob>
```

Generates a random number of the specified length. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-generateRandom(len: int): Promise<DataBlob>--><!--Device-Random-generateRandom(len: int): Promise<DataBlob>-End-->

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
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

ArkTS example:

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
let promiseGenerateRand = rand.generateRandom(12);
promiseGenerateRand.then(randData => {
  console.info('[Promise]: rand result: ' + randData.data);
}).catch((error: BusinessError) => {
  console.error(`[Promise] failed: errCode: ${error.code}, errMsg: ${error.message}`);
});
```

JS example:

```TypeScript
<div class="container">
    <text class="TestTitle">Crypto test</text>
    <input class="btn" @click="RandTest">Rand asynchronous test</input>
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

function randTest() {
    let rand = cryptoFramework.createRandom();
    let seed = new Uint8Array([1, 2, 3]);
    rand.setSeed({ data : seed });

    rand.generateRandom(12, function (finishErr, randData){
        if (finishErr) {
            console.error("GenerateRandom failed. Code:" + finishErr.code + " : " + finishErr.message);
        } else {
            console.info("GenerateRandom successfully:" + randData);
        }
    })
}

export default {
    data: {
        result: ''
    },
    RandTest() {
        randTest();
    }
};
```

## generateRandomSync

```TypeScript
generateRandomSync(len: number): DataBlob
```

Generates a random number of the specified length. This API returns the result synchronously. &lt;br&gt;&lt;br&gt;**NOTE：**&lt;br&gt;It is recommended to prioritize the use of asynchronous API, [generateRandom](#generateRandom). Synchronous API may take a long time and block the main thread due to system busyness, high load, and other reasons. Therefore, it is advised to invoke synchronous API within a child thread to avoid blocking the main thread.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 10 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-generateRandomSync(len: int): DataBlob--><!--Device-Random-generateRandomSync(len: int): DataBlob-End-->

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
| [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

ArkTS example:

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
try {
  let randData = rand.generateRandomSync(12);
  if (randData != null) {
    console.info('[Sync]: rand result: ' + randData.data);
  } else {
    console.error('[Sync]: get rand result: fail.');
  }
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

JS example:

```TypeScript
<div class="container">
    <text class="TestTitle">Crypto test</text>
    <input class="btn" @click="RandTestSync">Rand synchronous test</input>
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

function randTestSync() {
    let rand = cryptoFramework.createRandom();
    let randLen = 24;
    try {
        let randData = rand.generateRandomSync(randLen);
        if (randData != null) {
            console.info("GenerateRandom successfully: " + randData.data);
        } else {
            console.error("GenerateRandom failed!");
        }
    } catch (error) {
        console.error(`GenerateRandom random number failed. Code: ${error.code}, message: ${error.message}`);
    }
}

export default {
    data: {
        result: ''
    },
    RandTestSync() {
        randTestSync();
    }
};
```

## setSeed

```TypeScript
setSeed(seed: DataBlob): void
```

Sets a seed.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-setSeed(seed: DataBlob): void--><!--Device-Random-setSeed(seed: DataBlob): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| seed | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error(`[Callback] generate random failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('[Callback]: generate random result: ' + randData.data);
    try {
      rand.setSeed(randData);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

## algName

```TypeScript
readonly algName: string
```

Indicates the random generation algorithm name. Currently, only CTR_DRBG is supported.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-readonly algName: string--><!--Device-Random-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 10 to 11: SystemCapability.Security.CryptoFramework
