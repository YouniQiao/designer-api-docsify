# InputAttribute

**起始版本：** 23

<!--Device-inputMethod-export interface InputAttribute--><!--Device-inputMethod-export interface InputAttribute-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## abilityName

```TypeScript
abilityName?: string
```

**类型：** string

**起始版本：** 23

<!--Device-InputAttribute-abilityName?: string--><!--Device-InputAttribute-abilityName?: string-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## consumeKeyEvents

```TypeScript
consumeKeyEvents?: boolean
```

**类型：** boolean

**默认值：** false

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputAttribute-consumeKeyEvents?: boolean--><!--Device-InputAttribute-consumeKeyEvents?: boolean-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## enterKeyType

```TypeScript
enterKeyType: EnterKeyType
```

**类型：** EnterKeyType

**起始版本：** 23

<!--Device-InputAttribute-enterKeyType: EnterKeyType--><!--Device-InputAttribute-enterKeyType: EnterKeyType-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## placeholder

```TypeScript
placeholder?: string
```

**类型：** string

**起始版本：** 23

<!--Device-InputAttribute-placeholder?: string--><!--Device-InputAttribute-placeholder?: string-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## textInputType

```TypeScript
textInputType: TextInputType
```

**类型：** [TextInputType](arkts-ime-inputmethod-textinputtype-e.md)

**起始版本：** 23

<!--Device-InputAttribute-textInputType: TextInputType--><!--Device-InputAttribute-textInputType: TextInputType-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

