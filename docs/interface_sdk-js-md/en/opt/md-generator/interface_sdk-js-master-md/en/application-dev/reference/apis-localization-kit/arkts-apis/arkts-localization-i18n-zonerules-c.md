# ZoneRules

Queries the time zone transition rule.

**Since:** 23

<!--Device-i18n-export class ZoneRules--><!--Device-i18n-export class ZoneRules-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
```

## nextTransition

```TypeScript
public nextTransition(date?: number): ZoneOffsetTransition
```

Obtains the **nextTransition** object for the specified time.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneRules-public nextTransition(date?: double): ZoneOffsetTransition--><!--Device-ZoneRules-public nextTransition(date?: double): ZoneOffsetTransition-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ZoneOffsetTransition](arkts-localization-i18n-zoneoffsettransition-c.md) |
