# AbstractProperty

Define AbstractProperty\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ interface.

AbstractProperty can be understood as a handler or an alias to a property inside LocalStorage / AppStorage singleton allows to read the value with @see get and to change the value with @see set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AbstractProperty<T>--><!--Device-unnamed-export declare interface AbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## get

```TypeScript
get(): T
```

Reads value of the referenced AppStorage/LocalStorage property.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-get(): T--><!--Device-AbstractProperty-get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| T | value of the referenced AppStorage/LocalStorage property. |

## info

```TypeScript
default info(): string
```

Returns the name of the referenced property

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-default info(): string--><!--Device-AbstractProperty-default info(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | name of the referenced property |

## onChange

```TypeScript
default onChange(onChangeFunc: OnChangeType<T> | undefined): void
```

Register callback function to be called on value change of the referenced property calling with value undefined clear the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-default onChange(onChangeFunc: OnChangeType<T> | undefined): void--><!--Device-AbstractProperty-default onChange(onChangeFunc: OnChangeType<T> | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onChangeFunc | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; \| undefined | Yes | register callback function |

## set

```TypeScript
default set(newValue: T): void
```

Assign a new value to the referenced property

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-default set(newValue: T): void--><!--Device-AbstractProperty-default set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | a new value of the referenced property |

