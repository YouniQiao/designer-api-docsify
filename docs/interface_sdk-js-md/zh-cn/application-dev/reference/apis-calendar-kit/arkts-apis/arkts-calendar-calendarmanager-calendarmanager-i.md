# CalendarManager

下列API示例中需先通过[getCalendarManager()](arkts-calendar-calendarmanager-getcalendarmanager-f.md)方法获取CalendarManager对象，再通过此对象调用对应方法，进行 Calendar的创建、删除、修改、查询等操作。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

## 导入模块

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## createCalendar

```TypeScript
createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>
```

根据日历账户信息，创建一个Calendar对象，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Calendar & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## createCalendar

```TypeScript
createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void
```

根据日历账户信息，创建一个Calendar对象，若创建的账户已存在（与CalendarAccount的name和type相同的账户已被创建）， 则返回之前的Calendar对象，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## deleteCalendar

```TypeScript
deleteCalendar(calendar: Calendar): Promise<void>
```

删除指定Calendar对象，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendar | [Calendar](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-calendar-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## deleteCalendar

```TypeScript
deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void
```

删除指定Calendar对象，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendar | [Calendar](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-calendar-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## editEvent

```TypeScript
editEvent(event: Event): Promise<number>
```

通过跳转到日程创建页面创建单个日程，入参Event不填日程id，不支持设置instanceStartTime、instanceEndTime、identifier、attendee、service、isLunar和timeZone属性，也不支持添加重要日程。使用Promise异步回调。 使用该接口创建的日程，系统日历可以进行查询和修改，申请到READ_WHOLE_CALENDAR权限的三方应用可以查询，申请到WRITE_WHOLE_CALENDAR权限的三方应用可以修改。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getAllCalendars

```TypeScript
getAllCalendars(): Promise<Calendar[]>
```

获取当前应用所有创建的Calendar对象以及默认Calendar对象，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**返回值：**

| 类型 |
| --- |
| Promise & lt;Calendar[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## getAllCalendars

```TypeScript
getAllCalendars(callback: AsyncCallback<Calendar[]>): void
```

获取当前应用所有创建的Calendar对象以及默认Calendar对象，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## getCalendar

```TypeScript
getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>
```

获取默认Calendar对象或者指定Calendar对象，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Calendar & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900003](../errorcode-calendarManager.md#23900003-未找到指定的账户) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## getCalendar

```TypeScript
getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void
```

获取默认Calendar对象，默认Calendar是日历存储首次运行时创建的，若创建Event时不关注其Calendar归属，则无须通过createCalendar()创建Calendar，直接使用默认Calendar，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900003](../errorcode-calendarManager.md#23900003-未找到指定的账户) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |

## getCalendar

```TypeScript
getCalendar(callback: AsyncCallback<Calendar>): void
```

获取默认Calendar对象，默认Calendar是日历存储首次运行时创建的，若创建Event时不关注其Calendar归属，则无须通过createCalendar()创建Calendar，直接使用默认Calendar，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
