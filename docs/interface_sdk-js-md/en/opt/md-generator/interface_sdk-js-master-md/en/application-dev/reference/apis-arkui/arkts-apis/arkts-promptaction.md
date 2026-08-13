# @ohos.promptAction

This module provides API for creating and displaying toasts, dialog boxes, and action menus. > **NOTE：**> > - This module cannot be used in the file declaration of the [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility). In > other words, the APIs of this module can be used only after a component instance is created; they cannot be called > in the lifecycle of the UIAbility. > > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used > where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext). It is recommended that you use the dialog box APIs provided by > **UIContext**&lt;!--Del--&gt;, except for UI-less scenarios such as > [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)&lt;!--DelEnd--&gt;.

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [promptAction](arkts-arkui-promptaction-n.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DismissDialogAction](arkts-arkui-promptaction-dismissdialogaction-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md) |
| [LevelMode](arkts-arkui-promptaction-levelmode-e.md) |
