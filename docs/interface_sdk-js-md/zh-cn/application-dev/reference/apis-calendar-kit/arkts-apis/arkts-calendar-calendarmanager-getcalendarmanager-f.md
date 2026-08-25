# getCalendarManager

## 导入模块

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## getCalendarManager

```TypeScript
function getCalendarManager(context: Context) : CalendarManager
```

根据上下文获取CalendarManager对象，用于管理日历。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CalendarManager](arkts-calendar-calendarmanager-calendarmanager-i.md) |
