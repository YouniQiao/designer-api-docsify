# ThisParameterType

```TypeScript
type ThisParameterType<T> = T extends (this: infer U, ...args: never) => any ? U : unknown
```

Extracts the type of the 'this' parameter of a function type, or 'unknown' if the function type has no 'this' parameter.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type ThisParameterType<T> = T extends (this: infer U, ...args: never) => any ? U : unknown--><!--Device-unnamed-type ThisParameterType<T> = T extends (this: infer U, ...args: never) => any ? U : unknown-End-->

**属性类型：** T extends (this: infer U, ...args: never) => any ? U : unknown

