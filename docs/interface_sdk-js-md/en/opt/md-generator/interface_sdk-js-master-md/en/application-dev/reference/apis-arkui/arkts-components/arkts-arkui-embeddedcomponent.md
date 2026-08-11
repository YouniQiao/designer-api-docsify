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
  loader: import('../api/@ohos.app.ability.Want').default,
  type: EmbeddedType
)
```

Creates a cross-process embedded component to display the UI of the EmbeddedUIExtensionAbility with the same bundle name.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EmbeddedComponentInterface-(  loader: import('../api/@ohos.app.ability.Want').default,  type: EmbeddedType): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentInterface-(  loader: import('../api/@ohos.app.ability.Want').default,  type: EmbeddedType): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| loader | import('../api/@ohos.app.ability.Want').default | Yes |
| type | [EmbeddedType](../arkts-apis/arkts-arkui-embeddedtype-e.md) | Yes |

## EmbeddedComponent

```TypeScript
EmbeddedComponent(
  loader: import('../api/@ohos.app.ability.Want').default,
  type: EmbeddedType,
  options?: EmbeddedOptions
)
```

Construct the EmbeddedComponent.&lt;br/&gt;Called when the EmbeddedComponent is used.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EmbeddedComponentInterface-(  loader: import('../api/@ohos.app.ability.Want').default,  type: EmbeddedType,  options?: EmbeddedOptions): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentInterface-(  loader: import('../api/@ohos.app.ability.Want').default,  type: EmbeddedType,  options?: EmbeddedOptions): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| loader | import('../api/@ohos.app.ability.Want').default | Yes |
| type | [EmbeddedType](../arkts-apis/arkts-arkui-embeddedtype-e.md) | Yes |
| options | [EmbeddedOptions](arkts-arkui-embeddedoptions-i.md) | No |

## Summary

- [EmbeddedOptions](arkts-arkui-embeddedcomponent-embeddedoptions-i.md)
- [TerminationInfo](arkts-arkui-embeddedcomponent-terminationinfo-i.md)
- [EmbeddedDpiFollowStrategy](arkts-arkui-embeddedcomponent-embeddeddpifollowstrategy-e.md)
- [EmbeddedWindowModeFollowStrategy](arkts-arkui-embeddedcomponent-embeddedwindowmodefollowstrategy-e.md)
