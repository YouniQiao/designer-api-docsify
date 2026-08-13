# CalendarManager

下列API示例中需先通过[getCalendarManager()](arkts-calendar-calendarmanager-getcalendarmanager-f.md#getCalendarManager)方法获取CalendarManager对象，再通过此对象调用对应方法，进行 Calendar的创建、删除、修改、查询等操作。

**起始版本：** 10

**废弃版本：** -1

<!--Device-calendarManager-export interface CalendarManager--><!--Device-calendarManager-export interface CalendarManager-End-->

**系统能力：** SystemCapability.Applications.CalendarData

## createCalendar

```TypeScript
createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>
```

根据日历账户信息，创建一个Calendar对象，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

<!--Device-CalendarManager-createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>--><!--Device-CalendarManager-createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>-End-->

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

const calendarAccount: calendarManager.CalendarAccount = {
  name: 'CreateMyCalendarByPromise',
  type: calendarManager.CalendarType.LOCAL,
  displayName : 'MyApplication'
};
calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
  console.info(`Succeeded in creating calendar data->${JSON.stringify(data)}`);
}).catch((error : BusinessError) => {
  // 检查权限是否已成功申请或者参数是否正确。
  console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
});
```

## createCalendar

```TypeScript
createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void
```

根据日历账户信息，创建一个Calendar对象，若创建的账户已存在（与CalendarAccount的name和type相同的账户已被创建）， 则返回之前的Calendar对象，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

<!--Device-CalendarManager-createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void--><!--Device-CalendarManager-createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

const calendarAccount: calendarManager.CalendarAccount = {
  name: 'CreateMyCalendarByCallBack',
  type: calendarManager.CalendarType.LOCAL
};
try {
  calendarMgr?.createCalendar(calendarAccount, (err: BusinessError, data: calendarManager.Calendar) => {
    if (err) {
      console.error(`Failed to create calendar. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
    }
  });
} catch (error) {
  // 检查权限是否已成功申请或者参数是否正确。
  console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
}
```

## deleteCalendar

```TypeScript
deleteCalendar(calendar: Calendar): Promise<void>
```

删除指定Calendar对象，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

<!--Device-CalendarManager-deleteCalendar(calendar: Calendar): Promise<void>--><!--Device-CalendarManager-deleteCalendar(calendar: Calendar): Promise<void>-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendar | [Calendar](../../apis-na/arkts-apis/arkts-na-i18n-calendar-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

const calendarAccount: calendarManager.CalendarAccount = {
  name: 'DeleteMyCalendarByPromise',
  type: calendarManager.CalendarType.LOCAL
};
calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
  console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
  calendarMgr?.getCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
    calendarMgr?.deleteCalendar(data).then(() => {
      console.info('Succeeded in deleting calendar');
    }).catch((err: BusinessError) => {
      // 检查参数是否正确。
      console.error(`Failed to delete calendar. Code: ${err.code}, message: ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    // 检查权限是否已成功申请或者参数是否正确。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((error: BusinessError) => {
  // 检查权限是否已成功申请或者参数是否正确。
  console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
})
```

## deleteCalendar

```TypeScript
deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void
```

删除指定Calendar对象，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR

<!--Device-CalendarManager-deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void--><!--Device-CalendarManager-deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendar | [Calendar](../../apis-na/arkts-apis/arkts-na-i18n-calendar-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

const calendarAccount: calendarManager.CalendarAccount = {
  name: 'DeleteMyCalendarByCallBack',
  type: calendarManager.CalendarType.LOCAL
};
calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
  console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
  calendarMgr?.getCalendar(calendarAccount, (err: BusinessError, data: calendarManager.Calendar) => {
    if (err) {
      console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
      calendarMgr?.deleteCalendar(data, (err1: BusinessError) => {
        if (err1) {
          // 检查参数是否正确。
          console.error(`Failed to delete calendar. Code: ${err1.code}, message: ${err1.message}`);
        } else {
          console.info('Succeeded in deleting calendar');
        }
      });
    }
  });
}).catch((error: BusinessError) => {
  // 检查权限是否已成功申请或者参数是否正确。
  console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
})
```

## editEvent

```TypeScript
editEvent(event: Event): Promise<number>
```

通过跳转到日程创建页面创建单个日程，入参Event不填日程id，不支持设置instanceStartTime、instanceEndTime、identifier、attendee、service、isLunar和timeZone属性，也不支持添加重要日程。使用Promise异步回调。 使用该接口创建的日程，系统日历可以进行查询和修改，申请到READ_WHOLE_CALENDAR权限的三方应用可以查询，申请到WRITE_WHOLE_CALENDAR权限的三方应用可以修改。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CalendarManager-editEvent(event: Event): Promise<number>--><!--Device-CalendarManager-editEvent(event: Event): Promise<number>-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## 示例

