# RunningMultiInstanceInfo（系统接口）

定义多实例应用在运行态的结构信息，通过appManager的 [getRunningMultiAppInfo](arkts-ability-appmanager-getrunningmultiappinfo-f-sys.md)来获取。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## instanceKey

```TypeScript
instanceKey: string
```

多实例应用的唯一实例标识。

**类型：** string

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## pids

```TypeScript
pids: Array<int>
```

应用的进程ID集合。

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## uid

```TypeScript
uid: int
```

表示应用程序的UID。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**示例**

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = 'ohos.samples.etsclock';
  appManager.getRunningMultiAppInfo(bundleName).then((info: appManager.RunningMultiAppInfo) => {
    console.info(`getRunningMultiAppInfo success`);
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`getRunningMultiAppInfo error, code: ${err.code}, msg:${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  console.error(`getRunningMultiAppInfo error, code: ${err.code}, msg:${err.message}`);
}
```
