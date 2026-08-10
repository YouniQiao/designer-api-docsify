# Parameters

```TypeScript
type Parameters<T extends (...args: any) => any> = T extends (...args: infer P) => any ? P : never
```

Obtain the parameters of a function type in a tuple

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type Parameters<T extends (...args: any) => any> = T extends (...args: infer P) => any ? P : never--><!--Device-unnamed-type Parameters<T extends (...args: any) => any> = T extends (...args: infer P) => any ? P : never-End-->

**属性类型：** T extends (...args: infer P) => any ? P : never

