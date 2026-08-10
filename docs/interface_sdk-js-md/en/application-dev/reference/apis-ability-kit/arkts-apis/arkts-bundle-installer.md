# @ohos.bundle.installer

在设备上安装、升级和卸载应用。

> **说明：**
> 
> 本模块为系统接口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace installer--><!--Device-unnamed-declare namespace installer-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { installer } from 'kits/@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getBundleInstaller](arkts-ability-installer-getbundleinstaller-f-sys.md#getbundleinstaller) | 获取BundleInstaller对象。使用callback异步回调。 |
| [getBundleInstaller](arkts-ability-installer-getbundleinstaller-f-sys.md#getbundleinstaller-1) | 获取BundleInstaller对象。使用Promise异步回调。 |
| [getBundleInstallerSync](arkts-ability-installer-getbundleinstallersync-f-sys.md#getbundleinstallersync) | 获取并返回BundleInstaller对象。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [BundleInstaller](arkts-ability-installer-bundleinstaller-i-sys.md) | Bundle installer interface, include install uninstall recover. |
| [CreateAppCloneParam](arkts-ability-installer-createappcloneparam-i-sys.md) | 创建分身应用可指定的参数信息。 |
| [DestroyAppCloneParam](arkts-ability-installer-destroyappcloneparam-i-sys.md) | 删除分身应用可指定的参数信息。 |
| [HashParam](arkts-ability-installer-hashparam-i-sys.md) | 应用程序安装卸载哈希参数信息。 |
| [InstallParam](arkts-ability-installer-installparam-i-sys.md) | 应用程序安装、卸载或恢复需指定的参数信息。 |
| [PGOParam](arkts-ability-installer-pgoparam-i-sys.md) | PGO（Profile-guided Optimization）配置文件参数信息。 |
| [Parameters](arkts-ability-installer-parameters-i-sys.md) | 扩展参数信息。 |
| [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) | 插件应用安装、卸载的参数信息。 |
| [UninstallParam](arkts-ability-installer-uninstallparam-i-sys.md) | 共享包卸载需指定的参数信息。 |
| [VerifyCodeParam](arkts-ability-installer-verifycodeparam-i-sys.md) | 应用程序代码签名文件信息。 |
<!--DelEnd-->

