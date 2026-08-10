# SecurityUIExtensionComponent

**SecurityUIExtensionComponent**用于将其他应用提供的UI嵌入到当前页面中。显示的内容运行在另一个进程中，当前应用不参与其布局和渲染。

通常用于需要进程隔离的模块化开发场景。目前，**SecurityUIExtensionComponent**只能启动[PhotoPicker]{@link @ohos.file.PhotoPickerComponent}类型的**UIExtensionAbility**。

## 子组件

无

## SecurityUIExtensionComponent

```TypeScript
SecurityUIExtensionComponent(
    want: import('../api/@ohos.app.ability.Want').default,
    options?: SecurityUIExtensionOptions
  )
```

创建**SecurityUIExtensionComponent**组件，用于嵌入显示远程**UIExtensionAbility**提供的UI。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: SecurityUIExtensionOptions  ): SecurityUIExtensionComponentAttribute--><!--Device-SecurityUIExtensionComponentInterface-(    want: import('../api/@ohos.app.ability.Want').default,    options?: SecurityUIExtensionOptions  ): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | import('../api/@ohos.app.ability.Want').default | Yes | 要加载的Ability信息。 通过bundleName和abilityName共同确定被拉起的UIExtensionAbility， 同时需要在parameters中配置ability.want.params.uiExtensionType字段指定UIExtensionAbility的类型， 当前仅支持'sysPicker/photoPicker'。 |
| options | [SecurityUIExtensionOptions](../arkts-apis/arkts-arkui-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md) | No | 用于构造**SecurityUIExtensionComponent**的参数。不填时各字段使用默认值。 |

## Summary

- [SecurityUIExtensionOptions](arkts-arkui-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md)
- [SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)
- [TerminationInfo](arkts-arkui-securityuiextensioncomponent-terminationinfo-i-sys.md)
- [SecurityDpiFollowStrategy](arkts-arkui-securityuiextensioncomponent-securitydpifollowstrategy-e-sys.md)
