# Required

```TypeScript
type Required<T> = {
    [P in keyof T]-?: T[P];
}
```

Make all properties in T required

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-type Required<T> = {    [P in keyof T]-?: T[P];}--><!--Device-unnamed-type Required<T> = {    [P in keyof T]-?: T[P];}-End-->

**Property type:** {
    [P in keyof T]-?: T[P];
}

