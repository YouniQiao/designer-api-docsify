# Normalizer

提供文本标准化的能力。

**起始版本：** 10

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getInstance

```TypeScript
static getInstance(mode: NormalizerMode): Normalizer
```

获取文本标准化对象。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [NormalizerMode](arkts-localization-i18n-normalizermode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Normalizer](arkts-localization-i18n-normalizer-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## normalize

```TypeScript
normalize(text: string): string
```

对字符串进行标准化处理。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
