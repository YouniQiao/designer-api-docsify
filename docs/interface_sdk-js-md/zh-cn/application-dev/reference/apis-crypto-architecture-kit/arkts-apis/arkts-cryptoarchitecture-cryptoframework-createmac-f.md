# createMac

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createMac

```TypeScript
function createMac(algName: string): Mac
```

创建消息认证码实例。

支持的规格详见[HMAC消息认证码算法规格](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Mac
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| algName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Mac](arkts-cryptoarchitecture-cryptoframework-mac-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |


## createMac

```TypeScript
function createMac(macSpec: MacSpec): Mac
```

创建消息认证码实例。

支持的规格详见[MAC消息认证码算法规格](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md)。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| macSpec | [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Mac](arkts-cryptoarchitecture-cryptoframework-mac-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
