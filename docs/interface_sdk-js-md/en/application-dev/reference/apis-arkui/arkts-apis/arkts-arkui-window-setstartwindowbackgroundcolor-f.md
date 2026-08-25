# setStartWindowBackgroundColor

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## setStartWindowBackgroundColor

```TypeScript
function setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>
```

Sets the background color of the splash screen of the UIAbility based on the specified module name and ability name within the same bundle name. This API uses a promise to return the result.This API takes effect for all processes of the same bundle name, for example, in multi-instance or clone scenarios.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| abilityName | string | Yes |
| color | [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
