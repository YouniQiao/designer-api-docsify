# RelativeContainer

Defines a relative layout component used for element alignment in complex scenarios. By setting the alignment rules of child components, it aligns child components relative to the container or other child components. It is suitable for complex UIs that require flexible layout and fewer nesting levels.

Child components can define their alignment rules within the container using alignRules.

> **NOTE** > > * This component is supported since API version 9. New APIs in later versions are marked with a superscript to > indicate their initial version. > > * In the **RelativeContainer** component, when width and > height are not set, the layout behavior of the corresponding attributes > is the same as when they are set to 100%. > > * Since API version 11, in the **RelativeContainer** component, setting > width and height to "auto" > means adapting to child components. When width is set to "auto", if a child component uses the container as an > anchor in the horizontal direction, "auto" does not take effect (that is, it is treated as if width is not set). > The same applies to the vertical direction. > > * Since API version 20, in the **RelativeContainer** component, setting > width and > height to **LayoutPolicy.wrapContent** means > adapting to child components while being constrained by the ancestor node size, and setting them to > **LayoutPolicy.fixAtIdealSize** means adapting to child components without being constrained by the ancestor node > size. When **width** is set to **wrapContent** or **fixAtIdealSize**, if a child component directly or indirectly > uses the container as an anchor in the horizontal direction, the container size in that direction does not adapt to > that component. The same applies to the vertical direction. > > * The margin of a child component in **RelativeContainer** differs from the universal > margin attribute. It refers to the distance from the child component to the anchor in that direction. For example, > when **alignRules** sets a left anchor, **margin.left** indicates the distance from the child component to the left > anchor. If **alignRules** does not set an anchor in a certain boundary direction (for example, neither **left** nor > **right** anchor is set), the **margin** in that direction does not take effect.

## Child Components

Multiple child components are supported.

## RelativeContainer

```TypeScript
RelativeContainer()
```

The **RelativeContainer** component is a container component used for relative layout of elements in complex scenarios.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [BarrierStyle](arkts-arkui-relativecontainer-comp-barrierstyle-i.md) | Defines the style of a barrier, which is used to define the ID, direction, and dependent components of a barrier. Child components can reference the barrier by its ID as an anchor for alignment and positioning. |
| [GuideLinePosition](arkts-arkui-relativecontainer-comp-guidelineposition-i.md) | Defines the position of a guideline. |
| [GuideLineStyle](arkts-arkui-relativecontainer-comp-guidelinestyle-i.md) | Defines the style of a guideline, which used to define the ID, direction, and position of a guideline, helping child components to be positioned and aligned in the **RelativeContainer**. |
| [LocalizedBarrierStyle](arkts-arkui-relativecontainer-comp-localizedbarrierstyle-i.md) | Defines the style of a localized barrier, which is used to define the ID, direction, and dependent components of a barrier that supports mirror mode. Child components can reference the barrier by its ID as an anchor for alignment and positioning. |

### Enums

| Name | Description |
| --- | --- |
| [BarrierDirection](arkts-arkui-relativecontainer-comp-barrierdirection-e.md) | Defines the direction of a barrier. |
| [LocalizedBarrierDirection](arkts-arkui-relativecontainer-comp-localizedbarrierdirection-e.md) | Enumerates the directions of barriers with mirror mode support. |

## Examples

```TypeScript
### Example 1: Implementing a Layout Using Containers and Components as Anchors

This example demonstrates how to use the alignRules API to implement a layout with containers and their internal components as anchors.


```

```TypeScript
### Example 2: Setting Margins for Child Components

This example shows how to set margins for child components in the container.


```

```TypeScript
### Example 3: Configuring the Container to Adapt Its Size to Content

This example shows how to configure the container to adapt its size to content by setting width or height to "auto".


```

```TypeScript
### Example 4: Applying Vertical Offsets

This example uses [bias](ts-types.md#bias11) to offset the position of a child component between two anchors in the vertical direction.


```

```TypeScript
### Example 5: Setting Guidelines

This example demonstrates how to set guidelines in a relative layout using the [guideLine](arkts-arkui-relativecontainer-comp-attribute.md#guideline) API, with child components using these guidelines as anchors.


```

```TypeScript
### Example 6: Implementing Barriers

This example shows how to set barriers in a relative layout using the [barrier](arkts-arkui-relativecontainer-comp-attribute.md#barrier) API, with child components using these barriers as anchors.


```

```TypeScript
### Example 7: Creating Chains

This example uses the [chainMode](ts-universal-attributes-location.md#chainmode12) API to implement a horizontal [SPREAD](ts-universal-attributes-location.md#chainstyle12) chain, a [SPREAD_INSIDE](ts-universal-attributes-location.md#chainstyle12) chain, and a [PACKED](ts-universal-attributes-location.md#chainstyle12) chain from top to bottom.


```

```TypeScript
### Example 8: Creating a Chain with Offsets

This example uses the [chainMode](ts-universal-attributes-location.md#chainmode12) and [bias](ts-types.md#bias11) APIs to implement a horizontally biased [PACKED](ts-universal-attributes-location.md#chainstyle12) chain.


```

```TypeScript
### Example 9: Implementing a Mirror Effect

This example demonstrates how to use [LocalizedAlignRuleOptions](ts-universal-attributes-location.md#localizedalignruleoptions12) and [LocalizedBarrierDirection](arkts-arkui-relativecontainer-comp-localizedbarrierdirection-e.md) for alignment when using barriers as anchors in mirror mode (direction set to Direction.Rtl).


```

```TypeScript
### Example 10: Setting Component Weights in a Chain

This example demonstrates how to use [chainWeight](ts-universal-attributes-location.md#chainweight14) to set the size weights of components in a chain.

You must first set the chain alignment rules of child components through alignRules (to ensure that the components form a chain in the horizontal or vertical direction), and then set the chain style (such as SPREAD, SPREAD_INSIDE, and PACKED) through chainMode. chainWeight takes effect only in chain mode.
```
