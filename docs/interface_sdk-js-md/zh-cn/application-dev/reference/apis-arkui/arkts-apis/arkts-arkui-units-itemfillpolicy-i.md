# ItemFillPolicy

定义一个适用于[WaterFlow](../../@internal/component/ets/water_flow)、[Grid](../../@internal/component/ets/grid)、  
[List](../../@internal/component/ets/list)、[Swiper](../../@internal/component/ets/swiper)和  
[LazyVWaterFlowLayout](../../../reference/apis-arkui/arkui-ts/ts-container-lazyvwaterflowlayout.md)组件的响应式布局策略。LazyVWaterFlowLayout组件从API版本26.0.0开始支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface ItemFillPolicy--><!--Device-unnamed-export declare interface ItemFillPolicy-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fillType

```TypeScript
fillType?: ResponsiveFillType
```

为不同的响应式断点指定列数。默认值为BREAKPOINT_DEFAULT。

**类型：** [ResponsiveFillType](arkts-arkui-responsivefilltype-t.md)

**默认值：** ResponsiveFillType.BREAKPOINT_DEFAULT

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ItemFillPolicy-fillType?: ResponsiveFillType--><!--Device-ItemFillPolicy-fillType?: ResponsiveFillType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

