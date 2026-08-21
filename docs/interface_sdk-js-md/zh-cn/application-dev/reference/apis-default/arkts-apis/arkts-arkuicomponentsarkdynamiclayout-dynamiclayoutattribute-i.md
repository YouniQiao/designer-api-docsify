# DynamicLayoutAttribute

动态布局容器组件，支持在运行时动态切换不同的布局算法，不改变子组件的状态。

@extends CommonMethod @interface DynamicLayoutAttribute

**继承/实现关系：** DynamicLayoutAttribute extends CommonMethod

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export declare interface DynamicLayoutAttribute--><!--Device-unnamed-export declare interface DynamicLayoutAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## attributeModifier

```TypeScript
attributeModifier(
      modifier: AttributeModifier<DynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-DynamicLayoutAttribute-attributeModifier(      modifier: AttributeModifier<DynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-DynamicLayoutAttribute-attributeModifier(      modifier: AttributeModifier<DynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | AttributeModifier&lt;[DynamicLayoutAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkuicomponentsarkdynamiclayout-dynamiclayoutattribute-c.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置组件的动态属性。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DynamicLayoutAttribute-default--><!--Device-DynamicLayoutAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

