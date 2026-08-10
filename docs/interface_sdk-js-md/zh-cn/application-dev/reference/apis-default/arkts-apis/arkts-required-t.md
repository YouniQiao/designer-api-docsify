# Required

```TypeScript
type Required<T> = {
    [P in keyof T]-?: T[P];
}
```

Make all properties in T required

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type Required<T> = {    [P in keyof T]-?: T[P];}--><!--Device-unnamed-type Required<T> = {    [P in keyof T]-?: T[P];}-End-->

**属性类型：** {
    [P in keyof T]-?: T[P];
}

