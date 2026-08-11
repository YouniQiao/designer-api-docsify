# getUkeyPinAuthState

## getUkeyPinAuthState

```TypeScript
function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>
```

获取PIN码认证状态。使用Promise异步回调。

**起始版本：** 22

<!--Device-huksExternalCrypto-function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>--><!--Device-huksExternalCrypto-function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>-End-->

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceId | string | 是 |
| params | Array&lt;HuksExternalCryptoParam&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;HuksExternalPinAuthState&gt; |

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

const testResourceId = "{\"providerName\":\"testProviderName\", \"bundleName\":\"com.example.cryptoapplication\", \"abilityName\":\"CryptoExtension\",\"index\":{\"key\":\"testKey\"}}";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
huksExternalCrypto.getUkeyPinAuthState(testResourceId, extProperties)
    .then((data) => {
      console.info(`promise: getUkeyPinAuthState success, data: ${data}`);
    });
```
