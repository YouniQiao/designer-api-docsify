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
    want: import('../api/@ohos.app.ability.Want').default,
    options?: SecurityUIExtensionOptions
  )
```

Creates a **SecurityUIExtensionComponent** component to embed and display the UI provided by a remote  
[UIExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: SecurityUIExtensionOptions  ): SecurityUIExtensionComponentAttribute--><!--Device-SecurityUIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: SecurityUIExtensionOptions  ): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | import('../api/@ohos.app.ability.Want').default | Yes | Ability information to load. The **UIExtensionAbilit**y to be started is determined by both **bundleName** and **abilityName**. In addition, the **ability.want.params.uiExtensionType** field must be specified in **parameters** to indicate the type of the **UIExtensionAbility**. Currently, only **sysPicker/photoPicker** is supported.  |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Options used to construct **SecurityUIExtensionComponent**. If this parameter is left empty, the default value is used for each field.  |

## Summary

