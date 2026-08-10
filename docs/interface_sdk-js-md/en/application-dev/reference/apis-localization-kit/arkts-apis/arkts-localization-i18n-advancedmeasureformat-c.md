# AdvancedMeasureFormat

提供数字格式化能力，支持根据单位使用场景自动转换合适的单位。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class AdvancedMeasureFormat--><!--Device-i18n-export class AdvancedMeasureFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(numberFormat: Intl.NumberFormat, options?: AdvancedMeasureFormatOptions)
```

创建数字格式化对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AdvancedMeasureFormat-constructor(numberFormat: Intl.NumberFormat, options?: AdvancedMeasureFormatOptions)--><!--Device-AdvancedMeasureFormat-constructor(numberFormat: Intl.NumberFormat, options?: AdvancedMeasureFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| numberFormat | Intl.NumberFormat | Yes | 用于格式化数字的对象。 |
| options | [AdvancedMeasureFormatOptions](arkts-localization-i18n-advancedmeasureformatoptions-i.md) | No |  |

## format

```TypeScript
format(num: double): string
```

对数字进行格式化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AdvancedMeasureFormat-format(num: double): string--><!--Device-AdvancedMeasureFormat-format(num: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| num | double | Yes | 需要格式化的数字。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 格式化后的文本。 |

