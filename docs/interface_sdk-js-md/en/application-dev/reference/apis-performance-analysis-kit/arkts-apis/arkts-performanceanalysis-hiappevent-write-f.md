# write

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## write

```TypeScript
function write(info: AppEventInfo): Promise<void>
```

应用事件打点方法，将AppEventInfo类型的事件进行存储，使用Promise方式作为异步回调。通过此接口写入的事件对象是开发者自定义的对象，为了避免与系统事件产生冲突混淆，不建议写入系统事件（[Event](arkts-performanceanalysis-hiappevent-event-n.md#event)中定义的系统事件名称常量）。此接口写入的事件可通过订阅事件观察者（[addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addwatcher)）进行处理。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function write(info: AppEventInfo): Promise<void>--><!--Device-hiAppEvent-function write(info: AppEventInfo): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) | Yes | 应用事件对象。其中的事件名称建议避免与 [Event](arkts-performanceanalysis-hiappevent-event-n.md#event)中定义的系统事件名称常量冲突混淆。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11101001 | Invalid event domain. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| 11101003 | Invalid number of event parameters. Possibly caused by the number of parameters &lt;br&gt;is over 32. |
| 11101002 | Invalid event name. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 11101005 | Invalid event parameter name. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 11101004 | Invalid string length of the event parameter. |
| 11101006 | Invalid array length of the event parameter. |
| 11100001 | Function disabled. Possibly caused by the param disable in ConfigOption is true. |

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

应用事件打点方法，将AppEventInfo类型的事件进行存储，使用callback方式作为异步回调。通过此接口写入的事件对象是开发者自定义的对象，为了避免与系统事件产生冲突混淆，不建议写入系统事件（[Event](arkts-performanceanalysis-hiappevent-event-n.md#event)中定义的系统事件名称常量）。此接口写入的事件可通过订阅事件观察者（[addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addwatcher)）进行订阅。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function write(info: AppEventInfo, callback: AsyncCallback<void>): void--><!--Device-hiAppEvent-function write(info: AppEventInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) | Yes | 应用事件对象。其内部定义的事件名称建议避免与[Event](arkts-performanceanalysis-hiappevent-event-n.md#event)中定义的系统事件名称常量产生冲突。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 打点回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11101001 | Invalid event domain. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| 11101003 | Invalid number of event parameters. Possibly caused by the number of parameters &lt;br&gt;is over 32. |
| 11101002 | Invalid event name. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 11101005 | Invalid event parameter name. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 11101004 | Invalid string length of the event parameter. |
| 11101006 | Invalid array length of the event parameter. |
| 11100001 | Function disabled. Possibly caused by the param disable in ConfigOption is true. |

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

