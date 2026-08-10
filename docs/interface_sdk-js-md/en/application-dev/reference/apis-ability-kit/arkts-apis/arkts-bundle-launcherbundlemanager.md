# @ohos.bundle.launcherBundleManager

本模块支持launcher应用（桌面有图标的应用）所需的查询能力，支持  
[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-i.md)信息的查询。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace launcherBundleManager--><!--Device-unnamed-declare namespace launcherBundleManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## Modules to Import

```TypeScript
import { launcherBundleManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getLauncherAbilityInfoSync](arkts-ability-launcherbundlemanager-getlauncherabilityinfosync-f.md#getlauncherabilityinfosync) | 查询指定bundleName及用户的[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-i.md)。 |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getalllauncherabilityinfo) | 查询指定用户下所有应用的[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-i.md)。使用callback异步回调。 |
| [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getalllauncherabilityinfo-1) | 查询指定用户下所有应用的[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-i.md)。使用Promise异步回调。 |
| [getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md#getlauncherabilityinfo) | 查询指定bundleName及用户的[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-i.md)。使用callback异步回调。 |
| [getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md#getlauncherabilityinfo-1) | 查询指定bundleName及用户的[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-i.md)。使用Promise异步回调。 |
| [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getshortcutinfo) | 查询当前用户下指定应用的快捷方式信息[ShortcutInfo](arkts-ability-shortcutinfo-i.md)，只支持查询主应用的ShortcutInfo，查询分身应用请使用  [getShortcutInfoByAppIndex](arkts-ability-launcherbundlemanager-getshortcutinfobyappindex-f-sys.md#getshortcutinfobyappindex)。使用callback异步回调。  获取调用方自身的信息时不需要权限。 |
| [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getshortcutinfo-1) | 查询当前用户下指定应用的快捷方式信息[ShortcutInfo](arkts-ability-shortcutinfo-i.md)，只支持查询主应用的ShortcutInfo，查询分身应用请使用  [getShortcutInfoByAppIndex](arkts-ability-launcherbundlemanager-getshortcutinfobyappindex-f-sys.md#getshortcutinfobyappindex)。使用Promise异步回调。  获取调用方自身的信息时不需要权限。 |
| [getShortcutInfoByAppIndex](arkts-ability-launcherbundlemanager-getshortcutinfobyappindex-f-sys.md#getshortcutinfobyappindex) | 查询当前用户下指定分身应用的快捷方式信息[ShortcutInfo](arkts-ability-shortcutinfo-i.md)。  调用方获取自己的信息时不需要权限。 |
| [getShortcutInfoSync](arkts-ability-launcherbundlemanager-getshortcutinfosync-f-sys.md#getshortcutinfosync) | 查询当前用户下指定应用的快捷方式信息[ShortcutInfo](arkts-ability-shortcutinfo-i.md)，只支持查询主应用的ShortcutInfo，查询分身应用请使用  [getShortcutInfoByAppIndex](arkts-ability-launcherbundlemanager-getshortcutinfobyappindex-f-sys.md#getshortcutinfobyappindex)。  获取调用方自身的信息时不需要权限。 |
| [getShortcutInfoSync](arkts-ability-launcherbundlemanager-getshortcutinfosync-f-sys.md#getshortcutinfosync-1) | 查询指定用户下指定应用的快捷方式信息[ShortcutInfo](arkts-ability-shortcutinfo-i.md)，只支持查询主应用的ShortcutInfo，查询分身应用请使用  [getShortcutInfoByAppIndex](arkts-ability-launcherbundlemanager-getshortcutinfobyappindex-f-sys.md#getshortcutinfobyappindex)。  获取调用方自身的信息时不需要权限。 |
| [startShortcut](arkts-ability-launcherbundlemanager-startshortcut-f-sys.md#startshortcut) | 拉起指定[ShortcutInfo](arkts-ability-shortcutinfo-i.md)中的ability。使用Promise异步回调。 |
| [startShortcutWithReason](arkts-ability-launcherbundlemanager-startshortcutwithreason-f-sys.md#startshortcutwithreason) | 根据指定的快捷方式信息，拉起对应的Ability，并携带快捷方式的启动原因。使用Promise异步回调。  被拉起方可以通过[LaunchParam](arkts-ability-abilityconstant-launchparam-i.md)的launchReasonMessage字段获取到启动原因，并根据启动原因进行业务逻辑处理。 |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [LauncherAbilityInfo](arkts-ability-launcherbundlemanager-launcherabilityinfo-t.md) | LauncherAbilityInfo信息。 |
| [ParameterItem](arkts-ability-launcherbundlemanager-parameteritem-t.md) | 快捷方式配置信息中的自定义数据。 |
| [ShortcutInfo](arkts-ability-launcherbundlemanager-shortcutinfo-t.md) | 应用[module.json5配置文件](../../../quick-start/module-configuration-file.md#shortcuts标签)中定义的快捷方式信息。 |
| [ShortcutWant](arkts-ability-launcherbundlemanager-shortcutwant-t.md) | 快捷方式内定义的目标[wants](../../../quick-start/module-configuration-file.md#wants标签)信息集合。 |

