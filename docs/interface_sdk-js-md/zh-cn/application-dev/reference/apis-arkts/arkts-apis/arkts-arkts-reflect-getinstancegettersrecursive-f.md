# getInstanceGettersRecursive

## 导入模块

```TypeScript
```

## getInstanceGettersRecursive

```TypeScript
export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>
```

返回类及其父类的公有实例getter方法。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-reflect-export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>--><!--Device-reflect-export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetClass | [Class](arkts-arkts-class-c.md) | 是 | 目标类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[InstanceMethod](arkts-arkts-reflect-instancemethod-c.md)&gt; | 实例getter方法的数组。 |

