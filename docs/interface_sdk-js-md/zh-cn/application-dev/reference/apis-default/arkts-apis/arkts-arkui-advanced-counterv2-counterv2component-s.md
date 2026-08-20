# CounterV2Component

CounterV2组件用于精确调节数值。

该组件基于[状态管理（V2）](../../../ui/state-management/arkts-state-management-overview.md#状态管理v2)实现，相较于 [状态管理（V1）](../../../ui/state-management/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组 件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制Counter的数据和状态，实现更高效的用户界面刷新。

> **说明：**
> 
> - 如果CounterV2设置通用属性和 &gt; 通用事件，编译工具链会额外生成节点__Common__，并将通用属性 &gt; 或通用事件挂载在__Common__上，而不是直接应用到CounterV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议CounterV2设置通用属性和通用事件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-declare struct CounterV2Component--><!--Device-unnamed-declare struct CounterV2Component-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

build函数用于构造CounterV2高级组件。

**ArkTS模式：** 该接口仅适用于ArkTS-Sta。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterV2Component-@Builder  build(): void--><!--Device-CounterV2Component-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@Param
  options: CounterV2Options
```

定义CounterV2组件的类型。

**类型：** [CounterV2Options](arkts-arkui-advanced-counterv2-counterv2options-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterV2Component-@Param  options: CounterV2Options--><!--Device-CounterV2Component-@Param  options: CounterV2Options-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

