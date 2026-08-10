# InputAttribute

编辑框属性，包含文本输入类型和Enter键功能类型。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputMethod-export interface InputAttribute--><!--Device-inputMethod-export interface InputAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## abilityName

```TypeScript
abilityName?: string
```

编辑框设置的ability名称。

- 编辑框设置ability名称时，长度不超过127个字符（如果超出将会自动截断为127个字符）。  
- 编辑框未设置ability名称时，默认为空字符串。  
- 该字段在调用绑定  
[attach](arkts-ime-inputmethod-inputmethodcontroller-i.md#attach)时提供给输入法应用。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-InputAttribute-abilityName?: string--><!--Device-InputAttribute-abilityName?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## consumeKeyEvents

```TypeScript
consumeKeyEvents?: boolean
```

编辑框是否具有完整处理字母、字符、功能等按键的能力。默认值为false。

- 值为true，表示具备此能力。  
- 值为false，表示不具备此能力。  
- 该字段在调用  
[attach](arkts-ime-inputmethod-inputmethodcontroller-i.md#attach)/ [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md)时提供给输入法应用。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputAttribute-consumeKeyEvents?: boolean--><!--Device-InputAttribute-consumeKeyEvents?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## enterKeyType

```TypeScript
enterKeyType: EnterKeyType
```

Enter键功能类型。

**Type:** [EnterKeyType](../../apis-arkui/arkts-apis/arkts-arkui-textinput-enterkeytype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputAttribute-enterKeyType: EnterKeyType--><!--Device-InputAttribute-enterKeyType: EnterKeyType-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## placeholder

```TypeScript
placeholder?: string
```

编辑框设置的占位符信息。 

- 编辑框设置占位符信息时，长度不超过255个字符（如果超出将会自动截断为255个字符），用于提示或引导用户输入临时性文本或符号。（例如：提示输入项为"必填"或"非必填"的输入结果反馈。）  
- 编辑框没有设置占位符信息时，默认为空字符串。  
- 该字段在调用  
[attach](arkts-ime-inputmethod-inputmethodcontroller-i.md#attach)时提供给输入法应用。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-InputAttribute-placeholder?: string--><!--Device-InputAttribute-placeholder?: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## textInputType

```TypeScript
textInputType: TextInputType
```

文本输入类型。

**Type:** [TextInputType](arkts-ime-inputmethod-textinputtype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputAttribute-textInputType: TextInputType--><!--Device-InputAttribute-textInputType: TextInputType-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

