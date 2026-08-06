# full/global

## Summary

### Functions

| Name | Description |
| --- | --- |
| [canIUse](global-caniuse-f.md#caniuse) | Defining syscap function. |
| [cancelAnimationFrame](global-cancelanimationframe-f.md#cancelanimationframe) | Cancels the vsync callback set by "requestAnimationFrame()". |
| [clearInterval](global-clearinterval-f.md#clearinterval) | Cancels the interval set by " setInterval()". |
| [clearMonitorForCrownEvents](global-clearmonitorforcrownevents-f.md#clearmonitorforcrownevents) | Removes the digital crown events monitor function. |
| [clearTimeout](global-cleartimeout-f.md#cleartimeout) | Cancels the timer set by "setTimeout()". |
| [createLocalParticleAbility](global-createlocalparticleability-f.md#createlocalparticleability) | Get the java interface instance. The java instance needs to register, otherwise it cannot be obtained.After obtaining the instance, you can call the function with the same name on the Java side. |
| [getApp](global-getapp-f.md#getapp) | Obtain the objects exposed in app.js |
| [requestAnimationFrame](global-requestanimationframe-f.md#requestanimationframe) | Sets a vsync after which a function will be executed. |
| [setInterval](global-setinterval-f.md#setinterval) | Sets the interval for repeatedly calling a function. |
| [setMonitorForCrownEvents](global-setmonitorforcrownevents-f.md#setmonitorforcrownevents) | Sets a digital crown events listener for current page, only be supported on the devices supporting digital crown.Please be awared, the listener will be removed automaticlly if the current page is pushed back or replaced, so it's recommaned to call this function in the onShow lifecycle callback of the page.And only one listener can be set for current page, the system will use the listener passed in through the latest calling of this function.Do not use this function in app.js, the behavior is not undefined. |
| [setTimeout](global-settimeout-f.md#settimeout) | Sets a timer after which a function will be executed. |

### Classes

| Name | Description |
| --- | --- |
| [Image](global-image-c.md) | You can create an Image object by calling new Image(). |
| [ImageBitmap](global-imagebitmap-c.md) | Defines the ImageBitmap. |
| [ImageData](global-imagedata-c.md) | An ImageData object is a common object that stores the actual pixel data of a Canvas object. |
| [OffscreenCanvas](global-offscreencanvas-c.md) | OffscreenCanvas provides a Canvas object that can be rendered off-screen.It works in both window and Web worker environments. |

