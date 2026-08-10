# HoverEvent

继承于[BaseEvent](arkts-arkui-baseevent-i.md)。

**Inheritance/Implementation:** HoverEvent extends [BaseEvent](arkts-arkui-baseevent-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface HoverEvent extends BaseEvent--><!--Device-unnamed-declare interface HoverEvent extends BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stopPropagation

```TypeScript
stopPropagation: () => void
```

阻塞[事件冒泡](../../../ui/arkts-interaction-basic-principles.md#事件冒泡)。 

**原子化服务API：** 从API version 11开始，该接口支持在原子化服务中使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HoverEvent-stopPropagation: () => void--><!--Device-HoverEvent-stopPropagation: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX?: number
```

鼠标光标或手写笔位置在当前应用屏幕坐标系中的X坐标。

单位：vp

取值范围：[0, +∞)

**原子化服务API：** 从API version 15开始，该接口支持在原子化服务中使用。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HoverEvent-displayX?: number--><!--Device-HoverEvent-displayX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY?: number
```

鼠标光标或手写笔位置在当前应用屏幕坐标系中的Y坐标。

单位：vp

取值范围：[0, +∞)

**原子化服务API：** 从API version 15开始，该接口支持在原子化服务中使用。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HoverEvent-displayY?: number--><!--Device-HoverEvent-displayY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: number
```

鼠标光标或手写笔位置在[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)中的X坐标。

单位：vp

取值范围：[0, +∞)

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-HoverEvent-globalDisplayX?: number--><!--Device-HoverEvent-globalDisplayX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: number
```

相对于全局显示的点的 Y 坐标。

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-HoverEvent-globalDisplayY?: number--><!--Device-HoverEvent-globalDisplayY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX?: number
```

鼠标光标或手写笔位置在当前应用窗口坐标系中的X坐标。

单位：vp

取值范围：[0, +∞)

**原子化服务API：** 从API version 15开始，该接口支持在原子化服务中使用。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HoverEvent-windowX?: number--><!--Device-HoverEvent-windowX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY?: number
```

鼠标光标或手写笔位置在当前应用窗口坐标系中的Y坐标。

单位：vp

取值范围：[0, +∞)

**原子化服务API：** 从API version 15开始，该接口支持在原子化服务中使用。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HoverEvent-windowY?: number--><!--Device-HoverEvent-windowY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x?: number
```

鼠标光标或手写笔位置在当前组件为基准的[组件坐标系](../../../ui/arkui-glossary.md#组件坐标系)中的X坐标。

单位：vp

取值范围：[0, +∞)

**原子化服务API：** 从API version 15开始，该接口支持在原子化服务中使用。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HoverEvent-x?: number--><!--Device-HoverEvent-x?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y?: number
```

鼠标光标或手写笔位置在当前组件为基准的[组件坐标系](../../../ui/arkui-glossary.md#组件坐标系)中的Y坐标。

单位：vp

取值范围：[0, +∞)

**原子化服务API：** 从API version 15开始，该接口支持在原子化服务中使用。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-HoverEvent-y?: number--><!--Device-HoverEvent-y?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

