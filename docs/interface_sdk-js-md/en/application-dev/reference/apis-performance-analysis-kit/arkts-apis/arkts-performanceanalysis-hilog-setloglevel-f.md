# setLogLevel

## setLogLevel

```TypeScript
function setLogLevel(level: LogLevel, prefer: PreferStrategy): void
```

Sets the minimum log level of the current application process.

You can configure different preference strategies using the **prefer** parameter. The **PREFER\_CLOSE\_LOG** strategy has the same effect as the **setMinLogLevel()** function.
    **NOTE**  
    
    This function does not take effect for debug applications.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-hilog-function setLogLevel(level: LogLevel, prefer: PreferStrategy): void--><!--Device-hilog-function setLogLevel(level: LogLevel, prefer: PreferStrategy): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Log level. |
| prefer | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Preference strategy. |

