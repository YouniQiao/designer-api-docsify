# offLocationIconStatusChange (System API)

## Modules to Import

```TypeScript
```

## offLocationIconStatusChange

```TypeScript
function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void
```

Unsubscribe location icon status changed.

**Since:** 23

<!--Device-geoLocationManager-function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void--><!--Device-geoLocationManager-function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocationIconStatus](arkts-location-geolocationmanager-locationiconstatus-e-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
