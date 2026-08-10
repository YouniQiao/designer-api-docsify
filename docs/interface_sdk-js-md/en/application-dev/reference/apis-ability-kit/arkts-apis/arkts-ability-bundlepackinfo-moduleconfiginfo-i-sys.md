# ModuleConfigInfo (System API)

包的module配置信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ModuleConfigInfo--><!--Device-unnamed-export interface ModuleConfigInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## abilities

```TypeScript
readonly abilities: Array<ModuleAbilityInfo>
```

module包含的ability组件信息。

**Type:** Array&lt;ModuleAbilityInfo&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ModuleConfigInfo-readonly abilities: Array<ModuleAbilityInfo>--><!--Device-ModuleConfigInfo-readonly abilities: Array<ModuleAbilityInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## apiVersion

```TypeScript
readonly apiVersion: ApiVersion
```

module的api版本。

**Type:** [ApiVersion](arkts-ability-freeinstall-apiversion-t-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ModuleConfigInfo-readonly apiVersion: ApiVersion--><!--Device-ModuleConfigInfo-readonly apiVersion: ApiVersion-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## deviceTypes

```TypeScript
readonly deviceTypes: Array<string>
```

module的设备类型。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ModuleConfigInfo-readonly deviceTypes: Array<string>--><!--Device-ModuleConfigInfo-readonly deviceTypes: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## distro

```TypeScript
readonly distro: ModuleDistroInfo
```

module发行版信息。

**Type:** [ModuleDistroInfo](arkts-ability-freeinstall-moduledistroinfo-t-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ModuleConfigInfo-readonly distro: ModuleDistroInfo--><!--Device-ModuleConfigInfo-readonly distro: ModuleDistroInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## extensionAbilities

```TypeScript
readonly extensionAbilities: Array<ExtensionAbility>
```

描述extensionAbilities的配置信息。

**Type:** Array&lt;ExtensionAbility&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ModuleConfigInfo-readonly extensionAbilities: Array<ExtensionAbility>--><!--Device-ModuleConfigInfo-readonly extensionAbilities: Array<ExtensionAbility>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## mainAbility

```TypeScript
readonly mainAbility: string
```

应用主ability的名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ModuleConfigInfo-readonly mainAbility: string--><!--Device-ModuleConfigInfo-readonly mainAbility: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

