# clearUkeyPinAuthState

## clearUkeyPinAuthState

```TypeScript
function clearUkeyPinAuthState(resourceId: string): Promise<void>
```

清除指定资源ID的PIN码认证状态。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-huksExternalCrypto-function clearUkeyPinAuthState(resourceId: string): Promise<void>--><!--Device-huksExternalCrypto-function clearUkeyPinAuthState(resourceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceId | string | 是 |

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
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
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

huksExternalCrypto.clearUkeyPinAuthState(testResourceId)
    .then(() => {
      console.info('promise: clearUkeyPinAuthState success.');
    });
```
