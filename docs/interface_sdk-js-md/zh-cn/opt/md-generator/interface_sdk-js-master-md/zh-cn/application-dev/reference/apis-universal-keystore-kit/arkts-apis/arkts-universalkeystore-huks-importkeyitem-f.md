# importKeyItem

## importKeyItem

```TypeScript
function importKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void
```

Imports a key in plaintext. This API uses an asynchronous callback to return the result.

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function importKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void--><!--Device-huks-function importKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.Huks.Core
- API版本9-11：SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000015](../errorcode-huks.md#12000015-调用其他系统服务失败) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000013](../errorcode-huks.md#12000013-密钥设置生物访问控制时待绑定的凭据不存在) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |

## 示例

```TypeScript
/* 以导入AES密钥为例 */
import { huks } from '@kit.UniversalKeystoreKit';

let plainTextSize32 = makeRandomArr(32);

function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value:
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let options: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
/* 导入密钥 */
huks.importKeyItem(keyAlias, options, (error) => {
  if (error) {
    console.error(`callback: importKeyItem failed`);
  } else {
    console.info(`callback: importKeyItem success`);
  }
});
```


## importKeyItem

```TypeScript
function importKeyItem(keyAlias: string, options: HuksOptions): Promise<void>
```

Imports a key in plaintext. This API uses a promise to return the result.

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function importKeyItem(keyAlias: string, options: HuksOptions): Promise<void>--><!--Device-huks-function importKeyItem(keyAlias: string, options: HuksOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000015](../errorcode-huks.md#12000015-调用其他系统服务失败) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000013](../errorcode-huks.md#12000013-密钥设置生物访问控制时待绑定的凭据不存在) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |

## 示例

```TypeScript
/* 以导入AES密钥为例 */
import { huks } from '@kit.UniversalKeystoreKit';

function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};

let plainTextSize32 = makeRandomArr(32);
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
/* 导入密钥 */
huks.importKeyItem(keyAlias, huksOptions)
  .then(() => {
    console.info(`promise: importKeyItem success`);
  });
```
