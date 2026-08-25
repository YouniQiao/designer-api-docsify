# isSystemReady (System API)

## Modules to Import

```TypeScript
```

## isSystemReady

```TypeScript
function isSystemReady(callback: AsyncCallback<void>): void
```

Checks whether the system is ready. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [isSystemReady](arkts-form-formhost-issystemready-f-sys.md)

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
import Base from '@ohos.base';

let formId: string = '12400633174999288';
formHost.isSystemReady((error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formHost isSystemReady, error: ${JSON.stringify(error)}`);
  }
});
```

```TypeScript
import Base from '@ohos.base';

let formId: string = '12400633174999288';
formHost.isSystemReady().then(() => {
  console.info('formHost isSystemReady success');
}).catch((error: Base.BusinessError) => {
  console.error(`formHost isSystemReady, error: ${JSON.stringify(error)}`);
});
```


## isSystemReady

```TypeScript
function isSystemReady(): Promise<void>
```

Checks whether the system is ready. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [isSystemReady](arkts-form-formhost-issystemready-f-sys.md)

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

See [isSystemReady](#issystemready)
