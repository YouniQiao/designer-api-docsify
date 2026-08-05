# lite/global

## Summary

### Functions

| Name | Description |
| --- | --- |
| [canIUse](global-caniuse-f.md#caniuse) | Defining syscap function. |
| [clearInterval](global-clearinterval-f.md#clearinterval) | Cancels the interval set by " setInterval()". |
| [clearMonitorForCrownEvents](global-clearmonitorforcrownevents-f.md#clearmonitorforcrownevents) | Removes the digital crown events monitor function. |
| [clearTimeout](global-cleartimeout-f.md#cleartimeout) | Cancels the timer set by " setTimeout()". |
| [createLocalParticleAbility](global-createlocalparticleability-f.md#createlocalparticleability) | Get the java interface instance. The java instance needs to register, otherwise it cannot be obtained. After obtaining the instance, you can call the function with the same name on the Java side. |
| [getApp](global-getapp-f.md#getapp) | Obtain the objects exposed in app.js |
| [setInterval](global-setinterval-f.md#setinterval) | Sets the interval for repeatedly calling a function. |
| [setMonitorForCrownEvents](global-setmonitorforcrownevents-f.md#setmonitorforcrownevents) | Sets a digital crown events listener for current page, only be supported on the devices supporting digital crown. Please be awared, the listener will be removed automaticlly if the current page is pushed back or replaced, so it's recommaned to call this function in the onShow lifecycle callback of the page. And only one listener can be set for current page, the system will use the listener passed in through the latest calling of this function. Do not use this function in app.js, the behavior is undefined. |
| [setTimeout](global-settimeout-f.md#settimeout) | Sets a timer after which a function will be executed. |

