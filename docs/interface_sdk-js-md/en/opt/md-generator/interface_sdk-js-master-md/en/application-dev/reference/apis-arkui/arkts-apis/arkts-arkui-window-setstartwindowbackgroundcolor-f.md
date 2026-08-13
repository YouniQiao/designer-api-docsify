# setStartWindowBackgroundColor

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## setStartWindowBackgroundColor

```TypeScript
function setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>
```

Sets the background color of the splash screen of the UIAbility based on the specified module name and ability name within the same bundle name. This API uses a promise to return the result. This API takes effect for all processes of the same bundle name, for example, in multi-instance or clone scenarios.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-window-function setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>--><!--Device-window-function setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| abilityName | string | Yes |
| color | [ColorMetrics](../../apis-na/arkts-apis/arkts-na-graphics-colormetrics-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics, window } from '@kit.ArkUI';

try {
  let promise = window.setStartWindowBackgroundColor("entry", "EntryAbility", ColorMetrics.numeric(0xff000000));
  promise.then(() => {
    console.info('Succeeded in setting the starting window color.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the starting window color. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set the starting window color. Cause code: ${exception.code}, message: ${exception.message}`);
}
```
