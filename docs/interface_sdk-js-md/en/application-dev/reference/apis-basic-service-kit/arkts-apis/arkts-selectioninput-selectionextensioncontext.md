# @ohos.selectionInput.SelectionExtensionContext(Word Selection Extension Context)

## Modules to Import

```TypeScript
import { SelectionExtensionContext } from '@kit.BasicServicesKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [SelectionExtensionContext](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md) | **SelectionExtensionContext** is the context of  [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md#SelectionExtensionAbility), which inherits from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md#ExtensionContext).  When a **SelectionExtensionAbility** component is instantiated, the system automatically creates the corresponding  **SelectionExtensionContext**. You can call the [startAbility](#startability) API in **SelectionExtensionContext** to start other abilities in the same app. This is applicable when you need to redirect to another ability in the same app in word selection extension, helping users quickly obtain the functions or information associated with the selected word.  > **NOTE：** >  > - This module is supported only on PCs/2-in-1 devices. You can use > **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports this > function. |

