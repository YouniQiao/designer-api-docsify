# startTimer (System API)

## Modules to Import

```TypeScript
import { systemTimer } from 'kits/@kit.BasicServicesKit';
```

## startTimer

```TypeScript
function startTimer(timer: long, triggerTime: long, callback: AsyncCallback<void>): void
```

开启定时器，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-systemTimer-function startTimer(timer: long, triggerTime: long, callback: AsyncCallback<void>): void--><!--Device-systemTimer-function startTimer(timer: long, triggerTime: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timer | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 定时器的ID。 |
| triggerTime | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 定时器的触发时间，单位：毫秒。&lt;br/&gt;若定时器类型包含了TIMER_TYPE_REALTIME，该triggerTime应为系统启动时间，建议通过 [systemDateTime.getUptime(STARTUP)](arkts-basicservices-systemdatetime-getuptime-f.md#getuptime)获取；&lt;br/&gt;若定时器类型不包含 TIMER_TYPE_REALTIME，该triggerTime应为墙上时间，建议通过 [systemDateTime.getTime()](arkts-basicservices-systemdatetime-gettime-f.md#gettime)获取。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: systemTimer.TimerOptions = {
  type: systemTimer.TIMER_TYPE_REALTIME,
  repeat:false
}
let triggerTime: number = new Date().getTime();
triggerTime += 3000;

try {
  systemTimer.createTimer(options).then((timerId: number) => {
    systemTimer.startTimer(timerId, triggerTime, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to start timer. message: ${error.message}, code: ${error.code}`);
        return;
      }
      console.info(`Succeeded in starting the timer.`);
    });
    console.info(`Succeeded in creating a timer. timerId: ${timerId}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to create timer. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to create timer. message: ${error.message}, code: ${error.code}`);
}
```


## startTimer

```TypeScript
function startTimer(timer: long, triggerTime: long): Promise<void>
```

开启定时器，使用Promise进行异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-systemTimer-function startTimer(timer: long, triggerTime: long): Promise<void>--><!--Device-systemTimer-function startTimer(timer: long, triggerTime: long): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timer | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 定时器的ID。 |
| triggerTime | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 定时器的触发时间，单位：毫秒。&lt;br/&gt;若定时器类型包含了TIMER_TYPE_REALTIME，该triggerTime应为系统启动时间，建议通过 [systemDateTime.getUptime(STARTUP)](arkts-basicservices-systemdatetime-getuptime-f.md#getuptime)获取；&lt;br/&gt;若定时器类型不包含 TIMER_TYPE_REALTIME，该triggerTime应为墙上时间，建议通过 [systemDateTime.getTime()](arkts-basicservices-systemdatetime-gettime-f.md#gettime)获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: systemTimer.TimerOptions = {
  type: systemTimer.TIMER_TYPE_REALTIME,
  repeat:false
}
let triggerTime: number = new Date().getTime();
triggerTime += 3000;

try {
  systemTimer.createTimer(options).then((timerId: number) => {
    systemTimer.startTimer(timerId, triggerTime).then(() => {
      console.info(`Succeeded in starting the timer.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to start timer. message: ${error.message}, code: ${error.code}`);
    });
    console.info(`Succeeded in creating a timer. timerId: ${timerId}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to create timer. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to create timer. message: ${error.message}, code: ${error.code}`);
}
```

