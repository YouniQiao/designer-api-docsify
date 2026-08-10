# EffectComponent

特效合并容器组件，用于子节点特效绘制的合并，实现特效的绘制性能优化。

> **说明：**
>
> - 该组件从API Version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
>
> - 本模块为系统接口。

> - 目前该组件仅支持子组件背景模糊效果的绘制合并优化。
>
> - 在对子组件的背景模糊特效进行绘制合并时，需要将子组件的backgroundBlurStyle(BlurStyle)属性替换成useEffect(true)。

## 子组件

可以包含子组件。

## EffectComponent

```TypeScript
EffectComponent()
```

创建特效绘制合并组件，用于对子组件背景模糊特效的绘制合并。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EffectComponentInterface-(): EffectComponentAttribute--><!--Device-EffectComponentInterface-(): EffectComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## EffectComponent

```TypeScript
EffectComponent(options?: EffectComponentOptions)
```

创建特效绘制合并组件，无参数或者参数为EffectLayer.None时用于对子组件背景模糊特效的绘制合并。有明确参数时表示当前渲染图层置于特殊图层。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EffectComponentInterface-(options?: EffectComponentOptions): EffectComponentAttribute--><!--Device-EffectComponentInterface-(options?: EffectComponentOptions): EffectComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EffectComponentOptions](../arkts-apis/arkts-arkui-effectcomponent-effectcomponentoptions-i-sys.md) | No | EffectComponent构造参数。 |

## Summary

- [EffectComponentOptions](arkts-arkui-effectcomponent-effectcomponentoptions-i-sys.md)
- [EffectLayer](arkts-arkui-effectcomponent-effectlayer-e-sys.md)
