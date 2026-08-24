# CustomComponent

Custom Component@extends CommonAttribute [since 7 - 17] @extends BaseCustomComponent [since 18]

**Inheritance/Implementation:** CustomComponent extends [BaseCustomComponent](arkts-arkui-basecustomcomponent-c.md)

**Since:** 7

<!--Device-unnamed-declare class CustomComponent--><!--Device-unnamed-declare class CustomComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## aboutToReuse

```TypeScript
aboutToReuse?(params: Record<string, Object | undefined | null>): void
```

aboutToReuse Method

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CustomComponent-aboutToReuse?(params: Record<string, Object | undefined | null>): void--><!--Device-CustomComponent-aboutToReuse?(params: Record<string, Object | undefined | null>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | Record&lt;string, Object \| undefined \| null&gt; | Yes | Custom component init params.<br>**Since:** 20 |

## onLayout

```TypeScript
onLayout?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void
```

Invoked when the custom component lays out its child components. Through this callback the component receives its child component layout information and size constraint from the ArkUI framework. State variables should not be changed in this callback. This API is supported since API version 9 and deprecated since API version 10. You are advised to use onPlaceChildren instead.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** onPlaceChildren

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CustomComponent-onLayout?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void--><!--Device-CustomComponent-onLayout?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| children | Array&lt;[LayoutChild](arkts-arkui-layoutchild-i.md)&gt; | Yes | Child component layout information. |
| constraint | ConstraintSizeOptions | Yes | Size constraint of the parent component. |

## onMeasure

```TypeScript
onMeasure?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void
```

Invoked when the custom component needs to determine its size. Through this callback the component receives its child component layout information and its own size constraints from the ArkUI framework. State variables should not be changed in this callback. This API is supported since API version 9 and deprecated since API version 10. You are advised to use onMeasureSize instead.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [onMeasureSize](arkts-arkui-basecustomcomponent-c.md#onmeasuresize)

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CustomComponent-onMeasure?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void--><!--Device-CustomComponent-onMeasure?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| children | Array&lt;[LayoutChild](arkts-arkui-layoutchild-i.md)&gt; | Yes | Child component layout information. |
| constraint | ConstraintSizeOptions | Yes | Size constraint of the parent component. |

