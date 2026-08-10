# Parameter (System API)

无障碍节点元素执行特定操作时，为操作提供具体设置的参数值。详见[AccessibilityAction](../../apis-arkui/arkts-apis/arkts-arkui-common-accessibilityaction-e.md/arkts-arkui-common-accessibilityaction-e.md)（无障碍节点元素可执行的操作）。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class Parameter--><!--Device-unnamed-export declare class Parameter-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityFocusScene

```TypeScript
accessibilityFocusScene?: AccessibilityFocusScene
```

Indicates the scene for AccessibilityAction.ACCESSIBILITY_FOCUS.

**Type:** [AccessibilityFocusScene](arkts-accessibility-accessibility-accessibilityfocusscene-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Parameter-accessibilityFocusScene?: AccessibilityFocusScene--><!--Device-Parameter-accessibilityFocusScene?: AccessibilityFocusScene-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## customAction

```TypeScript
customAction?: string
```

Indicates the action for AccessibilityAction.EXECUTE_CUSTOM_ACTION.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Parameter-customAction?: string--><!--Device-Parameter-customAction?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## injectActionType

```TypeScript
injectActionType?: InjectActionType
```

设置注入的动作。

**Type:** [InjectActionType](arkts-accessibility-accessibility-injectactiontype-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Parameter-injectActionType?: InjectActionType--><!--Device-Parameter-injectActionType?: InjectActionType-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## offset

```TypeScript
offset?: string
```

设置光标的偏移量，如：'1'。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Parameter-offset?: string--><!--Device-Parameter-offset?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## scrollType

```TypeScript
scrollType?: string
```

组件滚动类型，包括'fullScreen'（全屏）和'halfScreen'（半屏）。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Parameter-scrollType?: string--><!--Device-Parameter-scrollType?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## selectTextBegin

```TypeScript
selectTextBegin?: string
```

选定组件内文本时的起始坐标，如：'2'。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Parameter-selectTextBegin?: string--><!--Device-Parameter-selectTextBegin?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## selectTextEnd

```TypeScript
selectTextEnd?: string
```

选定组件内文本时的结束坐标，如：'8'。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Parameter-selectTextEnd?: string--><!--Device-Parameter-selectTextEnd?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## selectTextInForWard

```TypeScript
selectTextInForWard?: boolean
```

表示选定组件内文本时是否向前选择。true表示向前选择，false表示不向前选择。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Parameter-selectTextInForWard?: boolean--><!--Device-Parameter-selectTextInForWard?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## setText

```TypeScript
setText?: string
```

设置组件文本时文本内容。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Parameter-setText?: string--><!--Device-Parameter-setText?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## spanId

```TypeScript
spanId?: string
```

对超链接文本进行点击操作时文本编号。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Parameter-spanId?: string--><!--Device-Parameter-spanId?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

