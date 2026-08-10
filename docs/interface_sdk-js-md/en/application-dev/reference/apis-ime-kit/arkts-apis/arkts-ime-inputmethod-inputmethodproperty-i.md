# InputMethodProperty

输入法应用属性。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-inputMethod-interface InputMethodProperty--><!--Device-inputMethod-interface InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## enabledState

```TypeScript
readonly enabledState?: EnabledState
```

非必填。

- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展  
- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod)），此字段表示该输入法启用状  
态。

**Type:** [EnabledState](arkts-ime-inputmethod-enabledstate-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-InputMethodProperty-readonly enabledState?: EnabledState--><!--Device-InputMethodProperty-readonly enabledState?: EnabledState-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## extra

```TypeScript
extra?: object
```

输入法扩展信息。

- API version 10起：非必填；  
- API version 9：必填。

**Type:** object

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodProperty-extra?: object--><!--Device-InputMethodProperty-extra?: object-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## icon

```TypeScript
readonly icon?: string
```

非必填。

- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。  
- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod)），此字段表示输入法图标数  
据，可以通过iconId查询获取。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodProperty-readonly icon?: string--><!--Device-InputMethodProperty-readonly icon?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## iconId

```TypeScript
readonly iconId?: long
```

非必填。

- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。  
- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod)），此字段表示icon字段的  
资源号。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodProperty-readonly iconId?: long--><!--Device-InputMethodProperty-readonly iconId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## id

```TypeScript
readonly id: string
```

必填。输入法扩展在应用内唯一标识，与name一起组成输入法扩展的全局唯一标识。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodProperty-readonly id: string--><!--Device-InputMethodProperty-readonly id: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## label

```TypeScript
readonly label?: string
```

非必填。

- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。  
- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod)），此字段表示输入法扩展对外  
显示的名称，优先使用InputMethodExtensionAbility中配置的label，若未配置，自动使用应用入口ability的label；当应用入口ability未配置label时，自动使用应用AppScope中配置的label。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodProperty-readonly label?: string--><!--Device-InputMethodProperty-readonly label?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## labelId

```TypeScript
readonly labelId?: long
```

非必填。

- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。  
- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod)），此字段表示label字段  
的资源号。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputMethodProperty-readonly labelId?: long--><!--Device-InputMethodProperty-readonly labelId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## methodId

```TypeScript
readonly methodId: string
```

输入法唯一标识。必填。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inputMethod.InputMethodProperty#id](arkts-ime-inputmethod-inputmethodproperty-i.md#id)

<!--Device-InputMethodProperty-readonly methodId: string--><!--Device-InputMethodProperty-readonly methodId: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## name

```TypeScript
readonly name: string
```

必填。输入法包名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputMethodProperty-readonly name: string--><!--Device-InputMethodProperty-readonly name: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## packageName

```TypeScript
readonly packageName: string
```

输入法包名。必填。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inputMethod.InputMethodProperty#name](arkts-ime-inputmethod-inputmethodproperty-i.md#name)

<!--Device-InputMethodProperty-readonly packageName: string--><!--Device-InputMethodProperty-readonly packageName: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