```TypeScript
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

const date = new Date();
const event: calendarManager.Event = {
  title: 'title',
  type: calendarManager.EventType.NORMAL,
  startTime: date.getTime(),
  endTime: date.getTime() + 60 * 60 * 1000
};
calendarMgr?.editEvent(event).then((eventId: number): void => {
  console.info(`create Event id = ${eventId}`);
});
```

## getAllCalendars

```TypeScript
getAllCalendars(): Promise<Calendar[]>
```

获取当前应用所有创建的Calendar对象以及默认Calendar对象，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

<!--Device-CalendarManager-getAllCalendars(): Promise<Calendar[]>--><!--Device-CalendarManager-getAllCalendars(): Promise<Calendar[]>-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**返回值：**

| 类型 |
| --- |
| Promise & lt;Calendar[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

calendarMgr?.getAllCalendars().then((data: calendarManager.Calendar[]) => {
  console.info(`Succeeded in getting all calendars, data -> ${JSON.stringify(data)}`);
  data.forEach((calendar) => {
    const account = calendar.getAccount();
    console.info(`account -> ${JSON.stringify(account)}`);
  })
}).catch((err: BusinessError) => {
  // 检查权限是否已成功申请。
  console.error(`Failed to get all calendars. Code: ${err.code}, message: ${err.message}`);
  
});
```

## getAllCalendars

```TypeScript
getAllCalendars(callback: AsyncCallback<Calendar[]>): void
```

获取当前应用所有创建的Calendar对象以及默认Calendar对象，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

<!--Device-CalendarManager-getAllCalendars(callback: AsyncCallback<Calendar[]>): void--><!--Device-CalendarManager-getAllCalendars(callback: AsyncCallback<Calendar[]>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

calendarMgr?.getAllCalendars((err: BusinessError, data: calendarManager.Calendar[]) => {
  if (err) {
    console.error(`Failed to get all calendars. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting all calendars, data -> ${JSON.stringify(data)}`);
    data.forEach((calendar) => {
      const account = calendar.getAccount();
      console.info(`account -> ${JSON.stringify(account)}`);
    })
  }
});
```

## getCalendar

```TypeScript
getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>
```

获取默认Calendar对象或者指定Calendar对象，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CalendarManager-getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>--><!--Device-CalendarManager-getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>-End-->

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900003](../errorcode-calendarManager.md#23900003-未找到指定的账户) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

calendarMgr?.getCalendar().then((data: calendarManager.Calendar) => {
  console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  // 检查权限是否已成功申请。
  console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
});
```

## getCalendar

```TypeScript
getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void
```

获取默认Calendar对象，默认Calendar是日历存储首次运行时创建的，若创建Event时不关注其Calendar归属，则无须通过createCalendar()创建Calendar，直接使用默认Calendar，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CalendarManager-getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void--><!--Device-CalendarManager-getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23900003](../errorcode-calendarManager.md#23900003-未找到指定的账户) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

const calendarAccount: calendarManager.CalendarAccount = {
  name: 'MyCalendar',
  type: calendarManager.CalendarType.LOCAL
};
calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
  console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
  calendarMgr?.getCalendar(calendarAccount, (err: BusinessError, data: calendarManager.Calendar) => {
    if (err) {
      console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
      // 检查权限是否已成功申请或者参数是否正确。
    } else {
      console.info(`Succeeded in getting calendar data -> ${JSON.stringify(data)}`);
    }
  });
}).catch((error: BusinessError) => {
  console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
  // 检查权限是否已成功申请或者参数是否正确。
})
```

## getCalendar

```TypeScript
getCalendar(callback: AsyncCallback<Calendar>): void
```

获取默认Calendar对象，默认Calendar是日历存储首次运行时创建的，若创建Event时不关注其Calendar归属，则无须通过createCalendar()创建Calendar，直接使用默认Calendar，使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CalendarManager-getCalendar(callback: AsyncCallback<Calendar>): void--><!--Device-CalendarManager-getCalendar(callback: AsyncCallback<Calendar>): void-End-->

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [23900004](../errorcode-calendarManager.md#23900004-内部程序错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// EntryAbility文件须按照calendarManager.getCalendarManager处示例代码进行配置
import { calendarMgr } from '../entryability/EntryAbility';
import { calendarManager } from '@kit.CalendarKit';

calendarMgr?.getCalendar((err: BusinessError, data:calendarManager.Calendar) => {
  if (err) {
    // 检查权限是否已成功申请或者参数是否正确。
    console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
  }
});
```
