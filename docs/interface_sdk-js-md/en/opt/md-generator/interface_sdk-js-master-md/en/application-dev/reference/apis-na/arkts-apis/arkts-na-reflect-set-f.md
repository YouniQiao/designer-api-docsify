# set

## Modules to Import

```TypeScript
```

## set

```TypeScript
function set<T extends object, P extends PropertyKey>(
        target: T,
        propertyKey: P,
        value: P extends keyof T ? T[P] : any,
        receiver?: any,
    ): boolean
```

Sets the property of target, equivalent to `target[propertyKey] = value` when `receiver === target`.

**Since:** -1

<!--Device-Reflect-function set<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,        value: P extends keyof T ? T[P] : any,        receiver?: any,    ): boolean--><!--Device-Reflect-function set<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,        value: P extends keyof T ? T[P] : any,        receiver?: any,    ): boolean-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | T | Yes |
| propertyKey | P | Yes |
| value | P extends keyof T ? T[P] : any | Yes |
| receiver | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |


## set

```TypeScript
function set(target: object, propertyKey: PropertyKey, value: any, receiver?: any): boolean
```

**Since:** -1

<!--Device-Reflect-function set(target: object, propertyKey: PropertyKey, value: any, receiver?: any): boolean--><!--Device-Reflect-function set(target: object, propertyKey: PropertyKey, value: any, receiver?: any): boolean-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| propertyKey | [PropertyKey](arkts-na-propertykey-t.md) | Yes |
| value | any | Yes |
| receiver | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
