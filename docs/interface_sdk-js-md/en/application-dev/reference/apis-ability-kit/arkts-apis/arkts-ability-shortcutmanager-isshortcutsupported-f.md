# isShortcutSupported

## Modules to Import

```TypeScript
import { shortcutManager } from 'kits/@kit.AbilityKit';
```

## isShortcutSupported

```TypeScript
function isShortcutSupported(): boolean
```

查询当前设备是否支持快捷方式。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-shortcutManager-function isShortcutSupported(): boolean--><!--Device-shortcutManager-function isShortcutSupported(): boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 表示当前设备是否支持快捷方式。&lt;br/&gt;返回值为true表示当前设备支持快捷方式；返回值为false表示当前设备不支持快捷方式。 |

## Examples

```TypeScript
import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = shortcutManager.isShortcutSupported();
  console.info('isShortcutSupported data is' + JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  console.error(`isShortcutSupported errData is errCode:${err.code}  message:${err.message}`);
}
```

