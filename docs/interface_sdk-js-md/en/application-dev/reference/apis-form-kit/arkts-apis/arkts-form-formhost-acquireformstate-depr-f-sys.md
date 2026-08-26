# acquireFormState (System API)

## Modules to Import

```TypeScript
```

## acquireFormState

```TypeScript
function acquireFormState(want: Want, callback: AsyncCallback<formInfo.FormStateInfo>): void
```

Obtains the widget state. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md)

**Required permissions:** ohos.permission.REQUIRE_FORM and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want** information carried to query the widget state. The information must contain the bundle name, ability name, module name, widget name, and widget dimensions. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;formInfo.FormStateInfo&gt; | Yes | Callback used to return the result. If the widget state is obtained, **error** is undefined and **data** is the widget state obtained; otherwise, **error** is an error object. |

**Examples**

```TypeScript
import Want from '@ohos.app.ability.Want';
import formInfo from '@ohos.app.form.formInfo';
import Base from '@ohos.base';

let want: Want = {
  'deviceId': '',
  'bundleName': 'ohos.samples.FormApplication',
  'abilityName': 'FormAbility',
  'parameters': {
    'ohos.extra.param.key.module_name': 'entry',
    'ohos.extra.param.key.form_name': 'widget',
    'ohos.extra.param.key.form_dimension': 2
  }
};
formHost.acquireFormState(want, (error: Base.BusinessError, data: formInfo.FormStateInfo) => {
  if (error.code) {
    console.error(`formHost acquireFormState, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`formHost acquireFormState, data: ${JSON.stringify(data)}`);
  }
});
```


## acquireFormState

```TypeScript
function acquireFormState(want: Want): Promise<formInfo.FormStateInfo>
```

Obtains the widget state. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md)

**Required permissions:** ohos.permission.REQUIRE_FORM and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want** information carried to query the widget state. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;formInfo.FormStateInfo & gt; | Promise used to return the widget state obtained. |

**Examples**

```TypeScript
import Want from '@ohos.app.ability.Want';
import formInfo from '@ohos.app.form.formInfo';
import Base from '@ohos.base';

let want: Want = {
  'deviceId': '',
  'bundleName': 'ohos.samples.FormApplication',
  'abilityName': 'FormAbility',
  'parameters': {
    'ohos.extra.param.key.module_name': 'entry',
    'ohos.extra.param.key.form_name': 'widget',
    'ohos.extra.param.key.form_dimension': 2
  }
};
formHost.acquireFormState(want).then((data: formInfo.FormStateInfo) => {
  console.info(`formHost acquireFormState, data: ${JSON.stringify(data)}`);
}).catch((error: Base.BusinessError) => {
  console.error(`formHost acquireFormState, error: ${JSON.stringify(error)}`);
});
```
