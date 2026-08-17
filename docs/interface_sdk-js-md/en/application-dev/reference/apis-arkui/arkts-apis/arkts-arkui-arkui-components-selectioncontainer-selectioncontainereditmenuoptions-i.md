# SelectionContainerEditMenuOptions

Defines custom edit menu options for SelectionContainer.

**Since:** 26.0.0

<!--Device-unnamed-export interface SelectionContainerEditMenuOptions--><!--Device-unnamed-export interface SelectionContainerEditMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OnMenuItemClickWithTextCallback } from 'OnMenuItemClickWithTextCallback';
import { SelectionContainer } from 'SelectionContainer';
import { SelectionContainerAttribute } from 'SelectionContainerAttribute';
import { SelectionContainerEditMenuOptions } from 'SelectionContainerEditMenuOptions';
import { SelectionContainerInstance } from 'SelectionContainerInstance';
import { SelectionContainerMenuOptions } from 'SelectionContainerMenuOptions';
import { SelectionContainerTextJoinStyle } from 'SelectionContainerTextJoinStyle';
import { SelectionContainerOptions } from 'SelectionContainerOptions';
import { SelectionContainerController } from 'SelectionContainerController';
```

## onCreateMenu

```TypeScript
onCreateMenu?: OnCreateMenuCallback
```

Passes the default menu, invokes before every display to generate a menu for triggering click events.

**Type:** OnCreateMenuCallback

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SelectionContainerEditMenuOptions-onCreateMenu?: OnCreateMenuCallback--><!--Device-SelectionContainerEditMenuOptions-onCreateMenu?: OnCreateMenuCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMenuItemClick

```TypeScript
onMenuItemClick?: OnMenuItemClickWithTextCallback
```

Invoked upon clicking an item, capable of intercepting the default system menu execution behavior.

**Type:** [OnMenuItemClickWithTextCallback](arkts-arkui-onmenuitemclickwithtextcallback-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SelectionContainerEditMenuOptions-onMenuItemClick?: OnMenuItemClickWithTextCallback--><!--Device-SelectionContainerEditMenuOptions-onMenuItemClick?: OnMenuItemClickWithTextCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPrepareMenu

```TypeScript
onPrepareMenu?: OnPrepareMenuCallback
```

Callback before displaying the menu when the selection text changes.

**Type:** OnPrepareMenuCallback

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SelectionContainerEditMenuOptions-onPrepareMenu?: OnPrepareMenuCallback--><!--Device-SelectionContainerEditMenuOptions-onPrepareMenu?: OnPrepareMenuCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

