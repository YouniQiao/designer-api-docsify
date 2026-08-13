# ThisParameterType

```TypeScript
type ThisParameterType<T> = T extends (this: infer U, ...args: never) => any ? U : unknown
```

Extracts the type of the 'this' parameter of a function type, or 'unknown' if the function type has no 'this' parameter.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-type ThisParameterType<T> = T extends (this: infer U, ...args: never) => any ? U : unknown--><!--Device-unnamed-type ThisParameterType<T> = T extends (this: infer U, ...args: never) => any ? U : unknown-End-->

**Property type:** T extends (this: infer U, ...args: never) => any ? U : unknown

