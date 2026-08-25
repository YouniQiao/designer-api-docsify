# Calendar

下列API示例中需先通过 [createCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#createcalendar) 、[getCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#getcalendar)中任一方法获取 Calendar对象，再通过此对象调用对应方法，对该Calendar下的日程进行创建、删除、修改、查询等操作。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

## 导入模块

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## addEvent

```TypeScript
addEvent(event: Event): Promise<number>
```

创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。

**起始版本：** 10

**需要权限：** 
- API版本23+：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## addEvent

```TypeScript
addEvent(event: Event, callback: AsyncCallback<number>): void
```

创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用callback异步回调。

**起始版本：** 10

**需要权限：** 
- API版本23+：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## addEvents

```TypeScript
addEvents(events: Event[]): Promise<void>
```

批量创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。

**起始版本：** 10

**需要权限：** 
- API版本23+：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| events | [Event[]](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## addEvents

```TypeScript
addEvents(events: Event[], callback: AsyncCallback<void>): void
```

批量创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用callback异步回调。

**起始版本：** 10

**需要权限：** 
- API版本23+：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| events | [Event[]](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## deleteEvent

```TypeScript
deleteEvent(id: number): Promise<void>
```

删除指定id的日程，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## deleteEvent

```TypeScript
deleteEvent(id: number, callback: AsyncCallback<void>): void
```

删除指定id的日程，使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## deleteEvents

```TypeScript
deleteEvents(ids: number[]): Promise<void>
```

根据日程id，批量删除日程，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ids | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## deleteEvents

```TypeScript
deleteEvents(ids: number[], callback: AsyncCallback<void>): void
```

根据日程id，批量删除日程，使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ids | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## getAccount

```TypeScript
getAccount(): CalendarAccount
```

获取日历账户信息。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**返回值：**

| 类型 |
| --- |
| [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) |

## getConfig

```TypeScript
getConfig(): CalendarConfig
```

获取日历配置信息。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**返回值：**

| 类型 |
| --- |
| [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) |

## getEvents

```TypeScript
getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>
```

获取Calendar下符合查询条件的Event，使用Promise异步回调。只有一个入参时，参数必须为查询条件，对应参数类型为EventFilter。当没有入参时， 可查询指定日历账户下的所有日程。

**起始版本：** 10

**需要权限：** 
- API版本23+：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventFilter | [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) | 否 |
| eventKey | (keyof Event)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Event[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## getEvents

```TypeScript
getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>):void
```

获取Calendar下符合查询条件的Event，使用callback异步回调。

**起始版本：** 10

**需要权限：** 
- API版本23+：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventFilter | [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) | 是 |
| eventKey | (keyof Event)[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Event[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## getEvents

```TypeScript
getEvents(callback: AsyncCallback<Event[]>):void
```

查询当前日历下所有日程，使用callback异步回调。 API version 20之前，默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime。 从API version 20开始，默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime、identifier。 若查询字段为空，则不返回该字段。

**起始版本：** 10

**需要权限：** 
- API版本23+：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Event[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## openEventEditPage

```TypeScript
openEventEditPage(id: number): Promise<void>
```

Opens the event edit page.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23900001](../errorcode-calendarManager.md#23900001-参数值错误) |
| [23900005](../errorcode-calendarManager.md#23900005-该日程不支持编辑) |

## queryEventInstances

```TypeScript
queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>
```

获取Calendar下符合查询条件的日程实例，使用Promise异步回调。

**起始版本：** 18

**需要权限：** 
- API版本23+：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| end | number | 是 |
| ids | number[] | 否 |
| eventKey | (keyof Event)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Event[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## setConfig

```TypeScript
setConfig(config: CalendarConfig): Promise<void>
```

设置日历配置信息，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23900001](../errorcode-calendarManager.md#23900001-参数值错误) |

## setConfig

```TypeScript
setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void
```

设置日历配置信息，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23900001](../errorcode-calendarManager.md#23900001-参数值错误) |

## updateEvent

```TypeScript
updateEvent(event: Event): Promise<void>
```

更新日程，入参Event需要填写被修改日程的id，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## updateEvent

```TypeScript
updateEvent(event: Event, callback: AsyncCallback<void>): void
```

更新日程，入参Event需要填写被修改日程的id，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## id

```TypeScript
readonly id: number
```

日历账户id，日历账户id是日历账户的唯一标识符，是数据库的自增主键，小于0代表日历账户创建失败，大于0代表日历账户创建成功，没有等于0的情况。

**类型：** number

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData
