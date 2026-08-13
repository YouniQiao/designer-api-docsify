# Pick

```TypeScript
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
}
```

From T, pick a set of properties whose keys are in the union K

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-type Pick<T, K extends keyof T> = {    [P in K]: T[P];}--><!--Device-unnamed-type Pick<T, K extends keyof T> = {    [P in K]: T[P];}-End-->

**Property type:** {
    [P in K]: T[P];
}

