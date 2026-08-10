# Checksum

校验对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-interface Checksum--><!--Device-zlib-interface Checksum-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## adler32

ArkTS-Dyn:
```TypeScript
adler32(adler: number, buf: ArrayBuffer): Promise<number>
```

ArkTS-Sta:
```TypeScript
adler32(adler: long, buf: ArrayBuffer): Promise<long>
```

计算Adler-32校验和。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Checksum-adler32(adler: long, buf: ArrayBuffer): Promise<long>--><!--Device-Checksum-adler32(adler: long, buf: ArrayBuffer): Promise<long>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adler | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Adler-32校验和的初始值。 |
| buf | ArrayBuffer | Yes | 计算校验和数据缓冲区。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回计算后的Adler-32校验和。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { zlib } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data[i] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.adler32(0, arrayBufferIn).then(data => {
  console.info('adler32 success', data);
})
```

## adler32Combine

ArkTS-Dyn:
```TypeScript
adler32Combine(adler1: number, adler2: number, len2: number): Promise<number>
```

ArkTS-Sta:
```TypeScript
adler32Combine(adler1: long, adler2: long, len2: long): Promise<long>
```

将两个Adler-32校验和合并。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Checksum-adler32Combine(adler1: long, adler2: long, len2: long): Promise<long>--><!--Device-Checksum-adler32Combine(adler1: long, adler2: long, len2: long): Promise<long>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adler1 | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 第一个要合并的Adler-32校验和。 |
| adler2 | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 第二个要合并的Adler-32校验和。 |
| len2 | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 第二个Adler-32校验和的数据块的长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回合并后的Adler-32校验和。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(12);
  let data = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    data[i] = str.charCodeAt(i);
  }
  let checksum = zlib.createChecksumSync()
  let adler1 = 0;
  let adler2 = 1;
  await checksum.adler32(0, arrayBufferIn).then(data => {
    console.info('adler32 success', data);
    adler1 = data;
  })
  await checksum.adler32(1, arrayBufferIn).then(data => {
    console.info('adler32 success', data);
    adler2 = data;
  })
  await checksum.adler32Combine(adler1, adler2, 12).then((data) => {
    console.info('adler32Combine success', data);
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

## crc32

ArkTS-Dyn:
```TypeScript
crc32(crc: number, buf: ArrayBuffer): Promise<number>
```

ArkTS-Sta:
```TypeScript
crc32(crc: long, buf: ArrayBuffer): Promise<long>
```

更新CRC-32校验。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Checksum-crc32(crc: long, buf: ArrayBuffer): Promise<long>--><!--Device-Checksum-crc32(crc: long, buf: ArrayBuffer): Promise<long>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| crc | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | CRC-32校验的初始值。 |
| buf | ArrayBuffer | Yes | 计算校验数据缓冲区。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回更新后的CRC-32校验。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data[i] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.crc32(0, arrayBufferIn).then((data) => {
  console.info('crc32 success', data);
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

## crc32Combine

ArkTS-Dyn:
```TypeScript
crc32Combine(crc1: number, crc2: number, len2: number): Promise<number>
```

ArkTS-Sta:
```TypeScript
crc32Combine(crc1: long, crc2: long, len2: long): Promise<long>
```

将两个CRC-32校验合并。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Checksum-crc32Combine(crc1: long, crc2: long, len2: long): Promise<long>--><!--Device-Checksum-crc32Combine(crc1: long, crc2: long, len2: long): Promise<long>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| crc1 | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 第一个要合并的CRC-32校验。 |
| crc2 | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 第二个要合并的CRC-32校验。 |
| len2 | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 第二个CRC-32校验的数据块的长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回合并后的CRC-32校验。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(12);
  let data = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    data[i] = str.charCodeAt(i);
  }
  let checksum = zlib.createChecksumSync()
  let crc1 = 0;
  let crc2 = 1;
  await checksum.crc32(0, arrayBufferIn).then(data => {
    console.info('crc32 success', data);
    crc1 = data;
  })
  await checksum.crc32(1, arrayBufferIn).then(data => {
    console.info('crc32 success', data);
    crc2 = data;
  })
  await checksum.crc32Combine(crc1, crc2, 12).then((data) => {
    console.info('crc32Combine success', data);
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
}
```

## crc64

ArkTS-Dyn:
```TypeScript
crc64(crc: number, buf: ArrayBuffer): Promise<number>
```

ArkTS-Sta:
```TypeScript
crc64(crc: long, buf: ArrayBuffer): Promise<long>
```

更新CRC-64校验。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Checksum-crc64(crc: long, buf: ArrayBuffer): Promise<long>--><!--Device-Checksum-crc64(crc: long, buf: ArrayBuffer): Promise<long>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| crc | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | CRC-64校验的初始值。 |
| buf | ArrayBuffer | Yes | 计算校验数据缓冲区。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回更新后的CRC-64校验。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data[i] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.crc64(0, arrayBufferIn).then((data) => {
  console.info('crc64 success', data);
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

## getCrc64Table

ArkTS-Dyn:
```TypeScript
getCrc64Table(): Promise<Array<number>>
```

ArkTS-Sta:
```TypeScript
getCrc64Table(): Promise<Array<long>>
```

输出CRC-64校验表。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Checksum-getCrc64Table(): Promise<Array<long>>--><!--Device-Checksum-getCrc64Table(): Promise<Array<long>>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;long&gt;&gt; | Promise对象。返回CRC-64校验表。 |

## Examples

```TypeScript
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()

checksum.getCrc64Table().then((data) => {
  console.info('getCrc64Table success');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

## getCrcTable

ArkTS-Dyn:
```TypeScript
getCrcTable(): Promise<Array<number>>
```

ArkTS-Sta:
```TypeScript
getCrcTable(): Promise<Array<long>>
```

输出CRC-32校验表。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Checksum-getCrcTable(): Promise<Array<long>>--><!--Device-Checksum-getCrcTable(): Promise<Array<long>>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;long&gt;&gt; | Promise对象。返回CRC-32校验表。 |

## Examples

```TypeScript
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()

checksum.getCrcTable().then((data) => {
  console.info('getCrcTable success');
}).catch((errData: BusinessError) => {
  console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
})
```

