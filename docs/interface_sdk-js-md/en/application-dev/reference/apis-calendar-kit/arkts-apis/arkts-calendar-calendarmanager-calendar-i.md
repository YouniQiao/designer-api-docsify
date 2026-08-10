# Calendar

下列API示例中需先通过  
[createCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#createcalendar)、[getCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#getcalendar)中任一方法获取Calendar对象，再通过此对象调用对应方法，对该Calendar下的日程进行创建、删除、修改、查询等操作。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-calendarManager-export interface Calendar--><!--Device-calendarManager-export interface Calendar-End-->

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## addEvent

```TypeScript
addEvent(event: Event): Promise<number>
```

创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** 
- API version 23+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Calendar-addEvent(event: Event): Promise<number>--><!--Device-Calendar-addEvent(event: Event): Promise<number>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes | Event对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回日程的id，id大于0。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900004 | 内部程序错误，可能原因: &lt;br&gt;1. dataShare数据库执行错误； &lt;br&gt;2. 空指针错误； &lt;br&gt;3. 数据解析错误。<br>**Applicable version:** 23 and later |
| 201 | 权限校验失败。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** 
- API version 23+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Calendar-addEvent(event: Event, callback: AsyncCallback<number>): void--><!--Device-Calendar-addEvent(event: Event, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes | Event对象。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 回调函数，当添加日程成功时，err为undefined，data为日程id；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900004 | 内部程序错误，可能原因: &lt;br&gt;1. dataShare数据库执行错误； &lt;br&gt;2. 空指针错误； &lt;br&gt;3. 数据解析错误。<br>**Applicable version:** 23 and later |
| 201 | 权限校验失败。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }
  });
}).catch((err: BusinessError) => {
  // Check whether the permission has been successfully applied for.
  console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
});
```

## addEvents

```TypeScript
addEvents(events: Event[]): Promise<void>
```

批量创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** 
- API version 23+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

<!--Device-Calendar-addEvents(events: Event[]): Promise<void>--><!--Device-Calendar-addEvents(events: Event[]): Promise<void>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| events | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md)[] | Yes | Event对象数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900004 | 内部程序错误，可能原因: &lt;br&gt;1. dataShare数据库执行错误； &lt;br&gt;2. 空指针错误； &lt;br&gt;3. 数据解析错误。<br>**Applicable version:** 23 and later |
| 201 | 权限校验失败。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.addEvents(events).then(() => {
      console.info('Succeeded in adding events');
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
  }
});
```

## addEvents

```TypeScript
addEvents(events: Event[], callback: AsyncCallback<void>): void
```

批量创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** 
- API version 23+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

