# getProperty

## 导入模块

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## getProperty

```TypeScript
function getProperty(resourceId: string, propertyId: string, params?: Array<HuksExternalCryptoParam>): Promise<Array<HuksExternalCryptoParam>>
```

调用此接口获取属性值并返回结果。使用Promise异步回调。propertyId表示查询属性的ID信息，当前仅支持GMT 0016-2023中定义的SKF接口名作为属性ID，支持的ID包括如下：  
- SKF_EnumDev  
- SKF_GetDevInfo  
- SKF_EnumApplication  
- SKF_EnumContainer

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceId | string | 是 |
| propertyId | string | 是 |
| params | Array&lt;[HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)&gt;&gt; |

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
