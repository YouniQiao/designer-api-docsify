# Calendar

下列API示例中需先通过 [createCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#createCalendar) 、[getCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#getCalendar)中任一方法获取 Calendar对象，再通过此对象调用对应方法，对该Calendar下的日程进行创建、删除、修改、查询等操作。

**起始版本：** 10

**废弃版本：** -1

<!--Device-calendarManager-export interface Calendar--><!--Device-calendarManager-export interface Calendar-End-->

**系统能力：** SystemCapability.Applications.CalendarData

## addEvent

```TypeScript
addEvent(event: Event): Promise<number>
```

创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** 
- API版本23+：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Calendar-addEvent(event: Event): Promise<number>--><!--Device-Calendar-addEvent(event: Event): Promise<number>-End-->

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
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const date = new Date();
const event: calendarManager.Event = {
  type: calendarManager.EventType.NORMAL,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## addEvent

```TypeScript
addEvent(event: Event, callback: AsyncCallback<number>): void
```

创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** 
- API版本23+：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Calendar-addEvent(event: Event, callback: AsyncCallback<number>): void--><!--Device-Calendar-addEvent(event: Event, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const date = new Date();
const event: calendarManager.Event = {
  type: calendarManager.EventType.NORMAL,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar().then((data: calendarManager.Calendar) => {
  console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
  calendar = data;
  calendar.addEvent(event, (err: BusinessError, data: number): void => {
    if (err) {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }
  });
}).catch((err: BusinessError) => {
  // 检查权限是否已成功申请。
  console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
});
```

## addEvents

```TypeScript
addEvents(events: Event[]): Promise<void>
```

批量创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** 
- API版本23+：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

<!--Device-Calendar-addEvents(events: Event[]): Promise<void>--><!--Device-Calendar-addEvents(events: Event[]): Promise<void>-End-->

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
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const date = new Date();
const events: calendarManager.Event[] = [
  {
    type: calendarManager.EventType.NORMAL,
    startTime: date.getTime(),
    endTime: date.getTime() + 60 * 60 * 1000
  },
  {
    type: calendarManager.EventType.NORMAL,
    startTime: date.getTime(),
    endTime: date.getTime() + 60 * 60 * 1000
  }
];
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.addEvents(events).then(() => {
      console.info('Succeeded in adding events');
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add events. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## addEvents

```TypeScript
addEvents(events: Event[], callback: AsyncCallback<void>): void
```

批量创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** 
- API版本23+：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

<!--Device-Calendar-addEvents(events: Event[], callback: AsyncCallback<void>): void--><!--Device-Calendar-addEvents(events: Event[], callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| events | [Event[]](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const date = new Date();
const events: calendarManager.Event[] = [
  {
    type: calendarManager.EventType.NORMAL,
    startTime: date.getTime(),
    endTime: date.getTime() + 60 * 60 * 1000
  },
  {
    type: calendarManager.EventType.NORMAL,
    startTime: date.getTime(),
    endTime: date.getTime() + 60 * 60 * 1000
  }
];
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.addEvents(events, (err: BusinessError) => {
      if (err) {
        // 检查权限是否已成功申请或者参数是否正确。
        console.error(`Failed to add events. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('Succeeded in adding events');
      }
    });
  }
});
```

## deleteEvent

```TypeScript
deleteEvent(id: number): Promise<void>
```

删除指定id的日程，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-Calendar-deleteEvent(id: number): Promise<void>--><!--Device-Calendar-deleteEvent(id: number): Promise<void>-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
let id: number = 0;
const date = new Date();
const event: calendarManager.Event = {
  type: calendarManager.EventType.NORMAL,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar data->${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id = data;
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.deleteEvent(id).then(() => {
      console.info('Succeeded in deleting event');
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to delete event. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## deleteEvent

```TypeScript
deleteEvent(id: number, callback: AsyncCallback<void>): void
```

删除指定id的日程，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-Calendar-deleteEvent(id: number, callback: AsyncCallback<void>): void--><!--Device-Calendar-deleteEvent(id: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
let id: number = 0;
const date = new Date();
const event: calendarManager.Event = {
  type: calendarManager.EventType.NORMAL,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id = data;
      calendar?.deleteEvent(id, (err: BusinessError) => {
        if (err) {
          // 检查参数是否正确。
          console.error(`Failed to delete event. Code: ${err.code}, message: ${err.message}`);
        } else {
          console.info('Succeeded in deleting event');
        }
      });
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## deleteEvents

```TypeScript
deleteEvents(ids: number[]): Promise<void>
```

根据日程id，批量删除日程，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-Calendar-deleteEvents(ids: number[]): Promise<void>--><!--Device-Calendar-deleteEvents(ids: number[]): Promise<void>-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ids | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
let id1: number = 0;
let id2: number = 0;
const date = new Date();
const event1: calendarManager.Event = {
  type: calendarManager.EventType.NORMAL,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
const event2: calendarManager.Event = {
  type: calendarManager.EventType.IMPORTANT,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event1).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id1 = data;
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    await calendar.addEvent(event2).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id2 = data;
    }).catch((err: BusinessError) => {
      // 检查参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.deleteEvents([id1, id2]).then(() => {
      console.info('Succeeded in deleting events');
    }).catch((err: BusinessError) => {
      // 检查参数是否正确。
      console.error(`Failed to delete events. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## deleteEvents

