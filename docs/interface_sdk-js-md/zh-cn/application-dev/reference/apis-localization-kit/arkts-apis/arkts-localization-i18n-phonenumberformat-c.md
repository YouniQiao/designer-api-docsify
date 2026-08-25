# PhoneNumberFormat

提供电话号码相关的能力，包括电话号码有效性判断、格式化和归属地获取。

**起始版本：** 8

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(country: string, options?: PhoneNumberFormatOptions)
```

创建电话号码格式化对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| country | string | 是 |
| options | [PhoneNumberFormatOptions](arkts-localization-i18n-phonenumberformatoptions-i.md) | 否 |

## format

```TypeScript
format(phoneNumber: string): string
```

对电话号码进行格式化。

> **说明：**&gt;
> 从API version 12开始，支持对拨号中的电话号码进行格式化。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## getLocationName

```TypeScript
getLocationName(phoneNumber: string, locale: string): string
```

获取电话号码归属地。

> **说明：**&gt;
> 从API version 23开始，支持对拨号中的电话号码实时获取归属地。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| locale | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## isValidNumber

```TypeScript
isValidNumber(phoneNumber: string): boolean
```

判断电话号码是否为当前电话号码格式化对象中国家的有效号码。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
