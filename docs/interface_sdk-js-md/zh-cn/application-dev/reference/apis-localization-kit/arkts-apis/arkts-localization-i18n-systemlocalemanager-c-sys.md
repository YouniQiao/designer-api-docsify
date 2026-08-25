# SystemLocaleManager（系统接口）

提供语言、地区和时区信息排序的能力。

**起始版本：** 10

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建SystemLocaleManager对象。

**起始版本：** 10

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getLanguageInfoArray

```TypeScript
getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>
```

获取排序后的语言信息列表。

**起始版本：** 10

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [languages](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontdescriptor-i.md) | Array & lt;string & gt; | 是 |
| options | [SortOptions](arkts-localization-i18n-sortoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[LocaleItem](arkts-localization-i18n-localeitem-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getRegionInfoArray

```TypeScript
getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>
```

获取排序后的国家或地区信息列表。

**起始版本：** 10

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| regions | Array & lt;string & gt; | 是 |
| options | [SortOptions](arkts-localization-i18n-sortoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[LocaleItem](arkts-localization-i18n-localeitem-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getTimeZoneCityItemArray

```TypeScript
static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>
```

获取排序后的时区城市组合信息列表。

**起始版本：** 10

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;[TimeZoneCityItem](arkts-localization-i18n-timezonecityitem-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
