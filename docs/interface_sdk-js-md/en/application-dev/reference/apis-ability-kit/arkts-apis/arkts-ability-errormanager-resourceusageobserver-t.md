# ResourceUsageObserver

```TypeScript
export type ResourceUsageObserver = (resourceType: ResourceType, resourceSize: long, detailInfo?: Record<string, long>) => void
```

The observer will be called by the system when resource usage exceed threshold.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-errorManager-export type ResourceUsageObserver = (resourceType: ResourceType, resourceSize: long, detailInfo?: Record<string, long>) => void--><!--Device-errorManager-export type ResourceUsageObserver = (resourceType: ResourceType, resourceSize: long, detailInfo?: Record<string, long>) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The type of resource.  |
| resourceSize | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | The amount of resources occupied. The value must be greater than **0**. \_\_\_HTML\_TAG\_USD\_0\_\_\_Unit: KB.  |
| detailInfo | ArkTS-Dyn: \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, number&gt;  \_\_\_HTML\_TAG\_USD\_2\_\_\_ArkTS-Sta：\_\_\_MD\_LINK\_USD\_1\_\_\_&lt;string, long&gt; | No | Key-value pair of the resource type and its size. \_\_\_HTML\_TAG\_USD\_0\_\_\_This parameter is available only when resourceType is set to PSS\_MEMORY. If resourceType is set to other types or default values, this parameter is left blank. The key is the lowercase memory type, and the value is the resource size of the corresponding subdivision item. The keys of subdivision items include arkts, native, ion, gpu, ashmem, and other. The second value must be greater than 0 *, in KB.  |

