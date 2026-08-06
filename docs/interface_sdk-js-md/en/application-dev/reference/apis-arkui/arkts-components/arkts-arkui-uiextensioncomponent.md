# UIExtensionComponent

**UIExtensionComponent** is used to embed UIs provided by other applications in the local application UI. The
embedded content runs in another process, and the local application does not participate in its layout and rendering.

It is usually used in modular development scenarios where process isolation is required.

## Constraints

This component does not support preview.

The ability to be started must be a UIExtensionAbility, an extension ability with UI. For details about how to implement a UIExtensionAbility, see  
[@ohos.app.ability.UIExtensionAbility (Base Class for ExtensionAbilities with UI)]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

The width and height of the component must be explicitly set to non-zero valid values.

The scenario where scrolling continues after the edge is reached is not supported. When both the  
**UIExtensionComponent** host and the UIExtensionAbility support content scrolling, gesture-based scrolling will cause simultaneous responses from both inside and outside the **UIExtensionComponent**. This includes, but is not limited to, scrollable containers such as [Scroll]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, [Swiper]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, [List]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_,and [Grid]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_. For details about how to avoid the simultaneous scrolling inside and outside the  
**UIExtensionComponent**, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

## Child Components

Not supported

## UIExtensionComponent

```TypeScript
UIExtensionComponent(
    want: import('../api/@ohos.app.ability.Want').default,
    options?: UIExtensionOptions
  )
```

Construct the UIExtensionComponent.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Called when the UIExtensionComponent is used.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: UIExtensionOptions  ): UIExtensionComponentAttribute--><!--Device-UIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: UIExtensionOptions  ): UIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | import('../api/@ohos.app.ability.Want').default | Yes | Ability to start.  |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Construction parameters. |

## Summary

