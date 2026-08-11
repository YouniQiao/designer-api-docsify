# PressureLevel

Enumerates the memory pressure levels. When an application clears the cache occupied by the **Web** component, the  
**Web** kernel releases the cache based on the memory pressure level.

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Value](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-value-i.md) | Description|
| ------------------------------- | - | ---------- |
| [MEMORY_PRESSURE_LEVEL_MODERATE](#memory_pressure_level_moderate) | 1 | Moderate memory pressure level. At this level, the **Web** kernel attempts to release the cache that has low reallocation overhead and does not need to be used immediately.|
| [MEMORY_PRESSURE_LEVEL_CRITICAL](#memory_pressure_level_critical) | 2 |

**Since:** 14

<!--Device-webview-enum PressureLevel--><!--Device-webview-enum PressureLevel-End-->

**System capability:** SystemCapability.Web.Webview.Core

## MEMORY_PRESSURE_LEVEL_MODERATE

```TypeScript
MEMORY_PRESSURE_LEVEL_MODERATE = 1
```

Modules are advised to free buffers that are cheap to re-allocate and not immediately needed.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PressureLevel-MEMORY_PRESSURE_LEVEL_MODERATE = 1--><!--Device-PressureLevel-MEMORY_PRESSURE_LEVEL_MODERATE = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## MEMORY_PRESSURE_LEVEL_CRITICAL

```TypeScript
MEMORY_PRESSURE_LEVEL_CRITICAL = 2
```

At this level, modules are advised to free all possible memory.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PressureLevel-MEMORY_PRESSURE_LEVEL_CRITICAL = 2--><!--Device-PressureLevel-MEMORY_PRESSURE_LEVEL_CRITICAL = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core
