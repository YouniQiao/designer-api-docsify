# setUninstallDisposedRule (System API)

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## setUninstallDisposedRule

```TypeScript
function setUninstallDisposedRule(appIdentifier: string, rule: UninstallDisposedRule, appIndex?: int): void
```

设置指定应用或分身应用的卸载处置规则。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function setUninstallDisposedRule(appIdentifier: string, rule: UninstallDisposedRule, appIndex?: int): void--><!--Device-appControl-function setUninstallDisposedRule(appIdentifier: string, rule: UninstallDisposedRule, appIndex?: int): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appIdentifier | string | Yes | 要设置卸载处置规则的应用的appIdentifier。&lt;br&gt; 如果应用没有appIdentifier可使用appId代替。appId是应用的唯一标识，由应用 Bundle名称和签名信息决定，获取方法参见[获取应用的appId](../../../quick-start/common-problem-of-application.md#如何获取应用信息中的appid)。 |
| rule | [UninstallDisposedRule](arkts-ability-appcontrol-uninstalldisposedrule-i-sys.md) | Yes | 表示要设置的卸载处置规则。 |
| appIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 表示分身应用的索引，默认值为0。&lt;br&gt; appIndex为0时，表示设置主应用的卸载处置规则。appIndex大于0时，表示设置指定分身应用的卸载处置规则。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 17700061 | AppIndex is not in the valid range. |
| 17700074 | The specified appIdentifier is invalid. |
| 17700075 | The specified bundleName of want is not the same with caller. |
| 201 | Permission denied. |
| 202 | Permission denied. A non-system application is not allowed to call a system API. |

