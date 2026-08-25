# CalendarManager

Before calling any of the following APIs to manage the calendar, you must use [getCalendarManager()](arkts-calendar-calendarmanager-getcalendarmanager-f.md) to obtain a **CalendarManager** object first.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## createCalendar

```TypeScript
createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>
```

Creates a Calendar object based on the calendar account information. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
- API version 10-20: ohos.permission.WRITE_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Calendar & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## createCalendar

```TypeScript
createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void
```

Creates a Calendar object based on the calendar account information. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
- API version 10-20: ohos.permission.WRITE_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## deleteCalendar

```TypeScript
deleteCalendar(calendar: Calendar): Promise<void>
```

Deletes a specified Calendar object. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
- API version 10-20: ohos.permission.WRITE_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| calendar | [Calendar](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-calendar-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## deleteCalendar

```TypeScript
deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void
```

Deletes a specified Calendar object. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
- API version 10-20: ohos.permission.WRITE_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| calendar | [Calendar](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-calendar-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## editEvent

```TypeScript
editEvent(event: Event): Promise<number>
```

Edits an event on the event creation page, with no event ID specified in **Event**. The **instanceStartTime**, **instanceEndTime**, **identifier**, **attendee**, **service**, **isLunar**, and **timeZone** attributes cannot be set. Important events cannot be added either. This API uses a promise to return the result.Events created using this API can be obtained and modified by the system calendar. Third-party applications can obtain and modify the events after they requested the **READ_WHOLE_CALENDAR** permission and the **WRITE_WHOLE_CALENDAR** permission, respectively.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getAllCalendars

```TypeScript
getAllCalendars(): Promise<Calendar[]>
```

Obtains the created and default Calendar objects of the current application. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 10-20: ohos.permission.READ_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Calendar[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## getAllCalendars

```TypeScript
getAllCalendars(callback: AsyncCallback<Calendar[]>): void
```

Obtains the created and default Calendar objects of the current application. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 10-20: ohos.permission.READ_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## getCalendar

```TypeScript
getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>
```

Obtains the default or specified Calendar object. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 10-20: ohos.permission.READ_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Calendar & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900003](../errorcode-calendarManager.md#23900003-specified-account-not-found) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## getCalendar

```TypeScript
getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void
```

Obtains a specified Calendar object. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 10-20: ohos.permission.READ_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| calendarAccount | [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900003](../errorcode-calendarManager.md#23900003-specified-account-not-found) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## getCalendar

```TypeScript
getCalendar(callback: AsyncCallback<Calendar>): void
```

Obtains the default Calendar object, which is created when the data storage runs for the first time. This API uses an asynchronous callback to return the result. You can call this API instead of createCalendar() to use the default calendar for a new event.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 10-20: ohos.permission.READ_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Calendar&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |
