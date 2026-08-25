# Effect

特效类型，继承自SceneResource。由createEffect接口获得。@extends SceneResource @interface Effect

**继承/实现关系：** Effect extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**起始版本：** 21

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getPropertyValue

```TypeScript
getPropertyValue(propertyName: string): Object | null | undefined
```

获取特定特效属性的值。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propertyName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Object \| null \| undefined |

## setPropertyValue

```TypeScript
setPropertyValue(propertyName: string, value: Object | undefined): boolean
```

设置特定特效属性的值。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propertyName | string | 是 |
| value | Object \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## effectId

```TypeScript
readonly effectId: string
```

特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，用于特效的创建，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'。

**类型：** string

**起始版本：** 21

**系统能力：** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

特效打开状态。true表示开启特效，false表示关闭特效。

**类型：** boolean

**起始版本：** 21

**系统能力：** SystemCapability.ArkUi.Graphics3D
