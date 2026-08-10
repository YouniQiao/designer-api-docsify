# ConstructorParameters

```TypeScript
type ConstructorParameters<T extends abstract new (...args: any) => any> = T extends abstract new (...args: infer P) => any ? P : never
```

Obtain the parameters of a constructor function type in a tuple

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type ConstructorParameters<T extends abstract new (...args: any) => any> = T extends abstract new (...args: infer P) => any ? P : never--><!--Device-unnamed-type ConstructorParameters<T extends abstract new (...args: any) => any> = T extends abstract new (...args: infer P) => any ? P : never-End-->

**属性类型：** T extends abstract new (...args: infer P) => any ? P : never

