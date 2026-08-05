# getFloatViewLimits

## getFloatViewLimits

```TypeScript
function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits
```

Obtains the limits of the float view based on the passed template type. The unit is px.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits--><!--Device-floatView-function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| templateType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Template type of the float view. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Limits of the float view, including the maximum size, minimum size, and aspect ratio. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Possible cause:Call the API on unsupported device. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause:System error, such as a null pointer, insufficient memory or a JS engine exception. |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. Possible cause:Internal IPC error. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible cause: Invalid template type. |

