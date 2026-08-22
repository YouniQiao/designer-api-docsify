# AbstractProperty

Define AbstractProperty&lt;T&gt; interface.

AbstractProperty can be understood as a handler or an alias to a property inside LocalStorage / AppStorage singleton allows to read the value with

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface AbstractProperty--><!--Device-unnamed-export declare interface AbstractProperty-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## get

```TypeScript
get(): T
```

Reads value of the referenced AppStorage/LocalStorage property.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-get(): T--><!--Device-AbstractProperty-get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| T | value of the referenced AppStorage/LocalStorage property. |

## info

```TypeScript
info(): string
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-AbstractProperty-info(): string--><!--Device-AbstractProperty-info(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
## onChange

```TypeScript
onChange(onChangeFunc: OnChangeType<T> | undefined): void
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-AbstractProperty-onChange(onChangeFunc: OnChangeType<T> | undefined): void--><!--Device-AbstractProperty-onChange(onChangeFunc: OnChangeType<T> | undefined): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onChangeFunc | [OnChangeType](arkts-arkui-onchangetype-t.md)&lt;T&gt; \| undefined | Yes |  |

## set

```TypeScript
set(newValue: T): void
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-AbstractProperty-set(newValue: T): void--><!--Device-AbstractProperty-set(newValue: T): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes |  |

## default

```TypeScript
default
```

Register callback function to be called on value change of the referenced property calling with value undefined clear the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-default--><!--Device-AbstractProperty-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

