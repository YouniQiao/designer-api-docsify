# getAllWindowLayoutInfo

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getAllWindowLayoutInfo

```TypeScript
function getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>
```

Obtains the layout information array of all windows visible on a display. The layout information is arranged based on the current window stacking order, and the topmost window in the hierarchy is at index 0 of the array. This API uses a promise to return the result.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-window-function getAllWindowLayoutInfo(displayId: long): Promise<Array<WindowLayoutInfo>>--><!--Device-window-function getAllWindowLayoutInfo(displayId: long): Promise<Array<WindowLayoutInfo>>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;WindowLayoutInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |


## getAllWindowLayoutInfo

```TypeScript
function getAllWindowLayoutInfo(displayId: number, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>
```

Obtains the array of window layout info visible on a specified screen.The width and height of each rect are calculated after scaling. The array is sorted by the current window level.The index of the array corresponding to the highest level is 0.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-window-function getAllWindowLayoutInfo(displayId: long, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>--><!--Device-window-function getAllWindowLayoutInfo(displayId: long, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |
| option | [WindowInfoOptions](arkts-arkui-window-windowinfooptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;WindowLayoutInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
