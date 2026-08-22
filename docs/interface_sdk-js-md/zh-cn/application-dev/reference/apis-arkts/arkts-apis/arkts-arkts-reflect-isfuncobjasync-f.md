# isFuncObjAsync

## 导入模块

```TypeScript
```

## isFuncObjAsync

```TypeScript
export function isFuncObjAsync(target: Function): boolean
```

判断函数对象是否由async函数降级生成。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-reflect-export function isFuncObjAsync(target: Function): boolean--><!--Device-reflect-export function isFuncObjAsync(target: Function): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | Function | 是 | 函数对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该函数对象由async函数降级生成则返回true。 |

