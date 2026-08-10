# ShortcutWant

快捷方式内定义的目标[wants](../../../quick-start/module-configuration-file.md#wants标签)信息集合。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ShortcutWant--><!--Device-unnamed-export interface ShortcutWant-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## parameters

```TypeScript
parameters?: Array<ParameterItem>
```

拉起快捷方式时的自定义数据，仅支持配置字符串类型的数据。其中键值均最大支持1024长度的字符串。

**Type:** Array&lt;ParameterItem&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ShortcutWant-parameters?: Array<ParameterItem>--><!--Device-ShortcutWant-parameters?: Array<ParameterItem>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## targetAbility

```TypeScript
targetAbility: string
```

快捷方式的目标组件名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutWant-targetAbility: string--><!--Device-ShortcutWant-targetAbility: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## targetBundle

```TypeScript
targetBundle: string
```

快捷方式的目标包名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutWant-targetBundle: string--><!--Device-ShortcutWant-targetBundle: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## targetModule

```TypeScript
targetModule?: string
```

快捷方式的目标模块名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutWant-targetModule?: string--><!--Device-ShortcutWant-targetModule?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

