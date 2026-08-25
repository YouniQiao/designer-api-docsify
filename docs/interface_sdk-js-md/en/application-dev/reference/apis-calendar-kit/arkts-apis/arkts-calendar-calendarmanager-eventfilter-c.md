# EventFilter

Implements an event filter.You can use [filterById()](#filterbyid), [filterByTime()](#filterbytime), [filterByTitle()](#filterbytitle) to obtain an event filter, and then pass the filter in getEvents() for filtering.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## filterById

```TypeScript
static filterById(ids: number[]): EventFilter
```

Defines a filter based on the event ID.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ids | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) |

## filterByTime

```TypeScript
static filterByTime(start: number, end: number): EventFilter
```

Defines a filter based on the event time.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| end | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) |

## filterByTitle

```TypeScript
static filterByTitle(title: string): EventFilter
```

Filters events by event title. This API supports fuzzy match.

**Since:** 10

**System capability:** SystemCapability.Applications.CalendarData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| title | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) |
