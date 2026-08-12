# PiPController

Implements a PiP controller that starts, stops, or updates a PiP window and registers callbacks.

Before calling any of the following APIs, you must use  
[PiPWindow.create()](arkts-arkui-pipwindow-create-f.md#create) to create a PiPController instance.

**Since:** 11

<!--Device-PiPWindow-interface PiPController--><!--Device-PiPWindow-interface PiPController-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { PiPWindow } from '@kit.ArkUI';
```

## getPiPSettingSwitch

```TypeScript
getPiPSettingSwitch(): Promise<boolean>
```

Obtains the status of the auto-start PiP switch in Settings. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PiPController-getPiPSettingSwitch(): Promise<boolean>--><!--Device-PiPController-getPiPSettingSwitch(): Promise<boolean>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300014-pip-internal-error) |

## Examples

```TypeScript
let pipSwitchStatus: boolean | undefined = undefined;
try {
  // Obtain the status of the switch for automatically starting the PiP window.
  let promise : Promise<boolean> = this.pipController.getPiPSettingSwitch();
  promise.then((data) => {
    // Save the obtained switch status.
    pipSwitchStatus = data;
    console.info('Succeeded in getting pip switch status. switchStatus: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to get pip switch status. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get pip switch status. Code: ${exception.code}, message: ${exception.message}`);
}
```

## getPiPWindowInfo

```TypeScript
getPiPWindowInfo(): Promise<PiPWindowInfo>
```

Obtains the PIP window information. This API uses a promise to return the result.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PiPController-getPiPWindowInfo(): Promise<PiPWindowInfo>--><!--Device-PiPController-getPiPWindowInfo(): Promise<PiPWindowInfo>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PiPWindowInfo](arkts-arkui-pipwindow-pipwindowinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300014-pip-internal-error) |

## Examples

```TypeScript
let pipWindowInfo: PiPWindow.PiPWindowInfo | undefined = undefined;
try {
  // Obtain the PiP window information.
  let promise : Promise<PiPWindow.PiPWindowInfo> = this.pipController.getPiPWindowInfo();
  promise.then((data) => {
    // Save the obtained PiP window information.
    pipWindowInfo = data;
    console.info('Success in get pip window info. Info: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to get pip window info. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get pip window info. Code: ${exception.code}, message: ${exception.message}`);
}
```

## isPiPActive

```TypeScript
isPiPActive(): Promise<boolean>
```

Check whether the PiP window is active. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PiPController-isPiPActive(): Promise<boolean>--><!--Device-PiPController-isPiPActive(): Promise<boolean>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300014-pip-internal-error) |

## Examples

```TypeScript
let pipActiveStatus: boolean | undefined = undefined;
try {
  // Check whether the PiP window is active.
  let promise : Promise<boolean> | undefined = this.pipController?.isPiPActive();
  promise?.then((data) => {
    // Save the obtained active status of the PiP window.
    pipActiveStatus = data;
    console.info('Succeeded in getting pip active status. activeStatus: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to get pip active status. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get pip active status. Code: ${exception.code}, message: ${exception.message}`);
}
```

## off('stateChange')

```TypeScript
off(type: 'stateChange'): void
```

Unsubscribes from PiP state events.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-off(type: 'stateChange'): void--><!--Device-PiPController-off(type: 'stateChange'): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |

## Examples

```TypeScript
// Unsubscribe from PiP state events.
this.pipController.off('stateChange');
```

## off('controlPanelActionEvent')

```TypeScript
off(type: 'controlPanelActionEvent'): void
```

Unsubscribes from PiP action events. The  
**[off('controlEvent')](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authinstance-i.md#off)**API is preferred.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-off(type: 'controlPanelActionEvent'): void--><!--Device-PiPController-off(type: 'controlPanelActionEvent'): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'controlPanelActionEvent' | Yes |

## Examples

```TypeScript
// Unsubscribe from PiP controller action events.
this.pipController.off('controlPanelActionEvent');
```

## off('controlEvent')

```TypeScript
off(type: 'controlEvent', callback?: Callback<ControlEventParam>): void
```

Unsubscribes from PiP action events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-off(type: 'controlEvent', callback?: Callback<ControlEventParam>): void--><!--Device-PiPController-off(type: 'controlEvent', callback?: Callback<ControlEventParam>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'controlEvent' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControlEventParam](arkts-arkui-pipwindow-controleventparam-i.md)&gt; | No |

## Examples

```TypeScript
let callbackFunc = (event: PiPWindow.ControlEventParam) => {
  console.info(`receive control event: ${event.controlType}, ${event.status}`);
}
// Unsubscribe from PiP controller action events.
this.pipController.off('controlEvent', callbackFunc);
```

## off('pipWindowSizeChange')

```TypeScript
off(type: 'pipWindowSizeChange', callback?: Callback<PiPWindowSize>): void
```

Unsubscribes from the PiP window size change event.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PiPController-off(type: 'pipWindowSizeChange', callback?: Callback<PiPWindowSize>): void--><!--Device-PiPController-off(type: 'pipWindowSizeChange', callback?: Callback<PiPWindowSize>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'pipWindowSizeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PiPWindowSize](arkts-arkui-pipwindow-pipwindowsize-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
const callback = (size: PiPWindow.PiPWindowSize) => {
  // ...
}
try {
  // Enable listening through the on API.
  this.pipController.on('pipWindowSizeChange', callback);
} catch (exception) {
  console.error(`Failed to enable the listener for pip window size changes. Code: ${exception.code}, message: ${exception.message}`);
}

try {
  // Disable the listening of a specified callback.
  this.pipController.off('pipWindowSizeChange', callback);
  // Unregister all the callbacks that have been registered through on().
  this.pipController.off('pipWindowSizeChange');
} catch (exception) {
  console.error(`Failed to disable the listener for pip window size changes. Code: ${exception.code}, message: ${exception.message}`);
}
```

## off('activeStatusChange')

```TypeScript
off(type: 'activeStatusChange', callback?: Callback<boolean>): void
```

Unsubscribes from PiP window active status change events.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PiPController-off(type: 'activeStatusChange', callback?: Callback<boolean>): void--><!--Device-PiPController-off(type: 'activeStatusChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activeStatusChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No |

## Examples

```TypeScript
let callback = (activeStatus: boolean) => {
  console.info(`pip window is visible: ${activeStatus}`);
}
// Unsubscribe from PiP window active status change events.
this.pipController.off('activeStatusChange', callback);
```

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void
```

Subscribes to PiP state events. To avoid potential memory leaks, you are advised to stop listening when it is no longer needed.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void--><!--Device-PiPController-on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | (state: PiPState, reason: string) = & gt; void | Yes |

## Examples

```TypeScript
// Subscribe to PiP state events.
this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
  let curState: string = '';
  switch (state) {
    case PiPWindow.PiPState.ABOUT_TO_START:
      curState = 'ABOUT_TO_START';
      break;
    case PiPWindow.PiPState.STARTED:
      curState = 'STARTED';
      break;
    case PiPWindow.PiPState.ABOUT_TO_STOP:
      curState = 'ABOUT_TO_STOP';
      break;
    case PiPWindow.PiPState.STOPPED:
      curState = 'STOPPED';
      break;
    case PiPWindow.PiPState.ABOUT_TO_RESTORE:
      curState = 'ABOUT_TO_RESTORE';
      break;
    case PiPWindow.PiPState.ERROR:
      curState = 'ERROR';
      break;
    default:
      break;
  }
  console.info('stateChange:' + curState + ' reason:' + reason);
});
```

## on('controlPanelActionEvent')

```TypeScript
on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void
```

Subscribes to PiP action events. To avoid potential memory leaks, you are advised to stop listening when it is no longer needed. The  
[on('controlEvent')](PiPWindow.PiPController.on(type: 'controlEvent', callback: Callback&lt;ControlEventParam&gt;))API is preferred.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void--><!--Device-PiPController-on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'controlPanelActionEvent' | Yes |
| callback | [ControlPanelActionEventCallback](arkts-arkui-pipwindow-controlpanelactioneventcallback-t.md) | Yes |

## Examples

```TypeScript
// Subscribe to PiP controller action events.
this.pipController.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
  switch (event) {
    case 'playbackStateChanged':
      if (status === 0) {
        // Stop the video.
      } else if (status === 1) {
        // Play the video.
      }
      break;
    case 'nextVideo':
      // Switch to the next video.
      break;
    case 'previousVideo':
      // Switch to the previous video.
      break;
    case 'fastForward':
      // Fast forward the video.
      break;
    case 'fastBackward':
      // Rewind the video.
      break;
    default:
      break;
  }
  console.info('registerActionEventCallback, event:' + event);
});
```

## on('controlEvent')

```TypeScript
on(type: 'controlEvent', callback: Callback<ControlEventParam>): void
```

Subscribes to PiP action events. To avoid potential memory leaks, you are advised to stop listening when it is no longer needed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-on(type: 'controlEvent', callback: Callback<ControlEventParam>): void--><!--Device-PiPController-on(type: 'controlEvent', callback: Callback<ControlEventParam>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'controlEvent' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControlEventParam](arkts-arkui-pipwindow-controleventparam-i.md)&gt; | Yes |

## Examples

```TypeScript
// Subscribe to PiP controller action events.
this.pipController.on('controlEvent', (control) => {
  switch (control.controlType) {
    case PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE:
      if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
        // Stop the video.
      } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
        // Play the video.
      }
      break;
    case PiPWindow.PiPControlType.VIDEO_NEXT:
      // Switch to the next video.
      break;
    case PiPWindow.PiPControlType.VIDEO_PREVIOUS:
      // Switch to the previous video.
      break;
    case PiPWindow.PiPControlType.FAST_FORWARD:
      // Fast forward the video.
      break;
    case PiPWindow.PiPControlType.FAST_BACKWARD:
      // Rewind the video.
      break;
    default:
      break;
  }
  console.info('registerControlEventCallback, controlType:' + control.controlType + ', status' + control.status);
});
```

## on('pipWindowSizeChange')

```TypeScript
on(type: 'pipWindowSizeChange', callback: Callback<PiPWindowSize>): void
```

Subscribes to PiP window size change events. To avoid potential memory leaks, you are advised to stop listening when it is no longer needed.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PiPController-on(type: 'pipWindowSizeChange', callback: Callback<PiPWindowSize>): void--><!--Device-PiPController-on(type: 'pipWindowSizeChange', callback: Callback<PiPWindowSize>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'pipWindowSizeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PiPWindowSize](arkts-arkui-pipwindow-pipwindowsize-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300014-pip-internal-error) |

## Examples

```TypeScript
try {
  // Subscribe to PiP window size change events.
  this.pipController.on('pipWindowSizeChange', (size: PiPWindow.PiPWindowSize) => {
    console.info('Succeeded in enabling the listener for pip window size changes. size: ' + JSON.stringify(size));
  });
} catch (exception) {
  console.error(`Failed to enable the listener for pip window size changes. Code: ${exception.code}, message: ${exception.message}`);
}
```

## on('activeStatusChange')

```TypeScript
on(type: 'activeStatusChange', callback: Callback<boolean>): void
```

Subscribes to PiP window active status change events. To avoid potential memory leaks, you are advised to stop listening when it is no longer needed.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PiPController-on(type: 'activeStatusChange', callback: Callback<boolean>): void--><!--Device-PiPController-on(type: 'activeStatusChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activeStatusChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
let callback = (activeStatus: boolean) => {
  console.info(`pip window is visible: ${activeStatus}`);
}
// Subscribe to PiP window active status change events.
this.pipController.on('activeStatusChange', callback);
```

## setAutoStartEnabled

```TypeScript
setAutoStartEnabled(enable: boolean): void
```

Sets whether to automatically start the PiP window when the application's main window which can start the PiP window transitions to the background. By default, the PiP window is not automatically started.

If the XComponent approach is used to implement PiP and the **Navigation** component is used for route management, the system caches the top stack information with the specified navigation ID upon the first call of  
**setAutoStartEnabled(true)**.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-setAutoStartEnabled(enable: boolean): void--><!--Device-PiPController-setAutoStartEnabled(enable: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## Examples

```TypeScript
let enable: boolean = true;
this.pipController.setAutoStartEnabled(enable); // Set whether to automatically start the PiP window when the application's main window transitions to the background.
```

## setPiPControlEnabled

```TypeScript
setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void
```

Sets the enabled status for a component displayed on the PiP controller.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void--><!--Device-PiPController-setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| controlType | [PiPControlType](arkts-arkui-pipwindow-pipcontroltype-e.md) | Yes |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let controlType: PiPWindow.PiPControlType = PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE; // Play/Pause component displayed on the video playback control panel.
let enabled: boolean = false; // The Play/Pause component displayed on the video playback control panel is in the disabled state.
this.pipController.setPiPControlEnabled(controlType, enabled); // Set the enabled status of the PiP controller.
```

## startPiP

```TypeScript
startPiP(): Promise<void>
```

Starts a PiP window. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-startPiP(): Promise<void>--><!--Device-PiPController-startPiP(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300034](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300034-operation-of-the-float-view-conflicts-with-those-of-other-floating-windows) |
| [1300015](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300015-repeated-pip-operations) |
| [1300014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300014-pip-internal-error) |
| [1300013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300013-failure-in-creating-a-pip-window) |
| [1300012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300012-abnormal-pip-window-status) |

## Examples

```TypeScript
// You can call pipController according to the pipController definition.
let promise : Promise<void> = this.pipController.startPiP(); // Start the PiP window.
promise.then(() => {
  console.info(`Succeeded in starting pip.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to start pip. Cause:${err.code}, message:${err.message}`);
});
```

## stopPiP

```TypeScript
stopPiP(): Promise<void>
```

Stops a PiP window. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-stopPiP(): Promise<void>--><!--Device-PiPController-stopPiP(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300011-failure-in-destroying-a-pip-window) |
| [1300015](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300015-repeated-pip-operations) |
| [1300012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300012-abnormal-pip-window-status) |

## Examples

```TypeScript
let promise : Promise<void> = this.pipController.stopPiP(); // Stop the PiP window.
promise.then(() => {
  console.info(`Succeeded in stopping pip.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to stop pip. Cause:${err.code}, message:${err.message}`);
});
```

## updateContentNode

```TypeScript
updateContentNode(contentNode: typeNode.XComponent): Promise<void>
```

Updates the PiP node content. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PiPController-updateContentNode(contentNode: typeNode.XComponent): Promise<void>--><!--Device-PiPController-updateContentNode(contentNode: typeNode.XComponent): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| contentNode | typeNode.XComponent | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300014-pip-internal-error) |

## Examples

```TypeScript
import { typeNode, UIContext } from '@kit.ArkUI';

let context: UIContext = this.getUIContext(); // Obtain UIContext using this.getUIContext().

try {
  let contentNode = typeNode.createNode(context, "XComponent"); // Create an XComponent node to render the PiP window content.
  this.pipController.updateContentNode(contentNode); // Update the PiP node content.
} catch (exception) {
  console.error(`Failed to update content node. Code: ${exception.code}, message: ${exception.message}`);
}
```

## updateContentSize

```TypeScript
updateContentSize(width: number, height: number): void
```

Updates the media content size when the media content changes.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-updateContentSize(width: int, height: int): void--><!--Device-PiPController-updateContentSize(width: int, height: int): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let width: number = 540; // The content width changes to 540 px.
let height: number = 960; // The content height changes to 960 px.
this.pipController.updateContentSize(width, height); // Update the size of the PiP window content.
```

## updatePiPControlStatus

```TypeScript
updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void
```

Updates the PiP controller status.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPController-updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void--><!--Device-PiPController-updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| controlType | [PiPControlType](arkts-arkui-pipwindow-pipcontroltype-e.md) | Yes |
| status | [PiPControlStatus](arkts-arkui-pipwindow-pipcontrolstatus-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let controlType: PiPWindow.PiPControlType = PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE; // Play/Pause component displayed on the video playback control panel.
let status: PiPWindow.PiPControlStatus = PiPWindow.PiPControlStatus.PLAY; // The Play/Pause component displayed on the video playback control panel is in the playing state.
this.pipController.updatePiPControlStatus(controlType, status); // Update the PiP controller status.
```
