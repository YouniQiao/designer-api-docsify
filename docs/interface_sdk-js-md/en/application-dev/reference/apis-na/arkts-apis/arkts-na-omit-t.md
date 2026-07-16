# Omit

```TypeScript
type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>
```

Construct a type with the properties of T except for those in type K.

<!--Device-unnamed-type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>--><!--Device-unnamed-type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>-End-->

**Property type:** Pick<T, Exclude<keyof T, K>>

