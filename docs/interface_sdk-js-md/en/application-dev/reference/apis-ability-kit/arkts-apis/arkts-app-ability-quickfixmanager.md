# @ohos.app.ability.quickFixManager

quickFixManager模块提供快速修复的能力，快速修复是系统提供给开发者的一种技术手段，支持开发者以远快于（小时级、分钟级）应用升级的方式进行缺陷修复。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace quickFixManager--><!--Device-unnamed-declare namespace quickFixManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.QuickFix

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { quickFixManager } from 'kits/@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [applyQuickFix](arkts-ability-quickfixmanager-applyquickfix-f-sys.md#applyquickfix) | 快速修复的补丁安装接口。使用callback异步回调。 |
| [applyQuickFix](arkts-ability-quickfixmanager-applyquickfix-f-sys.md#applyquickfix-1) | 快速修复的补丁安装接口。使用Promise异步回调。 |
| [getApplicationQuickFixInfo](arkts-ability-quickfixmanager-getapplicationquickfixinfo-f-sys.md#getapplicationquickfixinfo) | 获取应用的快速修复信息。使用callback异步回调。 |
| [getApplicationQuickFixInfo](arkts-ability-quickfixmanager-getapplicationquickfixinfo-f-sys.md#getapplicationquickfixinfo-1) | 获取应用的快速修复信息。使用Promise异步回调。 |
| [revokeQuickFix](arkts-ability-quickfixmanager-revokequickfix-f-sys.md#revokequickfix) | 撤销快速修复的接口，使用callback方式返回结果。 |
| [revokeQuickFix](arkts-ability-quickfixmanager-revokequickfix-f-sys.md#revokequickfix-1) | 撤销快速修复的接口。使用Promise异步回调。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ApplicationQuickFixInfo](arkts-ability-quickfixmanager-applicationquickfixinfo-i-sys.md) | 应用级别的快速修复信息。 |
| [HapModuleQuickFixInfo](arkts-ability-quickfixmanager-hapmodulequickfixinfo-i-sys.md) | hap级别的快速修复信息。 |
<!--DelEnd-->

