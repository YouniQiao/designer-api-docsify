# ShortcutWant (System API)

Describes a collection of target [Wants](../../../quick-start/module-configuration-file.md#wants) information defined within a shortcut.

**Since:** 23

<!--Device-unnamed-export interface ShortcutWant--><!--Device-unnamed-export interface ShortcutWant-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

## parameters

```TypeScript
parameters?: Array<ParameterItem>
```

Custom data for launching the shortcut. The data must be strings. Both keys and values can be strings up to 1024 characters long.

**Type:** Array&lt;[ParameterItem](arkts-ability-shortcutinfo-parameteritem-i-sys.md)&gt;

**Since:** 23

<!--Device-ShortcutWant-parameters?: Array<ParameterItem>--><!--Device-ShortcutWant-parameters?: Array<ParameterItem>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

## targetAbility

```TypeScript
targetAbility: string
```

Target ability name of the shortcut.

**Type:** string

**Since:** 23

<!--Device-ShortcutWant-targetAbility: string--><!--Device-ShortcutWant-targetAbility: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

## targetBundle

```TypeScript
targetBundle: string
```

Target bundle name of the shortcut.

**Type:** string

**Since:** 23

<!--Device-ShortcutWant-targetBundle: string--><!--Device-ShortcutWant-targetBundle: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

## targetModule

```TypeScript
targetModule?: string
```

Target module name of the shortcut.

**Type:** string

**Since:** 23

<!--Device-ShortcutWant-targetModule?: string--><!--Device-ShortcutWant-targetModule?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

