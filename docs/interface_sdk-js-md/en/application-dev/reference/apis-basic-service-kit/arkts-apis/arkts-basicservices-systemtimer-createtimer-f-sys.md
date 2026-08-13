# createTimer (System API)

## Modules to Import

```TypeScript
import { systemTimer } from '@kit.BasicServicesKit';
```

## createTimer

```TypeScript
function createTimer(options: TimerOptions, callback: AsyncCallback<long>): void
```

Creates a timer. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API must be used together with > [systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md#destroyTimer-(System-API)). Otherwise > , memory leakage occurs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-systemTimer-function createTimer(options: TimerOptions, callback: AsyncCallback<long>): void--><!--Device-systemTimer-function createTimer(options: TimerOptions, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | Yes | Timer initialization options, including the timer type, whether the timer is a repeating timer, interval, and **WantAgent** options. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the timer ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. &lt;br&gt; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: systemTimer.TimerOptions = {
  type: systemTimer.TIMER_TYPE_REALTIME,
  repeat: false
};
try {
  systemTimer.createTimer(options, (error: BusinessError, timerId: Number) => {
    if (error) {
      console.error(`Failed to create timer. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in creating a timer. timerId: ${timerId}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to create timer. message: ${error.message}, code: ${error.code}`);
}
```


## createTimer

```TypeScript
function createTimer(options: TimerOptions): Promise<long>
```

Creates a timer. This API uses a promise to return the timer ID. > **NOTE：**> > This API must be used together with > [systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md#destroyTimer-(System-API)). Otherwise > , memory leakage occurs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-systemTimer-function createTimer(options: TimerOptions): Promise<long>--><!--Device-systemTimer-function createTimer(options: TimerOptions): Promise<long>-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | Yes | Timer initialization options, including the timer type, whether the timer is a repeating timer, interval, and **WantAgent** options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the timer ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: systemTimer.TimerOptions = {
  type: systemTimer.TIMER_TYPE_REALTIME,
  repeat:false
};
try {
  systemTimer.createTimer(options).then((timerId: Number) => {
    console.info(`Succeeded in creating a timer. timerId: ${timerId}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to create timer. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to create timer. message: ${error.message}, code: ${error.code}`);
}
```

