# makeBindable

## makeBindable

```TypeScript
export declare function makeBindable<T>(value: T, onChange: Callback<T>): Bindable<T>
```

Create a bindable property instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function makeBindable<T>(value: T, onChange: Callback<T>): Bindable<T>--><!--Device-unnamed-export declare function makeBindable<T>(value: T, onChange: Callback<T>): Bindable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | indicates the value of a state property. |
| onChange | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | indicates the invoked callback when the property is changed. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | bindable property instance. |

