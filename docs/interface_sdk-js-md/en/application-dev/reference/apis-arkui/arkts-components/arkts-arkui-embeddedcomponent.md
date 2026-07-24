# EmbeddedComponent

The **EmbeddedComponent** is a component used to embed into the current page the UI provided by another
[EmbeddedUIExtensionAbility]{@link @ohos.app.ability.EmbeddedUIExtensionAbility:EmbeddedUIExtensionAbility} in the
same application. The EmbeddedUIExtensionAbility runs in an independent process for UI layout and rendering.

It is usually used in modular development scenarios where process isolation is required.

> **NOTE**

## Constraints

The **EmbeddedComponent** is supported only on devices configured with multi-process permissions.

The **EmbeddedComponent** can be used only in the UIAbility, and the EmbeddedUIExtensionAbility to start must belong to the same application as the UIAbility.

## Child Components

Not supported

## EmbeddedComponent

```TypeScript
EmbeddedComponent(
  loader: import('../api/type: EmbeddedType
)
```

Creates a cross-process embedded component to display the UI of the EmbeddedUIExtensionAbility with the same bundle name.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EmbeddedComponentInterface-(  loader: import('../api/type: EmbeddedType): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentInterface-(  loader: import('../api/type: EmbeddedType): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | import('../api/@ohos.app.ability.Want').default | Yes | EmbeddedUIExtensionAbility to load.  |
| type | [EmbeddedType](../arkts-apis/arkts-arkui-embeddedtype-e.md) | Yes | Type of the provider.  |

## EmbeddedComponent

```TypeScript
EmbeddedComponent(
  loader: import('../api/type: EmbeddedType,
  options?: EmbeddedOptions
)
```

Construct the EmbeddedComponent.<br/>Called when the EmbeddedComponent is used.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EmbeddedComponentInterface-(  loader: import('../api/type: EmbeddedType,  options?: EmbeddedOptions): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentInterface-(  loader: import('../api/type: EmbeddedType,  options?: EmbeddedOptions): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | import('../api/@ohos.app.ability.Want').default | Yes | indicates initialization parameter.  |
| type | [EmbeddedType](../arkts-apis/arkts-arkui-embeddedtype-e.md) | Yes | indicates type of the EmbeddedComponent.  |
| options | [EmbeddedOptions](arkts-arkui-embeddedoptions-i.md) | No | construction configuration of EmbeddedComponent.  |

## Summary

- [EmbeddedOptions](arkts-arkui-embeddedcomponent-embeddedoptions-i.md)
- [TerminationInfo](arkts-arkui-embeddedcomponent-terminationinfo-i.md)
- [EmbeddedDpiFollowStrategy](arkts-arkui-embeddedcomponent-embeddeddpifollowstrategy-e.md)
- [EmbeddedWindowModeFollowStrategy](arkts-arkui-embeddedcomponent-embeddedwindowmodefollowstrategy-e.md)
