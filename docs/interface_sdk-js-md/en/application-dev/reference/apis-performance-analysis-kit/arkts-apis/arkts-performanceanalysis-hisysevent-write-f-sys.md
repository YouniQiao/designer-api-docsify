# write (System API)

## Modules to Import

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## write

```TypeScript
function write(info: SysEventInfo): Promise<void>
```

Writes event information to the event file. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 11200001 |
| 11200002 |
| [11200003](../errorcode-hisysevent-sys.md#11200003-environment-error) |
| [11200004](../errorcode-hisysevent-sys.md#11200004-invalid-event-length) |
| [11200051](../errorcode-hisysevent-sys.md#11200051-invalid-event-parameter) |
| [11200052](../errorcode-hisysevent-sys.md#11200052-length-of-event-parameter-values-of-the-string-type-exceeding-the-limit) |
| [11200053](../errorcode-hisysevent-sys.md#11200053-number-of-event-parameters-exceeding-the-limit) |
| [11200054](../errorcode-hisysevent-sys.md#11200054-length-of-event-parameter-values-of-the-array-type-exceeding-the-limit) |


## write

```TypeScript
function write(info: SysEventInfo, callback: AsyncCallback<void>): void
```

Writes event information to the event file. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 11200001 |
| 11200002 |
| [11200003](../errorcode-hisysevent-sys.md#11200003-environment-error) |
| [11200004](../errorcode-hisysevent-sys.md#11200004-invalid-event-length) |
| [11200051](../errorcode-hisysevent-sys.md#11200051-invalid-event-parameter) |
| [11200052](../errorcode-hisysevent-sys.md#11200052-length-of-event-parameter-values-of-the-string-type-exceeding-the-limit) |
| [11200053](../errorcode-hisysevent-sys.md#11200053-number-of-event-parameters-exceeding-the-limit) |
| [11200054](../errorcode-hisysevent-sys.md#11200054-length-of-event-parameter-values-of-the-array-type-exceeding-the-limit) |
