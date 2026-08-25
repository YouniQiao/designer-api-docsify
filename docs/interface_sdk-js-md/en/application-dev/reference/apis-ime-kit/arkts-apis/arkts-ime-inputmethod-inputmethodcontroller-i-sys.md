# InputMethodController

In the following API examples, you must first use [getController](arkts-ime-inputmethod-getcontroller-f.md) to obtain an **InputMethodController** instance, and then call the APIs using the obtained instance.

**Since:** 6

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(displayId: number): Promise<void>
```

Hides the soft keyboard on a specified screen. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to hide the soft keyboard only when the edit box is focused.

**Since:** 23

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## showSoftKeyboard

```TypeScript
showSoftKeyboard(displayId: number): Promise<void>
```

Shows the soft keyboard on a specified screen. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to show the soft keyboard only when the edit box is focused.

**Since:** 23

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
