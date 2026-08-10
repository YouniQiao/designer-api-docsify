# getFloatViewLimits

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## getFloatViewLimits

```TypeScript
function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits
```

根据传入的模板类型获取对应标准悬浮窗窗口的限制，单位为px。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits--><!--Device-floatView-function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| templateType | [FloatViewTemplateType](arkts-arkui-floatview-floatviewtemplatetype-e.md) | Yes | 标准悬浮窗模板类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md) | 返回标准悬浮窗窗口的限制，包括最大尺寸、最小尺寸和宽高比的限制范围。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |
| 801 | Capability not supported. Possible cause: Call the API on unsupported device. |
| 1300002 | This window state is abnormal. Possible cause: System error, such as a null pointer, insufficient memory or a JS engine exception. |
| 1300016 | Parameter error. Possible cause: Invalid template type. |

## Examples

```TypeScript
// Obtain the float view limit of the rounded rectangle template.
let limits: floatView.FloatViewLimits = floatView.getFloatViewLimits(floatView.FloatViewTemplateType.ROUNDED_RECTANGLE);
console.info('Float view limits: ' + JSON.stringify(limits));
```

