# DynamicLayoutAttribute

The [universal attributes]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ are supported. > **NOTE** > > - When the layout algorithm is [RowLayoutAlgorithm]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ or > [ColumnLayoutAlgorithm]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, > the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ attributes set > for child components take effect. > > - When the layout algorithm is [StackLayoutAlgorithm]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_, > the [layoutGravity]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ attribute set for child components takes effect. > > - When the layout algorithm is > [CustomLayoutAlgorithm]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_, > the [setMeasuredSize]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_ method of the > [FrameNode]\_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_ component of **DynamicLayout** has a higher priority than the > [sizing]\_\_\_JSDOC\_LINK\_DESC\_USD\_10\_\_\_ and [border styling]\_\_\_JSDOC\_LINK\_DESC\_USD\_11\_\_\_ attributes. The > [measure]\_\_\_JSDOC\_LINK\_DESC\_USD\_12\_\_\_ and [layout]\_\_\_JSDOC\_LINK\_DESC\_USD\_13\_\_\_ methods > of the child component [FrameNode]\_\_\_JSDOC\_LINK\_DESC\_USD\_14\_\_\_ have a higher priority than the > [ignoreLayoutSafeArea]\_\_\_JSDOC\_LINK\_DESC\_USD\_15\_\_\_ attribute. The \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ are supported.

**Inheritance/Implementation:** DynamicLayoutAttribute extends [CommonMethod<DynamicLayoutAttribute>](CommonMethod<DynamicLayoutAttribute>)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-unnamed-export declare class DynamicLayoutAttribute extends CommonMethod<DynamicLayoutAttribute>--><!--Device-unnamed-export declare class DynamicLayoutAttribute extends CommonMethod<DynamicLayoutAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

