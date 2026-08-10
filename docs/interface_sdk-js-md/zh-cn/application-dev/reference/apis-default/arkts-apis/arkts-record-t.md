# Record

```TypeScript
type Record<K extends keyof any, T> = {
    [P in K]: T;
}
```

Construct a type with a set of properties K of type T

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type Record<K extends keyof any, T> = {    [P in K]: T;}--><!--Device-unnamed-type Record<K extends keyof any, T> = {    [P in K]: T;}-End-->

**属性类型：** {
    [P in K]: T;
}

