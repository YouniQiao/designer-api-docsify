# deleteProperty

## Modules to Import

```TypeScript
```

## deleteProperty

```TypeScript
function deleteProperty(target: object, propertyKey: PropertyKey): boolean
```

Removes a property from an object, equivalent to `delete target[propertyKey]`, except it won't throw if `target[propertyKey]` is non-configurable.

**Since:** -1

<!--Device-Reflect-function deleteProperty(target: object, propertyKey: PropertyKey): boolean--><!--Device-Reflect-function deleteProperty(target: object, propertyKey: PropertyKey): boolean-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| propertyKey | [PropertyKey](arkts-na-propertykey-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
