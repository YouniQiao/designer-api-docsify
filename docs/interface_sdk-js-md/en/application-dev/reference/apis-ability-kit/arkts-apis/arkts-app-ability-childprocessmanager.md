# @ohos.app.ability.childProcessManager

The childProcessManager module provides the child process management capability. Currently, it provides APIs to create and start a child process The created child process will exit when the parent process exits and cannot run independently.

**Since:** 23

<!--Device-unnamed-declare namespace childProcessManager--><!--Device-unnamed-declare namespace childProcessManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { childProcessManager } from 'childProcessManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [isArkChildProcessSupported](arkts-ability-childprocessmanager-isarkchildprocesssupported-f.md#isarkchildprocesssupported) | Checks whether the caller is allowed to create ark child processes on this device. Some devices may not support creating ark child processes, so it is recommended to use this interface to verify support beforehand. |
| [isNativeChildProcessSupported](arkts-ability-childprocessmanager-isnativechildprocesssupported-f.md#isnativechildprocesssupported) | Checks whether the caller is allowed to create native child processes on this device. Some devices may not support creating native child processes, so it is recommended to use this interface to verify support beforehand. |
| [startArkChildProcess](arkts-ability-childprocessmanager-startarkchildprocess-f.md#startarkchildprocess) | Starts an [ArkTS child process](../../../application-models/ability-terminology.md#arkts-child-process). This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801 is returned. > **NOTE：**> > The child process started by calling this API does not inherit the resources of the parent process. If the child > process is created successfully, its PID is returned, and its > [ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart) function is executed. After the > function is done, the child process is not automatically destroyed. Instead, it must be destroyed by calling > [process.abort](../../apis-arkts/arkts-apis/arkts-arkts-process-abort-f.md#abort). After the process that calls this API is destroyed, the > created child process is also destroyed. |
| [startChildProcess](arkts-ability-childprocessmanager-startchildprocess-f.md#startchildprocess) | Starts an [ArkTS child process](../../../application-models/ability-terminology.md#arkts-child-process). This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 160 00061 is returned. > **NOTE：**> > If the child process is created successfully, its PID is returned, and its > [ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart) function is executed. Once the > function is done, the child process is automatically destroyed. > > The child process started by calling this API does not support asynchronous ArkTS API calls. It supports only > synchronous ArkTS API calls. |
| [startChildProcess](arkts-ability-childprocessmanager-startchildprocess-f.md#startchildprocess) | Starts an [ArkTS child process](../../../application-models/ability-terminology.md#arkts-child-process). This API uses an asynchronous callback to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 160 00061 is returned. > **NOTE：**> > If the child process is created successfully, its PID is returned, and its > [ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart) function is executed. Once the > function is done, the child process is automatically destroyed. > > The child process started by calling this API does not support asynchronous ArkTS API calls. It supports only > synchronous ArkTS API calls. |
| [startNativeChildProcess](arkts-ability-childprocessmanager-startnativechildprocess-f.md#startnativechildprocess) | Starts a [native child process](../../../application-models/ability-terminology.md#native-child-process). This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801 is returned. > **NOTE：**> > The child process started by calling this API does not inherit the resources of the parent process. After the > child process is created, its PID is returned, the dynamic link library file specified in the parameters is > loaded, and the entry function of the child process is executed. Once the entry function is done, the child > process is automatically destroyed. After the process that calls this API is destroyed, the created child process > is also destroyed. |

### Enums

| Name | Description |
| --- | --- |
| [StartMode](arkts-ability-childprocessmanager-startmode-e.md) | Enumerates the child process start modes. |

