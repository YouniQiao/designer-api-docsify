# getShortcutInfoByAppIndex (System API)

## Modules to Import

```TypeScript
import { launcherBundleManager } from 'kits/@kit.AbilityKit';
```

## getShortcutInfoByAppIndex

```TypeScript
function getShortcutInfoByAppIndex(bundleName: string, appIndex: int): Array<ShortcutInfo>
```

查询当前用户下指定分身应用的快捷方式信息[ShortcutInfo](arkts-ability-launcherbundlemanager-shortcutinfo-t.md)。

调用方获取自己的信息时不需要权限。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-launcherBundleManager-function getShortcutInfoByAppIndex(bundleName: string, appIndex: int): Array<ShortcutInfo>--><!--Device-launcherBundleManager-function getShortcutInfoByAppIndex(bundleName: string, appIndex: int): Array<ShortcutInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用Bundle名称。 |
| appIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 分身应用的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;ShortcutInfo&gt; | Array形式返回当前用户下指定分身应用的[ShortcutInfo]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not support. |
| 17700061 | The specified app index is invalid. |
| 201 | Verify permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700001 | The specified bundle name is not found. |

## Examples

```TypeScript
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = launcherBundleManager.getShortcutInfoByAppIndex("com.example.demo", 1);
  console.info('getShortcutInfoByAppIndex successfully, data is ' + JSON.stringify(data));
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`Failed to getShortcutInfoByAppIndex. Code: ${code}, message: ${message}`);
}
```

