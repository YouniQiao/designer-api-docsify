# getAllFormsInfo (System API)

## Modules to Import

```TypeScript
```

## getAllFormsInfo

```TypeScript
function getAllFormsInfo(callback: AsyncCallback<Array<formInfo.FormInfo>>): void
```

Obtains the widget information provided by all applications on the device. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md)

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.FormInfo&gt;&gt; | Yes |

**Examples**

```TypeScript
import formInfo from '@ohos.app.form.formInfo';
import Base from '@ohos.base';

formHost.getAllFormsInfo((error: Base.BusinessError, data: formInfo.FormInfo[]) => {
  if (error.code) {
    console.error(`formHost getAllFormsInfo, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`formHost getAllFormsInfo, data: ${JSON.stringify(data)}`);
  }
});
```

```TypeScript
import formInfo from '@ohos.app.form.formInfo';
import Base from '@ohos.base';

formHost.getAllFormsInfo().then((data: formInfo.FormInfo[]) => {
  console.info(`formHost getAllFormsInfo data: ${JSON.stringify(data)}`);
}).catch((error: Base.BusinessError) => {
  console.error(`formHost getAllFormsInfo, error: ${JSON.stringify(error)}`);
});
```


## getAllFormsInfo

```TypeScript
function getAllFormsInfo(): Promise<Array<formInfo.FormInfo>>
```

Obtains the widget information provided by all applications on the device. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md)

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;formInfo.FormInfo & gt; & gt; |

**Examples**

See [getAllFormsInfo](#getallformsinfo)
