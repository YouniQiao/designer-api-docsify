# getKeepAliveAppServiceExtensions (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getKeepAliveAppServiceExtensions

```TypeScript
function getKeepAliveAppServiceExtensions(): Promise<Array<KeepAliveBundleInfo>>
```

获取所有保活的AppServiceExtensionAbility应用信息，此信息由[KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md)定义。使用Promise异步回调。该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_APP_KEEP_ALIVE

<!--Device-appManager-function getKeepAliveAppServiceExtensions(): Promise<Array<KeepAliveBundleInfo>>--><!--Device-appManager-function getKeepAliveAppServiceExtensions(): Promise<Array<KeepAliveBundleInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;KeepAliveBundleInfo&gt;&gt; | Promise对象，返回用户保活应用信息的数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appManager.getKeepAliveAppServiceExtensions().then((data) => {
    console.info(`getKeepAliveAppServiceExtensions success, data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`getKeepAliveAppServiceExtensions fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] getKeepAliveAppServiceExtensions error: ${code}, ${message}`);
}
```

