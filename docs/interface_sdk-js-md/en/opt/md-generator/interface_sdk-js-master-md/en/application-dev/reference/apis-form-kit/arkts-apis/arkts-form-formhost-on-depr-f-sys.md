# on (System API)

## on('formUninstall')

```TypeScript
function on(type: 'formUninstall', callback: Callback<string>): void
```

Subscribes to widget uninstall events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Widget uninstall is different from widget removal. When an application is uninstalled, the corresponding widget
> is automatically uninstalled.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** @ohos.app.form.formHost:formHost#on

<!--Device-formHost-function on(type: 'formUninstall', callback: Callback<string>): void--><!--Device-formHost-function on(type: 'formUninstall', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'formUninstall' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |
