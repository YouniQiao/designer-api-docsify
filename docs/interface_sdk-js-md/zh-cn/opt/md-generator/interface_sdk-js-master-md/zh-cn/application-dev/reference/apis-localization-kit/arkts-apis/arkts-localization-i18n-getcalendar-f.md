# getCalendar

## 导入模块

```TypeScript
```

## getCalendar

```TypeScript
export function getCalendar(locale: string, type?: string): Calendar
```

获取指定区域和历法的日历对象。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-i18n-export function getCalendar(locale: string, type?: string): Calendar--><!--Device-i18n-export function getCalendar(locale: string, type?: string): Calendar-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string | 是 |
| type | string | 否 |

**返回值：**

| 类型 |
| --- |
| [Calendar](../../apis-na/arkts-apis/arkts-na-i18n-calendar-c.md) |

**示例**

```TypeScript
let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans', 'chinese'); // 获取中国农历日历对象
```
