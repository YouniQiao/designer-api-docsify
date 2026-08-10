# TypeDecorator

```TypeScript
export declare type TypeDecorator = <T>(type: TypeConstructor<T>) => PropertyDecorator
```

属性装饰器，用于装饰嵌套类中属于自定义class类的属性。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export declare type TypeDecorator = <T>(type: TypeConstructor<T>) => PropertyDecorator--><!--Device-unnamed-export declare type TypeDecorator = <T>(type: TypeConstructor<T>) => PropertyDecorator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [TypeConstructor](arkts-arkui-arkui-statemanagement-typeconstructor-i.md)&lt;T&gt; | Yes | 标记类属性的类型，仅支持自定义class类型，传入其他类型会导致持久化失败。 |

**Return value:**

| Type | Description |
| --- | --- |
| PropertyDecorator | 属性装饰器，用于装饰嵌套类中属于自定义class类的属性。 |

