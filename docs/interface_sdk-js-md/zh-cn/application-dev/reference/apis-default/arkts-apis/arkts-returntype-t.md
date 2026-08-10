# ReturnType

```TypeScript
type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any
```

Obtain the return type of a function type

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any--><!--Device-unnamed-type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any-End-->

**属性类型：** T extends (...args: any) => infer R ? R : any

