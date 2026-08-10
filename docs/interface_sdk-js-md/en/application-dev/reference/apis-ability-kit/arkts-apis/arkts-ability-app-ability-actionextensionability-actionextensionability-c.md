# ActionExtensionAbility

ActionExtensionAbility是为开发者提供的自定义操作业务模板，继承自  
[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)。

开发者通过实现ActionExtensionAbility，为其他应用提供内容查看与处理功能。例如，开发者使用ActionExtensionAbility实现了文本翻译功能。其他应用可以通过调用该ActionExtensionAbility来处理需要翻译的内容，并获取到处理后的翻译内容。

各类Ability的继承关系详见[继承关系说明](../../../reference/apis-ability-kit/js-apis-app-ability-ability.md#ability的继承关系说明)。

**Inheritance/Implementation:** ActionExtensionAbility extends [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export default class ActionExtensionAbility extends UIExtensionAbility--><!--Device-unnamed-export default class ActionExtensionAbility extends UIExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { ActionExtensionAbility } from 'kits/@kit.AbilityKit';
```

