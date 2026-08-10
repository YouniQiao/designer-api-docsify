# getInstanceGettersRecursive

## getInstanceGettersRecursive

```TypeScript
export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>
```

Returns public instance getters of a class and its parents.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-reflect-export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>--><!--Device-reflect-export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetClass | [Class](arkts-arkts-class-c.md) | 是 | the target class. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;InstanceMethod&gt; | an array of instance getters. |

