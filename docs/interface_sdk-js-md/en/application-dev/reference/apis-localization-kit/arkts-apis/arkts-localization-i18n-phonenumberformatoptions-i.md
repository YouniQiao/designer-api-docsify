# PhoneNumberFormatOptions

电话号码格式化时可设置的配置项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export interface PhoneNumberFormatOptions--><!--Device-i18n-export interface PhoneNumberFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## type

```TypeScript
type?: string
```

表示对电话号码格式化的类型，取值包括：'E164', 'INTERNATIONAL', 'NATIONAL', 'RFC3966', 'TYPING'。

-在API version 8版本，type为必填项。 

-API version 9版本开始，type为选填项。

-API version 12版本开始支持TYPING，表示对拨号中的电话号码实时格式化。

-API version 23版本开始，TYPING支持实时获取拨号中的电话号码的归属地。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhoneNumberFormatOptions-type?: string--><!--Device-PhoneNumberFormatOptions-type?: string-End-->

**System capability:** SystemCapability.Global.I18n

