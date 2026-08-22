# getTimeZone

## Modules to Import

```TypeScript
```

## getTimeZone

```TypeScript
export function getTimeZone(zoneID?: string): TimeZone
```

Obtains the TimeZone object corresponding to the specified time zone ID.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getTimeZone(zoneID?: string): TimeZone--><!--Device-i18n-export function getTimeZone(zoneID?: string): TimeZone-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoneID | string | No | Time zone ID. The default value is the system time zone. |

**Return value:**

| Type | Description |
| --- | --- |
| [TimeZone](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-timezone-c.md) | TimeZone object corresponding to the time zone ID. |

