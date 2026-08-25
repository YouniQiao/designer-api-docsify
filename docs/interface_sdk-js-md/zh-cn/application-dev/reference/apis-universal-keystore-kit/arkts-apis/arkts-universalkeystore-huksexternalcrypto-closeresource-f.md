# closeResource

## 导入模块

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## closeResource

```TypeScript
function closeResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>
```

关闭指定资源ID的资源。使用Promise异步回调。该接口会回调 [onClearUkeyPinAuthState](../../../reference/apis-universal-keystore-kit/js-apis-CryptoExtensionAbility.md#cryptoextensionabilityonclearukeypinauthstate) 清理该资源关联的PIN认证状态，以及会回调 [onFinishSession](../../../reference/apis-universal-keystore-kit/js-apis-CryptoExtensionAbility.md#cryptoextensionabilityonfinishsession) 清理该资源关联的会话handle。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceId | string | 是 |
| params | [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000020](../errorcode-huks.md#12000020-依赖的模块报错) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |
