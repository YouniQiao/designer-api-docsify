# setEventParam

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## setEventParam

```TypeScript
function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>
```

Sets custom event parameters. This API uses a promise to return the result. During the same lifecycle, system events and application events can be associated through event domain and event name.System events only support crash, freeze and resource leak events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | Record&lt;string, [ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md)&gt; | Yes |
| domain | string | Yes |
| name | string | No |

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
| [11101004](../errorcode-hiappevent.md#11101004-invalid-event-parameter-string-length) |
| [11101005](../errorcode-hiappevent.md#11101005-invalid-event-parameter-name) |
| [11101007](../errorcode-hiappevent.md#11101007-invalid-number-of-custom-event-parameters) |
