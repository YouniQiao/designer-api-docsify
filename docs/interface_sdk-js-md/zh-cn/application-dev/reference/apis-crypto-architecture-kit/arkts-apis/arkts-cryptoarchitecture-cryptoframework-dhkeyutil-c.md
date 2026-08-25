# DHKeyUtil

根据素数P的长度和私钥长度（bit位数）生成DH公共密钥参数。

**起始版本：** 11

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## genDHCommonParamsSpec

```TypeScript
static genDHCommonParamsSpec(pLen: number, skLen?: number): DHCommonParamsSpec
```

根据素数P的长度和私钥长度（单位为bit）生成DH公共密钥参数。详见 [DH密钥生成规格](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md#dh)。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pLen | number | 是 |
| skLen | number | 否 |

**返回值：**

| 类型 |
| --- |
| [DHCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-dhcommonparamsspec-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
