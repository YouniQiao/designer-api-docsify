# Required

```TypeScript
type Required<T> = {
    [P in keyof T]-?: T[P];
}
```

Make all properties in T required

**Since:** -1

<!--Device-unnamed-type Required<T> = {    [P in keyof T]-?: T[P];}--><!--Device-unnamed-type Required<T> = {    [P in keyof T]-?: T[P];}-End-->

**Property type:** {
    [P in keyof T]-?: T[P];
}

