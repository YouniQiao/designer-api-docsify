# getAllWindowLayoutInfo

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getAllWindowLayoutInfo

```TypeScript
function getAllWindowLayoutInfo(displayId: long): Promise<Array<WindowLayoutInfo>>
```

获取指定屏幕上可见的窗口布局信息数组，其中返回的每个Rect的宽、高是已经过缩放计算后的值，按当前窗口层级排列，层级最高的对应数组index为0，使用Promise异步回调。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-window-function getAllWindowLayoutInfo(displayId: long): Promise<Array<WindowLayoutInfo>>--><!--Device-window-function getAllWindowLayoutInfo(displayId: long): Promise<Array<WindowLayoutInfo>>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 需要获取窗口布局信息的displayId，该参数应为整数，且为当前实际存在屏幕的displayId，可以通过窗口属性 [WindowProperties](arkts-arkui-window-windowproperties-i.md)获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;WindowLayoutInfo&gt;&gt; | Promise对象。返回获取到的窗口布局信息对象数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Function getAllWindowLayoutInfo can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal.<br>**Applicable version:** 15 - 18 |


## getAllWindowLayoutInfo

```TypeScript
function getAllWindowLayoutInfo(displayId: long, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>
```

根据option指定的过滤条件获取指定屏幕上可见的窗口布局信息数组，其中返回的每个Rect的宽、高是已经过缩放计算后的值，按当前窗口层级排列，层级最高的对应数组index为0，使用Promise异步回调。当未传入option或其中的字段都为默认值时，当前接口与[getAllWindowLayoutInfo](arkts-arkui-window-getallwindowlayoutinfo-f.md#getallwindowlayoutinfo)等价。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-window-function getAllWindowLayoutInfo(displayId: long, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>--><!--Device-window-function getAllWindowLayoutInfo(displayId: long, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 需要获取窗口布局信息的displayId，该参数应为整数，且为当前实际存在屏幕的displayId，可以通过窗口属性 [WindowProperties](arkts-arkui-window-windowproperties-i.md)获取。 |
| option | [WindowInfoOptions](arkts-arkui-window-windowinfooptions-i.md) | No | 过滤选项。用于指定返回信息是否排除系统窗、比指定窗口层级更低或更高的窗口的信息。默认不过滤。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;WindowLayoutInfo&gt;&gt; | Promise对象。返回获取到的窗口布局信息对象数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal task error. |
| 801 | Capability not supported. Function getAllWindowLayoutInfo can not work correctly due to limited device capabilities. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

