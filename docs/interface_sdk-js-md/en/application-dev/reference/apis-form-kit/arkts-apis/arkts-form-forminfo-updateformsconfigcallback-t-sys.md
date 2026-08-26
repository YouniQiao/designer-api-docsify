# UpdateFormsConfigCallback (System API)

```TypeScript
type UpdateFormsConfigCallback = (configInfo: Array<FormCustomConfig>) => void
```

Callback for updating the forms.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configInfo | Array&lt;[FormCustomConfig](arkts-form-forminfo-formcustomconfig-i-sys.md)&gt; | Yes | the config info list of the forms. |

**Examples**

```TypeScript
import { formInfo } from '@kit.FormKit';

let updateFormsConfigCallback: formInfo.UpdateFormsConfigCallback =
  (configInfo: Array<formInfo.FormCustomConfig>): void => {
    console.info('update forms config callback, config count: ' + configInfo.length);
  };
```
