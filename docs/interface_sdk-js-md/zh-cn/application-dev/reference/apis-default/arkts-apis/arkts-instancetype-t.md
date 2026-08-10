# InstanceType

```TypeScript
type InstanceType<T extends abstract new (...args: any) => any> = T extends abstract new (...args: any) => infer R ? R : any
```

Obtain the return type of a constructor function type

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type InstanceType<T extends abstract new (...args: any) => any> = T extends abstract new (...args: any) => infer R ? R : any--><!--Device-unnamed-type InstanceType<T extends abstract new (...args: any) => any> = T extends abstract new (...args: any) => infer R ? R : any-End-->

**属性类型：** T extends abstract new (...args: any) => infer R ? R : any

