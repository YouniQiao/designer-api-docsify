# TouchPadEventContact

```TypeScript
declare interface TouchPadEventContact
```

描述原始触控板事件中的单个触点。

**起始版本：** 26.1.0

<!--Device-unnamed-declare interface TouchPadEventContact--><!--Device-unnamed-declare interface TouchPadEventContact-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: number
```

触点的唯一标识。该标识在触点按下至抬起或取消期间保持不变。取值限定为整数。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEventContact-id: int--><!--Device-TouchPadEventContact-id: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## phase

```TypeScript
phase: TouchPadEventPhase
```

触点阶段。

**类型：** [TouchPadEventPhase](../arkts-apis/arkts-arkui-touchpadeventphase-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEventContact-phase: TouchPadEventPhase--><!--Device-TouchPadEventContact-phase: TouchPadEventPhase-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## positionX

```TypeScript
positionX: number
```

触点在触控板逻辑坐标范围内归一化后的X轴位置。取值范围：[0,1]。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEventContact-positionX: double--><!--Device-TouchPadEventContact-positionX: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## positionY

```TypeScript
positionY: number
```

触点在触控板逻辑坐标范围内归一化后的Y轴位置。取值范围：[0,1]。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-TouchPadEventContact-positionY: double--><!--Device-TouchPadEventContact-positionY: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
