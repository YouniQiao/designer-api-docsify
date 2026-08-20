# ToolBarV2Modifier

ToolBarV2Modifier提供设置工具栏高度(height)、背景色(backgroundColor)、左右内边距（padding，仅在子项数量小于5个时生效）、是否显示按压态（stateEffect）的方法。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ToolBarV2Modifier--><!--Device-unnamed-export declare class ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## backgroundColor

```TypeScript
public backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier
```

设置工具栏背景色的接口，调用该方法可自定义绘制。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ToolBarV2Modifier-public backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-public backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backgroundColor | [ColorMetrics](arkts-graphics-colormetrics-c.md) | 是 | toolBarV2's backgroundColor. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](arkts-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | 设置背景色后的ToolBarV2Modifier对象，可用于链式调用其他方法进一步自定义工具栏样式。 |

## height

```TypeScript
public height(height: LengthMetrics): ToolBarV2Modifier
```

设置工具栏高度的接口，调用该方法可自定义绘制，此高度不包含分割线高度。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2Modifier-public height(height: LengthMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-public height(height: LengthMetrics): ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | 是 | toolBarV2's height. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](arkts-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | 设置高度后的ToolBarV2Modifier对象，可用于链式调用其他方法进一步自定义工具栏样式。 |

## padding

```TypeScript
public padding(padding: LengthMetrics): ToolBarV2Modifier
```

设置工具栏左右内边距的接口，调用该方法可自定义绘制。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2Modifier-public padding(padding: LengthMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-public padding(padding: LengthMetrics): ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| padding | [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | 是 | left and right padding. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](arkts-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | 设置内边距后的ToolBarV2Modifier对象，可用于链式调用其他方法进一步自定义工具栏样式。 |

## stateEffect

```TypeScript
public stateEffect(stateEffect: boolean): ToolBarV2Modifier
```

设置是否显示按压态效果的接口。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2Modifier-public stateEffect(stateEffect: boolean): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-public stateEffect(stateEffect: boolean): ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateEffect | boolean | 是 | press status effect. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](arkts-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | 设置按压态效果后的ToolBarV2Modifier对象，可用于链式调用其他方法进一步自定义工具栏样式。 |

