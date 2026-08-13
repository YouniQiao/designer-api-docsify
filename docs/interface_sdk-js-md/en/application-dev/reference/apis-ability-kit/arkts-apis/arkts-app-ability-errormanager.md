# @ohos.app.ability.errorManager

The ErrorManager module provides capabilities for registering and unregistering error observers, which are primarily used to listen for errors such as JavaScript crashes and application freezes.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace errorManager--><!--Device-unnamed-declare namespace errorManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [offFreeze](arkts-ability-errormanager-offfreeze-f.md#offFreeze) | Unregister the observer for freeze event. This function can only be called from main thread. |
| [offUnhandledRejection](arkts-ability-errormanager-offunhandledrejection-f.md#offUnhandledRejection) | Unregister unhandled rejection observer. |
| [off_error](arkts-ability-errormanager-offerror-f.md#off_error) | Unregisters an error observer. This API uses an asynchronous callback to return the result. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. |
| [off_error](arkts-ability-errormanager-offerror-f.md#off_error) | Unregisters an error observer. This API uses a promise to return the result. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. |
| off_freeze | Unregisters an observer for the main thread freeze event of the application. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. If the observer passed in does not match the observer registered via the **on** API, error code 16300004 is thrown. Therefore, you are advised to handle this using **try-catch** logic. |
| [off_globalErrorOccurred](arkts-ability-errormanager-offglobalerroroccurred-f.md#off_globalErrorOccurred) | Unregisters a global error observer. Once unregistered, global listening cannot be implemented. If the observer passed in is not in the observer queue registered via the **on** API, error code 16300004 is thrown. Therefore, you are advised to handle this using **try-catch** logic. |
| [off_globalUnhandledRejectionDetected](arkts-ability-errormanager-offglobalunhandledrejectiondetected-f.md#off_globalUnhandledRejectionDetected) | Unregisters a rejected promise observer. After the deregistration, promise exceptions in the process cannot be listened for. If the observer passed in is not in the observer queue registered via the **on** API, error code 16300004 is thrown. Therefore, you are advised to handle this using **try-catch** logic. |
| [off_loopObserver](arkts-ability-errormanager-offloopobserver-f.md#off_loopObserver) | Unregisters an observer for the message processing duration of the main thread. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. |
| off_unhandledRejection | Unregisters an observer for the promise rejection. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. |
| [onFreeze](arkts-ability-errormanager-onfreeze-f.md#onFreeze) | Register an observer for freeze event. This function can only be called from main thread. Please note that each process only supports registering one observer. If you register multiple times, the later one will overwrite the previous one. |
| [onUnhandledRejection](arkts-ability-errormanager-onunhandledrejection-f.md#onUnhandledRejection) | Register unhandled rejection observer. |
| [on_error](arkts-ability-errormanager-onerror-f.md#on_error) | Registers an error observer. Once registered, it can capture JavaScript crashes occurring within the application, which are a type of application crash. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. |
| on_freeze | Registers an observer for the main thread freeze event of the application. If the observer is registered multiple times, only the last one takes effect. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. > **NOTE：**> > If the callback function runs for more than 1 second, the > [AppRecovery](arkts-app-ability-apprecovery.md#@ohos.app.ability.appRecovery) feature may not work. The execution duration can > be calculated by parsing the time difference between **begin** and **Freeze callback execution completed** in > HiLogs. If the execution duration exceeds 1 second, you can optimize the callback logic by using methods such as > asynchronous processing, reducing operations that block other tasks, and optimizing the data structures to reduce > the execution duration. |
| [on_globalErrorOccurred](arkts-ability-errormanager-onglobalerroroccurred-f.md#on_globalErrorOccurred) | Registers a global error observer via the **errorManager.on** API within any thread of a process. Once registered, it can capture exceptions occurring in any thread across the entire process. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes. |
| [on_globalUnhandledRejectionDetected](arkts-ability-errormanager-onglobalunhandledrejectiondetected-f.md#on_globalUnhandledRejectionDetected) | Registers a rejected promise observer with any thread in the process. Once registered, it can capture a rejected promise that is not captured in the current thread of the application. |
| [on_loopObserver](arkts-ability-errormanager-onloopobserver-f.md#on_loopObserver) | Registers an observer for the message processing duration of the main thread. After the registration, the execution time of a message processed by the main thread of the application can be captured. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. |
| on_unhandledRejection | Registers an observer for the promise rejection. After the registration, a rejected promise that is not captured in the current thread of the application can be captured. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic. |
| [setDefaultErrorHandler](arkts-ability-errormanager-setdefaulterrorhandler-f.md#setDefaultErrorHandler) | Returns the previously registered handler when a JavaScript crash exception occurs. It can only be used in the main thread. If an invalid parameter is passed or the API is called from a child thread, an error code is thrown and **undefined** is returned. You are advised to handle it with try-catch logic. If the API parameter is empty, subsequently registered handlers are not able to establish a connection with previously registered handlers, thereby breaking the chain call mechanism. |
| [setDefaultFreezeObserver](arkts-ability-errormanager-setdefaultfreezeobserver-f.md#setDefaultFreezeObserver) | Set the default freeze observer, This function will be executed right after the callback function registered through errorManager.on is executed. You can use it to implement chain calls instead of errorManager.on. If an empty observer is set for a certain module, it will cause the call chain to be interrupted. This API must be called in the main thread. |
| [setDefaultResourceUsageObserver](arkts-ability-errormanager-setdefaultresourceusageobserver-f.md#setDefaultResourceUsageObserver) | Set the default resource usage observer. You can use it to implement chain calls. If an empty observer is set for a certain module, it will cause the call chain to be interrupted. This API must be called on the main thread. |

### Interfaces

| Name | Description |
| --- | --- |
| [GlobalError](arkts-ability-errormanager-globalerror-i.md) | Describes the object related to the exception event name, message, error stack information, exception thread name, and exception thread type. |

### Enums

| Name | Description |
| --- | --- |
| [InstanceType](arkts-ability-errormanager-instancetype-e.md) | Enumerates the VM instance types. |
| [ResourceType](arkts-ability-errormanager-resourcetype-e.md) | Define the resource types of the application. |

### Types

| Name | Description |
| --- | --- |
| [ErrorHandler](arkts-ability-errormanager-errorhandler-t.md) | The ErrorHandler will be called when the ArkTS runtime throws an exception that is not caught by the user. |
| [ErrorObserver](arkts-ability-errormanager-errorobserver-t.md) | Defines the ErrorObserver module. |
| [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | Defines an observer for the main thread freeze event of the application. It is used by the application to customize freeze information. |
| [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | Defines an exception observer that can be used as an input parameter for [errorManager.on('globalErrorOccurred')](arkts-ability-errormanager-onerror-f.md#on_error) and [errorManager.on('globalUnhandledRejectionDetected')](arkts-ability-errormanager-onerror-f.md#on_error) to monitor event processing on the main thread of the current application. |
| [LoopObserver](arkts-ability-errormanager-loopobserver-t.md) | Defines the LoopObserver module. It can be used as a parameter of **errormanager.on** to listen for and handle main thread timeout events in the current application. |
| [ResourceUsageObserver](arkts-ability-errormanager-resourceusageobserver-t.md) | The observer will be called by the system when resource usage exceed threshold. |
| [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | The observer will be called by system when an unhandled rejection occurs. |

