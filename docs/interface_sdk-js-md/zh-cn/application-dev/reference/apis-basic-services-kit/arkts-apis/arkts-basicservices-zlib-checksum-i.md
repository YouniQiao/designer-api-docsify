# Checksum

校验对象。

**起始版本：** 12

**系统能力：** SystemCapability.BundleManager.Zlib

## 导入模块

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## adler32

```TypeScript
adler32(adler: number, buf: ArrayBuffer): Promise<number>
```

计算Adler-32校验和。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [adler](arkts-basicservices-zlib-zstream-i.md) | number | 是 |
| buf | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## adler32Combine

```TypeScript
adler32Combine(adler1: number, adler2: number, len2: number): Promise<number>
```

将两个Adler-32校验和合并。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| adler1 | number | 是 |
| adler2 | number | 是 |
| len2 | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## crc32

```TypeScript
crc32(crc: number, buf: ArrayBuffer): Promise<number>
```

更新CRC-32校验。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| crc | number | 是 |
| buf | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## crc32Combine

```TypeScript
crc32Combine(crc1: number, crc2: number, len2: number): Promise<number>
```

将两个CRC-32校验合并。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| crc1 | number | 是 |
| crc2 | number | 是 |
| len2 | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## crc64

```TypeScript
crc64(crc: number, buf: ArrayBuffer): Promise<number>
```

更新CRC-64校验。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| crc | number | 是 |
| buf | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getCrc64Table

```TypeScript
getCrc64Table(): Promise<Array<number>>
```

输出CRC-64校验表。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

## getCrcTable

```TypeScript
getCrcTable(): Promise<Array<number>>
```

输出CRC-32校验表。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |
