# ZoneRules

Queries the time zone transition rule.

**Since:** 23

<!--Device-i18n-export class ZoneRules--><!--Device-i18n-export class ZoneRules-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
import { i18n } from '@kit.LocalizationKit';
```

## nextTransition

```TypeScript
public nextTransition(date?: double): ZoneOffsetTransition
```

Obtains the **nextTransition** object for the specified time.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneRules-public nextTransition(date?: double): ZoneOffsetTransition--><!--Device-ZoneRules-public nextTransition(date?: double): ZoneOffsetTransition-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | double | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ZoneOffsetTransition](../../apis-na/arkts-apis/arkts-na-i18n-zoneoffsettransition-c.md) | ZoneOffsetTransition** object for next transition. |

