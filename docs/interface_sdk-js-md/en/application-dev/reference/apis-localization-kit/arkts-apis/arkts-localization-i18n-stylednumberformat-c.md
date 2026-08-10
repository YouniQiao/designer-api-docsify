# StyledNumberFormat

提供富文本数字格式化的能力。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class StyledNumberFormat--><!--Device-i18n-export class StyledNumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)
```

创建需要富文本显示的数字格式化的对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-StyledNumberFormat-constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)--><!--Device-StyledNumberFormat-constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| numberFormat | Intl.NumberFormat \| SimpleNumberFormat | Yes | 用于格式化数字的对象。 |
| options | [StyledNumberFormatOptions](arkts-localization-i18n-stylednumberformatoptions-i.md) | No | 指定数字格式化对象的配置项。默认值：默认的文本样式。 |

## format

```TypeScript
format(value: double): StyledString
```

使用数字格式化对象对数字进行格式化，返回富文本对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-StyledNumberFormat-format(value: double): StyledString--><!--Device-StyledNumberFormat-format(value: double): StyledString-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 需要格式化的数字。 |

**Return value:**

| Type | Description |
| --- | --- |
| [StyledString](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-c.md) | 格式化后的富文本对象。 |

