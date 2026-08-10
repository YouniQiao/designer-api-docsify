# deleteProperty

## deleteProperty

```TypeScript
function deleteProperty(target: object, propertyKey: PropertyKey): boolean
```

Removes a property from an object, equivalent to `delete target[propertyKey]`,except it won't throw if `target[propertyKey]` is non-configurable.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Reflect-function deleteProperty(target: object, propertyKey: PropertyKey): boolean--><!--Device-Reflect-function deleteProperty(target: object, propertyKey: PropertyKey): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | object | Yes |  |
| propertyKey | [PropertyKey](../../apis-image-kit/arkts-apis/arkts-image-image-propertykey-e.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

