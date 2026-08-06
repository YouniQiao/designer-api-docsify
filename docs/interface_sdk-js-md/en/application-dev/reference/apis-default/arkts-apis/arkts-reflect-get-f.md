# get

## get

```TypeScript
function get<T extends object, P extends PropertyKey>(
        target: T,
        propertyKey: P,
        receiver?: unknown,
    ): P extends keyof T ? T[P] : any
```

Gets the property of target, equivalent to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ when \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Reflect-function get<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,        receiver?: unknown,    ): P extends keyof T ? T[P] : any--><!--Device-Reflect-function get<T extends object, P extends PropertyKey>(        target: T,        propertyKey: P,        receiver?: unknown,    ): P extends keyof T ? T[P] : any-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | T | Yes |  |
| propertyKey | P | Yes |  |
| receiver | unknown | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| P extends keyof T ? T[P] : any |  |

