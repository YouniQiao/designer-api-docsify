# deleteProperty

## Modules to Import

```TypeScript
```

## deleteProperty

```TypeScript
function deleteProperty(target: object, propertyKey: PropertyKey): boolean
```

Removes a property from an object, equivalent to `delete target[propertyKey]`, except it won't throw if `target[propertyKey]` is non-configurable.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| propertyKey | [PropertyKey](../../apis-image-kit/arkts-apis/arkts-image-image-propertykey-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
