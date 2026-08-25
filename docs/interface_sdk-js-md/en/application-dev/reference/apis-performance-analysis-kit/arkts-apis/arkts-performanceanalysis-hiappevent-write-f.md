# write

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## write

```TypeScript
function write(info: AppEventInfo): Promise<void>
```

Writes events of the **AppEventInfo** type. This API uses a promise to return the result. The event object written by calling this API is a custom object. To avoid conflicts with system events, you are not advised to write it to system events (system event name constants defined in [Event](arkts-performanceanalysis-hiappevent-event-n.md)). The events written by this API can be subscribed to through ([addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11100001](../errorcode-hiappevent.md#11100001-application-event-logging-disabled) |
| [11101001](../errorcode-hiappevent.md#11101001-invalid-event-domain-name) |
| [11101002](../errorcode-hiappevent.md#11101002-invalid-event-name) |
| [11101003](../errorcode-hiappevent.md#11101003-invalid-number-of-event-parameters) |
| [11101004](../errorcode-hiappevent.md#11101004-invalid-event-parameter-string-length) |
| [11101005](../errorcode-hiappevent.md#11101005-invalid-event-parameter-name) |
| [11101006](../errorcode-hiappevent.md#11101006-invalid-array-length-of-event-parameter-values) |


## write

```TypeScript
function write(info: AppEventInfo, callback: AsyncCallback<void>): void
```

Writes events of the **AppEventInfo** type. This API uses an asynchronous callback to return the result. The event object written by calling this API is a custom object. To avoid conflicts with system events, you are not advised to write it to system events (system event name constants defined in [Event](arkts-performanceanalysis-hiappevent-event-n.md)). The events written by this API can be subscribed to through ([addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11100001](../errorcode-hiappevent.md#11100001-application-event-logging-disabled) |
| [11101001](../errorcode-hiappevent.md#11101001-invalid-event-domain-name) |
| [11101002](../errorcode-hiappevent.md#11101002-invalid-event-name) |
| [11101003](../errorcode-hiappevent.md#11101003-invalid-number-of-event-parameters) |
| [11101004](../errorcode-hiappevent.md#11101004-invalid-event-parameter-string-length) |
| [11101005](../errorcode-hiappevent.md#11101005-invalid-event-parameter-name) |
| [11101006](../errorcode-hiappevent.md#11101006-invalid-array-length-of-event-parameter-values) |
