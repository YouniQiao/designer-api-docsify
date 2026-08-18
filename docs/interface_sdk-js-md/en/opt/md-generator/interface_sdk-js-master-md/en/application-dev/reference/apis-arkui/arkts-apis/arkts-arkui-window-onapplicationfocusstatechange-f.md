# onApplicationFocusStateChange

## Modules to Import

```TypeScript
```

## onApplicationFocusStateChange

```TypeScript
function onApplicationFocusStateChange(callback: Callback<boolean>): void
```

Register the callback for application process focus state changes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-window-function onApplicationFocusStateChange(callback: Callback<boolean>): void--><!--Device-window-function onApplicationFocusStateChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Examples**

```TypeScript
import { window } from '@kit.ArkUI';

try {
  window.onApplicationFocusStateChange((data) =>{
      console.info(`Succeeded in enabling the listener for application focus state changes. Data: ${data}`);
  })
} catch(exception){
  console.error(`Failed to enable the listener for application focus state changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```
