# RunningAppClone (System API)

The RunningAppClone module defines the information of an application clone in the running state.

**Since:** 23

<!--Device-unnamed-export interface RunningAppClone--><!--Device-unnamed-export interface RunningAppClone-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## appCloneIndex

```TypeScript
appCloneIndex: int
```

Index of an application clone.

**Type:** int

**Since:** 23

<!--Device-RunningAppClone-appCloneIndex: int--><!--Device-RunningAppClone-appCloneIndex: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## pids

```TypeScript
pids: Array<int>
```

Process ID set of the application.

**Type:** Array&lt;int&gt;

**Since:** 23

<!--Device-RunningAppClone-pids: Array<int>--><!--Device-RunningAppClone-pids: Array<int>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uid

```TypeScript
uid: int
```

UID of the application.

**Type:** int

**Since:** 23

<!--Device-RunningAppClone-uid: int--><!--Device-RunningAppClone-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Examples**

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName: string = 'ohos.samples.etsclock';
  appManager.getRunningMultiAppInfo(bundleName).then((info: appManager.RunningMultiAppInfo) => {
      hilog.info(0x0000, 'testTag', `getRunningMultiAppInfo success`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `getRunningMultiAppInfo error, code: ${err.code}, msg:${err.message}`);
    })
} catch (err) {
  hilog.error(0x0000, 'testTag', `getRunningMultiAppInfo error, code: ${err.code}, msg:${err.message}`);
}
```

