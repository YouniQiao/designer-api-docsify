# Effect

特效资源.

**继承/实现关系：** Effect extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**起始版本：** 21

<!--Device-unnamed-export interface Effect extends SceneResource--><!--Device-unnamed-export interface Effect extends SceneResource-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getPropertyValue

```TypeScript
getPropertyValue(propertyName: string): Object | null | undefined
```

获取特定特效属性的值.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Effect-getPropertyValue(propertyName: string): Object | null | undefined--><!--Device-Effect-getPropertyValue(propertyName: string): Object | null | undefined-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propertyName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Object |

## setPropertyValue

```TypeScript
setPropertyValue(propertyName: string, value: Object | undefined): boolean
```

设置特定特效属性的值

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Effect-setPropertyValue(propertyName: string, value: Object | undefined): boolean--><!--Device-Effect-setPropertyValue(propertyName: string, value: Object | undefined): boolean-End-->

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

特效的ID.这是用于创建特效的ID.

**类型：** string

**起始版本：** 21

<!--Device-Effect-readonly effectId: string--><!--Device-Effect-readonly effectId: string-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

控制特效是否启用.

**类型：** boolean

**起始版本：** 21

<!--Device-Effect-enabled: boolean--><!--Device-Effect-enabled: boolean-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D
