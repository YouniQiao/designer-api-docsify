# SecurityUIExtensionComponent

**SecurityUIExtensionComponent** is used to embed the UI provided by another application on the current page. The
displayed content runs in another process, and the current application does not participate in its layout and
rendering.

It is typically used in modular development scenarios that require process isolation. Currently,
**SecurityUIExtensionComponent** can only start **UIExtensionAbility** of the
[PhotoPicker]{@link @ohos.file.PhotoPickerComponent} type.

## Child Components

None

## SecurityUIExtensionComponent

```TypeScript
SecurityUIExtensionComponent(
    want: import('../api/options?: SecurityUIExtensionOptions
  )
```

Creates a **SecurityUIExtensionComponent** component to embed and display the UI provided by a remote [UIExtensionAbility]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility}.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionComponentInterface-(    want: import('../api/options?: SecurityUIExtensionOptions  ): SecurityUIExtensionComponentAttribute--><!--Device-SecurityUIExtensionComponentInterface-(    want: import('../api/options?: SecurityUIExtensionOptions  ): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | import('../api/@ohos.app.ability.Want').default | Yes | Ability information to load. The **UIExtensionAbilit**y to be started is determined by both **bundleName** and **abilityName**. In addition, the **ability.want.params.uiExtensionType** field must be specified in **parameters** to indicate the type of the **UIExtensionAbility**. Currently, only **sysPicker/photoPicker** is supported.  |
| options | [SecurityUIExtensionOptions](arkts-arkui-securityuiextensionoptions-i-sys.md) | No | Options used to construct **SecurityUIExtensionComponent**. If this parameter is left empty, the default value is used for each field.  |

## Summary

- [SecurityUIExtensionOptions](arkts-arkui-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md)
- [SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)
- [TerminationInfo](arkts-arkui-securityuiextensioncomponent-terminationinfo-i-sys.md)
- [SecurityDpiFollowStrategy](arkts-arkui-securityuiextensioncomponent-securitydpifollowstrategy-e-sys.md)
