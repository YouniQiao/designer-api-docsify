# global

## Summary

### Functions

| Name | Description |
| --- | --- |
| [canIUse](arkts-arkui-global-caniuse-f.md#canIUse) | Defining syscap function. |
| [clearInterval](arkts-arkui-global-clearinterval-f.md#clearInterval) | Cancels the interval set by " setInterval()". |
| [clearMonitorForCrownEvents](arkts-arkui-global-clearmonitorforcrownevents-f.md#clearMonitorForCrownEvents) | Removes the digital crown events monitor function. |
| [clearTimeout](arkts-arkui-global-cleartimeout-f.md#clearTimeout) | Cancels the timer set by " setTimeout()". |
| [createLocalParticleAbility](arkts-arkui-global-createlocalparticleability-f.md#createLocalParticleAbility) | Get the java interface instance. The java instance needs to register, otherwise it cannot be obtained. After obtaining the instance, you can call the function with the same name on the Java side. |
| [getApp](arkts-arkui-global-getapp-f.md#getApp) | Obtain the objects exposed in app.js |
| [setInterval](arkts-arkui-global-setinterval-f.md#setInterval) | Sets the interval for repeatedly calling a function. |
| [setMonitorForCrownEvents](arkts-arkui-global-setmonitorforcrownevents-f.md#setMonitorForCrownEvents) | Sets a digital crown events listener for current page, only be supported on the devices supporting digital crown. Please be awared, the listener will be removed automaticlly if the current page is pushed back or replaced, so it's recommaned to call this function in the onShow lifecycle callback of the page. And only one listener can be set for current page, the system will use the listener passed in through the latest calling of this function. Do not use this function in app.js, the behavior is undefined. |
| [setTimeout](arkts-arkui-global-settimeout-f.md#setTimeout) | Sets a timer after which a function will be executed. |

