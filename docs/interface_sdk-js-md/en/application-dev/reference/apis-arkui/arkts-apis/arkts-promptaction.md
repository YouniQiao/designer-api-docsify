# @ohos.promptAction

This module provides API for creating and displaying toasts, dialog boxes, and action menus. > **NOTE：**> > - This module cannot be used in the file declaration of the [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility). In > other words, the APIs of this module can be used only after a component instance is created; they cannot be called > in the lifecycle of the UIAbility. > > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used > where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext). It is recommended that you use the dialog box APIs provided by > **UIContext**&lt;!--Del--&gt;, except for UI-less scenarios such as > [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)&lt;!--DelEnd--&gt;.

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [promptAction](arkts-arkui-promptaction-n.md) | This module provides API for creating and displaying toasts, dialog boxes, and action menus. > **NOTE：**> > - This module cannot be used in the file declaration of the [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility). In > other words, the APIs of this module can be used only after a component instance is created; they cannot be called > in the lifecycle of the UIAbility. > > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used > where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext). It is recommended that you use the dialog box APIs provided by > **UIContext**&lt;!--Del--&gt;, except for UI-less scenarios such as > [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)&lt;!--DelEnd--&gt;. |

### Classes

| Name | Description |
| --- | --- |
| [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) | Defines the display order of a dialog box. |

### Interfaces

| Name | Description |
| --- | --- |
| [DismissDialogAction](arkts-arkui-promptaction-dismissdialogaction-i.md) | Provides information about the action to dismiss the dialog box. |

### Enums

| Name | Description |
| --- | --- |
| [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md) | Enumerates the display area modes of the dialog box overlay within a page. |
| [LevelMode](arkts-arkui-promptaction-levelmode-e.md) | Enumerates the display level modes of the dialog box. |

