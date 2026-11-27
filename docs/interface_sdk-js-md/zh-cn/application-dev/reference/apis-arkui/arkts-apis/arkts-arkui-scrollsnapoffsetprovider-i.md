# ScrollSnapOffsetProvider

```TypeScript
declare interface ScrollSnapOffsetProvider
```

用于自定义限位滚动的距离和吸附位置。此接口适用于Grid、WaterFlow和List组件的scrollSnapStrategy属性，开发者实现接口后，将对象传入scrollSnapStrategy即可使用。完整示例参考[示例24（自定义滚动吸附位置）](../../../reference/apis-arkui/arkui-ts/ts-container-grid.md#示例24自定义滚动吸附位置)。

自定义限位滚动分为两个阶段：先按指定的距离惯性滚动，再通过限位动画滚动到目标吸附位置。两个回调分别在两个阶段的起始时机调用：  
- calculateApproachOffset：在惯性滚动开始时调用一次。  
- calculateSnapOffset：在惯性阶段结束、限位动画开始前调用一次。

> **说明：** 

> - 偏移量的单位是vp，速度的单位是vp/s。
> - 两个回调均在UI线程同步调用，应仅用于计算，不应修改组件布局或应用状态。
> - 回调不提供item的位置和尺寸，开发者需要自行记录或计算这些信息。

**起始版本：** 26.1.0

<!--Device-unnamed-declare interface ScrollSnapOffsetProvider--><!--Device-unnamed-declare interface ScrollSnapOffsetProvider-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## calculateApproachOffset

```TypeScript
calculateApproachOffset(velocity: number, decayOffset: number): number
```

用于计算惯性阶段滚动距离的回调，在惯性滚动开始时调用一次。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ScrollSnapOffsetProvider-calculateApproachOffset(velocity: number, decayOffset: number): number--><!--Device-ScrollSnapOffsetProvider-calculateApproachOffset(velocity: number, decayOffset: number): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| velocity | number | 是 | 惯性滚动开始时的速度，朝内容末端滚动时为正。反向布局和RTL方向由组件统一处理。<br>单位：vp/s |
| decayOffset | number | 是 | 按默认惯性滚动预测的滑行距离。<br>单位：vp <br>取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 惯性阶段的滚动距离，不能为NaN或Infinity，可以超过decayOffset。返回负数、NaN或Infinity，或回调抛出异常时，该阶段按默认的惯性滑行距离滚动，随后正常进入限位动画阶段。<br>单位：vp <br>取值范围：[0, +∞) |

## calculateSnapOffset

```TypeScript
calculateSnapOffset(velocity: number): number
```

用于计算最终吸附位置的回调，在惯性阶段结束、限位动画开始前调用一次。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ScrollSnapOffsetProvider-calculateSnapOffset(velocity: number): number--><!--Device-ScrollSnapOffsetProvider-calculateSnapOffset(velocity: number): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| velocity | number | 是 | 惯性滚动结束时的剩余速度，朝内容末端滚动时为正。反向布局和RTL方向由组件统一处理。<br>单位：vp/s |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 最终吸附位置相对内容起点的滚动偏移量，必须为有限数值。沿逻辑主轴朝内容末端方向偏移为正，反方向为负，0表示内容起点。实际滚动方向由目标位置与当前滚动位置决定：目标偏移量大于当前偏移量时朝内容末端滚动，小于时朝内容起点滚动，相等时不滚动。超出可滚动范围时，目标位置限制在可滚动范围的边界。回调返回NaN、Infinity或抛出异常时，组件在当前滚动位置停止。<br>单位：vp <br>取值范围：组件可滚动范围对应的滚动偏移量。 |
