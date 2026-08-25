# createVerify

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createVerify

```TypeScript
function createVerify(algName: string): Verify
```

创建验签实例。

支持的规格详见[签名验签规格](../../../security/CryptoArchitectureKit/crypto-sign-sig-verify-overview.md)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| algName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Verify](arkts-cryptoarchitecture-cryptoframework-verify-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
