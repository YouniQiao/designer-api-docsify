# openResource

## openResource

```TypeScript
function openResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>
```

打开指定资源ID的资源。使用Promise异步回调。

> **说明：**
> 
> 打开的资源必须使用[closeResource](arkts-universalkeystore-huksexternalcrypto-closeresource-f.md#closeresource)关闭。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-huksExternalCrypto-function openResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>--><!--Device-huksExternalCrypto-function openResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>-End-->

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceId | string | 是 |
| params | [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000020](../errorcode-huks.md#12000020-依赖的模块报错) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000025](../errorcode-huks.md#12000025-资源超过限制) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |

## 示例

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

const testResourceId = JSON.stringify({
  providerName: "testProviderName",
  bundleName: "com.example.cryptoapplication",
  abilityName: "CryptoExtension",
  index: {
    key: "testKey"
  } as ESObject
});

huksExternalCrypto.openResource(testResourceId)
    .then(() => {
      console.info('promise: openResource success.');
    });
```
