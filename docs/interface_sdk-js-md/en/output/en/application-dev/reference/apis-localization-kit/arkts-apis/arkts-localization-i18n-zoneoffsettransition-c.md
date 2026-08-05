# ZoneOffsetTransition

Provides the API for obtaining a timezone transition information.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-i18n-export class ZoneOffsetTransition--><!--Device-i18n-export class ZoneOffsetTransition-End-->

**System capability:** SystemCapability.Global.I18n

## getMilliseconds

ArkTS-Dyn:
```TypeScript
public getMilliseconds(): number
```

ArkTS-Sta:
```TypeScript
public getMilliseconds(): double
```

Obtains the timestamp of the time zone transition point.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ZoneOffsetTransition-public getMilliseconds(): double--><!--Device-ZoneOffsetTransition-public getMilliseconds(): double-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Timestamp of the time zone transition point. It is measured as the number of milliseconds |

## getOffsetAfter

ArkTS-Dyn:
```TypeScript
public getOffsetAfter(): number
```

ArkTS-Sta:
```TypeScript
public getOffsetAfter(): int
```

Obtains the offset after the time zone transition.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ZoneOffsetTransition-public getOffsetAfter(): int--><!--Device-ZoneOffsetTransition-public getOffsetAfter(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Post-transition offset, that is, the time difference between the post-transition time and UTC, |

## getOffsetBefore

ArkTS-Dyn:
```TypeScript
public getOffsetBefore(): number
```

ArkTS-Sta:
```TypeScript
public getOffsetBefore(): int
```

Obtains the offset before the time zone transition.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ZoneOffsetTransition-public getOffsetBefore(): int--><!--Device-ZoneOffsetTransition-public getOffsetBefore(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Pre-transition offset, that is, the time difference between the pre-transition time and UTC, |

