# @ohos.bundle.pluginBundleManager

本模块提供应用对自分发插件的管理能力，包括安装、卸载本地插件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace pluginBundleManager--><!--Device-unnamed-declare namespace pluginBundleManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## Modules to Import

```TypeScript
import { pluginBundleManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAllLocalPluginInfoForSelf](arkts-ability-pluginbundlemanager-getalllocalplugininfoforself-f.md#getalllocalplugininfoforself) | 查询当前应用中所有自分发插件的信息。使用Promise异步回调。 |
| [installLocalPlugin](arkts-ability-pluginbundlemanager-installlocalplugin-f.md#installlocalplugin) | 为当前应用安装自分发插件（即应用通过自有渠道分发、自主管理的插件）。使用Promise异步回调。 |
| [uninstallLocalPlugin](arkts-ability-pluginbundlemanager-uninstalllocalplugin-f.md#uninstalllocalplugin) | 卸载当前应用已通过自分发方式安装的指定插件。使用Promise异步回调。 |

### Types

| Name | Description |
| --- | --- |
| [PluginBundleInfo](arkts-ability-pluginbundlemanager-pluginbundleinfo-t.md) | 插件信息。 |
| [PluginModuleInfo](arkts-ability-pluginbundlemanager-pluginmoduleinfo-t.md) | 插件的模块信息。 |

