# Display

屏幕实例。描述Display对象的属性和方法。

下列API示例中都需先使用[getAllDisplays()](arkts-arkui-display-getalldisplays-f.md#getalldisplays)、  
[getDefaultDisplaySync()](arkts-arkui-display-getdefaultdisplaysync-f.md#getdefaultdisplaysync)中的任一方法获取到Display实例，再通过此实例调用对应方法。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-display-interface Display--><!--Device-display-interface Display-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAvailableArea

```TypeScript
getAvailableArea(): Promise<Rect>
```

获取当前设备屏幕的可用区域，使用Promise异步回调。

可用区域是扣除系统UI（如状态栏、Dock栏）后，可供应用程序自由使用的区域。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-getAvailableArea(): Promise<Rect>--><!--Device-Display-getAvailableArea(): Promise<Rect>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Rect&gt; | Promise对象。返回当前屏幕可用矩形区域。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400001 | Invalid display or screen. Possible cause: 1. This display is abnormal. 2. Internal task error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let promise = displayClass.getAvailableArea();
  promise.then((data) => {
    console.info(`Succeeded in getting the available area in this display. data: ${JSON.stringify(data)}`);
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

获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。使用callback异步回调。建议应用布局规避该区域。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-getCutoutInfo(callback: AsyncCallback<CutoutInfo>): void--><!--Device-Display-getCutoutInfo(callback: AsyncCallback<CutoutInfo>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CutoutInfo&gt; | Yes | 回调函数。返回不可用屏幕区域对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400001 | Invalid display or screen. Possible cause: 1. This display is abnormal. 2. Internal task error. |

## Examples

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

获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。使用Promise异步回调。建议应用布局规避该区域。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-getCutoutInfo(): Promise<CutoutInfo>--><!--Device-Display-getCutoutInfo(): Promise<CutoutInfo>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CutoutInfo&gt; | Promise对象。返回描述不可用屏幕区域的CutoutInfo对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400001 | Invalid display or screen. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();
let promise: Promise<display.CutoutInfo> = displayClass.getCutoutInfo();
promise.then((data: display.CutoutInfo) => {
  console.info(`Succeeded in getting cutoutInfo. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get cutoutInfo. Code: ${err.code}, message: ${err.message}`);
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
| 801 | Capability not supported.Function getDisplayCapability can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

## getLiveCreaseRegion

```TypeScript
getLiveCreaseRegion(): FoldCreaseRegion
```

获取当前显示模式下的实时折痕区域。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Display-getLiveCreaseRegion(): FoldCreaseRegion--><!--Device-Display-getLiveCreaseRegion(): FoldCreaseRegion-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| [FoldCreaseRegion](arkts-arkui-display-foldcreaseregion-i.md) | 返回设备在当前显示模式下的折叠折痕区域。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
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

获取屏幕的圆角信息。屏幕圆角信息由产品配置决定，只有配置了屏幕圆角半径的物理屏幕才能返回圆角信息，否则返回空数组，虚拟屏同样返回空数组。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Display-getRoundedCorner(): Array<RoundedCorner>--><!--Device-Display-getRoundedCorner(): Array<RoundedCorner>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;RoundedCorner&gt; | 返回当前屏幕的圆角信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let data = displayClass.getRoundedCorner();
  console.info(`Succeeded in getting rounded corner. Data: ${JSON.stringify(data)}`);
} catch (error) {
  console.error(`Failed to get rounded corner. Code: ${error.code}, message: ${error.message}`);
}
```

## off('availableAreaChange')

```TypeScript
off(type: 'availableAreaChange', callback?: Callback<Rect>): void
```

关闭当前设备屏幕可用区域变化的监听。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-off(type: 'availableAreaChange', callback?: Callback<Rect>): void--><!--Device-Display-off(type: 'availableAreaChange', callback?: Callback<Rect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableAreaChange' | Yes | 监听事件，固定为'availableAreaChange'，表示屏幕可用区域变更。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Rect&gt; | No | 需要取消注册的回调函数。返回改变后的可用区域。若无此参数，则取消注册屏幕可用区域变化监听的所有回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<display.Rect> = (data: display.Rect) => {
  console.info(`Listening enabled. Data: ${JSON.stringify(data)}`);
};
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  displayClass.off('availableAreaChange', callback);
} catch (exception) {
  console.error(`Failed to unregister callback. Code: ${exception.code}, message: ${exception.message}`);
}
```

## offAvailableAreaChange

```TypeScript
offAvailableAreaChange(callback?: Callback<Rect>): void
```

Unregister the callback for available area changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Display-offAvailableAreaChange(callback?: Callback<Rect>): void--><!--Device-Display-offAvailableAreaChange(callback?: Callback<Rect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Rect&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

## on('availableAreaChange')

```TypeScript
on(type: 'availableAreaChange', callback: Callback<Rect>): void
```

开启当前设备屏幕可用区域的监听。当屏幕旋转、进入/退出自由多窗模式、设置Dock栏/状态栏等系统控件可见性变化时，触发回调函数，返回可用区域信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-on(type: 'availableAreaChange', callback: Callback<Rect>): void--><!--Device-Display-on(type: 'availableAreaChange', callback: Callback<Rect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableAreaChange' | Yes | 监听事件。固定为'availableAreaChange'，表示屏幕可用区域变更。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Rect&gt; | Yes | 回调函数。返回改变后的可用区域。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<display.Rect> = (data: display.Rect) => {
  console.info(`Listening enabled. Data: ${JSON.stringify(data)}`);
};
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  displayClass.on('availableAreaChange', callback);
} catch (exception) {
  console.error(`Failed to register callback. Code: ${exception.code}, message: ${exception.message}`);
}
```

## onAvailableAreaChange

```TypeScript
onAvailableAreaChange(callback: Callback<Rect>): void
```

Register the callback for available area changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Display-onAvailableAreaChange(callback: Callback<Rect>): void--><!--Device-Display-onAvailableAreaChange(callback: Callback<Rect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Rect&gt; | Yes | Callback used to return the available area |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

## alive

```TypeScript
alive: boolean
```

显示设备的启用状态，表示设备是否处于正常运行状态。true表示已启用，处于正常运行状态；false表示未启用，未处于正常运行状态。

SystemCapability.WindowManager.WindowManager.Core

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

显示设备的可用区域高度，单位为px，该参数为大于0的整数。

SystemCapability.WindowManager.WindowManager.Core

该接口在2in1设备、Tablet设备中可正常调用；在其他设备中不可用，请通过height属性获取当前设备屏幕的可用区域高度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-availableHeight: long--><!--Device-Display-availableHeight: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## availableWidth

```TypeScript
availableWidth: long
```

显示设备的可用区域宽度，单位为px，该参数为大于0的整数。

SystemCapability.WindowManager.WindowManager.Core

该接口在2in1设备、Tablet设备中可正常调用；在其他设备中不可用，请通过width属性获取当前设备屏幕的可用区域宽度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-availableWidth: long--><!--Device-Display-availableWidth: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## colorSpaces

```TypeScript
colorSpaces: Array<colorSpaceManager.ColorSpace>
```

显示设备支持的所有色域类型。

SystemCapability.WindowManager.WindowManager.Core

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

显示设备的物理像素密度，表示每英寸上的像素点数。该参数为浮点数，单位为px。一般取值160.0、480.0等，实际能取到的值取决于不同设备设置里提供的可选值。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-densityDPI: double--><!--Device-Display-densityDPI: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## densityPixels

```TypeScript
densityPixels: double
```

显示设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数，计算方式为：![densityPixels](../../../reference/apis-arkui/figures/densityPixels.jpg)

该参数为浮点数，受densityDPI范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的densityDPI。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Display-densityPixels: double--><!--Device-Display-densityPixels: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## hdrFormats

```TypeScript
hdrFormats: Array<hdrCapability.HDRFormat>
```

显示设备支持的所有HDR格式。

SystemCapability.WindowManager.WindowManager.Core

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

显示设备的屏幕高度，单位为px，该参数为整数。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Display-height: long--><!--Device-Display-height: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## id

```TypeScript
id: long
```

显示设备的屏幕ID，该参数为大于等于0的整数。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-id: long--><!--Device-Display-id: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## name

```TypeScript
name: string
```

显示设备的名称。

SystemCapability.WindowManager.WindowManager.Core

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

表示显示设备当前显示的方向。

SystemCapability.WindowManager.WindowManager.Core

**Type:** [Orientation](arkts-arkui-window-orientation-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-orientation: Orientation--><!--Device-Display-orientation: Orientation-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## refreshRate

```TypeScript
refreshRate: int
```

显示设备当前采用的刷新率，该参数为整数，单位为Hz。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-refreshRate: int--><!--Device-Display-refreshRate: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## rotation

```TypeScript
rotation: int
```

显示设备的屏幕顺时针旋转角度。

值为0时，表示显示设备屏幕顺时针旋转为0°，表示显示设备的标准显示方向；

值为1时，表示显示设备屏幕顺时针旋转为90°；

值为2时，表示显示设备屏幕顺时针旋转为180°；

值为3时，表示显示设备屏幕顺时针旋转为270°。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Display-rotation: int--><!--Device-Display-rotation: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## scaledDensity

```TypeScript
scaledDensity: double
```

显示设备上的字体的缩放因子。该参数为浮点数，通常与densityPixels相同。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-scaledDensity: double--><!--Device-Display-scaledDensity: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## screenShape

```TypeScript
screenShape?: ScreenShape
```

显示设备的屏幕形状，默认值为RECTANGLE。

SystemCapability.WindowManager.WindowManager.Core

**Type:** [ScreenShape](arkts-arkui-display-screenshape-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Display-screenShape?: ScreenShape--><!--Device-Display-screenShape?: ScreenShape-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## sourceMode

```TypeScript
sourceMode?: DisplaySourceMode
```

显示设备的显示模式枚举，默认值为DisplaySourceMode.NONE。

SystemCapability.Window.SessionManager

**Type:** [DisplaySourceMode](arkts-arkui-display-displaysourcemode-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Display-sourceMode?: DisplaySourceMode--><!--Device-Display-sourceMode?: DisplaySourceMode-End-->

**System capability:** SystemCapability.Window.SessionManager

## state

```TypeScript
state: DisplayState
```

显示设备的状态。

SystemCapability.WindowManager.WindowManager.Core

**Type:** [DisplayState](arkts-arkui-display-displaystate-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-state: DisplayState--><!--Device-Display-state: DisplayState-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## supportedRefreshRates

```TypeScript
supportedRefreshRates?: Array<int>
```

显示设备支持的所有刷新率，从小到大排序。刷新率值为正整数，单位为Hz。默认为空。

SystemCapability.Window.SessionManager

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Display-supportedRefreshRates?: Array<int>--><!--Device-Display-supportedRefreshRates?: Array<int>-End-->

**System capability:** SystemCapability.Window.SessionManager

## width

```TypeScript
width: long
```

显示设备的屏幕宽度，单位为px，该参数为整数。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Display-width: long--><!--Device-Display-width: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## x

```TypeScript
x?: long
```

显示设备左上角相对于原点的y轴坐标，原点为主屏左上角，单位为px，该参数为整数，默认值为0。仅DisplaySourceMode为MAIN和EXTEND时返回实际值，其余默认返回默认值0。

SystemCapability.Window.SessionManager

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Display-x?: long--><!--Device-Display-x?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## xDPI

```TypeScript
xDPI: double
```

x轴方向中每英寸屏幕的确切物理像素值，该参数为浮点数。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-xDPI: double--><!--Device-Display-xDPI: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## y

```TypeScript
y?: long
```

显示设备左上角相对于原点的y轴坐标，原点为主屏左上角，单位为px，该参数为整数，默认值为0。仅DisplaySourceMode为MAIN和EXTEND时返回实际值，其余默认返回默认值0。

SystemCapability.Window.SessionManager

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Display-y?: long--><!--Device-Display-y?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## yDPI

```TypeScript
yDPI: double
```

y轴方向中每英寸屏幕的确切物理像素值，该参数为浮点数。

SystemCapability.WindowManager.WindowManager.Core

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Display-yDPI: double--><!--Device-Display-yDPI: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

