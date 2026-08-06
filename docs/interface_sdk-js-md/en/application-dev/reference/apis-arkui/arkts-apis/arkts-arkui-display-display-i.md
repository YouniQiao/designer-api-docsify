# Display

Implements a Display instance, with attributes and APIs defined.

Before calling any API in Display, you must use  
[getAllDisplays()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or  
[getDefaultDisplaySync()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain a Display instance.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-display-interface Display--><!--Device-display-interface Display-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## getAvailableArea

```TypeScript
getAvailableArea(): Promise<Rect>
```

Obtains the available area of the display of the current device. This API uses a promise to return the result.

The available area is the space left for applications after the system UI (such as the status bar and dock bar)is accounted for.

This API can be properly called on devices running OpenHarmony 7.0.0 or later.For devices running versions earlier than OpenHarmony 7.0.0,this API can be properly called on PCs/2-in-1 devices and tablets,but does not work for other device types. To obtain the available area on the current device screen,you can use the width and height attributes in Display.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-getAvailableArea(): Promise<Rect>--><!--Device-Display-getAvailableArea(): Promise<Rect>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Rect&gt; | Promise used to return the available area, which is a rectangle. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. Possible cause: 1. This display is abnormal. 2. Internal task error. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let promise = displayClass.getAvailableArea();
  promise.then((data) => {
    console.info(`Succeeded get the available area in this display. data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get the available area in this display. Code: ${err.code}, message: ${err.message}`);
  })
} catch (exception) {
  console.error(`Failed to obtain the default display object. Code: ${exception.code}, message: ${exception.message}`);
}
```

## getCutoutInfo

```TypeScript
getCutoutInfo(callback: AsyncCallback<CutoutInfo>): void
```

Obtains the cutout information of the display. This API uses an asynchronous callback to return the result. You are advised not to use the cutout area during application layout.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-getCutoutInfo(callback: AsyncCallback<CutoutInfo>): void--><!--Device-Display-getCutoutInfo(callback: AsyncCallback<CutoutInfo>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CutoutInfo&gt; | Yes | Callback used to return the **CutoutInfo** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. Possible cause: 1. This display is abnormal. 2. Internal task error. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();

displayClass.getCutoutInfo((err: BusinessError, data: display.CutoutInfo) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to get cutoutInfo. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting cutoutInfo. Data: ${JSON.stringify(data)}`);
});
```

## getCutoutInfo

```TypeScript
getCutoutInfo(): Promise<CutoutInfo>
```

Obtains the cutout information of the display. This API uses a promise to return the result. You are advised not to use the cutout area during application layout.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-getCutoutInfo(): Promise<CutoutInfo>--><!--Device-Display-getCutoutInfo(): Promise<CutoutInfo>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CutoutInfo&gt; | Promise used to return the CutoutInfo object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();
let promise: Promise<display.CutoutInfo> = displayClass.getCutoutInfo();
promise.then((data: display.CutoutInfo) => {
  console.info(`Succeeded in getting cutoutInfo. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}`);
});
```

## getDisplayCapability

```TypeScript
getDisplayCapability(): string
```

Get current display capability, including foldstatus, displaymode, rotation, and orientation information.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Display-getDisplayCapability(): string--><!--Device-Display-getDisplayCapability(): string-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| string | Indicates the current foldstatus, displaymode, rotation, and orientation information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Function getDisplayCapability can not work correctly due to limited device capabilities. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

## getLiveCreaseRegion

```TypeScript
getLiveCreaseRegion(): FoldCreaseRegion
```

Obtains the live crease region of the foldable device in the current display mode.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Display-getLiveCreaseRegion(): FoldCreaseRegion--><!--Device-Display-getLiveCreaseRegion(): FoldCreaseRegion-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Live crease region of the device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

**Example**

```TypeScript
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let data: display.FoldCreaseRegion = displayClass.getLiveCreaseRegion();
  console.info(`Succeeded in getting the live crease region. Data: ${JSON.stringify(data)}`);
} catch (exception) {
  console.error(`Failed to get the live crease region. Code: ${exception.code}, message: ${exception.message}`);
}
```

## getRoundedCorner

```TypeScript
getRoundedCorner(): Array<RoundedCorner>
```

