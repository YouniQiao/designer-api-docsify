# Calendar

In the following API examples, you need to use [createCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#createcalendar) or getCalendar() to obtain a **Calendar** object before calling related APIs.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## addEvent

```TypeScript
addEvent(event: Event): Promise<number>
```

Adds an event, with no event ID, instanceStartTime, and instanceEndTime specified in Event. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
- API version 10-20: ohos.permission.WRITE_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## addEvent

```TypeScript
addEvent(event: Event, callback: AsyncCallback<number>): void
```

Adds an event, with no event ID, instanceStartTime, and instanceEndTime specified in Event. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
- API version 10-20: ohos.permission.WRITE_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## addEvents

```TypeScript
addEvents(events: Event[]): Promise<void>
```

Adds events in batches, with no event ID, instanceStartTime, and instanceEndTime specified in Event. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
- API version 10-20: ohos.permission.WRITE_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| events | [Event[]](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## addEvents

```TypeScript
addEvents(events: Event[], callback: AsyncCallback<void>): void
```

Adds events in batches, with no event ID, instanceStartTime, and instanceEndTime specified in Event. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
- API version 10-20: ohos.permission.WRITE_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| events | [Event[]](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## deleteEvent

```TypeScript
deleteEvent(id: number): Promise<void>
```

Deletes an event with the specified ID. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## deleteEvent

```TypeScript
deleteEvent(id: number, callback: AsyncCallback<void>): void
```

Deletes an event with the specified ID. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## deleteEvents

```TypeScript
deleteEvents(ids: number[]): Promise<void>
```

Deletes a batch of events with the specified IDs. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ids | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## deleteEvents

```TypeScript
deleteEvents(ids: number[], callback: AsyncCallback<void>): void
```

Deletes a batch of events with the specified IDs. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ids | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## getAccount

```TypeScript
getAccount(): CalendarAccount
```

Obtains the calendar account information.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) |

## getConfig

```TypeScript
getConfig(): CalendarConfig
```

Obtains the calendar configuration information.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) |

## getEvents

```TypeScript
getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>
```

Obtains all events in a calendar that match the filter criteria. This API uses a promise to return the result. If there is only one input parameter, the filter criteria, corresponding to the type EventFilter, must be set as the parameter. If no input parameter is specified, all events under the specified calendar account can be queried.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 10-20: ohos.permission.READ_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventFilter | [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) | No |
| eventKey | (keyof Event)[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Event[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## getEvents

```TypeScript
getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>):void
```

Obtains all events in a calendar that match the filter criteria. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 10-20: ohos.permission.READ_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventFilter | [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) | Yes |
| eventKey | (keyof Event)[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Event[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## getEvents

```TypeScript
getEvents(callback: AsyncCallback<Event[]>):void
```

Obtains all events in the current calendar. This API uses an asynchronous callback to return the result.For versions earlier than API version 20, the default fields to be obtained include id, type, title, startTime, endTime, isAllDay, description, timeZone, location, service, attendee, and reminderTime. Since API version 20, the default fields to be obtained include id, type, title, startTime, endTime, isAllDay, description, timeZone, location, service, attendee, reminderTime, and identifier. The field is not returned if it is empty.

**Since:** 10

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 10-20: ohos.permission.READ_CALENDAR

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Event[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## openEventEditPage

```TypeScript
openEventEditPage(id: number): Promise<void>
```

Obtains the event instance that meets the viewing or editing condition in a calendar based on the event ID. This API uses a promise to return the result.This API can be used to view and edit calendar events in the system calendar.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23900001](../errorcode-calendarManager.md#23900001-parameter-value-error) |
| [23900005](../errorcode-calendarManager.md#23900005-event-not-editable) |

## queryEventInstances

```TypeScript
queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>
```

Queries the event instance with a specified event key in a calendar. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** 
- API version 21+: ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
- API version 18-20: ohos.permission.READ_CALENDAR

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| end | number | Yes |
| ids | number[] | No |
| eventKey | (keyof Event)[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Event[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23900004](../errorcode-calendarManager.md#23900004-internal-program-error) |

## setConfig

```TypeScript
setConfig(config: CalendarConfig): Promise<void>
```

Sets the calendar configuration information. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23900001](../errorcode-calendarManager.md#23900001-parameter-value-error) |

## setConfig

```TypeScript
setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void
```

Sets the calendar configuration information. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23900001](../errorcode-calendarManager.md#23900001-parameter-value-error) |

## updateEvent

```TypeScript
updateEvent(event: Event): Promise<void>
```

Updates an event, with the ID of the updated event specified in Event. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## updateEvent

```TypeScript
updateEvent(event: Event, callback: AsyncCallback<void>): void
```

Updates an event. The ID of the updated event must be specified in Event. If not, the event cannot be updated. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## id

```TypeScript
readonly id: number
```

Calendar account ID, which is the unique identifier of a calendar account and is the auto-increment primary key of the database. If the value is less than 0, the account creation fails; if the value is greater than 0, the account creation succeeds.

**Type:** number

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.CalendarData
