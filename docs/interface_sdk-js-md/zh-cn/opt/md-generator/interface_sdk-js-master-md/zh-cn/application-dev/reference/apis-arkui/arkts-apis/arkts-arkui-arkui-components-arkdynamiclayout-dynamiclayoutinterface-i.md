# DynamicLayoutInterface

动态布局容器组件，支持在运行时动态切换不同的布局算法，不改变子组件的状态。

> **说明：**

**起始版本：** 24

<!--Device-unnamed-export interface DynamicLayoutInterface--><!--Device-unnamed-export interface DynamicLayoutInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(algorithm: LayoutAlgorithm): DynamicLayoutAttribute
```

动态布局容器。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本24开始，该接口支持在ArkTS卡片中使用。

<!--Device-DynamicLayoutInterface-(algorithm: LayoutAlgorithm): DynamicLayoutAttribute--><!--Device-DynamicLayoutInterface-(algorithm: LayoutAlgorithm): DynamicLayoutAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| algorithm | [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md) |
