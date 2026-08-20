# isLiteralInitializedInterface

## 导入模块

```TypeScript
```

## isLiteralInitializedInterface

```TypeScript
export function isLiteralInitializedInterface(target: Object): boolean
```

判断对象是否为通过字面量初始化的接口。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-reflect-export function isLiteralInitializedInterface(target: Object): boolean--><!--Device-reflect-export function isLiteralInitializedInterface(target: Object): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | Object | 是 | 目标对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 布尔值，表示target是否为通过字面量 初始化的接口。 |

