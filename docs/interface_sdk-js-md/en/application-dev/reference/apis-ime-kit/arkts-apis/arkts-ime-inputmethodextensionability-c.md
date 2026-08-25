# InputMethodExtensionAbility

The **InputMethodExtensionAbility** module provides APIs for developing input methods and managing the lifecycle of input method extensions.   
> **NOTE：**
   
> 
   
> The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version. The APIs of this module can be used only in the stage model.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { InputMethodExtensionAbility } from 'kits/@kit.IMEKit';
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called when the **InputMethodExtensionAbility** is started to implement initialization.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## onDestroy

```TypeScript
onDestroy(): void
```

Called when this **InputMethodExtensionAbility** is destroyed to clear resources.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## context

```TypeScript
context: InputMethodExtensionContext
```

Context of the **InputMethodExtension**, which is inherited from **ExtensionContext**.

**Type:** [InputMethodExtensionContext](arkts-ime-inputmethodextensioncontext-c.md)

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework
