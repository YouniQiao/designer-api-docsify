# UIExtensionComponent

**UIExtensionComponent** is used to embed UIs provided by other applications in the local application UI. The embedded content runs in another process, and the local application does not participate in its layout and rendering. It is usually used in modular development scenarios where process isolation is required.

## Constraints This component does not support preview. The ability to be started must be a UIExtensionAbility, an extension ability with UI. For details about how to implement a UIExtensionAbility, see [@ohos.app.ability.UIExtensionAbility (Base Class for ExtensionAbilities with UI)](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability). The width and height of the component must be explicitly set to non-zero valid values. The scenario where scrolling continues after the edge is reached is not supported. When both the **UIExtensionComponent** host and the UIExtensionAbility support content scrolling, gesture-based scrolling will cause simultaneous responses from both inside and outside the **UIExtensionComponent**. This includes, but is not limited to, scrollable containers such as Scroll, Swiper, List, and Grid. For details about how to avoid the simultaneous scrolling inside and outside the **UIExtensionComponent**, see [Example 2](../../../reference/apis-arkui/arkui-ts/ts-container-ui-extension-component-sys.md#example-2-isolating-scrolling-inside-and-outside-of-uiextensioncomponent). ###### Child Components Not supported

## UIExtensionComponent

```TypeScript
UIExtensionComponent(
    want: import('../api/@ohos.app.ability.Want').default,
    options?: UIExtensionOptions
  )
```

Construct the UIExtensionComponent.<br/> Called when the UIExtensionComponent is used.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: UIExtensionOptions  ): UIExtensionComponentAttribute--><!--Device-UIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: UIExtensionOptions  ): UIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | import('../api/@ohos.app.ability.Want').default | Yes |
| options | [UIExtensionOptions](arkts-arkui-uiextensionoptions-i-sys.md) | No |

## Summary

- [TerminationInfo](arkts-arkui-terminationinfo-i-sys.md)
- [UIExtensionOptions](arkts-arkui-uiextensionoptions-i-sys.md)
- [UIExtensionProxy](arkts-arkui-uiextensionproxy-i-sys.md)
- [ReceiveCallback](arkts-arkui-receivecallback-t-sys.md)
- [DpiFollowStrategy](arkts-arkui-dpifollowstrategy-e-sys.md)
- [WindowModeFollowStrategy](arkts-arkui-windowmodefollowstrategy-e-sys.md)
