# getSelfManagedBrowserPolicyVersion

## Modules to Import

```TypeScript
import { browser } from 'kits/@kit.MDMKit';
```

## getSelfManagedBrowserPolicyVersion

```TypeScript
function getSelfManagedBrowserPolicyVersion(): string
```

获取当前设备浏览器策略版本。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

<!--Device-browser-function getSelfManagedBrowserPolicyVersion(): string--><!--Device-browser-function getSelfManagedBrowserPolicyVersion(): string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Return value:**

| Type | Description |
| --- | --- |
| string | 浏览器策略版本。 |

## Examples

```TypeScript
import { browser } from '@kit.MDMKit';

try {
  let version: string = browser.getSelfManagedBrowserPolicyVersion();
  console.info(`Succeeded in getting self managed browser policy version, result : ${version}`);
} catch(err) {
  console.error(`Failed to get self managed browser policy version. Code is ${err.code}, message is ${err.message}`);
}
```