```TypeScript
deleteEvents(ids: number[], callback: AsyncCallback<void>): void
```

根据日程id，批量删除日程，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-Calendar-deleteEvents(ids: number[], callback: AsyncCallback<void>): void--><!--Device-Calendar-deleteEvents(ids: number[], callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ids | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
let id1: number = 0;
let id2: number = 0;
const date = new Date();
const event1: calendarManager.Event = {
  type: calendarManager.EventType.NORMAL,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
const event2: calendarManager.Event = {
  type: calendarManager.EventType.IMPORTANT,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event1).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id1 = data;
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    await calendar.addEvent(event2).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id2 = data;
    }).catch((err: BusinessError) => {
      // 检查参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.deleteEvents([id1, id2], (err: BusinessError) => {
      if (err) {
        // 检查参数是否正确。
        console.error(`Failed to delete events. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('Succeeded in deleting events');
      }
    });
  }
});
```

## getAccount

```TypeScript
getAccount(): CalendarAccount
```

获取日历账户信息。

**起始版本：** 10

**废弃版本：** -1

<!--Device-Calendar-getAccount(): CalendarAccount--><!--Device-Calendar-getAccount(): CalendarAccount-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**返回值：**

| 类型 |
| --- |
| [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) |

## 示例

```TypeScript
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { BusinessError } from '@kit.BasicServicesKit';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    const account = calendar.getAccount();
    console.info(`succeeded in getting account, account -> ${JSON.stringify(account)}`);
  }
});
```

## getConfig

```TypeScript
getConfig(): CalendarConfig
```

获取日历配置信息。

**起始版本：** 10

**废弃版本：** -1

<!--Device-Calendar-getConfig(): CalendarConfig--><!--Device-Calendar-getConfig(): CalendarConfig-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**返回值：**

| 类型 |
| --- |
| [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) |

## 示例

```TypeScript
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { BusinessError } from '@kit.BasicServicesKit';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    const config = calendar.getConfig();
    console.info(`Succeeded in getting config, config -> ${JSON.stringify(config)}`);
  }
});
```

## getEvents

```TypeScript
getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>
```

获取Calendar下符合查询条件的Event，使用Promise异步回调。只有一个入参时，参数必须为查询条件，对应参数类型为EventFilter。当没有入参时， 可查询指定日历账户下的所有日程。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** 
- API版本23+：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

<!--Device-Calendar-getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>--><!--Device-Calendar-getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>-End-->

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
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const date = new Date();
const event: calendarManager.Event = {
  title: 'MyEvent',
  type: calendarManager.EventType.IMPORTANT,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    // 根据MyEvent进行模糊查询，如果存在类似标题为MyEvent1类型的日程，也可查询出来
    const filter = calendarManager.EventFilter.filterByTitle('MyEvent');
    calendar.getEvents(filter).then((data: calendarManager.Event[]) => {
      console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      // 检查参数是否正确。
      console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## getEvents

```TypeScript
getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>):void
```

获取Calendar下符合查询条件的Event，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** 
- API版本23+：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

<!--Device-Calendar-getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>):void--><!--Device-Calendar-getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>):void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventFilter | [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) | 是 |
| eventKey | (keyof Event)[] | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Event[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
let id1: number = 0;
let id2: number = 0;
const date = new Date();
const event1: calendarManager.Event = {
  type: calendarManager.EventType.NORMAL,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
const event2: calendarManager.Event = {
  type: calendarManager.EventType.IMPORTANT,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event1).then((data: number) => {
      console.info(`Succeeded in adding event, id1 -> ${data}`);
      id1 = data;
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    await calendar.addEvent(event2).then((data: number) => {
      console.info(`Succeeded in adding event, id2 -> ${data}`);
      id2 =data;
    }).catch((err: BusinessError) => {
      // 检查参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    const filter = calendarManager.EventFilter.filterById([id1, id2]);
    calendar.getEvents(filter, ['title', 'type', 'startTime', 'endTime'], (err: BusinessError, data: calendarManager.Event[]) => {
      if (err) {
        // 检查参数是否正确。
        console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
      }
    });
  }
});
```

## getEvents

```TypeScript
getEvents(callback: AsyncCallback<Event[]>):void
```

查询当前日历下所有日程，使用callback异步回调。 API version 20之前，默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime。 从API version 20开始，默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime、identifier。 若查询字段为空，则不返回该字段。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** 
- API版本23+：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

<!--Device-Calendar-getEvents(callback: AsyncCallback<Event[]>):void--><!--Device-Calendar-getEvents(callback: AsyncCallback<Event[]>):void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Event[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.getEvents((err: BusinessError, data: calendarManager.Event[]) => {
      if (err) {
        console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
      }
    });
  }
});
```

## openEventEditPage

```TypeScript
openEventEditPage(id: number): Promise<void>
```

Opens the event edit page.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Calendar-openEventEditPage(id: number): Promise<void>--><!--Device-Calendar-openEventEditPage(id: number): Promise<void>-End-->

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
| [23900005](../errorcode-calendarManager.md#23900005-该日程不支持编辑) |
| [23900001](../errorcode-calendarManager.md#23900001-参数值错误) |

## 示例

```TypeScript
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { BusinessError } from '@kit.BasicServicesKit';
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar: calendarManager.Calendar | undefined = undefined;
const date = new Date();
const event: calendarManager.Event = {
    title: 'MyEvent',
    type: calendarManager.EventType.NORMAL,
    startTime: date.getTime(),
    endTime: date.getTime() + 60 * 60 * 1000
  };
calendarMgr?.getCalendar(async (err: BusinessError, data: calendarManager.Calendar) => {
    if (err) {
      // 检查权限是否已成功申请。
      console.error(`Failed to get calendar, Code is ${err.code}, message is ${err.message}`);
    } else {
      console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
      calendar = data;
      let eventId: number = 0;
      await calendar?.addEvent(event).then((dataId: number) => {
        console.info(`Succeeded in adding event id-> ${dataId}`);
        eventId = dataId;
      }).catch((err: BusinessError) => {
        // 检查权限是否已成功申请或者参数是否正确。
        console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
        return;
      });
      // 根据id进行查询
      const filterId = calendarManager.EventFilter.filterById([eventId]);
      calendar?.getEvents(filterId).then((data: calendarManager.Event[]) => {
        console.info(`Succeeded in getting event: ${JSON.stringify(data)}`);
      }).catch((err: BusinessError) => {
        // 检查参数是否正确或者传入的id是否存在或者权限是否有限制
        console.error(`Failed to get event, Code is ${err.code}, message is ${err.message}`);
        return;
      });
      calendar?.openEventEditPage(eventId).then(() => {
        console.info(`Succeeded in opening EventEditPage`);
      }).catch((err: BusinessError) => {
        // 检查传入的id是否存在或者权限是否有限制或者日程是否支持编辑
        console.error(`Failed to open eventeditpage, Code is ${err.code}, message is ${err.message}`);
      });
    }
 });
```

## queryEventInstances

```TypeScript
queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>
```

获取Calendar下符合查询条件的日程实例，使用Promise异步回调。

**起始版本：** 18

**废弃版本：** -1

**需要权限：** 
- API版本23+：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Calendar-queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>--><!--Device-Calendar-queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>-End-->

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
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { BusinessError } from '@kit.BasicServicesKit';
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const date = new Date();
const event: calendarManager.Event = {
  title: 'MyEvent',
  type: calendarManager.EventType.IMPORTANT,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar?.queryEventInstances(date.getTime(), date.getTime() + 60 * 60 * 1000, undefined,
      ['title', 'startTime', 'endTime', 'instanceStartTime', 'instanceEndTime']).then((data: calendarManager.Event[]) => {
      console.info(`Succeeded in getting event instances, data -> ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      // 检查参数是否正确。
      console.error(`Failed to get event instances. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## setConfig

```TypeScript
setConfig(config: CalendarConfig): Promise<void>
```

设置日历配置信息，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-Calendar-setConfig(config: CalendarConfig): Promise<void>--><!--Device-Calendar-setConfig(config: CalendarConfig): Promise<void>-End-->

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

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const config: calendarManager.CalendarConfig = {
  enableReminder: true,
  color: '#aabbcc'
};
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.setConfig(config).then(() => {
      console.info(`Succeeded in setting config, data->${JSON.stringify(config)}`);
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to set config. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## setConfig

```TypeScript
setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void
```

设置日历配置信息，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-Calendar-setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void--><!--Device-Calendar-setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23900001](../errorcode-calendarManager.md#23900001-参数值错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const config: calendarManager.CalendarConfig = {
  enableReminder: true,
  color: '#aabbcc'
};
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.setConfig(config, (err: BusinessError) => {
      if (err) {
        // 检查权限是否已成功申请或者参数是否正确。
        console.error(`Failed to set config. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info(`Succeeded in setting config, config -> ${JSON.stringify(config)}`);
      }
    });
  }
});
```

## updateEvent

```TypeScript
updateEvent(event: Event): Promise<void>
```

更新日程，入参Event需要填写被修改日程的id，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-Calendar-updateEvent(event: Event): Promise<void>--><!--Device-Calendar-updateEvent(event: Event): Promise<void>-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const date = new Date();
const oriEvent: calendarManager.Event = {
  title: 'update',
  type: calendarManager.EventType.NORMAL,
  description: 'updateEventTest',
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(oriEvent).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      oriEvent.id = data;
      oriEvent.title = 'newUpdate';
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.updateEvent(oriEvent).then(() => {
      console.info(`Succeeded in updating event`);
    }).catch((err: BusinessError) => {
      // 参数是否正确。
      console.error(`Failed to update event. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## updateEvent

```TypeScript
updateEvent(event: Event, callback: AsyncCallback<void>): void
```

更新日程，入参Event需要填写被修改日程的id，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-Calendar-updateEvent(event: Event, callback: AsyncCallback<void>): void--><!--Device-Calendar-updateEvent(event: Event, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const date = new Date();
const oriEvent: calendarManager.Event = {
  title: 'update',
  type: calendarManager.EventType.NORMAL,
  description: 'updateEventTest',
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.getCalendar(async (err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(oriEvent).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      oriEvent.id = data;
      oriEvent.title = 'newUpdate';
    }).catch((err: BusinessError) => {
      // 检查权限是否已成功申请或者参数是否正确。
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.updateEvent(oriEvent, (err: BusinessError) => {
      if (err) {
        // 检查参数是否正确。
        console.error(`Failed to update event. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('Succeeded in updating event');
      }
    });
  }
});
```

## id

```TypeScript
readonly id: number
```

日历账户id，日历账户id是日历账户的唯一标识符，是数据库的自增主键，小于0代表日历账户创建失败，大于0代表日历账户创建成功，没有等于0的情况。

**类型：** number

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Calendar-readonly id: number--><!--Device-Calendar-readonly id: number-End-->

**系统能力：** SystemCapability.Applications.CalendarData
