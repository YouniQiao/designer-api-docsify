# deleteDisposedStatusSync (System API)

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## deleteDisposedStatusSync

```TypeScript
function deleteDisposedStatusSync(appId: string, appIndex?: int): void
```

以同步方法删除指定应用或分身应用的处置状态。成功返回null，失败抛出对应异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function deleteDisposedStatusSync(appId: string, appIndex?: int): void--><!--Device-appControl-function deleteDisposedStatusSync(appId: string, appIndex?: int): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | 要删除拦截规则的应用的appId或appIdentifier。使用appId设置的拦截规则只能通过appId删除，使用appIdentifier设置的同理。&lt;br/&gt; **说明：**&lt;br/&gt; appId是应用的唯一标识，由应用Bundle名称和签名信息决定，获取方法参见 [获取应用的appId](../../../quick-start/common-problem-of-application.md#如何获取应用信息中的appid)。&lt;br&gt; [appIdentifier](arkts-ability-bundleinfo-signatureinfo-i.md)也是应用的唯一标识，详情信息可参考 [什么是appIdentifier](../../../quick-start/common-problem-of-application.md#什么是appidentifier)，获取方法参见 [获取应用的appIdentifier](../../../quick-start/common-problem-of-application.md#如何获取应用信息中的appidentifier)。 |
| appIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 表示分身应用的索引，默认值为0。&lt;br&gt; appIndex为0时，表示删除主应用的处置状态。appIndex大于0时，表示删除指定分身应用的处置状态。<br>**Since:** 12 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 17700061 | AppIndex is not in the valid range.<br>**Applicable version:** 12 and later |
| 201 | Permission denied. |
| 202 | Permission denied. A non-system application is not allowed to call a system API. |
| 17700005 | The specified app ID is invalid. |

