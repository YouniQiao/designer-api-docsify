# createTimer (System API)

## Modules to Import

```TypeScript
import { systemTimer } from 'kits/@kit.BasicServicesKit';
```

## createTimer

```TypeScript
function createTimer(options: TimerOptions, callback: AsyncCallback<number>): void
```

Creates a timer. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API must be used together with
> [systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md). Otherwise
> , memory leakage occurs.

**Since:** 7

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## createTimer

```TypeScript
function createTimer(options: TimerOptions): Promise<number>
```

Creates a timer. This API uses a promise to return the timer ID.

> **NOTE：**&gt;
> This API must be used together with
> [systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md). Otherwise
> , memory leakage occurs.

**Since:** 7

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
