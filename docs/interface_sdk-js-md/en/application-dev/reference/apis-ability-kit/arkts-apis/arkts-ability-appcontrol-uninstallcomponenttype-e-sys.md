# UninstallComponentType (System API)

标识卸载时功能组件类型。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-appControl-export enum UninstallComponentType--><!--Device-appControl-export enum UninstallComponentType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## EXTENSION

```TypeScript
EXTENSION = 1
```

服务扩展能力类型。仅支持service类型的[ExtensionAbility](../../../quick-start/module-configuration-file.md#extensionabilities标签)。

被拉起的ExtensionAbility通过want中bundleName、moduleName、abilityName字段共同确定。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-UninstallComponentType-EXTENSION = 1--><!--Device-UninstallComponentType-EXTENSION = 1-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## UI_EXTENSION

```TypeScript
UI_EXTENSION = 2
```

UI扩展能力类型。

被拉起的UIExtensionAbility通过want中bundleName、moduleName、abilityName字段共同确定，同时want.parameters中的ability.want.params.uiExtensionType字段需要配置为  
[UIExtensionAbility](../../../application-models/uiextensionability-sys.md)的类型。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-UninstallComponentType-UI_EXTENSION = 2--><!--Device-UninstallComponentType-UI_EXTENSION = 2-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

