# ResourceUsageObserver

```TypeScript
export type ResourceUsageObserver = (resourceType: ResourceType, resourceSize: long, detailInfo?: Record<string, long>) => void
```

定义应用资源使用情况的观察者回调函数，作为  
[errorManager.setDefaultResourceUsageObserver](arkts-ability-errormanager-setdefaultresourceusageobserver-f.md#setdefaultresourceusageobserver)的入参，用于监听各类资源占用变化，并支持应用执行自定义资源处理逻辑。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-errorManager-export type ResourceUsageObserver = (resourceType: ResourceType, resourceSize: long, detailInfo?: Record<string, long>) => void--><!--Device-errorManager-export type ResourceUsageObserver = (resourceType: ResourceType, resourceSize: long, detailInfo?: Record<string, long>) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceType | [ResourceType](arkts-ability-errormanager-resourcetype-e.md) | Yes | 表示应用资源超基线的类型。 |
| resourceSize | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 表示应用资源超基线的资源使用量。 |
| detailInfo | ArkTS-Dyn: [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number&gt;  <br>ArkTS-Sta：[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, long&gt; | No | 表示应用资源超基线资源使用量的细分项字典。<br>**说明**：仅在resourceType为PSS_MEMORY时存在，为其他类型或缺 省时为空；<br>key为小写内存类型，value为对应细分项资源大小；<br>细分项的key包含arkts、native、ion、gpu、ashmem和other。 第二个值必须大于**0**。单位：KB。 |

