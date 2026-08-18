# SecurityUIExtensionComponent

**SecurityUIExtensionComponent** is used to embed the UI provided by another application on the current page. The displayed content runs in another process, and the current application does not participate in its layout and rendering. It is typically used in modular development scenarios that require process isolation. Currently, **SecurityUIExtensionComponent** can only start **UIExtensionAbility** of the [PhotoPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-photopickercomponent-s.md#photopickercomponent) type.

## Child Components None

## SecurityUIExtensionComponent

```TypeScript
SecurityUIExtensionComponent(
    want: import('../api/@ohos.app.ability.Want').default,
    options?: SecurityUIExtensionOptions
  )
```

Creates a **SecurityUIExtensionComponent** component to embed and display the UI provided by a remote [UIExtensionAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: SecurityUIExtensionOptions  ): SecurityUIExtensionComponentAttribute--><!--Device-SecurityUIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: SecurityUIExtensionOptions  ): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | import('../api/@ohos.app.ability.Want').default | Yes |
| options | [SecurityUIExtensionOptions](arkts-arkui-securityuiextensionoptions-i-sys.md) | No |

## Summary

- [SecurityUIExtensionOptions](arkts-arkui-securityuiextensionoptions-i-sys.md)
- [SecurityUIExtensionProxy](arkts-arkui-securityuiextensionproxy-i-sys.md)
- [TerminationInfo](arkts-arkui-terminationinfo-i-sys.md)
- [SecurityDpiFollowStrategy](arkts-arkui-securitydpifollowstrategy-e-sys.md)
