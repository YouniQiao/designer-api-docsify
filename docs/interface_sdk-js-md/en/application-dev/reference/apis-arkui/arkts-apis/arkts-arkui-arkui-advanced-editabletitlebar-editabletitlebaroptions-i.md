# EditableTitleBarOptions

Indicates the options of the editable title bar.

**Since:** 12

<!--Device-unnamed-export declare interface EditableTitleBarOptions--><!--Device-unnamed-export declare interface EditableTitleBarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { EditableTitleBarOptions, EditableTitleBarMenuItem, EditableTitleBarItem, EditableLeftIconType, EditableTitleBar } from '@kit.ArkUI';
```

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the title bar.

Default value: **BlurStyle.NONE**

**Type:** BlurStyle

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EditableTitleBarOptions-backgroundBlurStyle?: BlurStyle--><!--Device-EditableTitleBarOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the title bar.

Default value: **'#00000000'**

**Type:** ResourceColor

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EditableTitleBarOptions-backgroundColor?: ResourceColor--><!--Device-EditableTitleBarOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## safeAreaEdges

```TypeScript
safeAreaEdges?: Array<SafeAreaEdge>
```

Edges for expanding the safe area.

Default value: **[SafeAreaEdge.TOP]**

**Type:** Array&lt;SafeAreaEdge&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EditableTitleBarOptions-safeAreaEdges?: Array<SafeAreaEdge>--><!--Device-EditableTitleBarOptions-safeAreaEdges?: Array<SafeAreaEdge>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## safeAreaTypes

```TypeScript
safeAreaTypes?: Array<SafeAreaType>
```

Types of the expanded safe areas.

Default value: **[SafeAreaType.SYSTEM]**

**Type:** Array&lt;SafeAreaType&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EditableTitleBarOptions-safeAreaTypes?: Array<SafeAreaType>--><!--Device-EditableTitleBarOptions-safeAreaTypes?: Array<SafeAreaType>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

