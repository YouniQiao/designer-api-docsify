# @ohos.app.ability.ApplicationStateChangeCallback

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ApplicationStateChangeCallback](arkts-na-app-ability-applicationstatechangecallback-applicationstatechangecallback-i.md) | The module is used to listen for state changes of the current application process. For ease of description, the term "application process" will be referred to as "process" in the following sections. You can call [ApplicationContext.on('applicationStateChange')](../../apis-ability-kit/arkts-apis/arkts-ability-applicationcontext-c.md#onabilitylifecycle) and pass in a custom ApplicationStateChangeCallback to listen for foreground/background state changes of the current process. This allows you to perform certain actions based on the process state changes, for example, tracking the duration of the process in the foreground and background, or clearing memory caches when the process moves to the background. |

