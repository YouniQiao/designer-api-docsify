# Random

随机数接口，定义随机数生成的方法。调用前，需通过[createRandom](arkts-cryptoarchitecture-cryptoframework-createrandom-f.md#createrandom)创建一个Random实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface Random--><!--Device-cryptoFramework-interface Random-End-->

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

开启硬件熵源。将从TEE中获取安全随机数作为该随机数实例的熵源。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Random-enableHardwareEntropy(): void--><!--Device-Random-enableHardwareEntropy(): void-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Rand

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | 该操作不支持。 |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620002 | 获取Native对象失败或参数转换失败。 |

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

ArkTS-Dyn:
```TypeScript
generateRandom(len: number, callback: AsyncCallback<DataBlob>): void
```

ArkTS-Sta:
```TypeScript
generateRandom(len: int, callback: AsyncCallback<DataBlob>): void
```

生成指定长度的随机数。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-generateRandom(len: int, callback: AsyncCallback<DataBlob>): void--><!--Device-Random-generateRandom(len: int, callback: AsyncCallback<DataBlob>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| len | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示生成随机数的长度，单位为bytes，范围在[1, INT_MAX]。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | Yes | 回调函数。当生成随机数成功时，err为undefined，data为获取到的随机数；否则为 错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |

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

ArkTS-Dyn:
```TypeScript
generateRandom(len: number): Promise<DataBlob>
```

ArkTS-Sta:
```TypeScript
generateRandom(len: int): Promise<DataBlob>
```

生成指定长度的随机数。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-generateRandom(len: int): Promise<DataBlob>--><!--Device-Random-generateRandom(len: int): Promise<DataBlob>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| len | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示生成随机数的长度，单位为bytes，范围在[1, INT_MAX]。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataBlob&gt; | Promise对象，返回生成的随机数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |

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

ArkTS-Dyn:
```TypeScript
generateRandomSync(len: number): DataBlob
```

ArkTS-Sta:
```TypeScript
generateRandomSync(len: int): DataBlob
```

同步生成指定长度的随机数。

&lt;br&gt;&lt;br&gt;**说明：**&lt;br&gt;建议优先使用异步API，{@link generateRandom}。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。因此建议在子线程中调用同步API，以避免阻塞主线程。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 10 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-generateRandomSync(len: int): DataBlob--><!--Device-Random-generateRandomSync(len: int): DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| len | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示生成随机数的长度，单位为bytes，范围在[1, INT_MAX]。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示生成的随机数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |

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

设置指定的种子。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-setSeed(seed: DataBlob): void--><!--Device-Random-setSeed(seed: DataBlob): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| seed | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | 设置的种子。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17620001 | 内存操作失败。 |

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

代表当前使用的随机数生成算法，目前只支持"CTR_DRBG"。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Random-readonly algName: string--><!--Device-Random-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Rand
- API version 10 to 11: SystemCapability.Security.CryptoFramework