Obtains the rounded corner information of the display. The rounded corner information of the display is determined by the product configuration. Only physical screens that have a defined corner-radius value returns rounded corner information; otherwise, an empty array is returned. Virtual displays always return an empty array.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Display-getRoundedCorner(): Array<RoundedCorner>--><!--Device-Display-getRoundedCorner(): Array<RoundedCorner>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;RoundedCorner&gt; | Rounded corner information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let data = displayClass.getRoundedCorner();
  console.info(`Succeeded in getting rounded corner. Data: ${JSON.stringify(data)}`);
} catch (error) {
  console.error(`Failed to getRoundedCorner. Code: ${error.code}, message: ${error.message}`);
}
```

## off('availableAreaChange')

```TypeScript
off(type: 'availableAreaChange', callback?: Callback<Rect>): void
```

Unsubscribes from changes of the available area on the display of the current device.

This API can be properly called on devices running OpenHarmony 7.0.0 or later.For devices running versions earlier than OpenHarmony 7.0.0,this API can be properly called on PCs/2-in-1 devices and tablets.If being called on other device types, it does not take effect and no error is reported.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-off(type: 'availableAreaChange', callback?: Callback<Rect>): void--><!--Device-Display-off(type: 'availableAreaChange', callback?: Callback<Rect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableAreaChange' | Yes | Event type. The event **'availableAreaChange'** is triggered when the available area of the display changes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Rect&gt; | No | Callback used to return the new available area. If this parameter is not specified, all subscriptions to the specified event are canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

**Example**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let callback: Callback<display.Rect> = (data: display.Rect) => {
  console.info(`Listening enabled. Data: ${JSON.stringify(data)}`);
};
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  displayClass.off("availableAreaChange", callback);
} catch (exception) {
  console.error(`Failed to unregister callback. Code: ${exception.code}, message: ${exception.message}`);
}
```

## offAvailableAreaChange

```TypeScript
offAvailableAreaChange(callback?: Callback<Rect>): void
```

Unregister the callback for available area changes.

This API can be properly called on devices running OpenHarmony 7.0.0 or later.For devices running versions earlier than OpenHarmony 7.0.0,this API can be properly called on PCs/2-in-1 devices and tablets.If being called on other device types, it does not take effect and no error is reported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Display-offAvailableAreaChange(callback?: Callback<Rect>): void--><!--Device-Display-offAvailableAreaChange(callback?: Callback<Rect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Rect&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

## on('availableAreaChange')

```TypeScript
on(type: 'availableAreaChange', callback: Callback<Rect>): void
```

Subscribes to changes of the available area on the display of the current device. This callback function is triggered when the screen rotates, the freeform mode is enabled or disabled, or the visibility of system components such as the dock bar and status bar changes, and returns the available area information.

This API can be properly called on devices running OpenHarmony 7.0.0 or later.For devices running versions earlier than OpenHarmony 7.0.0,this API can be properly called on PCs/2-in-1 devices and tablets.If being called on other device types, it does not take effect and no error is reported.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-on(type: 'availableAreaChange', callback: Callback<Rect>): void--><!--Device-Display-on(type: 'availableAreaChange', callback: Callback<Rect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableAreaChange' | Yes | Event type. The event **'availableAreaChange'** is triggered when the available area of the display changes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Rect&gt; | Yes | Callback used to return the new available area. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

**Example**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let callback: Callback<display.Rect> = (data: display.Rect) => {
  console.info(`Listening enabled. Data: ${JSON.stringify(data)}`);
};
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  displayClass.on("availableAreaChange", callback);
} catch (exception) {
  console.error(`Failed to register callback. Code: ${exception.code}, message: ${exception.message}`);
}
```

## onAvailableAreaChange

```TypeScript
onAvailableAreaChange(callback: Callback<Rect>): void
```

Register the callback for available area changes.

This API can be properly called on devices running OpenHarmony 7.0.0 or later.For devices running versions earlier than OpenHarmony 7.0.0,this API can be properly called on PCs/2-in-1 devices and tablets.If being called on other device types, it does not take effect and no error is reported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Display-onAvailableAreaChange(callback: Callback<Rect>): void--><!--Device-Display-onAvailableAreaChange(callback: Callback<Rect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Rect&gt; | Yes | Callback used to return the available area |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

## alive

```TypeScript
alive: boolean
```

Whether the display is alive. The value **true** indicates that the display is alive and running properly, and **false** indicates the opposite.

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-alive: boolean--><!--Device-Display-alive: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## availableHeight

```TypeScript
availableHeight: long
```

eight of the available area, in px. The value is an integer greater than 0.

This API can be properly called on devices running OpenHarmony 7.0.0 or later.For devices running versions earlier than OpenHarmony 7.0.0,this API can be properly called on PCs/2-in-1 devices and tablets,but does not work for other device types.To obtain the height of the available area on the current device screen, you can use the height attribute.

**Type:** long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-availableHeight: long--><!--Device-Display-availableHeight: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## availableWidth

```TypeScript
availableWidth: long
```

Width of the available area, in px. The value is an integer greater than 0.

This API can be properly called on devices running OpenHarmony 7.0.0 or later.For devices running versions earlier than OpenHarmony 7.0.0,this API can be properly called on PCs/2-in-1 devices and tablets,but does not work for other device types.To obtain the width of the available area on the current device screen, you can use the width attribute.

**Type:** long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-availableWidth: long--><!--Device-Display-availableWidth: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## colorSpaces

```TypeScript
colorSpaces: Array<colorSpaceManager.ColorSpace>
```

All color spaces supported by the display.

**Type:** Array&lt;colorSpaceManager.ColorSpace&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-colorSpaces: Array<colorSpaceManager.ColorSpace>--><!--Device-Display-colorSpaces: Array<colorSpaceManager.ColorSpace>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## densityDPI

```TypeScript
densityDPI: double
```

Physical pixel density of the display, that is, the number of pixels per inch. The value is a floating-point number, in px. Generally, the value is **160.0** or **480.0**. The actual value depends on the optional values provided by the device in use.

**Type:** double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-densityDPI: double--><!--Device-Display-densityDPI: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## densityPixels

```TypeScript
densityPixels: double
```

Logical pixel density of the display, which is the scaling coefficient between physical pixels and logical pixels. The calculation method is as follows:\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_!  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_The value is a floating-point number and is restricted by the range of **densityDPI**. The value range is [0.5, 4.0]. Generally, the value is **1.0** or **3.0**. The actual value depends on the density DPI provided by the device in use.

**Type:** double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Display-densityPixels: double--><!--Device-Display-densityPixels: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## hdrFormats

```TypeScript
hdrFormats: Array<hdrCapability.HDRFormat>
```

All HDR formats supported by the display.

**Type:** Array&lt;hdrCapability.HDRFormat&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-hdrFormats: Array<hdrCapability.HDRFormat>--><!--Device-Display-hdrFormats: Array<hdrCapability.HDRFormat>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## height

```TypeScript
height: long
```

Height of the display, in px. The value is an integer.

**Type:** long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Display-height: long--><!--Device-Display-height: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## id

```TypeScript
id: long
```

Display ID, which is an integer greater than or equal to 0.

**Type:** long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-id: long--><!--Device-Display-id: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## name

```TypeScript
name: string
```

Name of the display.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-name: string--><!--Device-Display-name: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## orientation

```TypeScript
orientation: Orientation
```

Orientation of the display.

**Type:** Orientation

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-orientation: Orientation--><!--Device-Display-orientation: Orientation-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## refreshRate

```TypeScript
refreshRate: int
```

Refresh rate of the display, in Hz. The value is an integer.

**Type:** int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-refreshRate: int--><!--Device-Display-refreshRate: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## rotation

```TypeScript
rotation: int
```

Clockwise rotation angle of the display.The value **0** indicates that the display rotates clockwise by 0��, which is the standard display direction.The value **1** indicates that the display rotates clockwise by 90��.The value **2** indicates that the display rotates clockwise by 180��.The value **3** indicates that the display rotates clockwise by 270��.

**Type:** int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Display-rotation: int--><!--Device-Display-rotation: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## scaledDensity

```TypeScript
scaledDensity: double
```

Scaling factor for fonts displayed on the display. The value must be a floating  
-point number. Generally, the value is the same as that of **densityPixels**.

**Type:** double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-scaledDensity: double--><!--Device-Display-scaledDensity: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## screenShape

```TypeScript
screenShape?: ScreenShape
```

Screen shape of the display. The default value is **RECTANGLE**.

**Type:** ScreenShape

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Display-screenShape?: ScreenShape--><!--Device-Display-screenShape?: ScreenShape-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## sourceMode

```TypeScript
sourceMode?: DisplaySourceMode
```

Display mode for screen content. The default value is **DisplaySourceMode.NONE**.

**Type:** DisplaySourceMode

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Display-sourceMode?: DisplaySourceMode--><!--Device-Display-sourceMode?: DisplaySourceMode-End-->

**System capability:** SystemCapability.Window.SessionManager

## state

```TypeScript
state: DisplayState
```

State of the display.

**Type:** DisplayState

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-state: DisplayState--><!--Device-Display-state: DisplayState-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## supportedRefreshRates

```TypeScript
supportedRefreshRates?: Array<int>
```

All refresh rates supported by the display, sorted in ascending order. The refresh rate is a positive integer,in Hz. The default value is empty.

**Type:** Array&lt;int&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Display-supportedRefreshRates?: Array<int>--><!--Device-Display-supportedRefreshRates?: Array<int>-End-->

**System capability:** SystemCapability.Window.SessionManager

## width

```TypeScript
width: long
```

Width of the display, in px. The value is an integer.

**Type:** long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Display-width: long--><!--Device-Display-width: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## x

```TypeScript
x?: long
```

X coordinate of the top-left corner of the display relative to the origin,which is the top-left corner of the primary screen, measured in px. The value is an integer. The default value is  
**0**. The actual value is returned only when **DisplaySourceMode** is set to **MAIN** or **EXTEND**; otherwise,the default value **0** is returned.

**Type:** long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Display-x?: long--><!--Device-Display-x?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## xDPI

```TypeScript
xDPI: double
```

Exact physical pixels per inch of the display in the X axis. The value must be a floating-point number.

**Type:** double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-xDPI: double--><!--Device-Display-xDPI: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## y

```TypeScript
y?: long
```

Y coordinate of the top-left corner of the display relative to the origin,which is the top-left corner of the primary screen, measured in px. The value is an integer. The default value is  
**0**. The actual value is returned only when **DisplaySourceMode** is set to **MAIN** or **EXTEND**; otherwise,the default value **0** is returned.

**Type:** long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Display-y?: long--><!--Device-Display-y?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## yDPI

```TypeScript
yDPI: double
```

Exact physical pixels per inch of the display in the Y axis. The value must be a floating-point number.

**Type:** double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-yDPI: double--><!--Device-Display-yDPI: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

