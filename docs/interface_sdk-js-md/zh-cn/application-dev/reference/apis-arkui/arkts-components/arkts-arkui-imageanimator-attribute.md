# ImageAnimator属性/事件

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：

**继承/实现关系：** ImageAnimatorAttribute extends CommonMethod<ImageAnimatorAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## duration

```TypeScript
duration(value: number)
```

设置播放时长。当[images](#images)中任意一帧图片设置了单独的duration后，该属性设置无效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## fillMode

```TypeScript
fillMode(value: FillMode)
```

设置当前播放方向下，动画开始前和结束后的状态。动画结束后的状态由fillMode和reverse属性共同决定。例如，fillMode为Forwards表示停止时维持动画最后一个关键帧的状态，若reverse为false则维持正播的 最后一帧，即最后一张图，若reverse为true则维持逆播的最后一帧，即第一张图。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [FillMode](../arkts-apis/arkts-arkui-fillmode-e.md) | 是 |

## fixedSize

```TypeScript
fixedSize(value: boolean)
```

设置图片大小是否固定为组件大小。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## images

```TypeScript
images(value: Array<ImageFrameInfo>)
```

设置图片帧信息集合。不支持动态更新，否则可能导致显示错乱、帧切换异常或内存上涨等问题（该属性按非动态更新设计，运行时修改不保证生效）。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ImageFrameInfo](arkts-arkui-imageframeinfo-i.md)&gt; | 是 |

## iterations

```TypeScript
iterations(value: number)
```

设置播放次数。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## monitorInvisibleArea

```TypeScript
monitorInvisibleArea(monitorInvisibleArea: boolean) : ImageAnimatorAttribute
```

设置组件是否通过系统 [onVisibleAreaChange](arkts-arkui-commonmethod-c.md#onvisibleareachange) 的可见性判定，控制组件的暂停和播放。

**起始版本：** 17

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本17开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [monitorInvisibleArea](#monitorinvisiblearea) | boolean | 是 |

## onCancel

```TypeScript
onCancel(event: () => void)
```

状态回调，动画取消时触发。当state被设置为[AnimationStatus.Initial](../arkts-apis/arkts-arkui-animationstatus-e.md)时触发；触发后图片显示回到第一帧（正播）或最后一帧（逆播）。与 [onFinish](#onfinish)的区别在于：onCancel对应回到Initial初始状态，onFinish对应动画自然结束或停止（Stopped）状态。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## onFinish

```TypeScript
onFinish(event: () => void)
```

状态回调，动画播放完成时（iterations设置的轮次全部播完且动画自然结束）或者停止播放时（state被切换为[AnimationStatus.Stopped](../arkts-apis/arkts-arkui-animationstatus-e.md)）触发。当动画处于 [AnimationStatus.Initial](../arkts-apis/arkts-arkui-animationstatus-e.md)状态时返回初始状态不会触发该事件，对应触发的是onCancel。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## onPause

```TypeScript
onPause(event: () => void)
```

状态回调，动画暂停播放时触发。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## onRepeat

```TypeScript
onRepeat(event: () => void)
```

状态回调，动画重复播放时触发。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## onStart

```TypeScript
onStart(event: () => void)
```

状态回调，动画开始播放时触发。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## preDecode

```TypeScript
preDecode(value: number)
```

设置预解码的图片数量。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。当前无可替代接口。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## reverse

```TypeScript
reverse(value: boolean)
```

设置播放方向。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## state

```TypeScript
state(value: AnimationStatus)
```

控制播放状态。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AnimationStatus](../arkts-apis/arkts-arkui-animationstatus-e.md) | 是 |
