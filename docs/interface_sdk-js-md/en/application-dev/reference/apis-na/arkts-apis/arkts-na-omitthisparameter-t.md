# OmitThisParameter

```TypeScript
type OmitThisParameter<T> = unknown extends ThisParameterType<T> ? T : T extends (...args: infer A) => infer R ? (...args: A) => R : T
```

Removes the 'this' parameter from a function type.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-type OmitThisParameter<T> = unknown extends ThisParameterType<T> ? T : T extends (...args: infer A) => infer R ? (...args: A) => R : T--><!--Device-unnamed-type OmitThisParameter<T> = unknown extends ThisParameterType<T> ? T : T extends (...args: infer A) => infer R ? (...args: A) => R : T-End-->

**Property type:** unknown extends ThisParameterType<T> ? T : T extends (...args: infer A) => infer R ? (...args: A) => R : T

