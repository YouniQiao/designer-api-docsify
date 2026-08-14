# @ohos.systemTime

The **systemTime** module provides system time and time zone features. You can use the APIs of this module to set and obtain the system time and time zone.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [systemDateTime](arkts-systemdatetime.md#@ohos.systemDateTime)

<!--Device-unnamed-declare namespace systemTime--><!--Device-unnamed-declare namespace systemTime-End-->

**System capability:** SystemCapability.MiscServices.Time

## Modules to Import

```TypeScript
import { systemTime } from 'systemTime';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getCurrentTime](arkts-basicservices-systemtime-getcurrenttime-f.md#getCurrentTime) | Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result. |
| [getCurrentTime](arkts-basicservices-systemtime-getcurrenttime-f.md#getCurrentTime) | Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result. |
| [getCurrentTime](arkts-basicservices-systemtime-getcurrenttime-f.md#getCurrentTime) | Obtains the time elapsed since the Unix epoch. This API uses a promise to return the result. |
| [getDate](arkts-basicservices-systemtime-getdate-f.md#getDate) | Obtains the current system date. This API uses an asynchronous callback to return the result. |
| [getDate](arkts-basicservices-systemtime-getdate-f.md#getDate) | Obtains the current system date. This API uses a promise to return the result. |
| [getRealActiveTime](arkts-basicservices-systemtime-getrealactivetime-f.md#getRealActiveTime) | Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result. |
| [getRealActiveTime](arkts-basicservices-systemtime-getrealactivetime-f.md#getRealActiveTime) | Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result. |
| [getRealActiveTime](arkts-basicservices-systemtime-getrealactivetime-f.md#getRealActiveTime) | Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses a promise to return the result. |
| [getRealTime](arkts-basicservices-systemtime-getrealtime-f.md#getRealTime) | Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous callback to return the result. |
| [getRealTime](arkts-basicservices-systemtime-getrealtime-f.md#getRealTime) | Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous callback to return the result. |
| [getRealTime](arkts-basicservices-systemtime-getrealtime-f.md#getRealTime) | Obtains the time elapsed since system startup, including the deep sleep time. This API uses a promise to return the result. |
| [getTimezone](arkts-basicservices-systemtime-gettimezone-f.md#getTimezone) | Obtains the system time zone. This API uses an asynchronous callback to return the result. |
| [getTimezone](arkts-basicservices-systemtime-gettimezone-f.md#getTimezone) | Obtains the system time zone. This API uses a promise to return the result. |
| [setDate](arkts-basicservices-systemtime-setdate-f.md#setDate) | Sets the system date. This API uses an asynchronous callback to return the result. |
| [setDate](arkts-basicservices-systemtime-setdate-f.md#setDate) | Sets the system date. This API uses a promise to return the result. |
| [setTime](arkts-basicservices-systemtime-settime-f.md#setTime) | Sets the system time. This API uses an asynchronous callback to return the result. |
| [setTime](arkts-basicservices-systemtime-settime-f.md#setTime) | Sets the system time. This API uses a promise to return the result. |
| [setTimezone](arkts-basicservices-systemtime-settimezone-f.md#setTimezone) | Sets the system time zone. This API uses an asynchronous callback to return the result. |
| [setTimezone](arkts-basicservices-systemtime-settimezone-f.md#setTimezone) | Sets the system time zone. This API uses a promise to return the result. |

