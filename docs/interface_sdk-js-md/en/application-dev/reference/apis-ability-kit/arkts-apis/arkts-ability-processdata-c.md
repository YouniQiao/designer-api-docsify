# ProcessData

The module defines process data. If a lifecycle change listener is registered by calling  
[appManager.on('applicationState')](@ohos.app.ability.appManager:appManager.on(type: 'applicationState', observer: ApplicationStateObserver)), the  
[onProcessCreated](../../../reference/apis-ability-kit/js-apis-inner-application-applicationStateObserver.md#applicationstateobserveronprocesscreated) callback in [ApplicationStateObserver](./application/ApplicationStateObserver) is invoked when the lifecycle of an application or ability changes.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class ProcessData--><!--Device-unnamed-declare class ProcessData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ProcessData-bundleName: string--><!--Device-ProcessData-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## isContinuousTask

```TypeScript
isContinuousTask: boolean
```

Whether the task is a continuous task. **true** if yes, **false** otherwise.

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ProcessData-isContinuousTask: boolean--><!--Device-ProcessData-isContinuousTask: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## isKeepAlive

```TypeScript
isKeepAlive: boolean
```

Whether the process is a resident task. **true** if yes, **false** otherwise.

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ProcessData-isKeepAlive: boolean--><!--Device-ProcessData-isKeepAlive: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: int
```

Process ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ProcessData-pid: int--><!--Device-ProcessData-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## state

```TypeScript
state: int
```

Application state. The options are as follows:

**0**: The application process is being initialized.

**1**: The application process has been initialized and is ready.

**2**: The application is running in the foreground.

**4**: The application is running in the background.

**5**: The application process is terminated.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ProcessData-state: int--><!--Device-ProcessData-state: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: int
```

UID of the application.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ProcessData-uid: int--><!--Device-ProcessData-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

