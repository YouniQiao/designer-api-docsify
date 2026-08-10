# innerBundleManager

本模块提供launcher应用使用的接口。

> **说明：**
> 
> 本模块从API version 9开始不再支持。建议使用[launcherBundleManager](arkts-bundle-launcherbundlemanager.md)
> 及[bundleMonitor](arkts-bundle-bundlemonitor.md)替代。
> 
> 本模块为系统接口。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.launcherBundleManager:launcherBundleManager](arkts-bundle-launcherbundlemanager.md)

<!--Device-unnamed-declare namespace innerBundleManager--><!--Device-unnamed-declare namespace innerBundleManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { BundleStatusCallback } from 'kits/@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getLauncherAbilityInfos](arkts-ability-innerbundlemanager-getlauncherabilityinfos-f-sys.md#getlauncherabilityinfos) | 根据给定的Bundle名称获取LauncherAbilityInfos，使用callback异步回调。 |
| [getLauncherAbilityInfos](arkts-ability-innerbundlemanager-getlauncherabilityinfos-f-sys.md#getlauncherabilityinfos-1) | 根据给定的Bundle名称获取LauncherAbilityInfos，使用Promise异步回调。 |
| [on](arkts-ability-innerbundlemanager-on-f-sys.md#on) | 注册Callback。 |
| [on](arkts-ability-innerbundlemanager-on-f-sys.md#on-1) | 注册Callback。 |
| [off](arkts-ability-innerbundlemanager-off-f-sys.md#off) | 取消注册Callback。 |
| [off](arkts-ability-innerbundlemanager-off-f-sys.md#off-1) | 取消注册Callback。 |
| [getAllLauncherAbilityInfos](arkts-ability-innerbundlemanager-getalllauncherabilityinfos-f-sys.md#getalllauncherabilityinfos) | 获取所有的LauncherAbilityInfos，使用callback异步回调。 |
| [getAllLauncherAbilityInfos](arkts-ability-innerbundlemanager-getalllauncherabilityinfos-f-sys.md#getalllauncherabilityinfos-1) | 获取LauncherAbilityInfos，使用Promise异步回调。 |
| [getShortcutInfos](arkts-ability-innerbundlemanager-getshortcutinfos-f-sys.md#getshortcutinfos) | 根据给定的Bundle名称获取快捷方式信息，使用callback异步回调。 |
| [getShortcutInfos](arkts-ability-innerbundlemanager-getshortcutinfos-f-sys.md#getshortcutinfos-1) | 根据给定的Bundle名称获取快捷方式信息，使用Promise异步回调。 |
<!--DelEnd-->

