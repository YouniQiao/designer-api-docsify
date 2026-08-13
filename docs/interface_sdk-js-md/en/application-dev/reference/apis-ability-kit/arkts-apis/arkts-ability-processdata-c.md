# ProcessData

The module defines process data. If a lifecycle change listener is registered by calling [appManager.on('applicationState')](arkts-ability-appmanager-onapplicationstate-f.md#on_applicationState) , the onProcessCreated callback in ApplicationStateObserver is invoked when the lifecycle of an application or ability changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class ProcessData--><!--Device-unnamed-declare class ProcessData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ProcessData-bundleName: string--><!--Device-ProcessData-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## isContinuousTask

```TypeScript
isContinuousTask: boolean
```

Whether the task is a continuous task. **true** if yes, **false** otherwise.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ProcessData-isContinuousTask: boolean--><!--Device-ProcessData-isContinuousTask: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## isKeepAlive

```TypeScript
isKeepAlive: boolean
```

Whether the process is a resident task. **true** if yes, **false** otherwise.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ProcessData-isKeepAlive: boolean--><!--Device-ProcessData-isKeepAlive: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: int
```

Process ID.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ProcessData-pid: int--><!--Device-ProcessData-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## state

```TypeScript
state: int
```

Application state. The options are as follows: **0**: The application process is being initialized. **1**: The application process has been initialized and is ready. **2**: The application is running in the foreground. **4**: The application is running in the background. **5**: The application process is terminated.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ProcessData-state: int--><!--Device-ProcessData-state: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: int
```

UID of the application.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ProcessData-uid: int--><!--Device-ProcessData-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

