# setEventParam

## Modules to Import

```TypeScript
```

## setEventParam

```TypeScript
function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>
```

Sets custom event parameters. This API uses a promise to return the result. During the same lifecycle, system events and application events can be associated through event domain and event name.System events only support crash, freeze and resource leak events.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-hiAppEvent-function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>--><!--Device-hiAppEvent-function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md)&gt; | Yes |
| domain | string | Yes |
| name | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11101001](../errorcode-hiappevent.md#11101001-invalid-event-domain-name) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11101002](../errorcode-hiappevent.md#11101002-invalid-event-name) |
| [11101005](../errorcode-hiappevent.md#11101005-invalid-event-parameter-name) |
| [11101004](../errorcode-hiappevent.md#11101004-invalid-event-parameter-string-length) |
| [11101007](../errorcode-hiappevent.md#11101007-invalid-number-of-custom-event-parameters) |
| [11100001](../errorcode-hiappevent.md#11100001-application-event-logging-disabled) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let params: Record<string, hiAppEvent.ParamType> = {
  "int_data": 100,
  "str_data": "strValue",
};

// Add custom parameters to the application event.
hiAppEvent.setEventParam(params, "test_domain", "test_event").then(() => {
  hilog.info(0x0000, 'hiAppEvent', `success to set event param`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
});
```
