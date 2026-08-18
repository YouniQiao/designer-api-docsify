# @ohos.systemTimer

The **systemTimer** module provides system timer features. You can use the APIs of this module to implement the alarm clock and other timer services.

**Since:** 23

<!--Device-unnamed-declare namespace systemTimer--><!--Device-unnamed-declare namespace systemTimer-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { systemTimer } from '@kit.BasicServicesKit';
import { systemTimer } from '@kit.BasicServicesKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [createTimer](arkts-basicservices-systemtimer-createtimer-f-sys.md#createtimer) | Creates a timer. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API must be used together with > [systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md#destroytimer-system-api). Otherwise > , memory leakage occurs. |
| [createTimer](arkts-basicservices-systemtimer-createtimer-f-sys.md#createtimer-system-api) | Creates a timer. This API uses a promise to return the timer ID. > **NOTE：**> > This API must be used together with > [systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md#destroytimer-system-api). Otherwise > , memory leakage occurs. |
| [destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md#destroytimer) | Destroys a timer. This API uses an asynchronous callback to return the result. |
| [destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md#destroytimer-system-api) | Destroys a timer. This API uses a promise to return the result. |
| [startTimer](arkts-basicservices-systemtimer-starttimer-f-sys.md#starttimer) | Starts a timer. This API uses an asynchronous callback to return the result. |
| [startTimer](arkts-basicservices-systemtimer-starttimer-f-sys.md#starttimer-system-api) | Starts a timer. This API uses a promise to return the result. |
| [stopTimer](arkts-basicservices-systemtimer-stoptimer-f-sys.md#stoptimer) | Stops the timer. This API uses an asynchronous callback to return the result. |
| [stopTimer](arkts-basicservices-systemtimer-stoptimer-f-sys.md#stoptimer-system-api) | Stops a timer. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | Defines the initialization options for the system timer. |
<!--DelEnd-->

<!--Del-->
### Constants（系统接口）

| Name | Description |
| --- | --- |
| [TIMER_TYPE_EXACT](arkts-basicservices-systemtimer-con-sys.md#timertypeexact) | Exact type. (If the system time is changed, the offset may be 1s at most.) |
| [TIMER_TYPE_IDLE](arkts-basicservices-systemtimer-con-sys.md#timertypeidle) | Idle timer type (supported only for system services). |
| [TIMER_TYPE_REALTIME](arkts-basicservices-systemtimer-con-sys.md#timertyperealtime) | CPU time type. (The start time of the timer cannot be later than the current system time.) |
| [TIMER_TYPE_WAKEUP](arkts-basicservices-systemtimer-con-sys.md#timertypewakeup) | Wakeup type. (If the wakeup type is not set, the system does not wake up until it exits the sleep state.) |
<!--DelEnd-->

