# setProperty

## 导入模块

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## setProperty

```TypeScript
function setProperty(resourceId: string, propertyId: string, params?: HuksExternalCryptoParam[]): Promise<void>
```

The set-type operations of the external crypto extension support calling custom interfaces. However, the custom interface must be registered with the provider.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceId | string | 是 |
| propertyId | string | 是 |
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
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000020](../errorcode-huks.md#12000020-依赖的模块报错) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin码被锁定) |
| [12000023](../errorcode-huks.md#12000023-ukey-pin码未认证) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |
