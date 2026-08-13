# getOwnPropertyDescriptor

## getOwnPropertyDescriptor

```TypeScript
function getOwnPropertyDescriptor<T extends object, P extends PropertyKey>(
        target: T,
        propertyKey: P,
    ): TypedPropertyDescriptor<P extends keyof T ? T[P] : any> | undefined
```

Gets the own property descriptor of the specified object. An own property descriptor is one that is defined directly on the object and is not inherited from the object's prototype.

**Since:** -1

**Deprecated since:** -1

<!--Device-Reflect-function getOwnPropertyDescriptor<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,    ): TypedPropertyDescriptor<P extends keyof T ? T[P] : any> | undefined--><!--Device-Reflect-function getOwnPropertyDescriptor<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,    ): TypedPropertyDescriptor<P extends keyof T ? T[P] : any> | undefined-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | T | Yes |
| propertyKey | P | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TypedPropertyDescriptor](arkts-na-lib-es5-typedpropertydescriptor-i.md)&lt;P extends keyof T ? T[P] : any&gt; |
