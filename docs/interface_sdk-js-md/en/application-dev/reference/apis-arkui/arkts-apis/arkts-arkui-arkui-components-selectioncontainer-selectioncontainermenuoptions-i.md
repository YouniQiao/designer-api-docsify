# SelectionContainerMenuOptions

Defines selection menu options for SelectionContainer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export interface SelectionContainerMenuOptions--><!--Device-unnamed-export interface SelectionContainerMenuOptions-End-->

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

## onAppear

```TypeScript
onAppear?: Callback<string>
```

Called when the selection menu appears. The callback parameter is the selected text concatenated in the visual order of Text components.

**Type:** Callback&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SelectionContainerMenuOptions-onAppear?: Callback<string>--><!--Device-SelectionContainerMenuOptions-onAppear?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDisappear

```TypeScript
onDisappear?: Callback<void>
```

Called when the selection menu disappears.

**Type:** Callback&lt;void&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SelectionContainerMenuOptions-onDisappear?: Callback<void>--><!--Device-SelectionContainerMenuOptions-onDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMenuHide

```TypeScript
onMenuHide?: Callback<string>
```

Called when the selection menu is hidden. The callback parameter is the selected text concatenated in the visual order of Text components.

**Type:** Callback&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SelectionContainerMenuOptions-onMenuHide?: Callback<string>--><!--Device-SelectionContainerMenuOptions-onMenuHide?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMenuShow

```TypeScript
onMenuShow?: Callback<string>
```

Called when the selection menu is displayed. The callback parameter is the selected text concatenated in the visual order of Text components.

**Type:** Callback&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SelectionContainerMenuOptions-onMenuShow?: Callback<string>--><!--Device-SelectionContainerMenuOptions-onMenuShow?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

