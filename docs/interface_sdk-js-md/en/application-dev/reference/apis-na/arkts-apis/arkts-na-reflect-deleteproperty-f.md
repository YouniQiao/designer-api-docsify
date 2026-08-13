# deleteProperty

## deleteProperty

```TypeScript
function deleteProperty(target: object, propertyKey: PropertyKey): boolean
```

Removes a property from an object, equivalent to `delete target[propertyKey]`, except it won't throw if `target[propertyKey]` is non-configurable.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-Reflect-function deleteProperty(target: object, propertyKey: PropertyKey): boolean--><!--Device-Reflect-function deleteProperty(target: object, propertyKey: PropertyKey): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | object | Yes |  |
| propertyKey | PropertyKey | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

