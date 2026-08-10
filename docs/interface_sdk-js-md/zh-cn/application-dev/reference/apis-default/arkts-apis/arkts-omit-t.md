# Omit

```TypeScript
type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>
```

Construct a type with the properties of T except for those in type K.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>--><!--Device-unnamed-type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>-End-->

**属性类型：** Pick<T, Exclude<keyof T, K>>

