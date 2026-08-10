# Pick

```TypeScript
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
}
```

From T, pick a set of properties whose keys are in the union K

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type Pick<T, K extends keyof T> = {    [P in K]: T[P];}--><!--Device-unnamed-type Pick<T, K extends keyof T> = {    [P in K]: T[P];}-End-->

**属性类型：** {
    [P in K]: T[P];
}

