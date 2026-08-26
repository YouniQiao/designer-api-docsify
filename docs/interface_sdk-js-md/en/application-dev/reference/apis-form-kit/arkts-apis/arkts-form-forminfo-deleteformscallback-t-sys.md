# DeleteFormsCallback (System API)

```TypeScript
type DeleteFormsCallback = (formIds: Array<string>) => void
```

callback for deleting the forms.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formIds | Array & lt;string & gt; | Yes | the form Id list of the forms to delete. |

**Examples**

```TypeScript
import { formInfo } from '@kit.FormKit';

let deleteFormsCallback: formInfo.DeleteFormsCallback =
  (formIds: Array<string>): void => {
    console.info('delete forms callback, form count: ' + formIds.length);
  };
```
