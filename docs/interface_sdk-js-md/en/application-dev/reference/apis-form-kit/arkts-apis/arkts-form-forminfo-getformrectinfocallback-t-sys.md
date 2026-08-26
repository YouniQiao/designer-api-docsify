# GetFormRectInfoCallback (System API)

```TypeScript
type GetFormRectInfoCallback = (formId: string) => Promise<formInfo.Rect>
```

Get form rect info callback

**Since:** 20

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[formInfo.Rect](arkts-form-forminfo-rect-i.md)&gt; | form rect info |

**Examples**

```TypeScript
import { formInfo } from '@kit.FormKit';

// The widget host needs to process the request, and calculate and return the widget dimension and position information.
let getFormRectInfoCallback: formInfo.GetFormRectInfoCallback =
  (formId: string): Promise<formInfo.Rect> => {
    return new Promise<formInfo.Rect>((resolve: (value: formInfo.Rect) => void) => {
      console.info(`formId is ${formId}`);
      let formRect: formInfo.Rect = {
        left: 0,
        top: 0,
        width: 0,
        height: 0
      };
      resolve(formRect);
    })
  };
```
