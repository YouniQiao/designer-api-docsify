# @ohos.systemDateTime

The **systemTime** module provides system time and time zone features. You can obtain the system time and time zone by using the following APIs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace systemDateTime--><!--Device-unnamed-declare namespace systemDateTime-End-->

**System capability:** SystemCapability.MiscServices.Time

## Modules to Import

```TypeScript
import { systemDateTime } from 'systemDateTime';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAutoTimeStatus](arkts-basicservices-systemdatetime-getautotimestatus-f.md#getAutoTimeStatus) | Obtains the switch status of the automatic time setting. This API returns the result synchronously. |
| [getCurrentTime](arkts-basicservices-systemdatetime-getcurrenttime-f.md#getCurrentTime) | Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result. |
| [getCurrentTime](arkts-basicservices-systemdatetime-getcurrenttime-f.md#getCurrentTime) | Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result. |
| [getCurrentTime](arkts-basicservices-systemdatetime-getcurrenttime-f.md#getCurrentTime) | Obtains the time elapsed since the Unix epoch. This API uses a promise to return the result. |
| [getDate](arkts-basicservices-systemdatetime-getdate-f.md#getDate) | Obtains the current system date. This API uses an asynchronous callback to return the result. |
| [getDate](arkts-basicservices-systemdatetime-getdate-f.md#getDate) | Obtains the current system date. This API uses a promise to return the result. |
| [getRealActiveTime](arkts-basicservices-systemdatetime-getrealactivetime-f.md#getRealActiveTime) | Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result. |
| [getRealActiveTime](arkts-basicservices-systemdatetime-getrealactivetime-f.md#getRealActiveTime) | Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result. |
| [getRealActiveTime](arkts-basicservices-systemdatetime-getrealactivetime-f.md#getRealActiveTime) | Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses a promise to return the result. |
| [getRealTime](arkts-basicservices-systemdatetime-getrealtime-f.md#getRealTime) | Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous callback to return the result. |
| [getRealTime](arkts-basicservices-systemdatetime-getrealtime-f.md#getRealTime) | Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous callback to return the result. |
| [getRealTime](arkts-basicservices-systemdatetime-getrealtime-f.md#getRealTime) | Obtains the time elapsed since system startup, including the deep sleep time. This API uses a promise to return the result. |
| [getTime](arkts-basicservices-systemdatetime-gettime-f.md#getTime) | Obtains the time elapsed since the Unix epoch. This API returns the result synchronously. |
| [getTimezone](arkts-basicservices-systemdatetime-gettimezone-f.md#getTimezone) | Obtains the system time zone. This API uses an asynchronous callback to return the result. |
| [getTimezone](arkts-basicservices-systemdatetime-gettimezone-f.md#getTimezone) | Obtains the system time zone. This API uses a promise to return the result. |
| [getTimezoneSync](arkts-basicservices-systemdatetime-gettimezonesync-f.md#getTimezoneSync) | Obtains the system time zone in synchronous mode. |
| [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getUptime) | Obtains the time elapsed since system startup. This API returns the result synchronously. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getNtpTime](arkts-basicservices-systemdatetime-getntptime-f-sys.md#getNtpTime) | Obtains the actual time calculated based on the last updated NTP time. This API returns the result synchronously. |
| [setAutoTimeStatus](arkts-basicservices-systemdatetime-setautotimestatus-f-sys.md#setAutoTimeStatus) | Sets the status of the automatic time setting. This API uses a promise to return the result. |
| [setDate](arkts-basicservices-systemdatetime-setdate-f-sys.md#setDate) | Sets the system date. This API uses an asynchronous callback to return the result. |
| [setDate](arkts-basicservices-systemdatetime-setdate-f-sys.md#setDate-(System-API)) | Sets the system date. This API uses a promise to return the result. |
| [setTime](arkts-basicservices-systemdatetime-settime-f-sys.md#setTime) | Sets the system time. This API uses an asynchronous callback to return the result. |
| [setTime](arkts-basicservices-systemdatetime-settime-f-sys.md#setTime-(System-API)) | Sets the system time. This API uses a promise to return the result. |
| [setTimezone](arkts-basicservices-systemdatetime-settimezone-f-sys.md#setTimezone) | Sets the system time zone. This API uses an asynchronous callback to return the result. |
| [setTimezone](arkts-basicservices-systemdatetime-settimezone-f-sys.md#setTimezone-(System-API)) | Sets the system time zone. This API uses a promise to return the result. |
| [updateNtpTime](arkts-basicservices-systemdatetime-updatentptime-f-sys.md#updateNtpTime) | Updates the NTP time from the NTP server This API returns the result asynchronously. In this way, the NTP time is updated from the NTP server only once within one hour. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [TimeType](arkts-basicservices-systemdatetime-timetype-e.md) | Enumerates the types of time to obtain. |

