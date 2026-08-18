# UIPickerComponent属性/事件

除支持通用属性外，还支持以下属性： 除支持通用事件外，还支持以下事件：

**继承/实现关系：** UIPickerComponentAttribute extends CommonMethod<UIPickerComponentAttribute>

**起始版本：** 22

<!--Device-unnamed-declare class UIPickerComponentAttribute--><!--Device-unnamed-declare class UIPickerComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## canLoop

```TypeScript
canLoop(isLoop: Optional<boolean>)
```

设置选项列是否可循环滚动。选项数量较多且需要无限滚动浏览时，可开启循环；选项较少或需要限制选择范围时，可关闭循环。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIPickerComponentAttribute-canLoop(isLoop: Optional<boolean>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-canLoop(isLoop: Optional<boolean>): UIPickerComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isLoop | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

## displayedItemCount

```TypeScript
displayedItemCount(count: Optional<number>)
```

设置UIPickerComponent容器可见选项的数量。未通过该接口设置时，可见选项的数量为7行。需要节省空间时减少可见项数量，需要提供更多预览信息时 增加可见项数量。此属性与[itemHeight](#itemheight)共同影响组件的显示效果，建议结合组件 height属性进行调整以保证完整显示。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UIPickerComponentAttribute-displayedItemCount(count: Optional<int>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-displayedItemCount(count: Optional<int>): UIPickerComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(enable: Optional<boolean>)
```

设置是否开启触控反馈。在需要增强用户交互体验的场景可开启触控反馈。 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下： > > "requestPermissions": [{"name": "ohos.permission.VIBRATE"}]

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIPickerComponentAttribute-enableHapticFeedback(enable: Optional<boolean>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-enableHapticFeedback(enable: Optional<boolean>): UIPickerComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

## itemHeight

```TypeScript
itemHeight(height: Optional<LengthMetrics>)
```

设置UIPickerComponent容器每个选项的高度。未通过该接口设置时，每个选项的高度为40vp。选项内容较多或需要更大字体显示时可增大高度以避免内容 裁剪，选项内容简洁或需要紧凑显示时可减小高度。此属性与 [displayedItemCount](#displayeditemcount)共同影响组件的显示效果，建议结合组件 height属性进行调整以保证完整显示。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UIPickerComponentAttribute-itemHeight(height: Optional<LengthMetrics>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-itemHeight(height: Optional<LengthMetrics>): UIPickerComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| height | [Optional](arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | 是 |

## onChange

```TypeScript
onChange(callback: Optional<OnUIPickerComponentCallback>)
```

滑动选择器选项时，若选中项发生变化，触发该事件。适用于需要在选中项变化时实时更新界面、加载对应数据或执行相关逻辑的场景。 > **说明：** > > - 如果某个选项有一半以上的区域进入选中项区域内，则该选项成为选中项。 > > - 选中项区域可通过设置[selectionIndicator](#selectionindicator)进行标识。 > 如果设置选中项指示器为背景，则背景区域即为选中项区域。如果设置选中项指示器为分割线，则上下分割线的中心线内的区域为选中项区域。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIPickerComponentAttribute-onChange(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-onChange(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;[OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md)&gt; | 是 |

## onScrollStop

```TypeScript
onScrollStop(callback: Optional<OnUIPickerComponentCallback>)
```

选择器滑动停止时，触发该事件。选择器滑动停止指某次行为触发的滑动动画完全结束。如果某次滑动动画还未结束时又触发了新的滑动动画， 则不属于滑动停止。适用于需要在滑动结束后提交最终选择结果、停止加载动画或执行一次性回调的场景。 > **说明：** > > **onChange与onScrollStop的差异：** > > - **触发时机**：onChange在选中项发生变化时立即触发；onScrollStop在滑动动画完全停止后触发。 > > - **触发频率**：连续滑动过程中，onChange可能多次触发（每次选中项变化都会触发）；onScrollStop只在滑动停止时触发一次。 > > - **使用场景**：onChange适用于需要实时响应的场景（如实时显示选中内容、联动更新其他组件）；onScrollStop适用于需要最终确认的场景 > （如提交最终选择结果、保存数据）。 > > - **两者关系**：一次完整的滑动操作可能先后触发这两个事件，可根据实际需求同时使用或选择使用。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIPickerComponentAttribute-onScrollStop(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-onScrollStop(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;[OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md)&gt; | 是 |

## selectionIndicator

```TypeScript
selectionIndicator(style: Optional<PickerIndicatorStyle>)
```

设置选中项指示器的样式。需要突出显示选中区域时使用背景指示器，需要简洁轻量标识时使用分割线指示器。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIPickerComponentAttribute-selectionIndicator(style: Optional<PickerIndicatorStyle>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-selectionIndicator(style: Optional<PickerIndicatorStyle>): UIPickerComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[PickerIndicatorStyle](arkts-arkui-pickerindicatorstyle-i.md)&gt; | 是 |
