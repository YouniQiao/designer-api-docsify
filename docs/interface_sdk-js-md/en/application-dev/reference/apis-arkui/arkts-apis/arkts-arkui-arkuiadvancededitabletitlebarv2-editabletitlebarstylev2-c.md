# EditableTitleBarStyleV2

Declaration of the title bar style configuration.

**Since:** 26.0.0

<!--Device-unnamed-export declare class EditableTitleBarStyleV2--><!--Device-unnamed-export declare class EditableTitleBarStyleV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { EditableLeftIconTypeV2, EditableTitleBarV2, EditableLeftIconV2, EditableLeftIconV2Options, EditableTitleV2, EditableTitleV2Options, EditableTitleBarItemV2, EditableTitleBarItemV2Options, EditableTitleBarMenuItemV2, EditableTitleBarMenuItemV2Options, EditableSaveButtonV2, EditableSaveButtonV2Options, EditableTitleBarStyleV2, EditableTitleBarStyleV2Options } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: EditableTitleBarStyleV2Options)
```

Constructor of EditableTitleBarStyleV2.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleBarStyleV2-constructor(options?: EditableTitleBarStyleV2Options)--><!--Device-EditableTitleBarStyleV2-constructor(options?: EditableTitleBarStyleV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EditableTitleBarStyleV2Options](../../apis-default/arkts-apis/arkts-arkuiadvancededitabletitlebarv2-editabletitlebarstylev2options-i.md) | No | The style options of the title bar |

## backgroundBlurStyle

```TypeScript
@Trace
  public backgroundBlurStyle?: BlurStyle
```

Background blur style.

**Type:** BlurStyle

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleBarStyleV2-@Trace  public backgroundBlurStyle?: BlurStyle--><!--Device-EditableTitleBarStyleV2-@Trace  public backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
@Trace
  public backgroundColor?: ResourceColor
```

Background color.

**Type:** ResourceColor

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleBarStyleV2-@Trace  public backgroundColor?: ResourceColor--><!--Device-EditableTitleBarStyleV2-@Trace  public backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentMargin

```TypeScript
@Trace
  public contentMargin?: LocalizedMargin
```

Content margin, supports RTL layout.

**Type:** LocalizedMargin

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleBarStyleV2-@Trace  public contentMargin?: LocalizedMargin--><!--Device-EditableTitleBarStyleV2-@Trace  public contentMargin?: LocalizedMargin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## safeAreaEdges

```TypeScript
@Trace
  public safeAreaEdges?: Array<SafeAreaEdge>
```

Indicates the edges of the safe area.

**Type:** Array&lt;SafeAreaEdge&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleBarStyleV2-@Trace  public safeAreaEdges?: Array<SafeAreaEdge>--><!--Device-EditableTitleBarStyleV2-@Trace  public safeAreaEdges?: Array<SafeAreaEdge>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## safeAreaTypes

```TypeScript
@Trace
  public safeAreaTypes?: Array<SafeAreaType>
```

Indicates the types of the safe area.

**Type:** Array&lt;SafeAreaType&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleBarStyleV2-@Trace  public safeAreaTypes?: Array<SafeAreaType>--><!--Device-EditableTitleBarStyleV2-@Trace  public safeAreaTypes?: Array<SafeAreaType>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