<!--Device-Calendar-addEvents(events: Event[], callback: AsyncCallback<void>): void--><!--Device-Calendar-addEvents(events: Event[], callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| events | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md)[] | Yes | Event对象数组。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当添加日程成功时，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900004 | 内部程序错误，可能原因: &lt;br&gt;1. dataShare数据库执行错误； &lt;br&gt;2. 空指针错误； &lt;br&gt;3. 数据解析错误。<br>**Applicable version:** 23 and later |
| 201 | 权限校验失败。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.addEvents(events, (err: BusinessError) => {
      if (err) {
        // Check whether the permission is granted or whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-Calendar-deleteEvent(id: number): Promise<void>--><!--Device-Calendar-deleteEvent(id: number): Promise<void>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | 日程id。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar data->${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id = data;
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.deleteEvent(id).then(() => {
      console.info('Succeeded in deleting event');
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Calendar-deleteEvent(id: number, callback: AsyncCallback<void>): void--><!--Device-Calendar-deleteEvent(id: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | 日程id，传入的日程id为整数，表示已创建日程的id，是日程的唯一标识符。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当删除日程成功时，err为undefined；否则为错误对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id = data;
      calendar?.deleteEvent(id, (err: BusinessError) => {
        if (err) {
          // Check whether the parameters are correct.
          console.error(`Failed to delete event. Code: ${err.code}, message: ${err.message}`);
        } else {
          console.info('Succeeded in deleting event');
        }
      });
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-Calendar-deleteEvents(ids: number[]): Promise<void>--><!--Device-Calendar-deleteEvents(ids: number[]): Promise<void>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ids | number[] | Yes | 日程id数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event1).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id1 = data;
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    await calendar.addEvent(event2).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id2 = data;
    }).catch((err: BusinessError) => {
      // Check whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.deleteEvents([id1, id2]).then(() => {
      console.info('Succeeded in deleting events');
    }).catch((err: BusinessError) => {
      // Check whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Calendar-deleteEvents(ids: number[], callback: AsyncCallback<void>): void--><!--Device-Calendar-deleteEvents(ids: number[], callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ids | number[] | Yes | 日程id数组。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当删除多个日程成功时，err为undefined；否则为错误对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event1).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id1 = data;
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    await calendar.addEvent(event2).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      id2 = data;
    }).catch((err: BusinessError) => {
      // Check whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.deleteEvents([id1, id2], (err: BusinessError) => {
      if (err) {
        // Check whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-Calendar-getAccount(): CalendarAccount--><!--Device-Calendar-getAccount(): CalendarAccount-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Return value:**

| Type | Description |
| --- | --- |
| [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | 日历账户信息。 |

## Examples

```TypeScript
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
import { calendarMgr } from '../entryability/EntryAbility';
import { BusinessError } from '@kit.BasicServicesKit';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // Check whether the permission has been successfully applied for.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-Calendar-getConfig(): CalendarConfig--><!--Device-Calendar-getConfig(): CalendarConfig-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Return value:**

| Type | Description |
| --- | --- |
| [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | 日历配置信息。 |

## Examples

```TypeScript
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
import { calendarMgr } from '../entryability/EntryAbility';
import { BusinessError } from '@kit.BasicServicesKit';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // Check whether the permission has been successfully applied for.
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

获取Calendar下符合查询条件的Event，使用Promise异步回调。只有一个入参时，参数必须为查询条件，对应参数类型为EventFilter。当没有入参时，可查询指定日历账户下的所有日程。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** 
- API version 23+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

<!--Device-Calendar-getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>--><!--Device-Calendar-getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventFilter | [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) | No | 查询条件。 |
| eventKey | (keyof Event)[] | No | 查询字段。API version 20之前，不填时默认查询字段包括id、type、title、startTime、endTime、isAllDay、 description、timeZone、location、service、attendee、reminderTime；从API version 20开始，不填时默认查询字段包括id、type、title、startTime、 endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime、identifier。若查询字段为空，则不返回该字段。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Event[]&gt; | Promise对象，返回的是Event对象数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900004 | 内部程序错误，可能原因: &lt;br&gt;1. dataShare数据库执行错误； &lt;br&gt;2. 空指针错误； &lt;br&gt;3. 数据解析错误。<br>**Applicable version:** 23 and later |
| 201 | 权限校验失败。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    // Perform fuzzy query based on MyEvent. If an event of the MyEvent1 type exists, the event can also be queried.
    const filter = calendarManager.EventFilter.filterByTitle('MyEvent');
    calendar.getEvents(filter).then((data: calendarManager.Event[]) => {
      console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      // Check whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** 
- API version 23+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

<!--Device-Calendar-getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>):void--><!--Device-Calendar-getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>):void-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventFilter | [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) | Yes | 查询条件。 |
| eventKey | (keyof Event)[] | Yes | 查询字段。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Event[]&gt; | Yes | 回调函数，当查询日程成功时，err为undefined，data为查询到的Event数组；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900004 | 内部程序错误，可能原因: &lt;br&gt;1. dataShare数据库执行错误； &lt;br&gt;2. 空指针错误； &lt;br&gt;3. 数据解析错误。<br>**Applicable version:** 23 and later |
| 201 | 权限校验失败。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event1).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    await calendar.addEvent(event2).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }).catch((err: BusinessError) => {
      // Check whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    const filter = calendarManager.EventFilter.filterById([id1, id2]);
    calendar.getEvents(filter, ['title', 'type', 'startTime', 'endTime'], (err: BusinessError, data: calendarManager.Event[]) => {
      if (err) {
        // Check whether the parameters are correct.
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

查询当前日历下所有日程，使用callback异步回调。API version 20之前，默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime。从API version 20开始，默认查询字段包括id、type、title、startTime、endTime、isAllDay、description、timeZone、location、service、attendee、reminderTime、identifier。若查询字段为空，则不返回该字段。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** 
- API version 23+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

<!--Device-Calendar-getEvents(callback: AsyncCallback<Event[]>):void--><!--Device-Calendar-getEvents(callback: AsyncCallback<Event[]>):void-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Event[]&gt; | Yes | 回调函数，当查询日程成功时，err为undefined，data为查询到的Event数组；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900004 | 内部程序错误，可能原因: &lt;br&gt;1. dataShare数据库执行错误； &lt;br&gt;2. 空指针错误； &lt;br&gt;3. 数据解析错误。<br>**Applicable version:** 23 and later |
| 201 | 权限校验失败。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // Check whether the permission has been successfully applied for.
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

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Calendar-openEventEditPage(id: number): Promise<void>--><!--Device-Calendar-openEventEditPage(id: number): Promise<void>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | 传入的日程id为整数，表示日历中已存在的日程id，是日程的唯一标识符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900005 | 该日程不支持编辑。 |
| 23900001 | 参数值错误。 |

## Examples

```TypeScript
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
      // Check whether the permission has been successfully applied for.
      console.error(`Failed to get calendar, Code is ${err.code}, message is ${err.message}`);
    } else {
      console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
      calendar = data;
      let eventId: number = 0;
      await calendar?.addEvent(event).then((dataId: number) => {
        console.info(`Succeeded in adding event id-> ${dataId}`);
        eventId = dataId;
      }).catch((err: BusinessError) => {
        // Check whether the permission is granted or whether the parameters are correct.
        console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
        return;
      });
      // Query by ID.
      const filterId = calendarManager.EventFilter.filterById([eventId]);
      calendar?.getEvents(filterId).then((data: calendarManager.Event[]) => {
        console.info(`Succeeded in getting event: ${JSON.stringify(data)}`);
      }).catch((err: BusinessError) => {
        // Check whether the parameters are correct, whether the passed ID exists, or whether there is any restriction on the permission.
        console.error(`Failed to get event, Code is ${err.code}, message is ${err.message}`);
        return;
      });
      calendar?.openEventEditPage(eventId).then(() => {
        console.info(`Succeeded in opening EventEditPage`);
      }).catch((err: BusinessError) => {
        // Check whether the passed ID exists, whether there is any restriction on the permission, or whether the event can be edited.
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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Required permissions:** 
- API version 23+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Calendar-queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>--><!--Device-Calendar-queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes | 日程开始时间，类型为13位时间戳。 |
| end | number | Yes | 日程结束时间，类型为13位时间戳。 |
| ids | number[] | No | 需要查询的日程id数组，可为空数组或undefined。 |
| eventKey | (keyof Event)[] | No | 所有查询日程的字段。不填时，默认查询字段为：id、title、startTime、endTime、instanceStartTime、instanceEndTime、 isAllDay、description、timeZone、location、service。若查询字段为空，则不返回该字段。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Event[]&gt; | Promise对象，返回的是Event对象数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900004 | 内部程序错误，可能原因: &lt;br&gt;1. dataShare数据库执行错误； &lt;br&gt;2. 空指针错误； &lt;br&gt;3. 数据解析错误。<br>**Applicable version:** 23 and later |
| 201 | 权限校验失败。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(event).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar?.queryEventInstances(date.getTime(), date.getTime() + 60 * 60 * 1000, undefined,
      ['title', 'startTime', 'endTime', 'instanceStartTime', 'instanceEndTime']).then((data: calendarManager.Event[]) => {
      console.info(`Succeeded in getting event instances, data -> ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      // Check whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-Calendar-setConfig(config: CalendarConfig): Promise<void>--><!--Device-Calendar-setConfig(config: CalendarConfig): Promise<void>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | Yes | 日历配置信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900001 | 参数值错误。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const config: calendarManager.CalendarConfig = {
  enableReminder: true,
  color: '#aabbcc'
};
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.setConfig(config).then(() => {
      console.info(`Succeeded in setting config, data->${JSON.stringify(config)}`);
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-Calendar-setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void--><!--Device-Calendar-setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | Yes | 日历配置信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当设置Config成功时，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 23900001 | 参数值错误。<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

let calendar : calendarManager.Calendar | undefined = undefined;
const config: calendarManager.CalendarConfig = {
  enableReminder: true,
  color: '#aabbcc'
};
calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    calendar.setConfig(config, (err: BusinessError) => {
      if (err) {
        // Check whether the permission is granted or whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-Calendar-updateEvent(event: Event): Promise<void>--><!--Device-Calendar-updateEvent(event: Event): Promise<void>-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes | Event对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(oriEvent).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      oriEvent.id = data;
      oriEvent.title = 'newUpdate';
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.updateEvent(oriEvent).then(() => {
      console.info(`Succeeded in updating event`);
    }).catch((err: BusinessError) => {
      // Check whether the parameters are correct.
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-Calendar-updateEvent(event: Event, callback: AsyncCallback<void>): void--><!--Device-Calendar-updateEvent(event: Event, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes | Event对象。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当更新日程成功时，err为undefined；否则为错误对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Configure the EntryAbility file based on the sample code in calendarManager.getCalendarManager.
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
    // Check whether the permission has been successfully applied for.
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendar = data;
    await calendar.addEvent(oriEvent).then((data: number) => {
      console.info(`Succeeded in adding event, id -> ${data}`);
      oriEvent.id = data;
      oriEvent.title = 'newUpdate';
    }).catch((err: BusinessError) => {
      // Check whether the permission is granted or whether the parameters are correct.
      console.error(`Failed to add event. Code: ${err.code}, message: ${err.message}`);
    });
    calendar.updateEvent(oriEvent, (err: BusinessError) => {
      if (err) {
        // Check whether the parameters are correct.
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

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Calendar-readonly id: number--><!--Device-Calendar-readonly id: number-End-->

**System capability:** SystemCapability.Applications.CalendarData

