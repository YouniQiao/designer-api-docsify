# Readonly

```TypeScript
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
}
```

Make all properties in T readonly

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type Readonly<T> = {    readonly [P in keyof T]: T[P];}--><!--Device-unnamed-type Readonly<T> = {    readonly [P in keyof T]: T[P];}-End-->

**属性类型：** {
    readonly [P in keyof T]: T[P];
}

