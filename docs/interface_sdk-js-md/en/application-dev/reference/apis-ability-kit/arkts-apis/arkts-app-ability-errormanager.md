# @ohos.app.ability.errorManager

The ErrorManager module provides capabilities for registering and unregistering error observers, which are primarily used to listen for errors such as JavaScript crashes and application freezes.

**Since:** 24

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
| [offFreeze](arkts-ability-errormanager-offfreeze-f.md) | Unregister the observer for freeze event. This function can only be called from main thread. |
| [offUnhandledRejection](arkts-ability-errormanager-offunhandledrejection-f.md) | Unregister unhandled rejection observer. |
| [off_error](arkts-ability-errormanager-offerror-f.md#offerror) | Unregisters an error observer. This API uses an asynchronous callback to return the result. |
| [off_error](arkts-ability-errormanager-offerror-f.md#offerror) | Unregisters an error observer. This API uses a promise to return the result. |
| [off_freeze](arkts-ability-errormanager-offfreeze-f.md) | Unregisters an observer for the main thread freeze event of the application. |
| [off_globalErrorOccurred](arkts-ability-errormanager-offglobalerroroccurred-f.md#offglobalerroroccurred) | Unregisters a global error observer. Once unregistered, global listening cannot be implemented. |
| [off_globalUnhandledRejectionDetected](arkts-ability-errormanager-offglobalunhandledrejectiondetected-f.md#offglobalunhandledrejectiondetected) | Unregisters a rejected promise observer. After the deregistration, promise exceptions in the process cannot be listened for. |
| [off_loopObserver](arkts-ability-errormanager-offloopobserver-f.md#offloopobserver) | Unregisters an observer for the message processing duration of the main thread. |
| [off_unhandledRejection](arkts-ability-errormanager-offunhandledrejection-f.md) | Unregisters an observer for the promise rejection. |
| [onFreeze](arkts-ability-errormanager-onfreeze-f.md) | Register an observer for freeze event. This function can only be called from main thread. Please note that each process only supports registering one observer. If you register multiple times, the later one will overwrite the previous one. |
| [onUnhandledRejection](arkts-ability-errormanager-onunhandledrejection-f.md) | Register unhandled rejection observer. |
| [on_error](arkts-ability-errormanager-onerror-f.md#onerror) | Registers an error observer. Once registered, it can capture JavaScript crashes occurring within the application, which are a type of application crash. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes. |
| [on_freeze](arkts-ability-errormanager-onfreeze-f.md) | Registers an observer for the main thread freeze event of the application. If the observer is registered multiple times, only the last one takes effect. |
| [on_globalErrorOccurred](arkts-ability-errormanager-onglobalerroroccurred-f.md#onglobalerroroccurred) | Registers a global error observer via the **errorManager.on** API within any thread of a process. Once registered, it can capture exceptions occurring in any thread across the entire process. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes. |
| [on_globalUnhandledRejectionDetected](arkts-ability-errormanager-onglobalunhandledrejectiondetected-f.md#onglobalunhandledrejectiondetected) | Registers a rejected promise observer with any thread in the process. Once registered, it can capture a rejected promise that is not captured in the current thread of the application. |
| [on_loopObserver](arkts-ability-errormanager-onloopobserver-f.md#onloopobserver) | Registers an observer for the message processing duration of the main thread. After the registration, the execution time of a message processed by the main thread of the application can be captured. |
| [on_unhandledRejection](arkts-ability-errormanager-onunhandledrejection-f.md) | Registers an observer for the promise rejection. After the registration, a rejected promise that is not captured in the current thread of the application can be captured. |
| [setDefaultErrorHandler](arkts-ability-errormanager-setdefaulterrorhandler-f.md) | Returns the previously registered handler when a JavaScript crash exception occurs. It can only be used in the main thread. |
| [setDefaultFreezeObserver](arkts-ability-errormanager-setdefaultfreezeobserver-f.md) | Set the default freeze observer, This function will be executed right after the callback function registered through errorManager.on is executed. You can use it to implement chain calls instead of errorManager.on. If an empty observer is set for a certain module, it will cause the call chain to be interrupted. This API must be called in the main thread. |
| [setDefaultResourceUsageObserver](arkts-ability-errormanager-setdefaultresourceusageobserver-f.md) | Set the default resource usage observer. You can use it to implement chain calls. If an empty observer is set for a certain module, it will cause the call chain to be interrupted. This API must be called on the main thread. |

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
| [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | Defines an exception observer that can be used as an input parameter for [errorManager.on('globalErrorOccurred')](arkts-ability-errormanager-onerror-f.md#onerror) and [errorManager.on('globalUnhandledRejectionDetected')](arkts-ability-errormanager-onerror-f.md#onerror) to monitor event processing on the main thread of the current application. |
| [LoopObserver](arkts-ability-errormanager-loopobserver-t.md) | Defines the LoopObserver module. It can be used as a parameter of **errormanager.on** to listen for and handle main thread timeout events in the current application. |
| [ResourceUsageObserver](arkts-ability-errormanager-resourceusageobserver-t.md) | The observer will be called by the system when resource usage exceed threshold. |
| [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | The observer will be called by system when an unhandled rejection occurs. |

