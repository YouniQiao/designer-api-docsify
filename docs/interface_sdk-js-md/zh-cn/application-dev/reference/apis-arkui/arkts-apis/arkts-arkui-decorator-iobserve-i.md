# IObserve

Define IObserve interface.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shouldAddRef

```TypeScript
shouldAddRef(iObjectsRenderId: RenderIdType): boolean
```

Collect the dependancy for UI component with state variable

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iObjectsRenderId | [RenderIdType](arkts-arkui-renderidtype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## renderingComponent

```TypeScript
readonly renderingComponent: int
```

Rendering component.

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## renderingId

```TypeScript
readonly renderingId: RenderIdType
```

Rendering component id.

**类型：** [RenderIdType](arkts-arkui-renderidtype-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
