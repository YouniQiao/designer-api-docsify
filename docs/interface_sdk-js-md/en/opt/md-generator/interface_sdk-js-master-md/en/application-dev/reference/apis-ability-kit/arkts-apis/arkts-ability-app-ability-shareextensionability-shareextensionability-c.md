# ShareExtensionAbility

ShareExtensionAbility provides extended capabilities for integrating a share details page. It inherits from [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility). By implementing ShareExtensionAbility, you can process content shared from other applications. For example, you could use ShareExtensionAbility to implement the text sharing feature. When a user initiates a share action in another application, your application will appear as an option in the system share panel. Upon selection, the system activates your application to process the content and display the share detail page. For details about the inheritance relationship of each ability, see Inheritance Relationship .

**Inheritance/Implementation:** ShareExtensionAbility extends [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility)

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export default class ShareExtensionAbility--><!--Device-unnamed-export default class ShareExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { ShareExtensionAbility } from '@kit.AbilityKit';
```
