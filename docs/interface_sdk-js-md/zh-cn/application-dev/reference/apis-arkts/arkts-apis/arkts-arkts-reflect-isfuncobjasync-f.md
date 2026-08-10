# isFuncObjAsync

## isFuncObjAsync

```TypeScript
export function isFuncObjAsync(target: Function): boolean
```

Determines if a functional object was lowered from an async function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-reflect-export function isFuncObjAsync(target: Function): boolean--><!--Device-reflect-export function isFuncObjAsync(target: Function): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | Function | 是 | the functional object. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the functional object was lowered from an async function. |

