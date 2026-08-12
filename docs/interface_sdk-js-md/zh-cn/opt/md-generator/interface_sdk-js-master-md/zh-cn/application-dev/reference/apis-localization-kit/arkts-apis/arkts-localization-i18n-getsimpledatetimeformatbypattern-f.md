# getSimpleDateTimeFormatByPattern

## getSimpleDateTimeFormatByPattern

```TypeScript
export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat
```

通过模式字符串获取SimpleDateTimeFormat对象。与[getSimpleDateTimeFormatBySkeleton](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md#getSimpleDateTimeFormatBySkeleton)接口获取的对象在格式化后显示差异请参考[SimpleDateTimeFormat.format](arkts-localization-i18n-simpledatetimeformat-c.md#format)的示例。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | string | 是 |
| locale | Intl.Locale | 否 |

**返回值：**

| 类型 |
| --- |
| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-localization-kit/errorcode-i18n.md#8900001-参数校验错误) |


## getSimpleDateTimeFormatByPattern

```TypeScript
export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat
```

通过模式字符串获取SimpleDateTimeFormat对象。与[getSimpleDateTimeFormatBySkeleton](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md#getSimpleDateTimeFormatBySkeleton)接口获取的对象在格式化后显示差异请参考[SimpleDateTimeFormat.format](arkts-localization-i18n-simpledatetimeformat-c.md#format)的示例。

**起始版本：** 18

**废弃版本：** 20

**替代接口：** [getSimpleDateTimeFormatByPattern](i18n.getSimpleDateTimeFormatByPattern(pattern:)

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | string | 是 |
| locale | intl.Locale | 否 |

**返回值：**

| 类型 |
| --- |
| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [890001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-localization-kit/errorcode-i18n.md#890001-参数校验错误) |
