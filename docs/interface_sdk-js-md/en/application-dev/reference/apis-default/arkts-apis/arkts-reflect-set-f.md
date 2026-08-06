# set

## set

```TypeScript
function set<T extends object, P extends PropertyKey>(
        target: T,
        propertyKey: P,
        value: P extends keyof T ? T[P] : any,
        receiver?: any,
    ): boolean
```

Sets the property of target, equivalent to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ when \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Reflect-function set<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,        value: P extends keyof T ? T[P] : any,        receiver?: any,    ): boolean--><!--Device-Reflect-function set<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,        value: P extends keyof T ? T[P] : any,        receiver?: any,    ): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| propertyKey | P | Yes |  |
| value | P extends keyof T ? T[P] : any | Yes |  |
| receiver | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |


## set

```TypeScript
function set(target: object, propertyKey: PropertyKey, value: any, receiver?: any): boolean
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | object | Yes |  |
| propertyKey | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |
| value | any | Yes |  |
| receiver | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

