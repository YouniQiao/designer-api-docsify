# ZoneRules

Provides the API for obtaining timezone offset changing rules information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-i18n-export class ZoneRules--><!--Device-i18n-export class ZoneRules-End-->

**System capability:** SystemCapability.Global.I18n

## nextTransition

```TypeScript
public nextTransition(date?: double): ZoneOffsetTransition
```

Get the next timezone offset transition after date.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneRules-public nextTransition(date?: double): ZoneOffsetTransition--><!--Device-ZoneRules-public nextTransition(date?: double): ZoneOffsetTransition-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | double | No | Indicates milliseconds. |

**Return value:**

| Type | Description |
| --- | --- |
| [ZoneOffsetTransition](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-zoneoffsettransition-c.md) | Returns a timezone offset transition after date. |

