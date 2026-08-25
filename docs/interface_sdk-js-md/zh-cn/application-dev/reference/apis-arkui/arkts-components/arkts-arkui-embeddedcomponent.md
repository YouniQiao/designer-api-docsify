# EmbeddedComponent

**EmbeddedComponent**组件用于支持在当前页面嵌入本应用内或满足跨应用权限条件的其他[EmbeddedUIExtensionAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-embeddeduiextensionability-embeddeduiextensionability-c.md)提供的UI。EmbeddedUIExtensionAbility运行在独立进程中，完成页面布局和渲染。
通常用于需要进程隔离的模块化开发场景。
> **说明：**>> EmbeddedComponent组件宽高默认值和最小值均为10vp。> 不支持如下与宽高相关的属性：“constraintSize”、“aspectRatio”、“layoutWeight”、“flexBasis”、“flexGrow”和“flexShrink”。

## 约束

**EmbeddedComponent**仅支持在拥有多进程权限的设备上使用。  
**EmbeddedComponent**只能在UIAbility中使用，且默认情况下被拉起的EmbeddedUIExtensionAbility需与UIAbility属于同一应用。 从API版本26.0.0开始，在同时满足以下条件时，允许**EmbeddedComponent**跨应用拉起EmbeddedUIExtensionAbility：  
- **EmbeddedComponent**所属应用申请了ohos.permission.SUPPORT_CROSS_APP_EMBED_FOR_OA权限（该权限仅企业普通应用可申请）；  
- 该应用的appIdentifier在EmbeddedUIExtensionAbility支持的应用清单（即extensionAbilities标签的appIdentifierAllowList属性）中。

## 子组件

不支持

## EmbeddedComponent

```TypeScript
EmbeddedComponent(
  loader: import('../api/@ohos.app.ability.Want').default,
  type: EmbeddedType
)
```

创建跨进程嵌入式组件，用于显示同包名或满足跨应用权限条件的EmbeddedUIExtensionAbility的UI。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loader | import('../api/@ohos.app.ability.Want').default | 是 |
| type | [EmbeddedType](../arkts-apis/arkts-arkui-embeddedtype-e.md) | 是 |

## EmbeddedComponent

```TypeScript
EmbeddedComponent(
  loader: import('../api/@ohos.app.ability.Want').default,
  type: EmbeddedType,
  options?: EmbeddedOptions
)
```

创建跨进程嵌入式组件，用于显示同包名或满足跨应用权限条件的EmbeddedUIExtensionAbility的UI。相对于API version 12的接口，新增options参数用于传递构造参数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loader | import('../api/@ohos.app.ability.Want').default | 是 |
| type | [EmbeddedType](../arkts-apis/arkts-arkui-embeddedtype-e.md) | 是 |
| options | [EmbeddedOptions](arkts-arkui-embeddedoptions-i.md) | 否 |

## 汇总

### 接口

| 名称 |
| --- |

### 枚举

| 名称 |
| --- |
