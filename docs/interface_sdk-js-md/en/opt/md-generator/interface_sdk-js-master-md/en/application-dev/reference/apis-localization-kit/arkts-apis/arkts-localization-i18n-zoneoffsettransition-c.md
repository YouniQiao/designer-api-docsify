# ZoneOffsetTransition

Provides the API for obtaining a timezone transition information.

**Since:** 23

**Deprecated since:** -1

<!--Device-i18n-export class ZoneOffsetTransition--><!--Device-i18n-export class ZoneOffsetTransition-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getMilliseconds

```TypeScript
public getMilliseconds(): number
```

Obtains the timestamp of the time zone transition point.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneOffsetTransition-public getMilliseconds(): double--><!--Device-ZoneOffsetTransition-public getMilliseconds(): double-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getOffsetAfter

```TypeScript
public getOffsetAfter(): number
```

Obtains the offset after the time zone transition.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneOffsetTransition-public getOffsetAfter(): int--><!--Device-ZoneOffsetTransition-public getOffsetAfter(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getOffsetBefore

```TypeScript
public getOffsetBefore(): number
```

Obtains the offset before the time zone transition.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ZoneOffsetTransition-public getOffsetBefore(): int--><!--Device-ZoneOffsetTransition-public getOffsetBefore(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
