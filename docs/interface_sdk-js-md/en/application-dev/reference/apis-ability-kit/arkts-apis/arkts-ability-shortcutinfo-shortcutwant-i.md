# ShortcutWant

Describes a collection of target [Wants](../../../quick-start/module-configuration-file.md#wants) information defined within a shortcut.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## parameters

```TypeScript
parameters?: Array<ParameterItem>
```

Custom data for launching the shortcut. The data must be strings. Both keys and values can be strings up to 1024 characters long.

**Type:** Array&lt;[ParameterItem](arkts-ability-shortcutinfo-parameteritem-i.md)&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## targetAbility

```TypeScript
targetAbility: string
```

Target ability name of the shortcut.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## targetBundle

```TypeScript
targetBundle: string
```

Target bundle name of the shortcut.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## targetModule

```TypeScript
targetModule?: string
```

Target module name of the shortcut.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher
