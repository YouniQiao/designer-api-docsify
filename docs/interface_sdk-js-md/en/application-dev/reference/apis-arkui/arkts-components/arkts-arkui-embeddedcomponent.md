# EmbeddedComponent

**EmbeddedComponent**组件用于支持在当前页面嵌入本应用内或满足跨应用权限条件的其他[EmbeddedUIExtensionAbility]{@link @ohos.app.ability.EmbeddedUIExtensionAbility:EmbeddedUIExtensionAbility}提供的UI。EmbeddedUIExtensionAbility运行在独立进程中，完成页面布局和渲染。

通常用于需要进程隔离的模块化开发场景。

> **说明：**
>
> EmbeddedComponent组件宽高默认值和最小值均为10vp。
> 不支持如下与宽高相关的属性：“constraintSize”、“aspectRatio”、“layoutWeight”、“flexBasis”、“flexGrow”和“flexShrink”。

## 约束

**EmbeddedComponent**仅支持在拥有多进程权限的设备上使用。

**EmbeddedComponent**只能在UIAbility中使用，且默认情况下被拉起的EmbeddedUIExtensionAbility需与UIAbility属于同一应用。从API版本26.0.0开始，在同时满足以下条件时，允许**EmbeddedComponent**跨应用拉起EmbeddedUIExtensionAbility：  
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

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EmbeddedComponentInterface-(  loader: import('../api/@ohos.app.ability.Want').default,  type: EmbeddedType): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentInterface-(  loader: import('../api/@ohos.app.ability.Want').default,  type: EmbeddedType): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | import('../api/@ohos.app.ability.Want').default | Yes | 表示要加载的EmbeddedUIExtensionAbility。 |
| type | [EmbeddedType](../arkts-apis/arkts-arkui-embeddedtype-e.md) | Yes | 提供方的类型。 |

## EmbeddedComponent

```TypeScript
EmbeddedComponent(
  loader: import('../api/@ohos.app.ability.Want').default,
  type: EmbeddedType,
  options?: EmbeddedOptions
)
```

创建跨进程嵌入式组件，用于显示同包名或满足跨应用权限条件的EmbeddedUIExtensionAbility的UI。相对于API version 12的接口，新增options参数用于传递构造参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EmbeddedComponentInterface-(  loader: import('../api/@ohos.app.ability.Want').default,  type: EmbeddedType,  options?: EmbeddedOptions): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentInterface-(  loader: import('../api/@ohos.app.ability.Want').default,  type: EmbeddedType,  options?: EmbeddedOptions): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | import('../api/@ohos.app.ability.Want').default | Yes | 要加载的EmbeddedUIExtensionAbility。 |
| type | [EmbeddedType](../arkts-apis/arkts-arkui-embeddedtype-e.md) | Yes | 提供方的类型。 |
| options | [EmbeddedOptions](../arkts-apis/arkts-arkui-embeddedcomponent-embeddedoptions-i.md) | No | 嵌入式组件的可选配置项，用于设置占位符、DPI跟随策略、窗口模式跟随策略等。 |

## Summary

- [EmbeddedOptions](arkts-arkui-embeddedcomponent-embeddedoptions-i.md)
- [TerminationInfo](arkts-arkui-embeddedcomponent-terminationinfo-i.md)
- [EmbeddedDpiFollowStrategy](arkts-arkui-embeddedcomponent-embeddeddpifollowstrategy-e.md)
- [EmbeddedWindowModeFollowStrategy](arkts-arkui-embeddedcomponent-embeddedwindowmodefollowstrategy-e.md)
