# Readonly

```TypeScript
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
}
```

Make all properties in T readonly

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-type Readonly<T> = {    readonly [P in keyof T]: T[P];}--><!--Device-unnamed-type Readonly<T> = {    readonly [P in keyof T]: T[P];}-End-->

**Property type:** {
    readonly [P in keyof T]: T[P];
}

