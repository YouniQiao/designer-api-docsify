# InterstitialDialogAction

The **InterstitialDialogAction** component is a dialog box used in atomic services to temporarily display information that requires user attention or actions to be taken while maintaining the current context. Users can trigger corresponding actions by clicking different areas of the dialog box.

**Since:** 12

<!--Device-unnamed-export declare class InterstitialDialogAction--><!--Device-unnamed-export declare class InterstitialDialogAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IconStyle, TitlePosition, BottomOffset, InterstitialDialogAction } from 'kits/@kit.ArkUI';
```

## closeDialog

```TypeScript
closeDialog(): void
```

Closes the dialog box.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InterstitialDialogAction-closeDialog(): void--><!--Device-InterstitialDialogAction-closeDialog(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(dialogOptions: DialogOptions)
```

A constructor used to create an **InterstitialDialogAction** instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InterstitialDialogAction-constructor(dialogOptions: DialogOptions)--><!--Device-InterstitialDialogAction-constructor(dialogOptions: DialogOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dialogOptions | [DialogOptions](arkts-arkui-atomicservice-interstitialdialogaction-dialogoptions-i.md) | Yes |

## openDialog

```TypeScript
openDialog(): void
```

Opens the dialog box.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InterstitialDialogAction-openDialog(): void--><!--Device-InterstitialDialogAction-openDialog(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
