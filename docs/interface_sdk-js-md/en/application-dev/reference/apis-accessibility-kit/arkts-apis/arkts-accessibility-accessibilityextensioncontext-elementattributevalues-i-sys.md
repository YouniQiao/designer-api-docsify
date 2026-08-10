# ElementAttributeValues

节点元素具备的属性名称及属性值类型信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-export interface ElementAttributeValues--><!--Device-unnamed-export interface ElementAttributeValues-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## accessibilityStateDescription

```TypeScript
accessibilityStateDescription?: string
```

元素的自定义无障碍状态播报文本信息。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-accessibilityStateDescription?: string--><!--Device-ElementAttributeValues-accessibilityStateDescription?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## accessibilityVisible

```TypeScript
accessibilityVisible?: boolean
```

表示元素是否是无障碍可见的。true表示元素是无障碍可见的，false表示元素是无障碍不可见的，默认值为true。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-accessibilityVisible?: boolean--><!--Device-ElementAttributeValues-accessibilityVisible?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## belongTreeId

```TypeScript
belongTreeId?: int
```

表示元素所属的组件树ID。默认值为-1。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-belongTreeId?: int--><!--Device-ElementAttributeValues-belongTreeId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## childrenIds

```TypeScript
childrenIds?: Array<long>
```

表示元素的子组件ID。

**Type:** Array&lt;long&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-childrenIds?: Array<long>--><!--Device-ElementAttributeValues-childrenIds?: Array<long>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## childrenTreeId

```TypeScript
childrenTreeId?: int
```

表示元素的子组件树ID。默认值为-1。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-childrenTreeId?: int--><!--Device-ElementAttributeValues-childrenTreeId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## currentItem

```TypeScript
currentItem?: AccessibilityGrid
```

表示当前元素所在网格中的位置。

**Type:** [AccessibilityGrid](arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-currentItem?: AccessibilityGrid--><!--Device-ElementAttributeValues-currentItem?: AccessibilityGrid-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## customActions

```TypeScript
customActions?: Array<string>
```

Indicates the custom actions supported by the component.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-customActions?: Array<string>--><!--Device-ElementAttributeValues-customActions?: Array<string>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## isEssential

```TypeScript
isEssential?: boolean
```

表示元素对用户是否是必需的。true表示元素是必需的，false表示元素不是必需的，默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-isEssential?: boolean--><!--Device-ElementAttributeValues-isEssential?: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## mainWindowId

```TypeScript
mainWindowId?: int
```

表示元素的主窗口ID。默认值为-1。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-mainWindowId?: int--><!--Device-ElementAttributeValues-mainWindowId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## navDestinationId

```TypeScript
navDestinationId?: long
```

表示元素所关联的导航目标ID。默认值为-1。

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-navDestinationId?: long--><!--Device-ElementAttributeValues-navDestinationId?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## parentId

```TypeScript
parentId?: long
```

表示元素的父组件ID。默认值为-1。

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-parentId?: long--><!--Device-ElementAttributeValues-parentId?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## span

```TypeScript
span?: AccessibilitySpan[]
```

表示元素在网格布局中所跨越的行列范围数组。

**Type:** [AccessibilitySpan](arkts-accessibility-accessibilityextensioncontext-accessibilityspan-i-sys.md)[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ElementAttributeValues-span?: AccessibilitySpan[]--><!--Device-ElementAttributeValues-span?: AccessibilitySpan[]-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

