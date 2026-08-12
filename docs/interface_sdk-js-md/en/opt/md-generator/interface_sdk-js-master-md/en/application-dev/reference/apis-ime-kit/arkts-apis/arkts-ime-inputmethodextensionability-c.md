# InputMethodExtensionAbility

The **InputMethodExtensionAbility** module provides APIs for developing input methods and managing the lifecycle of input method extensions.

> **NOTE：**
> 
> - The APIs of this module can be used only in the stage model.

**Since:** 9

<!--Device-unnamed-declare class InputMethodExtensionAbility--><!--Device-unnamed-declare class InputMethodExtensionAbility-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { InputMethodExtensionAbility } from '@kit.IMEKit';
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called when the **InputMethodExtensionAbility** is started to implement initialization.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionAbility-onCreate(want: Want): void--><!--Device-InputMethodExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## Examples

```TypeScript
import { InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    console.info('onCreate, want:' + want.abilityName);
  }
}
```

## onDestroy

```TypeScript
onDestroy(): void
```

Called when this **InputMethodExtensionAbility** is destroyed to clear resources.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionAbility-onDestroy(): void--><!--Device-InputMethodExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Examples

```TypeScript
import { InputMethodExtensionAbility } from '@kit.IMEKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onDestroy(): void {
    console.info('onDestroy');
  }
}
```

## context

```TypeScript
context: InputMethodExtensionContext
```

Context of the **InputMethodExtension**, which is inherited from **ExtensionContext**.

**Type:** [InputMethodExtensionContext](arkts-ime-inputmethodextensioncontext-c.md)

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodExtensionAbility-context: InputMethodExtensionContext--><!--Device-InputMethodExtensionAbility-context: InputMethodExtensionContext-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework
