# preloadApplication (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## preloadApplication

```TypeScript
function preloadApplication(bundleName: string, userId: int, mode: PreloadMode, appIndex?: int): Promise<void>
```

预加载应用进程。接口返回成功并不代表预加载成功，具体结果以目标应用进程是否创建成功为准。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PRELOAD_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-appManager-function preloadApplication(bundleName: string, userId: int, mode: PreloadMode, appIndex?: int): Promise<void>--><!--Device-appManager-function preloadApplication(bundleName: string, userId: int, mode: PreloadMode, appIndex?: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 预加载的应用包名。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 预加载的用户Id。 |
| mode | [PreloadMode](arkts-ability-appmanager-preloadmode-e-sys.md) | Yes | 预加载模式。 |
| appIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 预加载应用分身的appIndex。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | Not system application. |
| 16300005 | The target bundle does not exist. |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let bundleName = "ohos.samples.etsclock";
  let userId = 100;
  let mode = appManager.PreloadMode.PRESS_DOWN;
  let appIndex = 0;
  appManager.preloadApplication(bundleName, userId, mode, appIndex)
    .then(() => {
      hilog.info(0x0000, 'testTag', `preloadApplication success`);
    })
    .catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `preloadApplication error, code: ${err.code}, msg:${err.message}`);
    })
} catch (err) {
  hilog.error(0x0000, 'testTag', `preloadApplication error, code: ${(err as BusinessError).code}, msg:${(err as BusinessError).message}`);
}
```

