# Partial

```TypeScript
type Partial<T> = {
    [P in keyof T]?: T[P];
}
```

Make all properties in T optional

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-type Partial<T> = {    [P in keyof T]?: T[P];}--><!--Device-unnamed-type Partial<T> = {    [P in keyof T]?: T[P];}-End-->

**Property type:** {
    [P in keyof T]?: T[P];
}

