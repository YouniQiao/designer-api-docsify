# off (System API)

## Modules to Import

```TypeScript
```

## off('formUninstall')

```TypeScript
function off(type: 'formUninstall', callback?: Callback<string>): void
```

Unsubscribes from widget uninstall events. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Widget uninstall is different from widget removal. When an application is uninstalled, the corresponding widget
> is automatically uninstalled.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-form-formhost-off-f-sys.md)

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'formUninstall' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |
