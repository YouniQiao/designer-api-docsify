# TouchPadEvent

```TypeScript
declare abstract class TouchPadEvent
```

描述原始触控板事件。该事件独立于触摸、鼠标、轴事件和系统手势事件。

**起始版本：** 26.1.0

<!--Device-unnamed-declare abstract class TouchPadEvent--><!--Device-unnamed-declare abstract class TouchPadEvent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getModifierKeyState

```TypeScript
getModifierKeyState(keys: Array<string>): boolean
```

获取功能键按压状态。支持Ctrl、Alt和Shift功能键。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-getModifierKeyState(keys: Array<string>): boolean--><!--Device-TouchPadEvent-getModifierKeyState(keys: Array<string>): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | 是 | 功能键列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 功能键按压状态。所有指定功能键均被按下时返回true，否则返回false。 |

## stopPropagation

```TypeScript
stopPropagation(): void
```

停止当前触控板事件在ArkUI节点事件链中的传播。该操作不影响触摸、鼠标、轴事件或系统手势事件。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-stopPropagation(): void--><!--Device-TouchPadEvent-stopPropagation(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## changedContact

```TypeScript
changedContact: TouchPadEventContact
```

本次发生变化并触发事件的触点信息。

**类型：** [TouchPadEventContact](arkts-arkui-common-comp-touchpadeventcontact-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-changedContact: TouchPadEventContact--><!--Device-TouchPadEvent-changedContact: TouchPadEventContact-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## contacts

```TypeScript
contacts: TouchPadEventContact[]
```

当前事件上报的全部触点。触点数量取决于硬件能力，对外接口不设置固定上限。

**类型：** [TouchPadEventContact](arkts-arkui-common-comp-touchpadeventcontact-i.md)[]

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-contacts: TouchPadEventContact[]--><!--Device-TouchPadEvent-contacts: TouchPadEventContact[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## deviceHeight

```TypeScript
deviceHeight: number
```

触摸板的高度。单位为：mm。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-deviceHeight: double--><!--Device-TouchPadEvent-deviceHeight: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## deviceId

```TypeScript
deviceId: number
```

触发事件的触控板设备ID。取值应≥0。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-deviceId: int--><!--Device-TouchPadEvent-deviceId: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## deviceWidth

```TypeScript
deviceWidth: number
```

触摸板的宽度。单位为：mm。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-deviceWidth: double--><!--Device-TouchPadEvent-deviceWidth: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX: number
```

光标在当前应用屏幕坐标系中的X坐标。单位为：vp。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-displayX: double--><!--Device-TouchPadEvent-displayX: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: number
```

光标在当前应用屏幕坐标系中的Y坐标。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-displayY: double--><!--Device-TouchPadEvent-displayY: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX: number
```

光标在全局坐标系中的X坐标。单位为：vp。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-globalDisplayX: double--><!--Device-TouchPadEvent-globalDisplayX: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY: number
```

光标在全局坐标系中的Y坐标。单位为：vp。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-globalDisplayY: double--><!--Device-TouchPadEvent-globalDisplayY: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## source

```TypeScript
source: SourceType
```

事件的输入源。

**类型：** [SourceType](arkts-arkui-common-comp-sourcetype-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-source: SourceType--><!--Device-TouchPadEvent-source: SourceType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## sourceTool

```TypeScript
sourceTool: SourceTool
```

事件的输入工具。

**类型：** [SourceTool](arkts-arkui-common-comp-sourcetool-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-sourceTool: SourceTool--><!--Device-TouchPadEvent-sourceTool: SourceTool-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## target

```TypeScript
target: EventTarget
```

触发事件的元素对象。

**类型：** [EventTarget](arkts-arkui-common-comp-eventtarget-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-target: EventTarget--><!--Device-TouchPadEvent-target: EventTarget-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## targetDisplayId

```TypeScript
targetDisplayId?: number
```

事件发生的屏幕ID。取值应≥0。默认值：**0**。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-targetDisplayId?: int--><!--Device-TouchPadEvent-targetDisplayId?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: number
```

事件时间戳，表示事件发生时距离系统启动的时间间隔。单位为：纳秒。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-timestamp: long--><!--Device-TouchPadEvent-timestamp: long-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: number
```

光标在当前应用窗口坐标系中的X坐标。单位为：vp。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-windowX: double--><!--Device-TouchPadEvent-windowX: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: number
```

光标在当前应用窗口坐标系中的Y坐标。单位为：vp。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-windowY: double--><!--Device-TouchPadEvent-windowY: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: number
```

光标在事件响应组件坐标系中的X坐标。单位为：vp。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-x: double--><!--Device-TouchPadEvent-x: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: number
```

光标在事件响应组件坐标系中的Y坐标。单位为：vp。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEvent-y: double--><!--Device-TouchPadEvent-y: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
