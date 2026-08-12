# write

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## write

```TypeScript
function write(info: AppEventInfo): Promise<void>
```

Writes events of the **AppEventInfo** type. This API uses a promise to return the result. The event object written by calling this API is a custom object. To avoid conflicts with system events, you are not advised to write it to system events (system event name constants defined in [Event](arkts-performanceanalysis-hiappevent-event-n.md#event)). The events written by this API can be subscribed to through ([addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addWatcher)).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function write(info: AppEventInfo): Promise<void>--><!--Device-hiAppEvent-function write(info: AppEventInfo): Promise<void>-End-->

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
| [11101001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101001-invalid-event-domain-name) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11101003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101003-invalid-number-of-event-parameters) |
| [11101002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101002-invalid-event-name) |
| [11101005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101005-invalid-event-parameter-name) |
| [11101004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101004-invalid-event-parameter-string-length) |
| [11101006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101006-invalid-array-length-of-event-parameter-values) |
| [11100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11100001-application-event-logging-disabled) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};

// Application event logging. This API uses a promise to return the result.
hiAppEvent.write({
  domain: "test_domain",
  name: "test_event",
  eventType: hiAppEvent.EventType.FAULT,
  params: eventParams,
}).then(() => {
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
});
```


## write

```TypeScript
function write(info: AppEventInfo, callback: AsyncCallback<void>): void
```

Writes events of the **AppEventInfo** type. This API uses an asynchronous callback to return the result. The event object written by calling this API is a custom object. To avoid conflicts with system events, you are not advised to write it to system events (system event name constants defined in [Event](arkts-performanceanalysis-hiappevent-event-n.md#event)). The events written by this API can be subscribed to through ([addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addWatcher)).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function write(info: AppEventInfo, callback: AsyncCallback<void>): void--><!--Device-hiAppEvent-function write(info: AppEventInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [11101001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101001-invalid-event-domain-name) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11101003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101003-invalid-number-of-event-parameters) |
| [11101002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101002-invalid-event-name) |
| [11101005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101005-invalid-event-parameter-name) |
| [11101004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101004-invalid-event-parameter-string-length) |
| [11101006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101006-invalid-array-length-of-event-parameter-values) |
| [11100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11100001-application-event-logging-disabled) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};

// Application event logging. This API uses an asynchronous callback to return the result.
hiAppEvent.write({
  domain: "test_domain",
  name: "test_event",
  eventType: hiAppEvent.EventType.FAULT,
  params: eventParams,
}, (err: BusinessError) => {
  if (err) {
    hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
    return;
  }
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
});
```
