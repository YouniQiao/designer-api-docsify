# RelativeContainer

The **RelativeContainer** component is a container component used for relative layout of elements in complex
scenarios.
Child components can define their alignment rules within the container using
[alignRules]{@link CommonMethod#alignRules}.
> **NOTE**
>
> * When [width]{@link CommonMethod#width} and [height]{@link CommonMethod#height} are not set,
> **RelativeContainer** defaults to 100% in both dimensions.
>
> * Since API version 11, setting [width]{@link CommonMethod#width} or [height]{@link CommonMethod#height} to
> **"auto"** enables child-adaptive sizing. However, if the child components use the container as an anchor in the
> horizontal direction, the **auto** value of **width** has no effect (equivalent to **width** not being set). The
> same rule applies to the vertical direction.
>
> * Since API version 20, the size adaptation behavior of child components in the **RelativeContainer** component
> follows the following rules, depending on the **LayoutPolicy** setting for
> [width]{@link CommonMethod#width} and [height]{@link CommonMethod#height}:
> **LayoutPolicy.wrapContent**: The child component adapts to its content size and is constrained by the size of the
> ancestor node. **LayoutPolicy.fixAtIdealSize**: The child component adapts to its ideal content size and is not
> constrained by the size of the ancestor node. If **width** is set to **wrapContent** or **fixAtIdealSize**, and the
> child component (in the horizontal direction) directly or indirectly uses the **RelativeContainer** as its anchor,
> the container's horizontal size will not adapt to the child component. The same rule applies to the vertical
> direction.
>
> * For a child component of the container,
> [margin]{@link CommonMethod#margin} has a different meaning from the universal attribute **margin**. It indicates
> the distance to the anchor in the respective direction. If there is no anchor in the respective direction,
> **margin** in that direction does not take effect.
>
> **Child Components**
>
> Multiple child components are supported.


## RelativeContainer

```TypeScript
RelativeContainer()
```

Defines the constructor of RelativeContainer.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RelativeContainerInterface-(): RelativeContainerAttribute--><!--Device-RelativeContainerInterface-(): RelativeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

- [BarrierStyle](arkts-arkui-relativecontainer-barrierstyle-i.md)
- [GuideLinePosition](arkts-arkui-relativecontainer-guidelineposition-i.md)
- [GuideLineStyle](arkts-arkui-relativecontainer-guidelinestyle-i.md)
- [LocalizedBarrierStyle](arkts-arkui-relativecontainer-localizedbarrierstyle-i.md)
- [BarrierDirection](arkts-arkui-relativecontainer-barrierdirection-e.md)
- [LocalizedBarrierDirection](arkts-arkui-relativecontainer-localizedbarrierdirection-e.md)
