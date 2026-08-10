# @ohos.bundle.bundleMonitor

本模块提供监听应用安装，卸载，更新的能力。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace bundleMonitor--><!--Device-unnamed-declare namespace bundleMonitor-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { bundleMonitor } from 'kits/@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [off](arkts-ability-bundlemonitor-off-f-sys.md#off) | 注销监听应用的安装，卸载，更新。使用callback异步回调。 |
| [offAdd](arkts-ability-bundlemonitor-offadd-f-sys.md#offadd) | 注销监听应用的安装。 |
| [offRemove](arkts-ability-bundlemonitor-offremove-f-sys.md#offremove) | 注销监听应用的卸载。 |
| [offUpdate](arkts-ability-bundlemonitor-offupdate-f-sys.md#offupdate) | 注销监听应用的更新。 |
| [on](arkts-ability-bundlemonitor-on-f-sys.md#on) | 注册监听应用的安装、卸载、更新。使用callback异步回调。 |
| [onAdd](arkts-ability-bundlemonitor-onadd-f-sys.md#onadd) | 注册监听应用的安装。 |
| [onRemove](arkts-ability-bundlemonitor-onremove-f-sys.md#onremove) | 注册监听应用的卸载。 |
| [onUpdate](arkts-ability-bundlemonitor-onupdate-f-sys.md#onupdate) | 注册监听应用的更新。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [BundleChangedInfo](arkts-ability-bundlemonitor-bundlechangedinfo-i-sys.md) | 应用变更信息。 |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [BundleChangedEvent](arkts-ability-bundlemonitor-bundlechangedevent-t-sys.md) | 监听的事件类型。 |
<!--DelEnd-->

