# Exclude

```TypeScript
type Exclude<T, U> = T extends U ? never : T
```

Exclude from T those types that are assignable to U

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type Exclude<T, U> = T extends U ? never : T--><!--Device-unnamed-type Exclude<T, U> = T extends U ? never : T-End-->

**属性类型：** T extends U ? never : T

