# enableAbilityWithCallback (System API)

## Modules to Import

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## enableAbilityWithCallback

```TypeScript
function enableAbilityWithCallback(name: string, capability: Array<accessibility.Capability>, connectCallback: ConnectCallback): Promise<void>
```

启用辅助扩展，并指定[ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md)作为辅助扩展应用状态变化的回调函数。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-config-function enableAbilityWithCallback(name: string, capability: Array<accessibility.Capability>, connectCallback: ConnectCallback): Promise<void>--><!--Device-config-function enableAbilityWithCallback(name: string, capability: Array<accessibility.Capability>, connectCallback: ConnectCallback): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 辅助扩展应用的名称，格式为：'bundleName/abilityName'。 |
| capability | Array&lt;accessibility.Capability&gt; | Yes | 辅助扩展应用的能力属性。 |
| connectCallback | [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md) | Yes | 辅助扩展应用的状态发生变化时调用的回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 9300001 | Invalid bundle name or ability name. |
| 9300002 | Target ability already enabled. |

## Examples

```TypeScript
import { accessibility, config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';
let capability: accessibility.Capability[] = ['retrieve'];
let connectCallback: config.ConnectCallback = {
  onDisconnect: () => {
    console.info(`Ability is disconnected.`);
  }
};

config.enableAbilityWithCallback(name, capability, connectCallback).then(() => {
  console.info(`Succeeded in enabling ability, name is ${name}, capability is ${capability}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to enable ability. Code: ${err.code}, message: ${err.message}`);
});
```

