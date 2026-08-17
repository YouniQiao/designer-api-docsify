# ZoneOffsetTransition

Provides the API for obtaining a timezone transition information.

**Since:** 23

<!--Device-i18n-export class ZoneOffsetTransition--><!--Device-i18n-export class ZoneOffsetTransition-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'i18n';
```

## getMilliseconds

```TypeScript
public getMilliseconds(): double
```

Obtains the timestamp of the time zone transition point.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneOffsetTransition-public getMilliseconds(): double--><!--Device-ZoneOffsetTransition-public getMilliseconds(): double-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| double | Timestamp of the time zone transition point. It is measured as the number of milliseconds from 00:00:00 on January 1, 1970 (UTC) to the time zone transition point, for example, 1762074000000. If the [raw offset]{ |

## getOffsetAfter

```TypeScript
public getOffsetAfter(): int
```

Obtains the offset after the time zone transition.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneOffsetTransition-public getOffsetAfter(): int--><!--Device-ZoneOffsetTransition-public getOffsetAfter(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | Post-transition offset, that is, the time difference between the post-transition time and UTC, measured in ms. For example, **-28800000** indicates that the time after the transition is 28800000 ms (8 hours) later than UTC. |

## getOffsetBefore

```TypeScript
public getOffsetBefore(): int
```

Obtains the offset before the time zone transition.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneOffsetTransition-public getOffsetBefore(): int--><!--Device-ZoneOffsetTransition-public getOffsetBefore(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | Pre-transition offset, that is, the time difference between the pre-transition time and UTC, measured in ms. For example, **-25200000** indicates that the pre-transition time is 25200000 ms (7 hours) slower than UTC. |

