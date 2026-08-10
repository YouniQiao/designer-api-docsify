# EditableTitleBarStyleV2Options

标题栏样式配置选项接口。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface EditableTitleBarStyleV2Options--><!--Device-unnamed-export declare interface EditableTitleBarStyleV2Options-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { EditableSaveButtonV2, EditableTitleBarStyleV2Options, EditableTitleBarStyleV2, EditableTitleBarItemV2, EditableLeftIconV2Options, EditableTitleBarMenuItemV2, EditableTitleBarV2, EditableTitleBarMenuItemV2Options, EditableSaveButtonV2Options, EditableTitleBarItemV2Options, EditableTitleV2Options, EditableTitleV2, EditableLeftIconV2, EditableLeftIconTypeV2 } from 'kits/@kit.ArkUI';
```

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

标题栏背景模糊样式。

默认值：BlurStyle.NONE，表示无模糊效果。

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarStyleV2Options-backgroundBlurStyle?: BlurStyle--><!--Device-EditableTitleBarStyleV2Options-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

标题栏背景色。

默认值：'#00000000'，表示背景透明。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarStyleV2Options-backgroundColor?: ResourceColor--><!--Device-EditableTitleBarStyleV2Options-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentMargin

```TypeScript
contentMargin?: LocalizedMargin
```

标题栏外边距，不支持设置负数。

默认值：

{

start: LengthMetrics.resource(\$r('sys.float.margin_left')),

end: LengthMetrics.resource(\$r('sys.float.margin_right'))

}。

**Type:** [LocalizedMargin](arkts-arkui-localizedmargin-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarStyleV2Options-contentMargin?: LocalizedMargin--><!--Device-EditableTitleBarStyleV2Options-contentMargin?: LocalizedMargin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## safeAreaEdges

```TypeScript
safeAreaEdges?: Array<SafeAreaEdge>
```

扩展安全区域的方向。

默认值：[SafeAreaEdge.TOP]。

**Type:** Array&lt;[SafeAreaEdge](../arkts-components/arkts-arkui-safeareaedge-e.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarStyleV2Options-safeAreaEdges?: Array<SafeAreaEdge>--><!--Device-EditableTitleBarStyleV2Options-safeAreaEdges?: Array<SafeAreaEdge>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## safeAreaTypes

```TypeScript
safeAreaTypes?: Array<SafeAreaType>
```

扩展安全区域的类型。

默认值：[SafeAreaType.SYSTEM]。

**Type:** Array&lt;[SafeAreaType](../arkts-components/arkts-arkui-safeareatype-e.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarStyleV2Options-safeAreaTypes?: Array<SafeAreaType>--><!--Device-EditableTitleBarStyleV2Options-safeAreaTypes?: Array<SafeAreaType>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

