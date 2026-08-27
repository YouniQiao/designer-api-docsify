# GetWantParamsCallback (System API)

```TypeScript
type GetWantParamsCallback = (formInfo: Array<formInfo.FormInfo>) => Array<Record<string, Object>>
```

Get want parameters callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formInfo | Array&lt;[formInfo.FormInfo](arkts-form-forminfo-forminfo-i.md)&gt; | Yes | The list of the form information. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Record&lt;string, Object&gt;&gt; | The want parameters list of the forms. |

**Examples**

```TypeScript
import { formInfo } from '@kit.FormKit';

let getWantParamsCallback: formInfo.GetWantParamsCallback =
  (formInfo: Array<formInfo.FormInfo>): Array<Record<string, Object>> => {
    console.info('get want params callback, form count: ' + formInfo.length);
    let wantParamsList: Array<Record<string, Object>> = [];
    for (let i = 0; i < formInfo.length; i++) {
      let params: Record<string, Object> = {
        'key': 'value'
      };
      wantParamsList.push(params);
    }
    return wantParamsList;
  };
```
