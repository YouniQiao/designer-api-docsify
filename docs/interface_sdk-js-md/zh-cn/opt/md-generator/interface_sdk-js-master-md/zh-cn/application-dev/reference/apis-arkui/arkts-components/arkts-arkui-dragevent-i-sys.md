# DragEvent

拖拽事件信息。

**起始版本：** 7

<!--Device-unnamed-declare interface DragEvent--><!--Device-unnamed-declare interface DragEvent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## enableInternalDropAnimation

```TypeScript
enableInternalDropAnimation(configuration: string): void
```

使用系统的内置动效，且该动效只有系统应用可使用。仅支持在onDrop阶段使用。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragEvent-enableInternalDropAnimation(configuration: string): void--><!--Device-DragEvent-enableInternalDropAnimation(configuration: string): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configuration | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [190003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-drag-event.md#190003-当前阶段不允许操作) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## executeFollowHandMorphDropAnimation

```TypeScript
executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void
```

设置一个跟手变形落位动效执行完成后的回调，该回调由系统在拖拽框架动效结束后触发。使用callback异步回调。

> **说明：**
> 
> 1. 该接口仅在[dragAnimationType](#dragAnimationType)设置为DragAnimationType.FOLLOW_HAND_MORPH时生效。
> 
> 2. 不要在回调中实现与动效无关的逻辑，避免影响执行效率。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragEvent-executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void--><!--Device-DragEvent-executeFollowHandMorphDropAnimation(onAnimationFinished: Callback<void>, animationOption?: string): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onAnimationFinished | [Callback](arkts-arkui-callback-i.md)&lt;void&gt; | 是 |
| animationOption | string | 否 |

## dragAnimationType

```TypeScript
dragAnimationType?: DragAnimationType
```

设置拖拽动画类型。该属性仅支持在[onDragStart](arkts-arkui-commonmethod-c.md#onDragStart)阶段设置，可在[onDragStart](arkts-arkui-commonmethod-c.md#onDragStart)、  
[onDragEnter](arkts-arkui-commonmethod-c.md#onDragEnter)、[onDragMove](arkts-arkui-commonmethod-c.md#onDragMove)、  
[onDragLeave](arkts-arkui-commonmethod-c.md#onDragLeave)、  
[onDrop](CommonMethod#onDrop(event: (event: DragEvent, extraParams?: string) => void))、  
[onDragEnd](arkts-arkui-commonmethod-c.md#onDragEnd)回调中获取。

默认值为DEFAULT 

**系统接口：** 此接口为系统接口。

**类型：** [DragAnimationType](arkts-arkui-draganimationtype-e-sys.md)

**默认值：** DragAnimationType.DEFAULT

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragEvent-dragAnimationType?: DragAnimationType--><!--Device-DragEvent-dragAnimationType?: DragAnimationType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
