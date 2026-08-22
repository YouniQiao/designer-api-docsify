# RunningAppClone（系统接口）

定义分身应用在运行态的结构信息。

**起始版本：** 23

<!--Device-unnamed-export interface RunningAppClone--><!--Device-unnamed-export interface RunningAppClone-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## appCloneIndex

```TypeScript
appCloneIndex: int
```

分身应用的索引。

**类型：** int

**起始版本：** 23

<!--Device-RunningAppClone-appCloneIndex: int--><!--Device-RunningAppClone-appCloneIndex: int-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## pids

```TypeScript
pids: Array<int>
```

应用的进程ID集合。

**类型：** Array&lt;int&gt;

**起始版本：** 23

<!--Device-RunningAppClone-pids: Array<int>--><!--Device-RunningAppClone-pids: Array<int>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## uid

```TypeScript
uid: int
```

表示应用程序的UID。

**类型：** int

**起始版本：** 23

<!--Device-RunningAppClone-uid: int--><!--Device-RunningAppClone-uid: int-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**示例**

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName: string = 'ohos.samples.etsclock';
  appManager.getRunningMultiAppInfo(bundleName).then((info: appManager.RunningMultiAppInfo) => {
    hilog.info(0x0000, 'testTag', `getRunningMultiAppInfo success`);
  }).catch((error: Error) => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', `getRunningMultiAppInfo error, code: ${err.code}, msg:${err.message}`);
  })
} catch (error: BusinessError) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `getRunningMultiAppInfo error, code: ${err.code}, msg:${err.message}`);
}
```

