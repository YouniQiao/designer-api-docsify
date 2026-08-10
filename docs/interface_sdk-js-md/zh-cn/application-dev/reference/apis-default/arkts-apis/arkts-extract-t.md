# Extract

```TypeScript
type Extract<T, U> = T extends U ? T : never
```

Extract from T those types that are assignable to U

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type Extract<T, U> = T extends U ? T : never--><!--Device-unnamed-type Extract<T, U> = T extends U ? T : never-End-->

**属性类型：** T extends U ? T : never

