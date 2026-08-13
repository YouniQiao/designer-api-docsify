# get

## get

```TypeScript
function get<T extends object, P extends PropertyKey>(
        target: T,
        propertyKey: P,
        receiver?: unknown,
    ): P extends keyof T ? T[P] : any
```

Gets the property of target, equivalent to `target[propertyKey]` when `receiver === target`.

**Since:** -1

**Deprecated since:** -1

<!--Device-Reflect-function get<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,        receiver?: unknown,    ): P extends keyof T ? T[P] : any--><!--Device-Reflect-function get<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,        receiver?: unknown,    ): P extends keyof T ? T[P] : any-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | T | Yes |
| propertyKey | P | Yes |
| receiver | unknown | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| P extends keyof T ? T[P] : any |
