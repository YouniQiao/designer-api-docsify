# getWindowsByCoordinate

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getWindowsByCoordinate

```TypeScript
function getWindowsByCoordinate(displayId: long, windowNumber?: int, x?: int, y?: int):
      Promise<Array<Window>>
```

查询本应用指定坐标下的可见窗口数组，按当前窗口层级排列，层级最高的窗口对应数组下标为0，使用Promise异步回调。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-window-function getWindowsByCoordinate(displayId: long, windowNumber?: int, x?: int, y?: int):      Promise<Array<Window>>--><!--Device-window-function getWindowsByCoordinate(displayId: long, windowNumber?: int, x?: int, y?: int):      Promise<Array<Window>>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 查询窗口所在的displayId，该参数应为整数，传入非整数会忽略掉小数部分，可以在窗口属性 [WindowProperties](arkts-arkui-window-windowproperties-i.md)中获取。 |
| windowNumber | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 查询的窗口数量，该参数应为大于0的整数，传入非整数会忽略掉小数部分，未设置或小于等于0返回所有满足条件的窗口。 |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 查询的x坐标，以屏幕左上角为原点，该参数应为非负整数，传入非整数会忽略掉小数部分，未设置或小于0返回所有可见窗口。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 查询的y坐标，以屏幕左上角为原点，该参数应为非负整数，传入非整数会忽略掉小数部分，未设置或小于0返回所有可见窗口。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Window&gt;&gt; | Promise对象。返回获取到的窗口对象数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

