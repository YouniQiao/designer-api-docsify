# defineProperty

## defineProperty

```TypeScript
function defineProperty(target: object, propertyKey: PropertyKey, attributes: PropertyDescriptor & ThisType<any>): boolean
```

Adds a property to an object, or modifies attributes of an existing property.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Reflect-function defineProperty(target: object, propertyKey: PropertyKey, attributes: PropertyDescriptor & ThisType<any>): boolean--><!--Device-Reflect-function defineProperty(target: object, propertyKey: PropertyKey, attributes: PropertyDescriptor & ThisType<any>): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | object | 是 |  |
| propertyKey | [PropertyKey](../../apis-image-kit/arkts-apis/arkts-image-image-propertykey-e.md) | 是 |  |
| attributes | [PropertyDescriptor](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-propertydescriptor-i.md) & ThisType&lt;any&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

