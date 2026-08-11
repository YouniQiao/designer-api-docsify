# create

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(config: FloatViewConfiguration): Promise<FloatViewController>
```

Creates a float view controller. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function create(config: FloatViewConfiguration): Promise<FloatViewController>--><!--Device-floatView-function create(config: FloatViewConfiguration): Promise<FloatViewController>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [FloatViewConfiguration](arkts-arkui-floatview-floatviewconfiguration-i.md) | Yes | Parameter for creating a float view controller. This parameter and the context for constructing this parameter cannot be null or undefined. Otherwise, error code 401 is thrown. Error code 1300016 is thrown for other parameter exceptions. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FloatViewController&gt; | Promise used to return the created float view controller. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Possible cause: Call the API on unsupported device. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: 1. This window context is abnormal. 2. System error, such as a null pointer, insufficient memory or a JS engine exception. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible cause: Invalid template type. |

