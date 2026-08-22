# getInstanceFieldsRecursive

## 导入模块

```TypeScript
```

## getInstanceFieldsRecursive

```TypeScript
export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>
```

返回类及其父类的公有实例字段。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-reflect-export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>--><!--Device-reflect-export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetClass | [Class](arkts-arkts-class-c.md) | 是 | 目标类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[InstanceField](arkts-arkts-reflect-instancefield-c.md)&gt; | 实例字段的数组。 |

