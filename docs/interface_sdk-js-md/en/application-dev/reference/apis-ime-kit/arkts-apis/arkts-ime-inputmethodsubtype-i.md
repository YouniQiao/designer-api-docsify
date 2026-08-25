# InputMethodSubtype

The **InputMethodSubtype** module provides APIs for managing the attributes of input method subtypes. The input method subtype allows the input method to switch to a specific mode or language, for example, the Chinese or English keyboard. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; &gt;The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';
```

## extra

```TypeScript
extra?: object
```

Extra information of the input method subtype. <br> <br> **NOTE：**<br> <br> - This parameter is optional since API version 10. <br> - This parameter is reserved and currently has no specific meaning.

**Type:** object

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## icon

```TypeScript
readonly icon?: string
```

Optional. Icon of the input method subtype. It can be obtained by using **iconId**. This parameter is reserved.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## iconId

```TypeScript
readonly iconId?: double
```

Optional. Icon ID of the input method subtype.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## id

```TypeScript
readonly id: string
```

Mandatory. ID of the input method subtype.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## label

```TypeScript
readonly label?: string
```

Optional. Label of the input method subtype.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## labelId

```TypeScript
readonly labelId?: double
```

Optional. Label ID of the input method subtype.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## language

```TypeScript
readonly language: string
```

Mandatory. Language of the input method subtype.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## locale

```TypeScript
readonly locale: string
```

Mandatory. Locale of the input method subtype.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## mode

```TypeScript
readonly mode?: 'upper' | 'lower'
```

Optional. Mode of the input method subtype, including **upper** (uppercase) and **lower** (lowercase).

**Type:** 'upper' \| 'lower'

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## name

```TypeScript
readonly name: string
```

Mandatory. Bundle name of the application to which the input method subtype belongs.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework
