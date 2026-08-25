# Display

Implements a Display instance, with attributes and APIs defined.Before calling any API in Display, you must use [getAllDisplays()](arkts-arkui-display-getalldisplays-f.md) or [getDefaultDisplaySync()](arkts-arkui-display-getdefaultdisplaysync-f.md) to obtain a Display instance.

**Since:** 7

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAvailableArea

```TypeScript
getAvailableArea(): Promise<Rect>
```

Obtains the available area of the display of the current device. This API uses a promise to return the result.The available area is the space left for applications after the system UI (such as the status bar and dock bar) is accounted for.This API can be properly called on devices running OpenHarmony 7.0.0 or later. For devices running versions earlier than OpenHarmony 7.0.0, this API can be properly called on PCs/2-in-1 devices and tablets, but does not work for other device types. To obtain the available area on the current device screen, you can use the width and height attributes in Display.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Rect & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |

## getCutoutInfo

```TypeScript
getCutoutInfo(callback: AsyncCallback<CutoutInfo>): void
```

Obtains the cutout information of the display. This API uses an asynchronous callback to return the result. You are advised not to use the cutout area during application layout.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CutoutInfo](arkts-arkui-display-cutoutinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |

## getCutoutInfo

```TypeScript
getCutoutInfo(): Promise<CutoutInfo>
```

Obtains the cutout information of the display. This API uses a promise to return the result. You are advised not to use the cutout area during application layout.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CutoutInfo](arkts-arkui-display-cutoutinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |

## getDisplayCapability

```TypeScript
getDisplayCapability(): string
```

Get current display capability, including foldstatus, displaymode, rotation, and orientation information.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## getLiveCreaseRegion

```TypeScript
getLiveCreaseRegion(): FoldCreaseRegion
```

Obtains the live crease region of the foldable device in the current display mode.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FoldCreaseRegion](arkts-arkui-display-foldcreaseregion-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## getRoundedCorner

```TypeScript
getRoundedCorner(): Array<RoundedCorner>
```

Obtains the rounded corner information of the display. The rounded corner information of the display is determined by the product configuration. Only physical screens that have a defined corner-radius value returns rounded corner information; otherwise, an empty array is returned. Virtual displays always return an empty array.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[RoundedCorner](arkts-arkui-display-roundedcorner-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## off('availableAreaChange')

```TypeScript
off(type: 'availableAreaChange', callback?: Callback<Rect>): void
```

Unsubscribes from changes of the available area on the display of the current device.This API can be properly called on devices running OpenHarmony 7.0.0 or later. For devices running versions earlier than OpenHarmony 7.0.0, this API can be properly called on PCs/2-in-1 devices and tablets. If being called on other device types, it does not take effect and no error is reported.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'availableAreaChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Rect&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## on('availableAreaChange')

```TypeScript
on(type: 'availableAreaChange', callback: Callback<Rect>): void
```

Subscribes to changes of the available area on the display of the current device. This callback function is triggered when the screen rotates, the freeform mode is enabled or disabled, or the visibility of system components such as the dock bar and status bar changes, and returns the available area information.This API can be properly called on devices running OpenHarmony 7.0.0 or later. For devices running versions earlier than OpenHarmony 7.0.0, this API can be properly called on PCs/2-in-1 devices and tablets. If being called on other device types, it does not take effect and no error is reported.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'availableAreaChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Rect&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## alive

```TypeScript
alive: boolean
```

Whether the display is alive. The value **true** indicates that the display is alive and running properly, and **false** indicates the opposite.

**Type:** boolean

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## availableHeight

```TypeScript
availableHeight: number
```

eight of the available area, in px. The value is an integer greater than 0.This API can be properly called on devices running OpenHarmony 7.0.0 or later. For devices running versions earlier than OpenHarmony 7.0.0, this API can be properly called on PCs/2-in-1 devices and tablets, but does not work for other device types. To obtain the height of the available area on the current device screen, you can use the height attribute.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## availableWidth

```TypeScript
availableWidth: number
```

Width of the available area, in px. The value is an integer greater than 0.This API can be properly called on devices running OpenHarmony 7.0.0 or later. For devices running versions earlier than OpenHarmony 7.0.0, this API can be properly called on PCs/2-in-1 devices and tablets, but does not work for other device types. To obtain the width of the available area on the current device screen, you can use the width attribute.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## colorSpaces

```TypeScript
colorSpaces: Array<colorSpaceManager.ColorSpace>
```

All color spaces supported by the display.

**Type:** Array&lt;colorSpaceManager.ColorSpace&gt;

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## densityDPI

```TypeScript
densityDPI: number
```

Physical pixel density of the display, that is, the number of pixels per inch. The value is a floating-point number. Generally, the value is **160.0** or **480.0**. The actual value depends on the optional values provided by the device in use.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## densityPixels

```TypeScript
densityPixels: number
```

Logical pixel density of the display, which is the scaling coefficient between physical pixels and logical pixels. The calculation method is as follows:! [densityPixels](../figures/densityPixels.jpg)The value is a floating-point number and is restricted by the range of **densityDPI**. The value range is [0.5, 4.0]. Generally, the value is **1.0** or **3.0**. The actual value depends on the density DPI provided by the device in use.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## hdrFormats

```TypeScript
hdrFormats: Array<hdrCapability.HDRFormat>
```

All HDR formats supported by the display.

**Type:** Array&lt;hdrCapability.HDRFormat&gt;

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## height

```TypeScript
height: number
```

Height of the display, in px. The value is an integer.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## id

```TypeScript
id: number
```

Display ID, which is an integer greater than or equal to 0.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## name

```TypeScript
name: string
```

Name of the display.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## orientation

```TypeScript
orientation: Orientation
```

Orientation of the display.

**Type:** Orientation

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## refreshRate

```TypeScript
refreshRate: number
```

Refresh rate of the display, in Hz. The value is an integer.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## rotation

```TypeScript
rotation: number
```

Clockwise rotation angle of the display. The value **0** indicates that the display rotates clockwise by 0��, which is the standard display direction. The value **1** indicates that the display rotates clockwise by 90��. The value **2** indicates that the display rotates clockwise by 180��. The value **3** indicates that the display rotates clockwise by 270��.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## scaledDensity

```TypeScript
scaledDensity: number
```

Scaling factor for fonts displayed on the display. The value must be a floating -point number. Generally, the value is the same as that of **densityPixels**.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## screenShape

```TypeScript
screenShape?: ScreenShape
```

Screen shape of the display. The default value is **ScreenShape.RECTANGLE**.

**Type:** [ScreenShape](arkts-arkui-display-screenshape-e.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## sourceMode

```TypeScript
sourceMode?: DisplaySourceMode
```

Display mode for screen content. The default value is **DisplaySourceMode.NONE**.

**Type:** [DisplaySourceMode](arkts-arkui-display-displaysourcemode-e.md)

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.Window.SessionManager

## state

```TypeScript
state: DisplayState
```

State of the display.

**Type:** [DisplayState](arkts-arkui-display-displaystate-e.md)

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## supportedRefreshRates

```TypeScript
supportedRefreshRates?: Array<number>
```

All refresh rates supported by the display, sorted in ascending order. The refresh rate is a positive integer, in Hz. The default value is empty array.

**Type:** Array&lt;number&gt;

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Window.SessionManager

## width

```TypeScript
width: number
```

Width of the display, in px. The value is an integer.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## x

```TypeScript
x?: number
```

X coordinate of the top-left corner of the display relative to the origin, which is the top-left corner of the primary screen, measured in px. The value is an integer. The default value is **0**. The actual value is returned only when **DisplaySourceMode** is set to **MAIN** or **EXTEND**; otherwise, the default value **0** is returned.

**Type:** number

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.Window.SessionManager

## xDPI

```TypeScript
xDPI: number
```

Exact physical pixels per inch of the display in the X axis. The value must be a floating-point number.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## y

```TypeScript
y?: number
```

Y coordinate of the top-left corner of the display relative to the origin, which is the top-left corner of the primary screen, measured in px. The value is an integer. The default value is **0**. The actual value is returned only when **DisplaySourceMode** is set to **MAIN** or **EXTEND**; otherwise, the default value **0** is returned.

**Type:** number

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.Window.SessionManager

## yDPI

```TypeScript
yDPI: number
```

Exact physical pixels per inch of the display in the Y axis. The value must be a floating-point number.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core
