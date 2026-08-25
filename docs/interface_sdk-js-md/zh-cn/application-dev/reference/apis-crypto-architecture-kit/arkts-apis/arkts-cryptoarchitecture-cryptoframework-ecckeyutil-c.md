# ECCKeyUtil

提供ECC密钥参数生成和基于指定椭圆曲线的点转换工具。

**起始版本：** 11

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## convertPoint

```TypeScript
static convertPoint(curveName: string, encodedPoint: Uint8Array): Point
```

根据椭圆曲线的曲线名，即相应的NID（Name Identifier），将指定的点数据转换为Point对象。当前支持压缩/非压缩格式的点数据。

> **说明：**&gt;
> 根据RFC5480规范中第2.2节的描述：
> 1. 非压缩格式的点数据表示为 **0x04**|x坐标|y坐标。
> 2. **Fp**域（当前不支持**F2m**域）中的压缩点数据表示如下：**0x03**|x坐标（当y坐标为奇数时）；**0x02**|x坐标（当y坐标为偶数时）。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| curveName | string | 是 |
| encodedPoint | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## genECCCommonParamsSpec

```TypeScript
static genECCCommonParamsSpec(curveName: string): ECCCommonParamsSpec
```

根据椭圆曲线相应的NID（Name Identifier）字符串名称生成相应的非对称公共密钥参数。详见 [ECC密钥生成规格](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md#ecc)和 [SM2密钥生成规格](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md#sm2)。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| curveName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [ECCCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |

## getEncodedPoint

```TypeScript
static getEncodedPoint(curveName: string, point: Point, format: string): Uint8Array
```

根据椭圆曲线的曲线名，即相应的NID（Name Identifier），按照指定的点数据格式，将Point对象转换为点数据。当前支持压缩/非压缩格式的点 数据。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| curveName | string | 是 |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | 是 |
| format | string | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
