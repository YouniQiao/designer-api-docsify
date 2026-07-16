# ReturnType

```TypeScript
type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any
```

Obtain the return type of a function type

<!--Device-unnamed-type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any--><!--Device-unnamed-type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any-End-->

**Property type:** T extends (...args: any) => infer R ? R : any

