# Omit

```TypeScript
type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>
```

Construct a type with the properties of T except for those in type K.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>--><!--Device-unnamed-type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>-End-->

**Property type:** Pick<T, Exclude<keyof T, K>>

